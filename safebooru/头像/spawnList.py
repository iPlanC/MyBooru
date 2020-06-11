import os

print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__)) + "\\data.json", "w", encoding="utf-8") as file:
    file.write("[\n")
    result = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    for resource in result:
        file.write("\"")
        file.write(resource)
        file.write("\", \n")
    file.write("\"end_of_list\"\n]")
