import json

x = {
  "name": "Peter",
  "alter": 30,
  "verheiratet": True,
  "geschieden": False,
  "kinder": ("Anna","Maxi"),
  "tiere": None,
  "autos": [
    {"model": "BMW 320", "ps": 220},
    {"model": "VW Golf", "ps": 150}
  ]
}

print(json.dumps(x, indent=4))