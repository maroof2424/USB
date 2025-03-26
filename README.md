# USB Backup Script

This script automatically detects when a USB drive is connected and copies its contents to a specified backup folder on your computer.

## Features
- Automatically detects USB connection
- Copies all files and folders from USB to a specified backup location
- Works on Windows, Linux, and macOS
- Monitors for new USB devices in real-time

## Requirements
- Python 3.x
- `psutil` package (install using `pip install psutil`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/usb-backup.git
   cd usb-backup
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script:
```bash
python usb_backup_script.py
```
It will continuously monitor for USB devices and copy their contents when detected.

## Configuration
You can change the backup location by modifying the `DESTINATION_FOLDER` variable in `usb_backup_script.py`:
```python
DESTINATION_FOLDER = "C:\\USB_Backup"
```


