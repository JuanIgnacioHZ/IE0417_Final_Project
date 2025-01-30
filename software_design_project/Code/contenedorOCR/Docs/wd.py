import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from OCR import leer_voucher
from OCR import prueba
from DB import agregar_elemento_db
from os import popen, system

class OnMyWatch:
    # Obtiene la dirección para imágenes cargadas de la
    # variable de entorno photo_source_dir
    DirectorioVigilante =  (popen('echo $photo_source_dir', 'r').read().replace('\n', '').split(' '))[0]


    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DirectorioVigilante, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif (event.event_type == 'created'):
            # Event is created, you can process it now
            print("Nueva imagen detectada: ",  event.src_path)
            procesar_imagen(event.src_path)

def procesar_imagen(imagen):

    # Obtiene el directorio de destinao
    DirectorioDestino =  (popen('echo $photo_processed_dir', 'r').read().replace('\n', '').split(' '))[0]

    # Empieza por agregar los datos a la base de datos
    agregar_elemento_db(leer_voucher(imagen))

    # Luego, mueve la imagen obtenida al directorio
    # donde se salvan las fotos ya procesadas
    cmd = str('mv ' + imagen + ' ' + DirectorioDestino)
    system(cmd)

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()

# Referencia:
# https://www.geeksforgeeks.org/create-a-watchdog-in-python-to-look-for-filesystem-changes/

