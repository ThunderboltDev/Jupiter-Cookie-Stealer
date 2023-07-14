@echo off
echo Installing python import requirements...
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
cd requirements
echo installing WinRAR....
curl -O -L https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-622.exe
start winrar-x64-622.exe
echo Installing Microsoft Visual C++ Redistributable...
curl -O -L https://aka.ms/vs/17/release/vc_redist.x64.exe
start VC_redist.x64
echo Installing python.....
curl -O -L https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe
start python-3.10.9-amd64.exe
exit