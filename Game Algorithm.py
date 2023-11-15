def valid_word(word):
    a = 0
    b = 0
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90:
            a += 1
        else:
            b += 1
    if 4 <= len(word) <= 25:
        c = True
    else:
        c = False
    if a == len(word) and b == 0 and c:
        return True
    else:
        return False

def find(word, m):
    a = 0
    for i in range(len(word)):
        if m == word[i]:
            a += 1
    if a == 0:
        return False
    else:
        return True

word = []
Tchar = []
l = 0
m = input("Enter a word: ")

for i in range(len(m)):
    word.append(m[i])

while not valid_word(word):
    m = input("Enter the word in uppercase and the number of letters between 4 and 25: ")
    word = list(m)

Tchar = ["*"] * len(m)

while l != 5 and l != len(word):
    a = input("Enter a character: ")
    if not find(word, a):
        l += 1
    else:
        for i in range(len(word)):
            while a in Tchar[i]:
                print("This character already exists, enter another character:")
            if a == word[i]:
                Tchar[i] = a
        print("".join(Tchar))

if l == 5:
    print("Sorry, you lose")
else:
    print("Congratulations, you win")