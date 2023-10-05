# py_screenshot

simple python script captures screenshots at regular intervals and uploads them to imgur. the imgur link is then sent to a discord channel using a webhook.

## why imgur?

due to discord webhooks not directly supporting the upload of images, imgur is utilized as an intermediary platform to host the screenshots before sharing them in the discord channel.

## requirements

- python 3.x
- required python packages: `pyautogui`, `imgurpython`, `requests`
- imgur account and api credentials (client id and client secret)
- discord server with a webhook url

## configuration

1. install dependencies: `pip install pyautogui imgurpython requests`
2. [visit imgur developer and create an application to obtain the client id and client secret.](https://api.imgur.com/oauth2/addclient)
3. obtain discord webhook url

## usage

1. run the script: `python py_screen.py`
2. script will take a screenshot, upload it to imgur, and send the imgur link to the specified discord channel via the webhook.
3. screenshots are taken at regular intervals (20 min by default). you can adjust this interval in the `time.sleep()` function in the `main()` method.

## disclaimer

this script is for educational and demonstration purposes only. do not use it to violate privacy or engage in any unethical activities. use it responsibly and respect the privacy of others.
