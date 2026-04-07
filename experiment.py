from worker import Worker
from scheduler import Scheduler
from client import Client
import numpy as np

def run_test(strategy, failure_rate):
    workers = [
        Worker(worker_id=1, failure_rate=failure_rate),
        Worker(worker_id=2, failure_rate=failure_rate),
        Worker(worker_id=3, failure_rate=failure_rate),
    ]

    if strategy == "baseline":
        scheduler = Scheduler(workers)

    elif strategy == "retry":
        scheduler = Scheduler(workers, max_retries=2)

    elif strategy == "replication":
        scheduler = Scheduler(workers, replication_factor=2)

    client = Client(scheduler)

    results, failures = client.send_requests(50)

    success = len(results)
    avg_latency = (
        np.mean([r["latency"] for r in results]) if results else 0
    )

    return success, failures, avg_latency


if __name__ == "__main__":
    strategies = ["baseline", "retry", "replication"]
    failure_rates = [0.1, 0.3, 0.5]

    for strategy in strategies:
        print(f"\n=== Strategy: {strategy} ===")

        for fr in failure_rates:
            success, failures, latency = run_test(strategy, fr)

            print(f"Failure Rate: {fr}")
            print(f"Success: {success}, Failures: {failures}")
            print(f"Avg Latency: {latency:.3f}s\n")