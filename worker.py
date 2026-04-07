import time
import random

class Worker:
    def __init__(self, worker_id, failure_rate=0.0):
        self.worker_id = worker_id
        self.failure_rate = failure_rate

    def process_request(self, request_id):
        # Simulate random failure
        if random.random() < self.failure_rate:
            raise Exception(f"Worker {self.worker_id} failed!")

        # Simulate LLM processing time
        processing_time = random.uniform(0.1, 0.5)
        time.sleep(processing_time)

        return {
            "worker_id": self.worker_id,
            "request_id": request_id,
            "latency": processing_time
        }