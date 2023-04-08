""""
    Only works with text. 
    Running the script will send your clipboard contents to discord using the webhook.

    You can do more automation: Make a batch file which runs this script, make a shortcut to it and add windows
    shortcut which runs the batch file (You can also make it run in minimized window).
"""


import win32clipboard
import discord_webhook

webhook = discord_webhook.DiscordWebhook(
    url="your webhook url"
)

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

webhook.set_content(content)
response = webhook.execute()