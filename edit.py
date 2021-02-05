text = open("poetry.txt","r", encoding="utf-8").read().split()

import string

for line in text:
    for word in line:
        if word in string.ascii_letters or word in string.digits:
            if line in text:
                text.remove(line)

f = open('edit_poetry.txt', 'w', encoding="utf-8")
for x in text:
    f.write(str(x) + "\n")
f.close()