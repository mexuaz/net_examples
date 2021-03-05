import requests, json

if __name__ == '__main__':
	name = input("Enter your firstname for search:")
	res = requests.get(f"http://localhost:8500/users/search?firstname={name}")
	if res.status_code != 200:
		raise RuntimeError(f"Error: {res.status_code}")
	info = res.json()
	
	for val in info:
		print("="*50)
		for k, v in val.items():
			print(k, v)

