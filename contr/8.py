with open('quotes.txt','r', encoding = 'utf-8') as f: 
    text = f.read() 
    quotes = text.split('\n') 

c = 0 
authors = [] 
for quote in quotes: 
    quote = quote.split(' — '); 
    if "разум" in quote[0]:
    c + = 1 
    authors.append(quote[1]) 

print(c, "цитат со словом «разум» у следующих авторов") 
for author in authors[:-1]: 
    print(author, end=", ") 
print(authors[-1])
