# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
rus_vowels = 'аоуэыяёеюи'
word = 'Архангельск'
word_vowels_cnt = 0
for letter in word.lower():
    if letter in rus_vowels:
        word_vowels_cnt += 1
print(f'Количество гласных букв в слове "{word}": {word_vowels_cnt}')



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_lengths = [len(word) for word in sentence.split()]
avg_word_length = sum(words_lengths) / len(words_lengths)
print(avg_word_length)
