FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir Pillow

COPY invert.py .

CMD [ "python", "./invert.py" ]