FROM maven:3.9.11 AS build
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

FROM openjdk:21-jdk-slim
WORKDIR /app
COPY --from=build /build/target/thinkbase-java.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]