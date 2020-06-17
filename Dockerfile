FROM python:3.6-alpine

WORKDIR /api
ADD . /api
RUN pip install -r requirements.txt
CMD ["python", "api.py"]