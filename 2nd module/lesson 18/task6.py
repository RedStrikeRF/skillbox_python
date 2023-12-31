import json

# Load JSON files
with open('json_old.json', encoding="utf-8") as json_file1:
    json1_dict = json.load(json_file1)

with open('json_new.json', encoding="utf-8") as json_file2:
    json2_dict = json.load(json_file2)

diff_list = ["services", "staff", "datetime"]

# Compare the parts specified in diff_list and print the differences
result = {}
for key in diff_list:
    if json1_dict['data'][key] != json2_dict['data'][key]:
        result[key] = {
            'old_value': json1_dict['data'][key],
            'new_value': json2_dict['data'][key]
        }

print(result)

# Write the differences to a result.json file
with open('result.json', 'w', encoding="utf-8") as outfile:
    json.dump(result, outfile)