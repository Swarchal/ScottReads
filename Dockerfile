FROM python:3.10

ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8787 8787
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8787"]
