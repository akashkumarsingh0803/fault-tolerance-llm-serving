# Fault Tolerance in Distributed LLM Serving

## Overview
This project evaluates fault tolerance strategies in distributed LLM serving systems, focusing on retry and replication mechanisms.

## System Architecture
Client → Scheduler → Worker Nodes

## Features
- Simulated distributed workers
- Failure injection (random crashes)
- Retry-based fault tolerance
- Replication-based fault tolerance
- Performance evaluation under different failure rates

## Experiments
- Number of workers: 3
- Requests: 50
- Failure rates: 0.1, 0.3, 0.5

## Results Summary
- Retry achieves highest success rate
- Replication improves reliability but less effective than retry
- Tradeoff between latency and reliability observed

## How to Run

### 1. Install dependencies
```bash
pip install ray numpy matplotlib pandas
```

### 2. Run experiments
```bash
python experiment.py
```

### 3. Plot results
```bash
python plot_results.py
```

## Author
Akash Kumar Singh
