import threading
import time

def thread_process(id):
    print(f"Thread_Process {id}: comenzando")
    time.sleep(10)
    print(f"Thread {id}: terminando")

def thread_animation(id):
    clock=0
    while True:
        clock+=1
        time.sleep(1)
        print(f"thread_animation {id}: {clock}")

if __name__ == "__main__":
    print("Main    : Antes de crear el thread de procesos")
    x = threading.Thread(target=thread_process, args=(1,))
    y = threading.Thread(target=thread_animation, args=(2,),daemon=True)
    print("Main    : Antes de lanzar el thread de procesos")
    x.start()
    y.start()
    print("Main    : Esperar a que hilo termine")
    x.join()
    print("Main    : Los procesos han terminado")