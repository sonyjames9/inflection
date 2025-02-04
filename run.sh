#!/bin/bash

python3 -m pytest tests_campaign/test_campaign_api.py --alluredir=/app/allure-results
allure serve allure-results