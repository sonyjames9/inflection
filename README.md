# inflection


```
Feature description - Marketing Campaign Scheduling
The Marketing Campaign Scheduling feature allows users to schedule email campaigns to be sent at specific dates and times(in UTC). Users can configure various parameters for their campaigns, such as selecting the recipient list, specifying the email template. The feature ensures that campaigns are sent out accurately and can handle large volumes of emails efficiently.
```


```
- Have implemented the base class and extended it in campaign/campaign_service.py
- campaign/base_api.py has all the methods - GET, POST, PATCH
- The tests_campaign/test_campaign_api.py is the one where all the tests and assertions are placed
- /inflection/test_plans has all the test cases
- utils/config.py has all the helper functions
- all the reports are user generated
```


---

Steps:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- pytest tests_campaign/test_campaign_api.py --alluredir=allure-results
- allure serve allure-results