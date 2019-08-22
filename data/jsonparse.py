import json

""" To Iterate through the dictionary 

for id, info in data.items():
    for item in info:
        print(item + ':', info[item])
    print('---')
    
 """


def readJSON(file):
    # Returns dictionaries from JSON
    try:
        with open(file, "r") as read_file:
            return json.load(read_file)
    except ValueError as e:
        print("Error: " + str(e))


def writeJSON(data, file):
    # Writes dictionary to JSON
    try:
        with open(file, "w") as write_file:
            json.dump(data, write_file)
    except IOError:
        print("Error: File does not exist")


def appendJSON(newData, file):
    # Adds an entry to JSON
    data = readJSON(file)
    data[len(data) + 1] = newData
    writeJSON(data, file)


def deleteJSON(id, file):
    # Deletes entry from JSON
    data = readJSON(file)
    del data[id]


def editJSON(id, newData, file):
    # Edits an entry in JSON
    data = readJSON(file)
    data[id] = newData
    writeJSON(data, file)
