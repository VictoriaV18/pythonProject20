def max_odd(array):
    odd_elm = [int(x) for x in array if isinstance(x,(int, float)) and int(x) %2 !=0]
    if not odd_elm:
        return None
    return max(odd_elm)
print(max_odd([1,2,3,4,4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))