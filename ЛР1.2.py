# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1.44  # Объем дискеты
sheets = 100  # Число страниц
str_numbers = 50  # Число строк
simbols_numbers = 25  # Число символов в строке
simbol_memory = 4  # Память для одного символа
book_memory = (sheets * str_numbers * simbols_numbers * simbol_memory) / 1024**2
book_numbers = int(memory // book_memory)
print("Количество книг, помещающихся на дискету:", book_numbers)
