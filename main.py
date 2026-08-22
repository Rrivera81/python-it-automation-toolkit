import platform

def gather_system_info():
    print("--- System Diagnostics ---")
    print(f"Operating System: {platform.system()}")
    print(f"OS Release: {platform.release()}")

if __name__ == "__main__":
    gather_system_info()