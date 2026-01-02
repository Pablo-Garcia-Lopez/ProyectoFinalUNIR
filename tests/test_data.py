def test_add_data(client):
    print("test_add_data")

    response = client.post(
        "/data",
        json={"name": "Test"}
    )

    print(response.get_json())

    assert response.status_code == 200

    response = client.get("/data")
    data = response.get_json()

    print(data)

    assert any(item["name"] == "Test" for item in data)
    print("----------")

def test_insert_duplicate(client):
    print("test_insert_duplicate")

    response = client.post(
        "/data",
        json={"name": "Test"}
    )

    response = client.post(
        "/data",
        json={"name": "Test"}
    )

    print(response.get_json())

    assert response.status_code == 409
    print("----------")

def test_delete_data(client):
    print("test_delete_data")

    response = client.post(
        "/data", 
        json={"name": "Test"}
        )
    assert response.status_code == 200
    response = client.get("/data")
    data = response.get_json()
    print(data)
    data_id = data[0]["id"] #We now know there's only one entry

    delete_response = client.delete(f"/data/{data_id}")
    assert delete_response.status_code == 200
    print(delete_response.get_json())

    response = client.get("/data")
    data = response.get_json()
    print(data)
    assert len(data) == 0
    print("----------")

def test_delete_nonexistant(client):
    print("test_delete_nonexistant")

    delete_response = client.delete(f"/data/0")
    assert delete_response.status_code == 404
    print(delete_response.get_json())
    print("----------")

def test_update_data(client):
    print("test_update_data")

    response = client.post(
        "/data", 
        json={"name": "Test"}
        )
    assert response.status_code == 200

    response = client.get("/data")
    data = response.get_json()
    print(data)

    data_id = data[0]["id"]
    update_response = client.put(
        f"/data/{data_id}",
        json={"name": "Updated Test"}
    )
    assert update_response.status_code == 200
    print(update_response.get_json())

    response = client.get("/data")
    data = response.get_json()
    print(data)
    assert data[0]["name"] == "Updated Test"
    print("----------")

def test_update_nonexistant(client):
    print("test_update_nonexistant")

    update_response = client.put(
        f"/data/0",
        json={"name": "Updated Test"}
    )
    assert update_response.status_code == 404
    print(update_response.get_json())
    print("----------")