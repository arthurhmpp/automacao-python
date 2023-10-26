import os

location = "/home/arthurhmp/Downloads/"

file_list = [i for i in os.listdir(location) if os.path.isfile(os.path.join(location, i))]

types = list(set([i.split('.')[-1] for i in file_list]))

for file_types in types:
    if os.path.isdir(location + file_types) == False:
        os.mkdir(location + file_types)

for file in file_list:
    from_path = os.path.join(location, file)
    to_path = os.path.join(location, file.split('.')[-1], file)

    os.replace(from_path, to_path)  