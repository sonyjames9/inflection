  #!/bin/bash

#  Build  Docker Image
docker build -t campaign-tests .

# Run the Tests in a Container
docker run --rm -v $(pwd)/allure-results:/app/allure-results campaign-tests

# Generate and Serve Allure Report
echo "📊 Generating Allure Report..."
allure serve allure-results