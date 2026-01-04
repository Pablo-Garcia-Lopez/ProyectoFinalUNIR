import requests

BASE_URL = "http://127.0.0.1:5000"

def add_data():
    name = input("Input name: ")
    response = requests.post(f"{BASE_URL}/data", json={"name": name})
    print("Response:", response.json())

def delete_data():
    data_id = input("Input the id to delete: ")
    response = requests.delete(f"{BASE_URL}/data/{data_id}")
    if response.status_code == 204:
        print("Element deleted successfully")
    else:
        print("Error:", response.text)

def list_data():
    response = requests.get(f"{BASE_URL}/data")
    print("Current data:")
    for item in response.json():
        print(f"- {item['id']}: {item['name']}")

def edit_data():
    data_id = input("Input the id to edit: ")
    name = input("New name: ")
    response = requests.put(
        f"{BASE_URL}/data/{data_id}",
        json={"name": name}
    )
    if response.status_code == 200:
        print("Element updated:", response.json())
    else:
        print("Error:", response.text)


def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. Add data")
        print("2. Delete data")
        print("3. List data")
        print("4. Edit data")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            add_data()
        elif option == "2":
            delete_data()
        elif option == "3":
            list_data()
        elif option == "4":
            edit_data()
        elif option == "5":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
