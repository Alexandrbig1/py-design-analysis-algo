import time
from typing import Dict
import random


class ThrottlingRateLimiter:
    def __init__(self, min_interval: float = 10.0):
        self.min_interval = min_interval
        self.user_requests: Dict[str, float] = {}

    def can_send_message(self, user_id: str) -> bool:
        current_time = time.time()
        return (
            user_id not in self.user_requests
            or (current_time - self.user_requests[user_id]) >= self.min_interval
        )

    def record_message(self, user_id: str) -> bool:
        if self.can_send_message(user_id):
            self.user_requests[user_id] = time.time()
            return True
        return False

    def time_until_next_allowed(self, user_id: str) -> float:
        if user_id not in self.user_requests:
            return 0.0
        return max(0.0, self.min_interval - (time.time() - self.user_requests[user_id]))


def test_throttling_limiter():
    limiter = ThrottlingRateLimiter(min_interval=10.0)

    print("\n=== Simulating Message Flow (Throttling) ===")
    for message_id in range(1, 11):
        user_id = str(message_id % 5 + 1)

        result = limiter.record_message(user_id)
        wait_time = limiter.time_until_next_allowed(user_id)

        print(
            f"Message {message_id:2d} | User {user_id} | "
            f"{'✓' if result else f'× (wait {wait_time:.1f}s)'}"
        )

        # Random delay between messages
        time.sleep(random.uniform(0.1, 1.0))

    print("\nWaiting for 4 seconds...")
    time.sleep(4)

    print("\n=== New Series of Messages After Waiting ===")
    for message_id in range(11, 21):
        user_id = message_id % 5 + 1
        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))
        print(
            f"Message {message_id:2d} | User {user_id} | "
            f"{'✓' if result else f'× (wait {wait_time:.1f}s)'}"
        )
        time.sleep(random.uniform(0.1, 1.0))


if __name__ == "__main__":
    test_throttling_limiter()