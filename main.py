filename = input("Введіть назву файлу: ")
text = input("Введіть текст, який бажаєте записати у файл: ")
with open(filename, "w") as file:
    file.write(text)
with open(filename, "r") as file:
    content = file.read()
    word_count = len(content.split())
print(f"Кількість слів у тексті: {word_count}")
new_filename = "first_10_chars.txt"
with open(filename, "r") as file:
    first_10_chars = file.read(10)
with open(new_filename, "w") as new_file:
    new_file.write(first_10_chars)
with open(new_filename, "r") as new_file:
    content = new_file.read()
    words = content.split()
    average_word_length = sum(len(word) for word in words) / len(words)
print(f"Середня довжина слова у новому файлі: {average_word_length}")
second_filename = input("Введіть назву другого файлу: ")
with open(second_filename, "r") as second_file:
    content = second_file.read()
    word_count_second_file = len(content.split())

if word_count > word_count_second_file:
    print(f"Файл '{filename}' містить більше слів.")
elif word_count < word_count_second_file:
    print(f"Файл '{second_filename}' містить більше слів.")
else:
    print("Кількість слів у обох файлах однакова.")
