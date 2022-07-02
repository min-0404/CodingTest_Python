T = int(input())
for test_case in range(1, T + 1):
    n = int(input());
    lst=list(map(int, input().split()))
    
    result = 0;

    cnt1 = 0; #짝수
    cnt2 = 0; #홀수
    compare = []
    #짝수일경우
    if n % 2 == 0:
        #전처리 과정
        for i in lst:
            if i % 2 == 0:
                cnt1 += 1;
                compare.append(0);
            else:
                cnt2 += 1;
                compare.append(1);
        if cnt1 != cnt2:
            result = -1;
            break;
            
        for i in range(n):
            for j in range(i+1, n):
                if 

    #홀수인경우
    else:
        for i in lst:
            if i % 2 == 0:
                cnt1 += 1;
            else:
                cnt2 += 1;
        if cnt1 + 1 != cnt2 or cnt1 != cnt2:
            result = -1;
            break; 
        
        
    
    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d" % test_case, result)
