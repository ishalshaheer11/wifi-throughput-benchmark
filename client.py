import socket, time, json, sys

HOST = '127.0.0.1'
PORT = 5555
RESULT_PORT = PORT + 1
DATA_SIZE_MB = 50  # sends 50MB of data each test

def run_client(label="test"):
    print(f"\n[CLIENT] Starting test: {label}")
    
    # Send data
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    chunk = b'X' * 65536  # 64KB chunks
    total = DATA_SIZE_MB * 1024 * 1024
    sent = 0
    start = time.time()

    while sent < total:
        to_send = min(len(chunk), total - sent)
        s.sendall(chunk[:to_send])
        sent += to_send

    s.close()
    client_elapsed = time.time() - start
    client_mbps = (sent * 8) / (client_elapsed * 1_000_000)
    print(f"[CLIENT] Sent {sent/1e6:.1f} MB in {client_elapsed:.2f}s = {client_mbps:.2f} Mbps")

    # Receive server result
    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    r.bind((HOST, RESULT_PORT))
    r.listen(1)
    conn, _ = r.accept()
    raw = b""
    while True:
        d = conn.recv(4096)
        if not d: break
        raw += d
    conn.close()
    r.close()

    result = json.loads(raw.decode())
    result['label'] = label
    result['client_mbps'] = round(client_mbps, 2)

    # Save to results file
    try:
        with open("results.json", "r") as f:
            all_results = json.load(f)
    except:
        all_results = []

    all_results.append(result)
    with open("results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"[CLIENT] Server measured: {result['mbps']} Mbps")
    print(f"[CLIENT] Result saved to results.json")

if __name__ == "__main__":
    label = sys.argv[1] if len(sys.argv) > 1 else "test"
    run_client(label)