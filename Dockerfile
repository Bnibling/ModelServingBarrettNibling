FROM python:3.7.6-stretch

COPY ./requirements.txt /modelserving/requirements.txt

WORKDIR /modelserving

RUN pip install -r requirements.txt

COPY . /modelserving

ENTRYPOINT ["python3","modelserving.py"]
