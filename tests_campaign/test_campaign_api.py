import allure
import pytest
from campaign.campaign_service import CampaignService
from utils.config import NameGenerator

campaign_service = CampaignService()

@allure.feature("Campaign Scheduling")
@allure.story("Create a new campaign")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_campaign():
    with allure.step("Fetch campaign details and create campaign"):
        response, status_code = campaign_service.create_campaign(
            NameGenerator.generate_campaign_name(), "EM-001", "RL-001", 10
        )
        campaign_id = response["data"]["id"]

    with allure.step("Verify response"):
        assert status_code == 201, f"Expected 201, got {status_code}"
        assert campaign_id is not None, "Campaign ID should be returned"


@allure.feature("Campaign Scheduling with existing name")
@allure.story("Create campaign with existing campaign name")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_duplicate_campaign():
    campaign_name = NameGenerator.generate_campaign_name_short()
    with allure.step("Create a campaign the first time"):
        campaign_service.create_campaign(campaign_name, "EM-001", "RL-001", 10)

    with allure.step("Create a duplicate campaign"):
        response, status_code = campaign_service.create_campaign(
            campaign_name, "EM-001", "RL-001", 10
        )

    with allure.step("Verify response"):
        assert status_code == 409, f"Expected 409, got {status_code}"
        assert (
            response["meta"]["status"] == "FAILURE"
        ), "Expected successful campaign creation"


@allure.feature("Campaign Scheduling")
@allure.story("Edit the name of a scheduled campaign")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_campaign_name():
    with allure.step("Create a campaign first"):
        # response, status_code, campaign_id = campaign_service.create_campaign(
        response, status_code = campaign_service.create_campaign(
            NameGenerator.generate_campaign_name(), "EM-001", "RL-001", 10
        )
        campaign_id = response["data"]["id"]
        print(f"response : {response}")
        print(f"campaign id : {campaign_id}")
        assert status_code == 201, f"Expected 201, got {status_code}"

    with allure.step("Edit campaign name"):
        response, status_code = campaign_service.edit_campaign_name(
            campaign_id, NameGenerator.generate_campaign_name()
        )

    with allure.step("Verify response"):
        assert status_code == 200, f"Expected 200, got {status_code}"
