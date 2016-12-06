with open('quotes.txt','r', encoding = 'utf-8') as k: 
    text = k.read() 
    quotes = text.split('\n')
    
for quote in quotes: 
    quote = quote.split(' — '); 
    words = quote[0].split(' ') 
    if len(words) < 10: 
       print(quote[0], ' — ', quote[1])
  

