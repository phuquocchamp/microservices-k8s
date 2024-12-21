## Microservice Architecture and System Design with Python & Kubernetes

This repository refers to the [freeCodeCamp.org](https://www.freecodecamp.org/) hands-on tutorial about microservices architecture and distributed systems using Python, Kubernetes, RabbitMQ, MongoDB, and MySQL.

Watch the [YouTube video](https://www.youtube.com/watch?v=hmkF77F9TLw) for more information.



### Connect MongoDB from host

Note: Máy đã cài đạt MongoDB

**1. Forward port of host - service**
Mở 1 terminal và chạy lệnh sau: 

```bash
kubectl port-forward svc/mongodb-service 27017:27017
```

**2. Connect to MongoBD**
Mở một terminal khác và chạy lệnh sau:
```bash
mongosh "mongodb://localhost:27017"
```



