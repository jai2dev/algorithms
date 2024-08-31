from threading import *
import time

class Node:
	def __init__(self,val):
		self.val=val
		self.next=None
		self.prev=None

class BoundedBlockingQueue:
	def __init__(self,capacity):
		self.capacity=capacity
		self.queue_lock=Lock()
		self.enqueue_condition=Condition(self.queue_lock)
		self.dequeue_condition=Condition(self.queue_lock)
		self.size=0
		self.head=Node(-1)
		self.tail=Node(-2)
		self.head.next=self.tail
		self.tail.prev=self.head


	def enqueue(self,v):
		with self.queue_lock:
			while self.size==self.capacity:
				self.enqueue_condition.wait()
			nex=self.tail
			prev=self.tail.prev
			cur=Node(v)
			cur.next=nex
			nex.prev=cur
			prev.next=cur
			cur.prev=prev
			self.size+=1
			self.dequeue_condition.notify()




	def deque(self):
		with self.queue_lock:
			while self.size==0:
				self.dequeue_condition.wait()
			prev=self.head
			cur=self.head.next
			nex=cur.next
			prev.next=nex
			nex.prev=prev
			v=cur.val
			cur.prev=None
			cur.next=None
			self.size-=1
			self.enqueue_condition.notify()
		return v

	def get_size(self):
		with self.queue_lock:
			return self.size

if __name__ == "__main__":
    def producer(queue, items):
        for item in items:
            print(f"Producing {item}")
            queue.enqueue(item)
            time.sleep(0.1)  # Simulate production time

    def consumer(queue, n):
        for _ in range(n):
            item = queue.deque()
            print(f"Consumed {item}")
            time.sleep(0.2)  # Simulate consumption time

    queue = BoundedBlockingQueue(5)
    items = range(10)
    
    producer_thread = Thread(target=producer, args=(queue, items))
    consumer_thread = Thread(target=consumer, args=(queue, len(items)))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


