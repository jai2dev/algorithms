from threading import Thread, Lock, Condition
import time

class Task:
    def __init__(self, command, id, runTime):
        self.command = command
        self.id = id
        self.runTime = runTime

class WorkerInterface:
    def __init__(self):
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.queue = []
        self.active_tasks = 0
        self.shutdown_flag = False
        self.worker_thread = Thread(target=self._worker)
        self.worker_thread.start()

    def run_task(self, task):
        try:
            time.sleep(task.runTime)  # Simulate task running time
            print(f"Task completed: {task.id}")
        except Exception as e:
            print(f"Task failed: {task.id} with error {e}")

    def submitWork(self, task):
        with self.lock:
            self.queue.append(task)
            self.active_tasks += 1
            self.condition.notify()

    def _worker(self):
        while True:
            with self.lock:
                while not self.queue and not self.shutdown_flag:
                    self.condition.wait()
                if self.shutdown_flag and not self.queue:
                    break
                task = self.queue.pop(0)
            self.run_task(task)
            with self.lock:
                self.active_tasks -= 1
                if self.active_tasks == 0:
                    self.condition.notify_all()

    def blockUntilComplete(self):
        with self.lock:
            while self.active_tasks > 0:
                self.condition.wait()
        print("All tasks are finished")

    def shutdown(self):
        with self.lock:
            self.shutdown_flag = True
            self.condition.notify_all()
        self.worker_thread.join()

# Example usage
if __name__ == '__main__':
    worker_interface = WorkerInterface()

    tasks = [Task("command", i, random.uniform(0.1, 0.5)) for i in range(5)]
    for task in tasks:
        worker_interface.submitWork(task)

    worker_interface.blockUntilComplete()
    worker_interface.shutdown()
