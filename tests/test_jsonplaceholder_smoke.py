import allure
import pytest

from api_clients.jsonplaceholder_client import JSONPlaceholderClient


@allure.epic("API Platform")
@allure.feature("Users")
@allure.story("List users")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("GET /users returns list with users")
@allure.label("owner", "raMoliner")
@allure.tag("smoke", "api")
@pytest.mark.smoke
def test_list_users_returns_data():
    client = JSONPlaceholderClient()

    with allure.step("Call GET /users"):
        r = client.list_users()

    with allure.step("Validate status code"):
        assert r.status_code == 200, f"Expected 200, got {r.status_code}. Body: {r.text[:200]}"

    with allure.step("Validate response schema (basic)"):
        data = r.json()
        assert isinstance(data, list), "Expected list"
        assert len(data) > 0, "Expected at least 1 user"
        assert "id" in data[0] and "email" in data[0], "Expected keys id,email in first user"


@allure.epic("API Platform")
@allure.feature("Posts")
@allure.story("Get post")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("GET /posts/1 returns post id=1")
@allure.label("owner", "raMoliner")
@allure.tag("smoke", "api")
@pytest.mark.smoke
def test_get_post_returns_expected_id():
    client = JSONPlaceholderClient()

    with allure.step("Call GET /posts/1"):
        r = client.get_post(1)

    assert r.status_code == 200, f"Expected 200, got {r.status_code}. Body: {r.text[:200]}"
    body = r.json()
    assert body["id"] == 1, f"Expected id=1, got {body.get('id')}"


@allure.epic("API Platform")
@allure.feature("Posts")
@allure.story("Create post")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("POST /posts returns created object")
@allure.label("owner", "raMoliner")
@allure.tag("smoke", "api")
@pytest.mark.smoke
def test_create_post_returns_created_payload():
    client = JSONPlaceholderClient()

    with allure.step("Call POST /posts"):
        r = client.create_post(title="hello", body="world", user_id=1)

    # JSONPlaceholder “finge” creación: suele devolver 201 + objeto con id
    assert r.status_code in (201, 200), f"Expected 201/200, got {r.status_code}. Body: {r.text[:200]}"
    payload = r.json()
    assert payload.get("title") == "hello"
    assert payload.get("body") == "world"
    assert payload.get("userId") == 1
    assert "id" in payload, "Expected id in response"
