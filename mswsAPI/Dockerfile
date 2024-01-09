# Copy the project files to the container
COPY . /usr/src/myapp

# Set the working directory
WORKDIR /usr/src/myapp

# Build the application
RUN mvn clean package

# Stage 2: Create the runtime image
FROM openjdk:17-jdk-slim

# Expose port 8090
EXPOSE 8090

# Copy the JAR file from the builder stage
COPY --from=builder /usr/src/myapp/target/your-application.jar /usr/app/your-application.jar

# Set the working directory
WORKDIR /usr/app

# Command to run the application
ENTRYPOINT ["java", "-jar", "your-application.jar"]