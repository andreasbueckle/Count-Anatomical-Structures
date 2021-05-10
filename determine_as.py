import json
from os import listdir

# download all JSON files into same directory as this py file
# get file names from directroy
all_filenames = listdir()
json_filenames = []
for i in all_filenames:
    if "json" in i:
        json_filenames.append(i)

# created nested list of cc_annotations
anatom_struct = []
for j in json_filenames:
    with open(j, "r") as current_file:
        data = json.load(current_file)
        anatom_struct.append(data["ccf_annotations"])

# flatten into one list
flattened_list = []
for m in anatom_struct:
    for n in m:
        flattened_list.append(n)

# get counts for each element
dict = {}
for k in flattened_list:
    if k in dict.keys():
        dict[k] = dict[k] + 1
    else:
        dict[k] = 1

# print results and compare counts to length of flattened_list
sum = 0
for item in dict:
    sum = sum + dict[item]
    print(str(item) + " was found " + str(dict[item]) + " times.")
    print()
print("Total #AS: " + str(sum))
print("Counts: " + str(len(flattened_list)))
print("Total #AS is equal to counts: " + str(sum == len(flattened_list)))



