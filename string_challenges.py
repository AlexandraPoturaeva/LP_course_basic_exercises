# Вывести последнюю букву в слове
print('Задание 1')
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
print('\nЗадание 2')
word = 'Архангельск'
word = word.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
print('\nЗадание 3')
rus_vowels = 'аоуэыяёеюи'
word = 'Архангельск'
word_vowels_cnt = 0
for letter in word.lower():
    word_vowels_cnt += letter in rus_vowels
print(f'Количество гласных букв в слове "{word}": {word_vowels_cnt}')


# Вывести количество слов в предложении
print('\nЗадание 4')
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
print('\nЗадание 5')
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
print('\nЗадание 6')
sentence = 'Мы приехали в гости'
words_lengths = [len(word) for word in sentence.split()]
avg_word_length = sum(words_lengths) / len(words_lengths)
print(avg_word_length)
