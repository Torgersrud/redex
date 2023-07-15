import csv

def frequentWords(text,wordset, N):
    text = "".join([i for i in text[1:-1] 
                    if 64 < ord(i) or 
                    ord(i) > 123  or
                        ord(i) == 32 or
                          i != "" or
                          i is not None])
    text = text.lower()
    text = text.replace("-", " ")
    text = text.split()

    words = {}
    for i in wordset:
        




        print(lst[0][2])
    for i in text:
        words.update({i:text.count(i)})
    a = sorted(words.items(), key=lambda kv: (kv[1]))
    lst = [i for i in a[::-1] if not i == chr(39)]

    x = [i[0] for i in lst[:N]]
    y = [i[1] for i in lst[:N]]
    return x,y




