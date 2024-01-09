FROM openjdk:17-jdk-slim as build
EXPOSE 8090

ARG JAR_FILE=target/mswsAPI-0.0.1-SNAPSHOT.jar

# Add the application's jar to the container
COPY ${JAR_FILE} app.jar

# Run the jar file
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]