import platform
import psutil


def gather_system_info():
    print("--- System Diagnostics ---")
    print(f"Operating System: {platform.system()}")
    print(f"OS Release: {platform.release()}")

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")

    if cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
        print("WARNING: System resource usage is high!")


if __name__ == "__main__":
    gather_system_info()