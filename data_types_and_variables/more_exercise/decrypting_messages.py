key = int(input())
number_of_lines = int(input())

message = ""

for _ in range(number_of_lines):
    letter = input()
    new_letter = chr(ord(letter) + key)
    message += new_letter

print(message)