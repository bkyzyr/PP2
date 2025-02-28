import json

with open("sample-data.json") as file:
    data = json.load(file)

print("interface status")
print("=" * 40)
print("DN")
print("-" * 40)

for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    print(dn)