def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()  # Приводим к нижнему регистру для сравнения

    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:  # Проверяем  корень в других словах
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)  # ['richiest', 'orichalcum', 'richies']
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)  # ['Disable', 'Disablement']

