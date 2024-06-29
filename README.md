## Keylogger Script

This Python script uses the `pynput` library to log keystrokes and sends the data to an FTP server. It listens for keystrokes, logs them to a file, and transfers the log file to a specified FTP server.

## Requirements
- Python 3.x
- `pynput` library
- FTP server access

## Installing pynput
```bash
pip install pynput
```

## Usage 
1.) Save the script to a file, for example keylogger.py.

2.) Run the script:
```
python keylogger.py
```
3.) The script will start logging keystrokes and save them to klog-res.txt.

4.) Upon termination, it connects to the FTP server and uploads klog-res.txt.
