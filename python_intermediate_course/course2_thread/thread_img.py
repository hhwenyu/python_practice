## python3
import threading
## conventionly, package uses lower.case but class or function is called by captial of the initial character 
## python2 a depracted package
#import _thread 

import requests
import datetime
import random
import os

path = 'images'
isExist = os.path.exists(path)
if not isExist:
	os.makedirs(path)
	print(f'{path} foler is created!')
def download_images(images_amount):
	for num in range(images_amount):
		random_image = f'https://picsum.photos/id/{num}/1928/1888/'
		req = requests.get(random_image,stream=True)
		if req.status_code == 200:
			with open(f'images/{random.randint(1,100)}.png', 'wb') as f:
				for chunk in req:
					f.write(chunk)
			print(f'{num} downloaded!')
#stime = datetime.datetime.now()
#download_images(images_amount=20)
#etime = datetime.datetime.now()
#print(f'execuation time:{etime -stime}')

## make sure the target only take the name of the function without the ()
## also you will need to use self.start to kick off the process
## single thread

#t1 = threading.Thread(target=func)
#t1.start()

print(threading.active_count())

stime = datetime.datetime.now()
threads = []
for i in range(5):
	t1 = threading.Thread(target=download_images,args=(4,))
	threads.append(t1)
	t1.start() ## kick off the task
	#t1.join() ## each thread until the previous one finish (sequentially)

for thread in threads:
	thread.join()


etime = datetime.datetime.now()
print(f'execuation time:{etime -stime}')
print(threading.active_count())
