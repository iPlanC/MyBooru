import os
import sys

type = sys.getfilesystemencoding()
print("generateing..")
folders = os.listdir(os.path.dirname(os.path.realpath(__file__)))
for each_path in folders:
    try:
        with open(each_path + "\\data.json", "w", encoding="utf-8") as file:
            file.write("[\n")
            result = os.listdir(each_path)
            result.remove("data.json")
            try:
                # result.sort(key= lambda x:int(x[:-4]))
                result.sort()
            except ValueError:
                print("1\t" + os.path.realpath(each_path) + "\\data.json")
                for resource in result:
                    if resource == "data.json" or resource == "spawnList.py" or resource == "desktop.ini":
                        continue
                    file.write("\"")
                    file.write(resource)
                    file.write("\", \n")
                file.write("\"end_of_list\"\n]")
            else :
                print("2\t" + os.path.realpath(each_path) + "\\data.json")
                for resource in result:
                    if resource == "data.json" or resource == "spawnList.py" or resource == "desktop.ini":
                        continue
                    file.write("\"")
                    file.write(resource)
                    file.write("\", \n")
                file.write("\"end_of_list\"\n]")
    except:
        continue
print("finished")
