piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
piano_tuple = ('do', 're', 'mi', 'fa', 'so', 'la', 'ti')

print(piano_keys[2:5])  # starts at 2 and ends at 5 (c, d, e)
print(piano_keys[2:])  # 2 to whole list
print(piano_keys[:5])  # starts from 0 to 5
print(piano_keys[2:5:2])  # jump is 2
print(piano_keys[::2])  # jump is 2
print(piano_keys[::-1])  # reverses the list

# same goes for tuple also

print(piano_tuple[2:5])
print(piano_tuple[2:])
print(piano_tuple[:5])
print(piano_tuple[2:5:2])
print(piano_tuple[::2])
print(piano_tuple[::-1])
