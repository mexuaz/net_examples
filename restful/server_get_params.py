from flask import Flask, json, request, jsonify
import re

api = Flask(__name__)


@api.route('/users/search', methods=['GET'])
def search():
	params = request.args
	with open('./db/users.json') as f:
		users = json.load(f)['users']
	ul = []
	for u in users:
		for k, v in params.items():
			if k in u.keys() and re.search(v, u[k], re.IGNORECASE):
				del u['username']
				del u['pass_sh1']
				ul.append(u)
	return jsonify(ul)


if __name__ == '__main__':
	# host=0.0.0.0 Listen on all public IPs
	api.run(host="localhost", port=8500, debug=False)
