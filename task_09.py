
def connect_dict(dict1, dict2):
    s1 = sum(v for v in dict1.values() if isinstance(v, (int, float)))
    s2 = sum(v for v in dict2.values() if isinstance(v, (int, float)))

    if s1 > s2:
        priority_dict = dict1
        secondary_dict = dict2
    else:
        priority_dict = dict2
        secondary_dict = dict1

    # Фильтрация и объединение словарей
    combined_dict = {k: v for k, v in priority_dict.items() if v >= 10}
    combined_dict.update({k: v for k, v in secondary_dict.items() if v >= 10 and k not in combined_dict})

    # Сортировка словаря по значениям
    sorted_dict = dict(sorted(combined_dict.items(), key=lambda item: item[1]))

    return sorted_dict
print(connect_dict({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dict({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dict({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))