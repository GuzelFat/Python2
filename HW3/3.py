"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов
"""

elements_list = [5, 5, 4, 9, 7, 2, 7, 5, 4, 3, 1]
doubled_elements_list = []

print(f'Исходный список: {elements_list}')

for index in range(len(elements_list)):
    if elements_list.count(elements_list[index]) > 1 and elements_list[index] not in doubled_elements_list:
        doubled_elements_list.append(elements_list[index])

for el in elements_list:
    if el in doubled_elements_list:
        while elements_list.count(el) != 1:
            elements_list.remove(el)

#  elements_list = list(set(elements_list))

print(f'Исходный список: {elements_list}')
print(f'Исходный список: {doubled_elements_list}')