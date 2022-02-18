FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code
RUN python library_app/manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "library_app/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]