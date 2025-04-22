import time
from src.interfaces.interfaces import LoggerProtocol

class Logger(LoggerProtocol):
    def __init__(self):
        self.logs = []
        self.start_time = time.time()
        self.response_times = []

    def log(self, role, message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.logs.append((timestamp, role, message))

    def record_performance(self):
        """Records performance metrics including session duration and bot response times."""
        
        elapsed = time.time() - self.start_time
        print(f"[Session duration: {elapsed:.2f} seconds]")

        if self.response_times:
            avg = sum(self.response_times) / len(self.response_times)
            min_rt = min(self.response_times)
            max_rt = max(self.response_times)
            print(f"[Bot response time] avg: {avg:.2f}s | min: {min_rt:.2f}s | max: {max_rt:.2f}s | count: {len(self.response_times)}")
        else:
            print("[Bot response time] No responses recorded.")

    def record_response_time(self, start, end):
        """Record a single bot response time (start and end timestamps in seconds)."""
        self.response_times.append(end - start)

    def dump_logs(self):
        for timestamp, role, message in self.logs:
            print(f"{timestamp} | {role}: {message}")
