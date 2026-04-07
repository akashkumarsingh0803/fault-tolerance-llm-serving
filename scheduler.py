import random

class Scheduler:
    def __init__(self, workers, max_retries=0, replication_factor=1):
        self.workers = workers
        self.max_retries = max_retries
        self.replication_factor = replication_factor

    def send_request(self, request_id):
        # If replication is enabled
        if self.replication_factor > 1:
            return self._replicated_request(request_id)
        else:
            return self._retry_request(request_id)

    def _retry_request(self, request_id):
        attempts = 0

        while attempts <= self.max_retries:
            worker = random.choice(self.workers)

            try:
                return worker.process_request(request_id)
            except Exception:
                attempts += 1

                if attempts > self.max_retries:
                    raise

    def _replicated_request(self, request_id):
        # Pick multiple workers
        selected_workers = random.sample(
            self.workers, 
            min(self.replication_factor, len(self.workers))
        )

        for worker in selected_workers:
            try:
                return worker.process_request(request_id)
            except Exception:
                continue

        # If all fail
        raise Exception("All replicas failed")