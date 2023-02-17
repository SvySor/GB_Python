# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def compress(data):
    new_data = ''
    prev_char = ''
    count = 1

    for char in data:
        if char != prev_char:
            if prev_char:
                new_data += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        new_data += str(count) + prev_char
        return new_data

def decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

initial_string = 'AAAAAAAAAABBBBBBBBBBBBBCCCCCCCDDDDDDDEEEEEEEEEEEEEEEE'
print(initial_string)
new_string = compress(initial_string)
print(new_string)
print(decode(new_string))
