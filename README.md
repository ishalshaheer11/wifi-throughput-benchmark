# Network Throughput Benchmarking Tool

A TCP network throughput benchmarking tool built from scratch using Python sockets.The tool consists of a server that receives data and measures throughput in Mbps,
and a client that sends 50MB payloads under different system conditions. Results are automatically logged to a JSON file and visualized as a bar chart.
Tested across three conditions — localhost baseline, high CPU load, and stress test — to analyze how system load affects real network throughput.
Built to gain hands-on experience with TCP/IP socket programming, client-server architecture, and network performance measurement.

# How to Run:
You need two terminal windows open, both navigated to this project folder.

Step 1 - Start the server in Terminal 1:
python server.py
You should see [SERVER] Waiting for connection on 127.0.0.1:5555... — leave this running.

Step 2 - Run a test in Terminal 2:
python client.py "localhost_baseline"
Give each test a descriptive label. You can run multiple tests with different labels to compare conditions.

Step 3 - Run more tests under different conditions:
python client.py "high_cpu_load"
python client.py "stress_test"
Note: restart the server between each test by pressing Ctrl+C and running python server.py again.

Step 4 - Generate the results chart:
python plot_results.py
This reads results.json and saves a bar chart as benchmark_results.png.

# Files:
- server.py — TCP server that receives data and measures throughput
- client.py — TCP client that sends 50MB and logs results
- plot_results.py — generates bar chart from results
- results.json — auto-generated, stores all test results
- benchmark_results.png — auto-generated results chart

# Tech Stack:
Python 3, TCP Sockets, Matplotlib
