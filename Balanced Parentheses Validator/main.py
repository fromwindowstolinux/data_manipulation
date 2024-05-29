from seed import result

def validate_data(input_data):
    stack = []
    opening_brackets = {"(", "[", "{"}
    closing_brackets = {")", "]", "}"}
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in input_data:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_pairs[stack.pop()] != char:
                return False
    
    return not stack

if __name__ == '__main__':
    for item in result:
        print(f"{item} - {validate_data(item)}")