#importing the operating system commands module
import os


print(os.system('gcc hello.c -o hello'))
print(os.system('./hello'))
ask_delete = input("Delete program: ")

if ask_delete == "yes":
    print(os.system('rm -rf hello'))
elif ask_delete == 'no':
    print("Shuting down!")

