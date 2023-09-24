import json

filepath= r"JSON exercise\my_first_json.json"

person = {"name": "Amin abdul Awal",
          "age": 22,
          "Married": False,
          "Job status": "looking for work",
          "hobbies": ["reading", "running","jiu jitsu"]
          }

with open(filepath, "r") as json_file:
    G = json.load(json_file)


G["highest education level"] = "banchelor's degree"

with open(filepath, "w") as json_file:
     json.dump(G,json_file,indent=4)

