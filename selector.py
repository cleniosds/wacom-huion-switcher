import os
import sys
import ctypes
import shutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Restarting with Administrator privileges...")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WACOM_SYS32 = os.path.join(BASE_DIR, "Wacom", "System32", "Wintab32.dll")
WACOM_SYS64 = os.path.join(BASE_DIR, "Wacom", "SysWOW64", "Wintab32.dll")

HUION_SYS32 = os.path.join(BASE_DIR, "Huion", "System32", "wintab32.dll")
HUION_SYS64 = os.path.join(BASE_DIR, "Huion", "SysWOW64", "wintab32.dll")

DEST_SYS32 = r"C:\Windows\System32\Wintab32.dll"
DEST_SYS64 = r"C:\Windows\SysWOW64\Wintab32.dll"

def copy_file(source, destination):
    try:
        shutil.copy2(source, destination)
        print(f"[OK] Copied: {source} → {destination}")
    except Exception as e:
        print(f"[ERROR] {e}")

def apply_wacom():
    print("\nApplying Wacom DLLs...")
    copy_file(WACOM_SYS32, DEST_SYS32)
    copy_file(WACOM_SYS64, DEST_SYS64)
    print("Done!\n")

def apply_huion():
    print("\nApplying Huion DLLs...")
    copy_file(HUION_SYS32, DEST_SYS32)
    copy_file(HUION_SYS64, DEST_SYS64)
    print("Done!\n")

def main():
    while True:
        print("\n=== Wintab DLL Selector ===")
        print("1 - Use Wacom DLL")
        print("2 - Use Huion DLL")
        print("0 - Exit")

        op = input("Choose: ")

        if op == "1":
            apply_wacom()
        elif op == "2":
            apply_huion()
        elif op == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
