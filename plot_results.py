import matplotlib.pyplot as plt

failure_rates = [0.1, 0.3, 0.5]

baseline = [43, 35, 26]
retry = [50, 48, 45]
replication = [50, 44, 37]

plt.figure()

plt.plot(failure_rates, baseline, marker='o', label='Baseline')
plt.plot(failure_rates, retry, marker='o', label='Retry')
plt.plot(failure_rates, replication, marker='o', label='Replication')

plt.xlabel("Failure Rate")
plt.ylabel("Successful Requests")
plt.title("Fault Tolerance Comparison in Distributed LLM Serving")

plt.legend()
plt.grid()

plt.show()