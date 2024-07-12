FROM python:3.8-slim-buster
WORKDIR /python-flaskapp
COPY . /python-flaskapp
RUN pip install -r requirements.txt
CMD ["python", "flask_app.py"]