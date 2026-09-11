text = input()
pattern = input()

# Please write your code here.
def find_pattern(i):
    global text, pattern
    if text[i:i + len(pattern)] == pattern:
        return i

    else:
        return -1

for i in range(len(text)):
    idx = find_pattern(i)
    if idx != -1:
        print(i)
        break
    elif i == len(text) - 1 and idx == -1:
        print(idx)    

