import requests

# Define your API key
api_key = "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"

# Make a GET request to a sample endpoint
url = "https://api.example.com/some-endpoint"
headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

# Check the authentication bearer
if "Authorization" in response.request.headers:
    auth_header = response.request.headers["Authorization"]
    bearer_token = auth_header.split(" ")[1]
    print(f"Bearer token: {bearer_token}")
else:
    print("Bearer token not found in the request headers.")
