from re import A
from campaign.base_api import BaseAPI
from utils.config import UTCTime


class CampaignService(BaseApi):
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

        return self.post("/campaigns", payload)
    
