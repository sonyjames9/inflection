from campaign.base_api import BaseAPI
from utils.config import UTCTime
import random


class CampaignService(BaseAPI):
    RECIPIENT_LISTS = ["RL-001", "RL-002", "RL-003", "RL-004"]
    EMAIL_TEMPLATES = ["EM-001", "EM-002", "EM-003", "EM-004"]

    def __init__(self):
        super().__init__("http://localhost:7070")

    def create_campaign(
        self, campaign_name, email_template_id, recipient_list_id, scheduled_minutes
    ):
        if recipient_list_id not in self.RECIPIENT_LISTS:
            return {
                "error": f"Invalid recipient list ID. Choose from {self.RECIPIENT_LISTS}"
            }

        if email_template_id not in self.EMAIL_TEMPLATES:
            return {
                "error": f"Invalid email template ID. Choose from {self.EMAIL_TEMPLATES}"
            }

        scheduled_time = UTCTime.get_utc_epoch(scheduled_minutes)

        payload = {
            "campaignName": campaign_name,
            "emailTemplateId": email_template_id,
            "recipientListId": recipient_list_id,
            "scheduledTime": scheduled_time,
        }

        response, status_code = self.post("/campaigns", payload)
        # campaign_id = response["data"].get("id")

        if response:
            # print(f"payload :  {payload}")
            # print(f"response :  {response}")
            # print(f"Status code :  {status_code}")
            # print(f"campaign_id :  {campaign_id}")
            return response, status_code
            # return response, status_code, campaign_id

        return 500, {"error": "Server error"}

    def edit_campaign_name(self, campaign_id, new_campaign_name):

        if not campaign_id.strip():
            return {"error": "Campaign id cannot be empty."}

        if not new_campaign_name.strip():
            return {"error": "New campaign name cannot be empty."}

        payload = {"campaignName": new_campaign_name}
        response, status_code = self.patch(f"/campaigns/{campaign_id}/name", payload)

        if response:
            # print(f"payload :  {payload}")
            # print(f"response :  {response}")
            # print(f"Status code :  {status_code}")
            return response, status_code
        return 500, {"error": "Server error"}
