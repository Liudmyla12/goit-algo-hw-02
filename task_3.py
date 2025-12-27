def check_brackets(text: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    opens = set(pairs.values())
    closes = set(pairs.keys())

    for ch in text:
        if ch in opens:
            stack.append(ch)
        elif ch in closes:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    examples = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        "([{}])",
        "([)]",
    ]

    for e in examples:
        result = "Симетрично" if check_brackets(e) else "Несиметрично"
        print(f"{e}: {result}")

