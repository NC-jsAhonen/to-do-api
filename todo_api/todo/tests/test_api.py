import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from todo.models import List, Item


@pytest.fixture
def auth_client(db):
    user = User.objects.create_user(username="testuser", password="pass")
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.mark.django_db
def test_create_list_item(auth_client):
    todo_list = List.objects.create()

    payload = {"text": "Buy milk", "list": todo_list.id}
    response = auth_client.post("/items/", payload, format="json")

    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "Buy milk"
    assert data["done"] is False
    assert data["list"] == todo_list.id
    assert Item.objects.count() == 1


@pytest.mark.django_db
def test_create_item_without_list_returns_error(auth_client):
    payload = {"text": "Buy eggs"} # no list provided

    response = auth_client.post("/items/", payload, format="json")

    # Should fail with 400 Bad Request
    assert response.status_code == 400
    data = response.json()
    assert "list" in data
    assert data["list"] == ["This field is required."]

    # No item should be created
    assert Item.objects.count() == 0


@pytest.mark.django_db
def test_get_list_with_items(auth_client):
    # Arrange: create list and items
    todo_list = List.objects.create()
    Item.objects.create(text="Buy milk", list=todo_list)
    Item.objects.create(text="Walk dog", list=todo_list)

    # Act: fetch the list
    response = auth_client.get(f"/lists/{todo_list.id}/", format="json")

    # Assert: response is OK and contains items
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == todo_list.id
    assert "items" in data
    assert len(data["items"]) == 2

    # Check that both items are in the response
    texts = [item["text"] for item in data["items"]]
    assert "Buy milk" in texts
    assert "Walk dog" in texts


@pytest.mark.django_db
def test_edit_list_item(auth_client):
    todo_list = List.objects.create()
    item = Item.objects.create(text="Old text", list=todo_list)

    payload = {"text": "Updated text"}
    response = auth_client.patch(f"/items/{item.id}/", payload, format="json")

    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Updated text"
    item.refresh_from_db()
    assert item.text == "Updated text"


@pytest.mark.django_db
def test_delete_list_item(auth_client):
    todo_list = List.objects.create()
    item = Item.objects.create(text="To be deleted", done=False, list=todo_list)

    response = auth_client.delete(f"/items/{item.id}/")

    assert response.status_code == 204
    assert Item.objects.count() == 0


@pytest.mark.django_db
def test_check_list_item(auth_client):
    todo_list = List.objects.create()
    item = Item.objects.create(text="Check me", done=False, list=todo_list)

    response = auth_client.patch(f"/items/{item.id}/check/", format="json")

    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True
    item.refresh_from_db()
    assert item.done is True
