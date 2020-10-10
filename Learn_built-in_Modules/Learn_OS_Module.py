import os

print(dir(os))     # return all the attributes in the given module name

print(os.getcwd())  # its return current path
        # C:\Users\gopir\PycharmProjects\Python_Oops\Learn_built-in_Modules

os.chdir('D:/')     # its change working dir

print(os.getcwd())

print(os.listdir())

#os.mkdir('zzz')     # create the folder in current active path
#
# print(os.listdir())

#os.makedirs('qqq/hello')

#print(os.listdir())

#os.rmdir('zzz')

#os.removedirs('qqq/hello')

print(os.stat('z.txt'))
print("*" * 20)
#walk()
for dirpath, dirs, files in os.walk('D:\AWS'):
    print(dirpath)
    print(dirs)
    print(files)
    print("*"*20)
