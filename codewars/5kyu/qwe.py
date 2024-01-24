import time

def func():
    run = 5
    stopPoint = time.time() + run
    while True:
        print(run)
        time.sleep(1)
        run +=1
        if time.time() > stopPoint:
            break

func()