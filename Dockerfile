# Use official Python image
FROM python:3.11-slim
COPY --from=openjdk:8-jre-slim /usr/local/openjdk-8 /usr/local/openjdk-8

ENV JAVA_HOME="/usr/local/openjdk-8"
ENV PATH="${JAVA_HOME}/bin:${PATH}"
RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-8/bin/java 1

# # Set working directory
WORKDIR /app

# Copy project files
# COPY   ./campaign ./docker-yml ./test_plans ./tests_campaign ./utils .dockerignore .gitignore Dockerfile README.md  requirements.txt run.sh /app/
COPY . /app

RUN  pip install --no-cache-dir -r /app/requirements.txt && \
  apt-get update && \
  apt-get install -y wget && \
  apt-get install -y curl && \
  wget https://github.com/allure-framework/allure2/releases/download/2.19.0/allure-2.19.0.tgz && \
  tar -xvzf allure-2.19.0.tgz && \
  mv allure-2.19.0 /app/allure

# Add Allure to PATH
ENV PATH="/app/allure/bin:$PATH"

EXPOSE 7070 7071 7072 40481


# Run tests with Allure
CMD ["sh", "./run.sh"]
