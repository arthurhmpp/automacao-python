import os

location = "/home/arthurhmp/Downloads/"

full_list = os.listdir(location)

file_list = [i for i in full_list if os.path.isfile and '.py' not in i]

types = list(set([i.split('.')[-1] for i in file_list]))

for file_types in types:
    os.mkdir(location + file_types)

for file in file_list:
    from_path = os.path.join(location, file)
    to_path = os.path.join(location, file.split('.')[-1], file)

    os.replace(from_path, to_path)