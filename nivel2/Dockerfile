FROM python
RUN apt-get update
RUN mkdir /nivel2
WORKDIR /nivel2
COPY . /nivel2
RUN pip install --no-cache-dir -r nivel2_app/requirements.txt
CMD ["python", "nivel2_app/nivel2.py"]
