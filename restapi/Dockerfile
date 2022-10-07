FROM python:3.10.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./manage.py /app
COPY ./restapi /app/restapi

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "restapi.wsgi:application"]