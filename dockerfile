FROM python:3.10.5-alpine3.16
WORKDIR /usr/src/app

RUN apk --no-cache add ca-certificates
# RUN apk --no-cace gcc musl-dev python3-dev libffi-dev openssl-dev cargo

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./buhbye.py" ]