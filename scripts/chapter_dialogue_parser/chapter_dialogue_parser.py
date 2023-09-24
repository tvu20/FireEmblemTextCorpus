import csv

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "age", "country"]
    
    writer.writerow(field)
    writer.writerow(["Oladele Damilola", "40", "Nigeria"])
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "United Kingdom"])

# with open('01-MarthEmbarks.txt', 'r') as f, open('01-MarthEmbarks.', 'w') as fo:
#     for line in f:
#         line = line.replace('"', '').replace('“', '').replace('”', '')
#         line = line.replace('…', '...')

#         split_string = line.split(':')
#         # print(split_string[1])
#         if len(split_string) > 1 and split_string[1][0] != " ":
#             split_string[1] = " " + split_string[1]

#         fo.write(':'.join(split_string))
#         # fo.write(line.replace('"', '').replace('“', '').replace('”', ''))