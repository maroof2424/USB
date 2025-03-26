import os
import shutil
import psutil
import time

# Destination folder to copy USB contents
DESTINATION_FOLDER = "C:\\USB_Backup"  # Change this as needed

# Ensure the destination folder exists
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

def get_usb_drive():
    """Find the first USB drive connected (Windows & Linux/macOS)."""
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'removable' in partition.opts or ('/media/' in partition.mountpoint or '/run/media/' in partition.mountpoint):
            return partition.mountpoint  # Return USB mount path
    return None

def copy_files(source, destination):
    """Copy all files from the USB to the destination folder."""
    try:
        if not os.path.exists(source):
            print("USB drive not found!")
            return

        usb_name = os.path.basename(os.path.normpath(source))  # Get USB name
        target_path = os.path.join(destination, usb_name)

        print(f"Copying files from {source} to {target_path}...")
        shutil.copytree(source, target_path, dirs_exist_ok=True)
        print("✅ Copy complete!")
    except Exception as e:
        print(f"⚠️ Error copying files: {e}")

def monitor_usb():
    """Monitor for USB connection and copy files automatically."""
    print("🔍 Monitoring for USB devices...")

    previous_drives = {p.device for p in psutil.disk_partitions()}

    while True:
        current_drives = {p.device for p in psutil.disk_partitions()}
        new_drives = current_drives - previous_drives  # Detect newly connected drives

        if new_drives:
            print("✅ USB device detected!")
            usb_drive = get_usb_drive()
            if usb_drive:
                copy_files(usb_drive, DESTINATION_FOLDER)
            else:
                print("⚠️ USB drive letter not found!")

        previous_drives = current_drives
        time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    monitor_usb()
