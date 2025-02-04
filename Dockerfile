# Use official Python image
FROM python:3.11

# # Set working directory
# WORKDIR /app

# Copy project files
COPY  campaign \
  docker-yml \
  test_plans \
  tests_campaign \ 
  utils \ 
  .dockerignore \ 
  .gitignore \ 
  Dockerfile \ 
  README.md \ 
  requirements.txt \ 
  run.sh \
  ./

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies and Allure CLI
RUN pip install --no-cache-dir -r requirements.txt && wget https://github.com/allure-framework/allure2/releases/download/2.19.0/allure-2.19.0.tgz && \
  tar -xvzf allure-2.19.0.tgz && \
  mv allure-2.19.0 /app/allure

# Add Allure to PATH
ENV PATH="/app/allure/bin:$PATH"

# Run tests with Allure
CMD ["sh", "./run.sh"]
