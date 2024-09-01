FROM python:3.11.9-alpine3.20

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV BACKEND_PORT=8080

EXPOSE ${BACKEND_PORT}

CMD [ "python", "main.py" ]