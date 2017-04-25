import frida
import sys


def on_message(message, data):
    print message

jscode = "blabla get it from a file."
process = frida.get_usb_device()
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()