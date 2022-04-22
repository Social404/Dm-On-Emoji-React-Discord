import requests,os,discord,datetime
from capmonster_python import HCaptchaTask
from discord.ext import commands
from time import sleep
import json as js
from colorama import Fore

bot = commands.Bot(command_prefix="!", self_bot=True)

#with open("message.json", "r") as file:
#	message = js.load(file)

message = {"content": "**Hello eaglez  <user>  !\n\nMINT is LIVE !\n\nDon't miss the chance to MINT ! :eagle:  **||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| https://eaglezfly.com/"}

tokens = open("tokens.txt", "r").read().splitlines()

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")

print(f"""{Fore.RED}
░█▀█░█░█░▀█▀░█▀█░█▀▄░█▄█░░░█▀▀░█▄█░█▀█░▀▀█░▀█▀
░█▀█░█░█░░█░░█░█░█░█░█░█░░░█▀▀░█░█░█░█░░░█░░█░
░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀░░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀░░▀▀▀{Fore.RESET}\n""")

print(f"{Fore.YELLOW}[!] Loaded {len(tokens)} tokens{Fore.LIGHTBLACK_EX} (tokens.txt)\n")

token = input(f"{Fore.RED}Listener Token: {Fore.RESET}")
server_id = input(f"{Fore.RED}Server ID: {Fore.RESET}")
message_id = input(f"{Fore.RED}Message ID: {Fore.RESET}")
capmonster_apikey = input(f"{Fore.RED}CapMonster API KEY: {Fore.RESET}")
proxy = input(f"{Fore.RED}Proxy (username:password@ip:port): {Fore.RESET}")

if proxy != "":
  proxies = {
    "https": f"http://{proxy}"
  }
else:
  proxies = None

headers_fingerprint = {
    "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

headers_mass_dm = {
	"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
	"accept-language": "en-GB",
	"content-type": "application/json",
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
	"TE": "trailers"
}

def request_cookie():
	response1 = requests.get("https://discord.com")
	cookie = response1.cookies.get_dict()
	cookie['locale'] = "us"
	return cookie

def request_fingerprint():
	response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_fingerprint).json()
	fingerprint = response2["fingerprint"]
	return fingerprint

def request_snowflake():
	snakeflow = discord.utils.time_snowflake(datetime_obj=datetime.datetime.now())
	return snakeflow

def captcha_bypass(url, key, captcha_rqdata):
	print(f"{Fore.YELLOW}[DEBUG] {Fore.RESET}Trying to solve the captcha..")
	capmonster = HCaptchaTask(capmonster_apikey)
	capmonster.set_user_agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36")
	task_id = capmonster.create_task(url, key, is_invisible=True, custom_data=captcha_rqdata)
	result = capmonster.join_task_result(task_id)
	response = result.get("gRecaptchaResponse")
	print(f"{Fore.GREEN}[DEBUG] {Fore.RESET}Captcha solved {Fore.LIGHTBLACK_EX}({response[-32:]})")
	return response

def open_channel(authorization, userID):
	json_data = {'recipient_id': userID}
	headers_mass_dm['x-fingerprint'] = request_fingerprint()
	headers_mass_dm['authorization'] = authorization
	headers_mass_dm['x-context-properties'] = "e30="
	response3 = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers_mass_dm, cookies=request_cookie(), json=json_data, proxies=proxies, timeout=20).json()
	channel = response3["id"]
	return channel

