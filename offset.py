import json

def load_from_json():
	with open('offsets.json', 'rb') as f:
		return json.load(f)

def save_to_json(offsets):
	with open('offsets.json', 'wb') as f:
		f.write(json.dumps(offsets))

__offsets = load_from_json()

x = __offsets[0]
y = __offsets[1]

