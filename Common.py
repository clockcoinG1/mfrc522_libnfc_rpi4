
from serial.tools import list_ports

continue_reading = True

def print_hex(prompt, data, end=None):
    print(prompt + ' '.join(['%02x' % x for x in data]), end=end)

def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, exit...")
    continue_reading = False
    exit()

def should_read():
    return continue_reading

def auto_find_port():
    return 0