def send_message(authorization, channel, msg, userID):
	snakeflow = request_snowflake()
	json = {'content': msg["content"], 'nonce': snakeflow, 'tts': "false"}
	headers_mass_dm['x-fingerprint'] = request_fingerprint()
	headers_mass_dm['authorization'] = authorization
	headers_mass_dm['referer'] = "https://discord.com/channels/@me/" + str(channel)
	response4 = requests.post("https://discord.com/api/v9/channels/" + str(channel) + "/messages", headers=headers_mass_dm, cookies=request_cookie(), data=js.dumps(json).replace("<user>", f"<@{userID}>").replace("<id>", f"{userID}"), proxies=proxies, timeout=20)
	if response4.status_code == 200:
		print(f"{Fore.LIGHTGREEN_EX}[+] DM Sent to {userID} {Fore.RESET}({Fore.LIGHTBLACK_EX}{authorization}{Fore.RESET}){Fore.RESET}")
	elif response4.status_code == 403:
		print(f"{Fore.LIGHTRED_EX}[!] Can't send to {userID} {Fore.RESET}({Fore.LIGHTRED_EX}DM Closed{Fore.RESET}){Fore.RESET}")
	elif response4.status_code == 400:
		print(f"{Fore.YELLOW}[DEBUG] {Fore.RESET}Captcha Detected {Fore.LIGHTBLACK_EX}({response4.json()['captcha_sitekey']})")
		json2 = {'captcha_key': captcha_bypass("https://discord.com", f"{response4.json()['captcha_sitekey']}", response4.json()['captcha_rqdata']), 'captcha_rqtoken': response4.json()['captcha_rqtoken'], 'content': msg["content"], 'nonce': snakeflow, 'tts': "false"}
		response5 = requests.post("https://discord.com/api/v9/channels/" + str(channel) + "/messages", headers=headers_mass_dm, cookies=request_cookie(), data=js.dumps(json2).replace("<user>", f"<@{userID}>").replace("<id>", f"{userID}"), proxies=proxies, timeout=20)
		if response5.status_code == 200:
			print(f"{Fore.LIGHTGREEN_EX}[+] DM Sent to {userID} {Fore.RESET}({Fore.LIGHTBLACK_EX}{authorization}{Fore.RESET}){Fore.RESET}")
		elif response5.status_code == 403:
			print(f"{Fore.LIGHTRED_EX}[!] Can't send to {userID} {Fore.RESET}({Fore.LIGHTRED_EX}DM Closed{Fore.RESET}){Fore.RESET}")
		else:
			print(response5.text)
	else:
		print(response4.text)

def check(token):
	headers_mass_dm['x-fingerprint'] = request_fingerprint()
	headers_mass_dm['authorization'] = token
	response = requests.get(f"https://discord.com/api/v9/users/@me/guilds", headers=headers_mass_dm, cookies=request_cookie(), proxies=proxies, timeout=20)
	if server_id in response.text:
		return True

def dm(token, userID, message):
	try:
		if check(token):
			channel = open_channel(token, userID)
			send_message(token, channel, message, userID)
			return True
		else:
			tokens.remove(token)
			print(f"{Fore.RED}[-] {token} | removed from the tokens pool{Fore.RESET}")
			bad = open("bad.txt", 'a')
			bad.write(token + "\n")
			bad.close()
	except Exception as err:
		print(err)
		pass

token_counter = 0
ratelimit_counter = 0

@bot.event
async def on_raw_reaction_add(reaction):
	global token_counter
	global ratelimit_counter
	if str(reaction.message_id) in message_id:
		reaction_id = str(reaction.user_id)
		if reaction_id not in open("sent.txt").read():
			file = open("sent.txt", 'a')
			file.write(reaction_id + "\n")
			file.close()
			dateTimeObj = datetime.datetime.now()
			timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M)")
			print(f"{Fore.YELLOW}[!] {reaction.member} | {reaction_id} reacted to the emoji{Fore.LIGHTBLACK_EX} | {timestampStr}{Fore.RESET}")
			while True:
				if token_counter >= int(len(tokens)):
						token_counter = 0
				if dm(tokens[token_counter], reaction.user_id, message):
					print(f"{Fore.BLUE}[!] {len(tokens)} tokens left{Fore.RESET}")
					ratelimit_counter += 1
					break
			if token_counter >= int(len(tokens)):
				token_counter = 0
			else:
				token_counter += 1
		if (ratelimit_counter >= int(len(tokens)) * 9):
			print(f"{Fore.YELLOW}[!] Sleeping for 800 seconds to avoid Ratelimit!{Fore.RESET}")
			sleep(800)
			ratelimit_counter = 0

bot.run(token)

# Not By Social404