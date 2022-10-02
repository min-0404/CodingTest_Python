def solution(babbling):
    
    cnt = 0
    for i in babbling:
        while 1:
            if i == "":
                cnt += 1
                break

                
            if i.startswith('aya'):
                i = i[3:]
                if i.startswith('aya'):
                    break
            elif i.startswith('ye'):
                i = i[2:]
                if i.startswith('ye'):
                    break
            elif i.startswith('woo'):
                i = i[3:]
                if i.startswith('woo'):
                    break
            elif i.startswith('ma'):
                i = i[2:]
                if i.startswith('ma'):
                    break
            else:
                break

    return cnt            
            