import json, matplotlib.pyplot as plt
import numpy as np

with open("results.json") as f:
    results = json.load(f)

labels = [r['label'] for r in results]
server_mbps = [r['mbps'] for r in results]
client_mbps = [r['client_mbps'] for r in results]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, client_mbps, width, label='Client-side Mbps', color='steelblue')
bars2 = ax.bar(x + width/2, server_mbps, width, label='Server-side Mbps', color='tomato')

ax.set_xlabel('Test Condition')
ax.set_ylabel('Throughput (Mbps)')
ax.set_title('Network Throughput Benchmark — Localhost vs Wi-Fi Simulation')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15)
ax.legend()
ax.bar_label(bars1, fmt='%.1f', padding=3)
ax.bar_label(bars2, fmt='%.1f', padding=3)

plt.tight_layout()
plt.savefig('benchmark_results.png', dpi=150)
plt.show()
print("Chart saved as benchmark_results.png")