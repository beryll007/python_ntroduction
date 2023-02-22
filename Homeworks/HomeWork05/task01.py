# задача 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def find_and_deleate_from_text(text, to_delete):
    
    words = text.split(' ')
    new_words = []
    for word in words:
        if to_delete not in word:
            new_words.append(word)
    new_text = ' '.join(new_words)
    
    return(new_text)

user_text = input('Input your text: ')
to_delete = input('Input the part of the word you want to remove from the text: ')
result = find_and_deleate_from_text(user_text, to_delete)
print(result)   