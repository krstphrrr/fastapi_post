FROM osgeo/gdal:latest

RUN apt-get update

RUN apt-get install python python3-pip \
    libpq-dev postgresql postgresql-contrib \
    unixodbc-dev python3-tk -y


WORKDIR /usr/src

COPY . .
COPY requirements.txt .

EXPOSE 5009

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5009"]


# docker image build -t post_api
# docker container run --rm -d --name post_api -p 5009:5009 post_api
# uvicorn main:app --host 0.0.0.0 --port 5009
