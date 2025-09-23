## Notification Service

Simple notification service, to create a discord notification via the specified webhook url.

# Endpoints
Api can be reached via `/notifications/v1`.

Currently available endpoints:

| Endpoint | URL Suffix                                          |
|----------|-----------------------------------------------------|
| /discord | Sends message to specified WEBHOOK_URL from env var |

# How to start
Build the image
``
docker build -t notificationservice:latest .
``

Api runs on port 8000. To start the container use

``
docker run -it -p 8000:8000 -e DISCORD_WEBHOOK_URL=<YOUR_DISCORD_WEBHOOK_URL> notificationservice:latest
``

# Swagger-UI
As soon as the container is started, the [Swagger-UI](http://localhost:8000/docs) will be exposed.