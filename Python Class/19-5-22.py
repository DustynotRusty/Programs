from concurrent.futures import thread
import time
import threading


def cal_sqre(num):
    print('Calculate the sqaure of given number')
    for n in num:
        time.sleep(0.1)
        print('Square is: ', n*n)


def cal_cube(num):
    print('Calculate the cube of the given number: ')
    for n in num:
        time.sleep(0.1)
        print('Cube is ', n*n*n)


ar = [4, 53, 2, 1, 2, 31, 9, 0, 8, 7642, 8531]
t = time.time()
th1 = threading.Thread(target=cal_sqre, args=(ar,))
th2 = threading.Thread(target=cal_cube, args=(ar,))
th1.start()
th1.join()
th2.start()
th2.join()
print('Total time taking by threads is', time.time()-t)
print('Again executing the main thread')
print('Thread 1 and Thread 2 have finished their execution')
