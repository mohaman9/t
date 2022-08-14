from telethon import TelegramClient, event
import requests

url = "https://cloudapiintegration.com/api/send.php"

print("Starting...")

APP_ID = 1606224
API_HASH = 64bafa6339b5f81cbbdc0d5526c1d396
SESSION = 1AZWarzsBuy1txvLkUsgzCc5TfYTh0GSpnJ_maYonkvi4c98XSV92UybyRjJXRZsAE2o7MIg-4j9xwrGpUq5rrjc5LL5Hcra9NyHpFEHnVrKUEoFhLfNiTh-wI3I9w8Fa-YoKup4XPVpLNZAuQc4pmL2u3JeUT3ZZAVoS2U6zwieTak_MtjJF8RaqiToFNAOl8v0-J1rxvyFSYsMZsNTT15-iqbZSWUKIFTXA8rGnLiGfk3RSY_KQZi_tV7ECmkuB8AXYLv7nnTD0kkbejOxqlVeP7H1W7kcFulLODOn9m5WP8A1d_0oWTBKRYOZcLyHOm6ysuWQKH1CMcJjRp0GXbgqKsPf3FR4=
FROM_ = tessstting from

bot = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    
bot.start()


@bot.on(events.NewMessage(incoming=True, chats=FROM))

async def sender_bH(event):
    querystring = {"access_token":"3c513317d6cc9db4e29d9e536bac0647","instance_id":"62F805E73E8A3","number":"917022504503","message":str(event.text),"type":"text"}

    response = requests.request("POST", url, params=querystring)

    print(response.text)


print("Bot has started.")
BotzHubUser.run_until_disconnected()
