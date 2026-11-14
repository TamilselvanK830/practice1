
import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file")



try:
    headers = {
        "X-API-Key": API_KEY
    }

    response = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    received_key = data.get("headers", {}).get("X-Api-Key")

    print("Server received key:", received_key)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)



try:
    response = requests.get(
        "https://httpbin.org/delay/10",
        timeout=3
    )

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)


try:
    response = requests.get(
        "https://httpbin.org/status/500",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.HTTPError:
    if response.status_code == 500:
        print("Server error 500 handled")
    else:
        print("Other HTTP error:", response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")


try:
    response = requests.get(
        "https://httpbin.org/json",
        timeout=5
    )

    response.raise_for_status()

    json_data = response.json()

    slideshow = json_data.get("slideshow", {})

    title = slideshow.get("title", "No title")
    author = slideshow.get("author", "No author")
    slides = slideshow.get("slides", [])

    result = {
        "title": title,
        "author": author,
        "slides": slides
    }

    with open("result.json", "w") as file:
        json.dump(result, file, indent=2)

    print("Nested JSON saved successfully!")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

except json.JSONDecodeError:
    print("Invalid JSON response")
