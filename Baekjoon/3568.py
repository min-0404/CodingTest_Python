str = input()

str = str.split(' ')

result = []
for i in str:
    if i[-1] == ',' or i[-1] ==  ';':
        result.append(i[:-1])
        continue
    result.append(i)

for i in range(1, len(result)):
    x = result[0]
    y = result[i][1:]
    y =  y[::-1]
    k = ""
    for j in range(len(y)):
        if y[j] == '[':
            k += ']'
        elif y[j] == ']':
            k += '['
        else:
            k += y[j]
            
    z = result[i][0]
    print(x + k + " " + z + ";")


