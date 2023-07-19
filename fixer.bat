@echo off
echo Installing python import requirements...
color 1
pip install opencv-python
pip install PyObfuscator
pip install robloxpy
pip install browser_cookie3
pip install wmi
pip install getmac
pip install psutil
pip install netifaces
pip install pynput
pip install pycryptodome
pip install Pillow
pip install uuid
pip install pyinstaller
cls
color 4
cd requirements
echo installing WinRAR....
curl -O https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-622.exe
echo running WinRAR installer...
winrar-x64-622.exe
echo Done Installing WinRAR! 
set /p choice=Do you have a 64 bit PC?(Y/N): 
set "choice=%choice:~0,1%"
set "choice=%choice:~0,1%"
if /i "%choice%"=="Y" (
    echo Great Installing 64 bit visual C++ Redistributable
    curl -O -L https://aka.ms/vs/17/release/vc_redist.x64.exe
    vc_redist.x64.exe
    echo Done installing visual C++ Redistributable!
) else if /i "%choice%"=="N" (
    echo Great Installing 32 bit visual C++ Redistributable
    curl -O -L https://aka.ms/vs/17/release/vc_redist.x86.exe
    vc_redist.x86.exe
    echo Done installing visual C++ Redistributable!
) else (
    echo Invalid choice. Please enter Y or N.
)
echo Done Installing requirements plase press any key to exit.
pause
exit
