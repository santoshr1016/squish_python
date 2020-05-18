# Packaging an existing Jar in a Docker image
FROM openjdk:8-jre-slim

RUN mkdir /app

COPY build/libs/*.jar /app/spring-boot-application.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar","/app/spring-boot-application.jar"]
