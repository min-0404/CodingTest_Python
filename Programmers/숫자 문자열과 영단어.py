def solution(s):

    lst1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lst2 = ["0", "1", '2', '3', '4', '5', '6', '7', '8', '9']
    dic = dict(zip(lst1, lst2))
    
    for key, value in dic.items():
        s = s.replace(key, value)
    
    s = int(s)
    return s