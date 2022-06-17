import sys
from cx_Freeze import setup, Executable

build_exe_options = ["tkinter"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"    

executables = [Executable("main.py", base=base)]

packages = ["idna", "os"]

options = {
    'build_exe': {    
        'packages':packages,
        'includes':build_exe_options

    },    
}

setup(
    name = "Minha Biblioteca",
    options = options,
    version = "1.0",
    description = 'Gerenciador de bibliotecas',
    executables = executables
)