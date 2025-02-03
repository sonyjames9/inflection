import allure
import pytest

from campaign.campaign_service import CampaignService

campaign_service = CampaignService()


@allure.feature("Campaign Scheduling")
@allure.story("Create a new campaign")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_campaign():
    with allure.step("Fetch campaign details and create campaign"):
        response, status_code = campaign_service.create_campaign(
            "T8", "EM-001", "RL-001", 10
            )
        
        with allure.step("Verify response"):
            assert status_code == 201, f"Expected 201, got {status_code}"
            assert (
                response["meta"]["status"] == "SUCCESS"
            ), "Expected successful campaign creation"
