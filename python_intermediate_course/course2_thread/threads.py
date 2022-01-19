## python3
import threading
## conventionly, package uses lower.case but class or function is called by captial of the initial character 
## python2 a depracted package
#import _thread 

import time


def func(amount):
	print('Start')
	time.sleep(amount)
	print(f'I slept for {amount}')
	print('End')

## make sure the target only take the name of the function without the ()
## also you will need to use self.start to kick off the process
## single thread

#t1 = threading.Thread(target=func)
#t1.start()

print(threading.active_count())

threads = []
for i in range(5):
	t1 = threading.Thread(target=func,args=(i,))
	threads.append(t1)
	t1.start() ## kick off the task
	#t1.join() ## each thread until the previous one finish (sequentially)

for thread in threads:
	thread.join()


print(threading.active_count())
