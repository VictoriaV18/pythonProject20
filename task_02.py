def coincidence(list,range):
    if list is None or range is None:
        return ()
    return [x for x in list if range[0]<=x<=range[1]]
list_ex = ()
range_ex = ()
print(coincidence(list_ex,range_ex))