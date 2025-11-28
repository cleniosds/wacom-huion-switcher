import os
import sys
import ctypes
import subprocess

SERVICE = "WTabletServicePro"

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

def get_status():
    try:
        result = subprocess.check_output(f'sc query "{SERVICE}"', shell=True, text=True)
        if "RUNNING" in result:
            return "RUNNING"
        elif "STOPPED" in result:
            return "STOPPED"
        else:
            return "UNKNOWN"
    except:
        return "ERROR"

def start_service():
    print("\nStarting service...")
    os.system(f'net start "{SERVICE}"')
    print("Done.\n")

def stop_service():
    print("\nStopping service...")
    os.system(f'net stop "{SERVICE}"')
    print("Done.\n")

def main():
    while True:
        status = get_status()
        print("\n=== Service Control ===")
        print(f"Service: {SERVICE}")
        print(f"Current status: {status}")
        print("---------------------------")
        print("1 - Start service")
        print("2 - Stop service")
        print("0 - Exit")

        op = input("Choose: ")

        if op == "1":
            start_service()
        elif op == "2":
            stop_service()
        elif op == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
