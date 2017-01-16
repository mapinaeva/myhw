def punct (text):
    for i, o in enumerate (text):
        text[i] = text[i].strip('.,?!;:-–—“”')
        text[i] = text[i].lower()
    return text
def findness (text):
    mass = []
    for word in text:
        if word.endswith('ness'):
            if word not in mass:
                mass.append(word)
    return mass 
def conc (text, r):
    sum = []
    k = 0
    for u, j in enumerate (r):
        for word in text:
            if word == j:
                k += 1
        sum.append(k)
        k = 0
    max = sum[0]
    for t, d in enumerate (sum):
        if d > max:
            max = d
            l = t
    return r[l]
                
f = open(input("Введите имя файла с расширением: "), "r")
t = f.read()
t = t.split()
k = punct(t)
r = findness(k)
w = conc (k, r)
print(w)

