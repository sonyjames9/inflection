from re import A
from campaign.base_api import BaseAPI
from utils.config import UTCTime


class CampaignService(BaseAPI):
    def __init__(self):
        super().__init__("http://localhost:7070")

    def create_campaign(
        self, campaign_name, email_template_id, recipient_list_id, scheduled_minutes
    ):
        scheduled_time = UTCTime.get_utc_epoch(scheduled_minutes)

        payload = {
            "campaignName": campaign_name,
            "emailTemplateId": email_template_id,
            "recipientListId": recipient_list_id,
            "scheduledTime": scheduled_time,
        }

        response, status_code = self.post("/campaigns", payload)

        if response:
            print(f"payload :  {payload}")
            print(f"response :  {response}")
            print(f"Status code :  {status_code}")
            return response, status_code
        return 500, {"error": "Server error"}
