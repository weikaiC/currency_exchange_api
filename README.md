Build and run the Docker image locally, as follows:

```
docker build -t asiayo-api .
docker run -d -p 8080:80 asiayo-api
```

In order to run the example server with docker compose, use this:

```
docker-compose up --build
```

swagger url

```
http://127.0.0.1:80/docs
```