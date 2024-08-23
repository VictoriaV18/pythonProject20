def sort_list(list):
   if not list:
       return []
   max_val = max(list)
   min_val = min(list)
   list = [max_val if x == min_val else min_val if x == max_val else x for x in list]
   list.append(min_val)
   return list
print(sort_list([]))
print(sort_list([2,4,6,8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))