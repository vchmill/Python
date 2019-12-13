text = open("book.txt", "r") 

d = dict() 

for data in text: 
    data = data.lower()

    data = data.strip()



    words = data.split(" ")
	
    for word in words:
        if word in d:            
            d[word] = d[word] + 1
        else:             
            d[word] = 1
			
for key in list(d.keys()):
    print(key, ":", d[key])
