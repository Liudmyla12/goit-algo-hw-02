from collections import deque


def is_palindrome(text: str) -> bool:
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    d = deque(cleaned)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    tests = [
        "А роза упала на лапу Азора",
        "Never odd or even",
        "Hello",
        "abba",
        "ab ba"
    ]

    for t in tests:
        print(f"{t} -> {is_palindrome(t)}")
