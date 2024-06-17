import pytest
from django.test import override_settings
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.parametrize("token", [None, "invalid-token"])
def test_invalid_auth(client, token):
    response = client.get(reverse("dump-data"), headers={"Authorization": token})
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid or missing API key"}


@override_settings(API_KEY="mock-api-token")
def test_trigger_dump_data(mocker, client):
    # mock the delay method for data dump
    mock_dump = mocker.patch(
        "common.tasks.dump_data_to_csv.dump_data_to_csv.delay",
        return_value=mocker.Mock(id="mock-task-id"),
    )

    response = client.post(
        reverse("dump-data"), headers={"Authorization": "mock-api-token"}
    )

    # assert the API response
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "message": "Data dumped in progress.",
    }

    # assert the task was enqueued
    mock_dump.assert_called_once()
