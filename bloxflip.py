import requests

auth_token = input("Please enter your auth token: ")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "X-Auth-Token": auth_token
}

url = "https://api.bloxflip.com/user"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    if data.get("success", False):
        roblox_id = data.get("robloxId")
        roblox_username = data.get("robloxUsername")
        if roblox_id is not None and roblox_username is not None:
            print(f"Your Roblox ID is: {roblox_id}")
            print(f"Your Roblox username is: {roblox_username}")
        else:
            print("Roblox ID or Roblox username not found in response.")
    else:
        print("Request was not successful.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
