# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, items_to_find):
    if items_to_find in items:  # Условие проверяет, есть ли товар в списке
        return items.index(items_to_find)  # Если есть, присваивает индекс и возвращает
    else:
        return None  # Если товар не найден, возвращает None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
