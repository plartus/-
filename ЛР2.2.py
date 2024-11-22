# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, delimiter=','):

    # Разделяю списки на элементы
    participants_1 = set(group_1.split(delimiter))
    participants_2 = set(group_2.split(delimiter))

    # Нахожу пересечение списков
    common_participants = participants_1.intersection(participants_2)

    # Возвращаю отсортированный список общих участников
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяю работу функции с разделителем '|'
common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(f"Общие участники: {common_participants}")
# TODO Провеьте работу функции с разделителем отличным от запятой
