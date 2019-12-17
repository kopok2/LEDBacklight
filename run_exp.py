import subprocess
from multiprocessing import Process
import time
def run_script(name):
    subprocess.call(["python", name])

if __name__ == '__main__':
    print("LED Backlight")
    print("Experiment no. "+str(int(open("expcount.txt", "r").read())+1))
    p = Process(target=run_script, args=('serial_read.py',))
    p1 = Process(target=run_script, args=('change_read.py',))
    p.start()
    p1.start()
    p1.join()
    open("killme.txt", "w").write("killme")
    p.join()
    time.sleep(1)
    open("killme.txt", "w").write("")
    exp = str(int(open("expcount.txt", "r").read())+1)
    open("expcount.txt", "w").write(exp)
    
    run_script("merger.py")
