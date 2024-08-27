
def connect_dicts(dict1, dict2):
    # Вычисляем сумму значений ключей в каждом словаре
    sum_dict1 = sum(value for value in dict1.values())
    sum_dict2 = sum(value for value in dict2.values())

    # Определяем приоритетный словарь
    if sum_dict2 >= sum_dict1:
        primary_dict, secondary_dict = dict2, dict1
    else:
        primary_dict, secondary_dict = dict1, dict2

    # Соединяем словари, оставляя только те ключи, у которых значения >= 10
    combined_dict = {k: v for k, v in secondary_dict.items() if v >= 10}
    combined_dict.update({k: v for k, v in primary_dict.items() if v >= 10})

    # Возвращаем словарь, отсортированный по значениям ключей
    return dict(sorted(combined_dict.items(), key=lambda item: item[1]))
print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))