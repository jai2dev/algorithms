from threading import *
import time
import heapq

class Task:
	def __init__(self,command,periodic,time,period=0):
		self.command=command
		self.periodic=periodic
		self.period=period
		self.time=time

class ScheduledExecutorService:
	def __init__(self,shutdown):
		self.lock=Lock()
		self.queue=[]
		self.keepRunning=True
		self.close_scheduler=False
		self.shutdown_time=shutdown
		self.scheduler=Thread(target=self._schedule)
		self.scheduler.start()
		self.shutdown_thread=Thread(target=self.shutdown)
		self.shutdown_thread.start()

	def _schedule(self):
		while self.keepRunning:
			with self.lock:
				current_time=time.time()
				if not self.queue:
					print( "Currently There are no task to schedule")
				else:
					task_time=self.queue[0][0]
					if task_time>current_time:
						time.sleep(1)
					task=heapq.heappop(self.queue)[1]
					Thread(target=self._run_task,args=(task,)).start()
					if task.periodic:
						task.time=time.time()+task.period
						heapq.heappush(self.queue,[task.time,task])
				
				# for task in self.queue:
				# 	if task.time>current_time:
				# 		continue
				# 	Thread(target=self._run_task,args=(task,)).start()
				# 	if task.periodic:
				# 		task.time=time.time()+task.period
				# 	else:
				# 		self.queue.remove(task)
			time.sleep(1)


	def _run_task(self,task):
		try:
			command=task.command
			command()
		except:
			raise "Task Execution Failed"

	def schedule(self,command, delay, unit):
		with self.lock:
			task=Task(command,False,time.time()+delay*unit)
			heapq.heappush(self.queue,[task.time,task])



	def scheduleAtFixedRate(self, command, initialDelay, period, unit):
		with self.lock:
			task=Task(command,True,time.time()+initialDelay*unit,period*unit)
			heapq.heappush(self.queue,[task.time,task])


	def scheduleWithFixedDelay(self, command, delay, unit,initialDelay=0):
		def _fixedDelayUtil():
			command()
			self.scheduleWithFixedDelay(command,delay,unit)

		with self.lock:
			task=Task(_fixedDelayUtil,False,time.time()+initialDelay*unit)
			heapq.heappush(self.queue,[task.time,task])


	def shutdown(self):
		while not self.close_scheduler:
			if self.shutdown_time<=time.time():
				self.keepRunning=False
				self.close_scheduler=True
				self.scheduler.join()



def print_schedule():
	print("schedule")

def print_scheduleAtFixedRate():
	print("scheduleAtFixedRate")

def print_scheduleWithFixedDelay():
	print("scheduleWithFixedDelay")

if __name__ == '__main__':
	scheduler=ScheduledExecutorService(time.time()+60)
	scheduler.schedule(print_schedule,5,1)
	scheduler.scheduleAtFixedRate(print_scheduleAtFixedRate,3,3,1)
	scheduler.scheduleWithFixedDelay(print_scheduleWithFixedDelay,1,1,5)
	scheduler.shutdown_thread.join()
	# sc