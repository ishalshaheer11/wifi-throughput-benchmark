# Network Throughput Benchmarking Tool

A TCP network throughput benchmarking tool built from scratch using Python sockets.The tool consists of a server that receives data and measures throughput in Mbps,
and a client that sends 50MB payloads under different system conditions. Results are automatically logged to a JSON file and visualized as a bar chart.
Tested across three conditions — localhost baseline, high CPU load, and stress test — to analyze how system load affects real network throughput.
Built to gain hands-on experience with TCP/IP socket programming, client-server architecture, and network performance measurement.

# How to Run
**Terminal 1:** `python server.py`
**Terminal 2:** `python client.py "test_label"`
**Chart:** `python plot_results.py`

# Tech Stack
Python 3, TCP Sockets, Matplotlib
