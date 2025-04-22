import time

class Logger:
    def __init__(self):
        self.logs = []
        self.start_time = time.time()

    def log(self, role, message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.logs.append((timestamp, role, message))

    def record_performance(self):
        elapsed = time.time() - self.start_time
        print(f"[Session duration: {elapsed:.2f} seconds]")

    def dump_logs(self):
        for timestamp, role, message in self.logs:
            print(f"{timestamp} | {role}: {message}")
