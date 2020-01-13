
import os
import platform
import subprocess
import sys

def pp():
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    # Light passthrough
    subprocess.run([pp_exe_path] + args)

def main():
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    # Light passthrough
    subprocess.run([hashcat_exe_path] + args)

bits = platform.architecture()[0][:-3]
ext = ".exe" if platform.uname().system == "Windows" else ".bin"

here = os.path.dirname(os.path.realpath(__file__))

# hashcat
hashcat_dir = os.path.join(here, "hashcat")
hashcat_exe = "hashcat"  + bits + ext
hashcat_exe_path = os.path.join(hashcat_dir, hashcat_exe)

# pp64
pp_dir = os.path.join(here, "pp")
pp_exe = "pp64"  + ext
pp_exe_path = os.path.join(pp_dir, pp_exe)

if __name__ == "__main__":
    main()
