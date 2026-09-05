import os
import shutil
import colorama

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

shutil.copytree("Roshan System - Python Version/textures", "Roshan System - C++ Version/textures", dirs_exist_ok=True)
print(colorama.Fore.BLUE + "Copied textures from the python version to the C++ version" + colorama.Fore.RESET)