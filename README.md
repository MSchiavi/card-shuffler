# card-shuffler-api

## Features

- **FastAPI** with Python 3.8
- Docker compose for easier development


## Development

The only dependencies for this project should be docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
docker-compose up -d
```

And navigate to http://localhost:8000/api/v1

Auto-generated docs will be at
http://localhost:8000/api/docs
*** Highly suggest you use these since you can also hit the endpoints and pass in parameters in a nice interface.

### Rebuilding containers:

```
docker-compose build
```

### Restarting containers:

```
docker-compose restart
```

### Bringing containers down:

```
docker-compose down
```

## Logging

```
docker-compose logs
```

Or for a specific service:

```
docker-compose logs -f name_of_service # frontend|backend|db
```

## Project Layout

```
backend
└── app
    ├── models # Deck Class
    ├── api
    │   └── api_v1
    │       └── endpoints
    ├── core    # config
    ├── db      # db models
    ├── utils # Helpful Tools.
    ├── tests   # pytest
    └── main.py # entrypoint to backend
```
