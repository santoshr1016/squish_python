### Running the Gradle Project
```text
1. Create the Dockerfile for the microservice 1
Assuming the jar is already build.
Follow the only-package.Dockerfile

2. Building it locally

docker build -t microservice_1 .
docker run --name microservice_1_app -p 8080:8080 -d microservice_1

3. Open the postman and call the endpoints

4. docker rmi microservice_1
```

