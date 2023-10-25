import os

location = "/home/arthurhmp/Downloads/"

folder_list = [i for i in os.listdir(location) if not os.path.isfile(i)]

folder_list


for folder in folder_list:
    path = os.path.join(location, folder)
    files = os.listdir(path)

    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(location,file)
        os.replace(from_path, to_path)
    os.rmdir(path)
