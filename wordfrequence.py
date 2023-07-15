from time import sleep

def frequentWords(text, N):
    text = "".join([i for i in text[1:-1]
                    if 64 < ord(i) or 
                    ord(i) > 123 or
                      ord(i) == 39 or
                        ord(i) == 32 or
                          i != ""])
    text = text.lower()
    text = text.replace("-", " ")
    text = text.split()
    s = set(text)
    words = {}
    for i in s:
        words.update({i:text.count(i)})
    a = sorted(words.items(), key=lambda kv: (kv[1]))
    lst = [i for i in a[::-1] if not i == chr(39)]

    x = [i[0] for i in lst[:N]]
    y = [i[1] for i in lst[:N]]
    return x,y

