import socket, time, json

HOST = '127.0.0.1'
PORT = 5555

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER] Waiting for connection on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"[SERVER] Connected from {addr}")
        total_bytes = 0
        start = time.time()

        while True:
            data = conn.recv(65536)
            if not data:
                break
            total_bytes += len(data)

        elapsed = time.time() - start
        mbps = (total_bytes * 8) / (elapsed * 1_000_000)

        result = {
            "bytes": total_bytes,
            "elapsed": round(elapsed, 3),
            "mbps": round(mbps, 2)
        }

        print(f"[SERVER] {total_bytes/1e6:.2f} MB in {elapsed:.2f}s = {mbps:.2f} Mbps")
        conn.close()

        # Send result back
        result_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_sock.connect((HOST, PORT + 1))
        result_sock.sendall(json.dumps(result).encode())
        result_sock.close()

if __name__ == "__main__":
    run_server()