import os
import json

files = ["FE16/AzureMoon", "FE16/CrimsonFlower", "FE16/SilverSnow", "FE16/VerdantWind", "FE16/WhiteClouds"]

output_path = os.path.join(os.getcwd(), "data", "FE16", "speakers.json")

input_path = os.path.join(os.getcwd(), "data")


names = []

file_content = {
    "descriptions": [],
    "counts": {}
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


with open(output_path, "w+") as f:
    sorted_counts = sorted(file_content["counts"].items(), key=lambda x:x[1], reverse=True)

    file_content["counts"] = dict(sorted_counts)
    json.dump(file_content, f)
