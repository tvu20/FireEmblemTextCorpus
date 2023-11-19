import os
import json
import glob

speakers_file_path = os.path.join(os.getcwd(), "data", "FE9", "speakers_cleaned.json")

output_path = os.path.join(os.getcwd(), "data", "FE9", "cooccurence.json")

books = ["FE9"]

file_content = {
    "nodes": [],
    "links": []
}

labels = {

}

existing_pairs = []

with open(speakers_file_path) as f:
    content = json.load(f)

    file_content["nodes"] = content["descriptions"]

    for i in range(len(content["descriptions"])):
        item = content["descriptions"][i]
        labels[item["name"]] = i

for book in books:
    input_path = os.path.join(os.getcwd(), "data", book, "chapters")

    for filename in glob.glob(os.path.join(input_path, "*.json")):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = json.load(f)

            speakers = data["speakers"]

            list_of_pairs = [(speakers[p1], speakers[p2]) for p1 in range(len(speakers)) for p2 in range(p1+1,len(speakers))]

            # print(list_of_pairs)

            for (p1, p2) in list_of_pairs:
                # invalid character
                if p1 not in labels or p2 not in labels:
                    continue

                # doesn't exist
                if (p1, p2) not in existing_pairs and (p2, p1) not in existing_pairs:
                    existing_pairs.append((p1, p2))
                    file_content["links"].append({ "source": labels[p1], "target": labels[p2], "value": 1 })

                # first order
                elif (p1, p2) in existing_pairs:
                    pair_index = existing_pairs.index((p1, p2))
                    file_content["links"][pair_index]["value"] += 1

                # second order
                elif (p2, p1) in existing_pairs:
                    pair_index = existing_pairs.index((p2, p1))
                    file_content["links"][pair_index]["value"] += 1


with open(output_path, "w+") as f:
    # json.dump(existing_pairs,f)
    json.dump(file_content, f)