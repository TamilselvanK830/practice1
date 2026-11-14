
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


response = requests.get(f"{BASE_URL}/users")

if response.status_code == 200:
    users = response.json()

    for user in users[:5]:
        print(
            f"{user['id']} - {user['name']} - {user['email']}"
        )


new_post = {
    "title": "Python Learning",
    "body": "Learning REST API using requests",
    "userId": 1
}

response = requests.post(
    f"{BASE_URL}/posts",
    json=new_post
)

post_data = response.json()

print(f"\nPOST: {response.status_code}, id: {post_data['id']}")


updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated complete post",
    "userId": 1
}

put_response = requests.put(
    f"{BASE_URL}/posts/1",
    json=updated_post
)


patch_data = {
    "title": "Partially Updated Title"
}

patch_response = requests.patch(
    f"{BASE_URL}/posts/1",
    json=patch_data
)


delete_response = requests.delete(
    f"{BASE_URL}/posts/1"
)

print(
    f"PUT: {put_response.status_code} | "
    f"PATCH: {patch_response.status_code} | "
    f"DELETE: {delete_response.status_code}"
)


response = requests.get(f"{BASE_URL}/posts/9999")

if response.status_code == 404:
    print(f"GET /posts/9999 -> {response.status_code} Not found")


def explain_status(code):

    messages = {
        200: "OK - Request successful",
        201: "Created - Resource created successfully",
        400: "Bad Request - Invalid request",
        401: "Unauthorized - Authentication required",
        404: "Not Found - Resource not found",
        500: "Internal Server Error - Server problem"
    }

    return messages.get(code, "Unknown status code")


print("\nStatus Code Explanations:")

for code in [200, 201, 400, 401, 404, 500]:
    print(code, ":", explain_status(code))
