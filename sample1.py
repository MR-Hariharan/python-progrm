word = ['h','a','r','i','h','a','r','a','n']
count1 = 0
count2 = 0
result = []
for c in word:
    if c == 'h':
        c =  'a'
        count1 = count1 + 1
        result.append(c)
    elif c == 'a':
        c = 'h'    
        count2 = count2 + 1
        result.append(c)
    else:
        result.append(c)    
print(count1,count2)        
print(result) 