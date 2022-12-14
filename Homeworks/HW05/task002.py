# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
        # if the character at the current index is the same as the character at the next index. If the characters are the same, the count is incremented to 1'''    
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        # the count and the character is concatenated to the encoded string'''
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def decode_message(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message

def open_from_file():
    with open('II четверть/Знакомство с языком Python/Homeworks/HW05/original.txt', 'r') as file:
        text = file.read()
    print('The file has been downloaded successufully!')
    return text


# the original string
# our_message = "AuuBBBCCCCCCcccccCCCCCCCCCA"
our_message = open_from_file()
print(f'Here is the original message: {our_message}')
# pass in the original string
encoded_message=encode_message(our_message)
with open('II четверть/Знакомство с языком Python/Homeworks/HW05/encoded.txt', 'w') as file:
        file.write(encoded_message)
print(f'Encoded message "{encoded_message}" has been saved in file! ')
# pass in the decoded string
decoded_message=decode_message(encoded_message)
with open('II четверть/Знакомство с языком Python/Homeworks/HW05/decoded.txt', 'w') as file:
        file.write(decoded_message)
print(f'Decoded message "{decoded_message}" has been saved in file! ')

# print("Original string: [" + our_message + "]")
# print("Encoded string: [" + encoded_message +"]")
# print("Decoded string: [" + decoded_message +"]")