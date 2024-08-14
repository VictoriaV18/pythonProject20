def multiply_numbers(inputs):
    if not isinstance(inputs, str):
        inputs = str(inputs)
    total = 1
    has_digits = False
    for char in inputs:
        if char.isdigit():
            has_digits = True
            total *= int(char)
    return total if has_digits else None
print(multiply_numbers(''))
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers('2.3'))
print(multiply_numbers([5, 6, 4]))