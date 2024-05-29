import random

# random bracket with length 6 char
def random_bracket(length=6):
    # Random length between 2 and 1000
    # length = random.randint(2, 1000)  
    bracket = ["(", ")", "[", "]", "{", "}"]
    random_bracket = [random.choice(bracket) for _ in range(length)]
    return "".join(random_bracket)

# hardcoded test brackets for the True input
test_brackets = [
    "()[]{}",
    "([{}])",
    "({[]})",
    "[]{}()",
    "[{()}]",
    "[({})]",
    "{}[]()",
    "{[()]}",
    "{([])}",
    "(){}[]"
]

# generate 10 random brackets
random_brackets = [random_bracket() for _ in range(10)]

# mixed test brackets and random brackets
result = test_brackets + random_brackets
random.shuffle(result)

if __name__ == '__main__':
    for item in result:
        print(item)
