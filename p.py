# from operator import index


# number = "1924"
# k = 2

# # lst = list(map(int, number));
# # lst2 = sorted(lst);
# # result = lst2[:k]

# # for i in lst[:]:
# #     if i in result:
# #         lst.remove(i);

# stack = [number[0]];
# for i in number[1:]:
#     while stack and stack[-1] < i and k >0:
#         stack.pop(); 
#         k -= 1;
#     stack.append(i);

# answer = "".join(stack)
# print(answer)  

# stack = [number[0]]
# for num in number[1:]:
#     while stack and stack[-1] < num and k > 0:
#         stack.pop()
#         k -= 1
#     stack.append(num)
        
# return "".join(stack) if k == 0 else "".join(stack[:-k])

dict = {}
sum = 0;
num = ["min", "seok"];
for i in num:
    dict[hash(i)] = i;
    sum += hash(i);
print(dict)
print(sum)

dict2= {}
sum2 = 0
num2 = ['1', '2']
for i in num2:
    dict2[hash(i)] = i;
    sum2 += hash(i);

# x = 10
# x = str(x)
# print(x)

x = 'ab'
y = int(x)
print(y)

# k = 'a'
# a = ord(k)
# b = int(k)
# print(a)
# print(b)
