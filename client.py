class Client:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def send_requests(self, num_requests):
        results = []
        failures = 0

        for i in range(num_requests):
            try:
                result = self.scheduler.send_request(i)
                results.append(result)
            except Exception as e:
                failures += 1

        return results, failures