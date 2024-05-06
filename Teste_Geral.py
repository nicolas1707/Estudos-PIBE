import sys

os = sys.platform
if os == "win32":
        # use Window-related code here
        print('Windows')
        import winreg

elif os == "linux": 
        # do something Linux specific
        import subprocess
        subprocess.Popen(["w", "--help"])
