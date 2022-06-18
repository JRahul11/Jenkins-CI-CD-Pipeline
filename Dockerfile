FROM python:3.7

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . .

# Local Deployment
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "jenkinsproject.wsgi:application"]

# Remote Deployment
CMD gunicorn jenkinsproject.wsgi:application --bind 0.0.0.0:$PORT