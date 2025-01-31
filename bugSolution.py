def function(a, b):
    try:
        return int(a) + int(b)
    except (ValueError, TypeError):
        return "Error: Inputs must be integers or convertible to integers."

result = function(5, '10')
print(result)

result2 = function(5, 'abc')
print(result2)