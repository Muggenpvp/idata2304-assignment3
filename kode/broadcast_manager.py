import threading

class BroadcastManager:
    def __init__(self):
        self.clients = []
        self.lock = threading.Lock()

    def register(self, conn):
        with self.lock:
            self.clients.append(conn)

    def unregister(self, conn):
        with self.lock:
            if conn in self.clients:
                self.clients.remove(conn)

    def broadcast(self, message, sender=None):
        with self.lock:
            for conn in list(self.clients):
                if conn == sender:
                    continue
                try:
                    conn.sendall((message + "\n").encode())
                except Exception:

                    self.clients.remove(conn)