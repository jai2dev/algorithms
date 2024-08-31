import time
from threading import *
import random
class Scheduler:
	def __init__(self):
		self.queue=[]
		self.queue_lock=Lock()
		self.task_count=0
		self.task_lock=Lock()
		self.tasks_done=Condition(self.task_lock)
		self.run_task=Thread(target=self._run_task)
		self.run_task.start()

	def schedule(self,task):
		with self.queue_lock:
			self.queue.append(task)
			with self.task_lock:
				self.task_count+=1

	def _run_task(self):
		while True:
			task=None
			with self.queue_lock:
				if not self.queue:
					time.sleep(0.1)
					continue
				task=self.queue.pop(0)
				with self.task_lock:
					self.task_count-=1
					if self.task_count==0:
						self.tasks_done.notify_all()
			if task:
				task()
				print("Task ran successfully")
			time.sleep(0.1)

	def wait_until_complete(self):
		with self.task_lock:
			while self.task_count>0:
				self.tasks_done.wait()
			print("All task completed")
		self.run_task.join()



if __name__ == '__main__':
	scheduler=Scheduler()
	def print_num(num):
		print(num)
	for i in range(5):
		scheduler.schedule(lambda num=i: print_num(num))

	scheduler.wait_until_complete()
