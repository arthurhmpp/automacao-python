import os

os.getcwd()

os.listdir()

os.listdir("/home/arthurhmp/")

#os.chdir
actual_dir = os.getcwd()
os.chdir("/home/arthurhmp/")
print(os.getcwd())
os.chdir(actual_dir)
print(os.getcwd())

os.mkdir("pasta2")

os.rename("teste.txt", "teste2.txt")
os.rename("pasta3", "pasta/pasta4")
os.rename("pasta/pasta4", "pasta2"  )

os.remove("pasta")

os.remove("teste2.txt")

os.rmdir("pasta2")

cmd = "date"
os.system(cmd)