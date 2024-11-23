import random

class Car:
    def __init__(self, car_id):
        self.car_id = car_id

    def generate_tasks(self, num_tasks):
        tasks = []
        for _ in range(num_tasks):
            task = {
                "id": random.randint(1000, 9999),
                "type": random.choice(["Image", "Video", "Data"]),
                "ram": random.randint(50, 200),  # RAM requirement in MB
                "storage": random.randint(100, 500),  # Storage requirement in MB
                "priority": random.choice(["Low", "Medium", "High"])
            }
            tasks.append(task)
        return tasks