import os

location = "/home/arthurhmp/Downloads/"

folder_list = [i for i in os.listdir(location) if os.path.isdir(os.path.join(location, i))]

for folder in folder_list:
    path = os.path.join(location, folder)
    files = os.listdir(path)

    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(location,file)
        os.replace(from_path, to_path)
    os.rmdir(path)
