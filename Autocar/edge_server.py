import random
from collections import deque

class EdgeServer:
    def __init__(self, server_id, ram, storage):
        self.server_id = server_id
        self.total_ram = ram
        self.total_storage = storage
        self.available_ram = ram
        self.available_storage = storage
        self.task_queue = deque()
        self.processed_tasks = []

    def can_process(self, task):
        return task['ram'] <= self.available_ram and task['storage'] <= self.available_storage

    def add_task(self, task):
        if self.can_process(task):
            self.available_ram -= task['ram']
            self.available_storage -= task['storage']
            self.task_queue.append(task)
            return True
        return False

    def process_tasks(self):
        while self.task_queue:
            task = self.task_queue.popleft()
            self.available_ram += task['ram']
            self.available_storage += task['storage']
            self.processed_tasks.append(task)