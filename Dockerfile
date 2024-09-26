FROM python:3.10-alpine as builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libgcc libstdc++ libc6-compat

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache libgcc libstdc++ libc6-compat python3

COPY --from=builder /install /usr/local

COPY . .

EXPOSE 7001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7001"]
