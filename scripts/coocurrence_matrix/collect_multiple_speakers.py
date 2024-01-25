import os
import json

files = ["FE14/Main", "FE14/Paralogues"]

# files = ["FE16/AzureMoon", "FE16/CrimsonFlower", "FE16/SilverSnow", "FE16/VerdantWind", "FE16/WhiteClouds"]

output_path = os.path.join(os.getcwd(), "data", "FE14", "speakers.json")

input_path = os.path.join(os.getcwd(), "data")


names = []

file_content = {
    "descriptions": [],
    "counts": {},
    "genderCounts": {}
}

print("collating multiple speakers")

for file_path in files:
    filename = os.path.join(input_path, file_path, "speakers.json")
    # print(filename)
    with open(filename, 'r') as f:
        input = json.load(f)
        for i in range(len(input["descriptions"])):
            character_item = input["descriptions"][i]
            character_name = character_item["name"]
            # tester.append(character_name)


            # no duplicates
            if character_name not in names:
                names.append(character_name)
                file_content["descriptions"].append(character_item)
                file_content["counts"][character_name] = input["counts"][character_name]

            else:
                file_content["counts"][character_name] += input["counts"][character_name]

                # file_content.descriptions.append(item)

        for gender_tag in input["genderCounts"]:
            if gender_tag not in file_content["genderCounts"]:
                file_content["genderCounts"][gender_tag] = 0

            file_content["genderCounts"][gender_tag] += input["genderCounts"][gender_tag]


with open(output_path, "w+") as f:
    sorted_counts = sorted(file_content["counts"].items(), key=lambda x:x[1], reverse=True)

    file_content["counts"] = dict(sorted_counts)
    json.dump(file_content, f)
