from flask import Flask, jsonify, request, Response
import json
import mysql.connector
#from flask_cors import CORS, cross_origin

app = Flask(__name__)

def Connection():
    return mysql.connector.connect(user='root', host='nivel2-db', port='3306', password='toor', database='nivel2-db-mysql')


@app.route('/active', methods=['GET', 'POST', 'PUT'])
def active():
    if request.method == 'GET':
        country = request.args.get("country", default = "no country", type = str)
        city = request.args.get("city", default = "no city", type = str)
        db = Connection();
        try:
            sql_select = "select city.active, city.city, country.country from city inner join country on country.id = city.id_country where country.country LIKE '%{}%' and city.city LIKE '%{}%'".format(country, city)
            cursor = db.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            if records == None:
                info = {"Response": "No hay parametros o no hay resultados"}
                return jsonify(info)
            else:
                for row in records:
                    if row[0] == 0:
                        v_active = False
                    else:
                        v_active = True

                    info = {
                            "active": "{}".format(v_active),
                            "country": "{}".format(row[2]),
                            "city": "{}".format(row[1])
                        }
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return jsonify(info)

    if request.method == 'POST':
        req_data = request.get_json()

        country = req_data['country']
        city = req_data['city']
        db = Connection();
        try:
            sql_insert = "INSERT INTO `country` (`country`) VALUES ('{}')".format(country)
            cursor = db.cursor()
            cursor.execute(sql_insert)
            db.commit()

            sql_select = "select id from country where country = '{}'".format(country)
            cursor.execute(sql_select)
            records = cursor.fetchall()
            for row in records:
                id_v = row[0]

            sql_insert_c = "INSERT INTO `city` (`city`, `id_country`, `active`) VALUES ('{}', '{}', '1')".format(city, id_v)
            cursor.execute(sql_insert_c)
            db.commit()

            info = {"Response": "Datos guardados correctamente"}
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return jsonify(info)


    if request.method == 'PUT':
        req_data = request.get_json()

        country = req_data['country']
        city = req_data['city']
        db = Connection();
        try:
            sql_select = "select city.id,city.active from city inner join country on country.id = city.id_country where country.country like '%{}%' and city.city like '%{}%'".format(country, city)

            cursor = db.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            for row in records:
                city_id = row[0]
                active = row[1]

            if active == 0:
                active_n = 1
                info = {"Response": "Se activo la venta"}
            else:
                active_n = 0
                info = {"Response": "Se desactivo la venta"}

            sql_update = "update city set active = {} where city.id = {}".format(active_n, city_id)
            cursor.execute(sql_update)
            db.commit()
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
