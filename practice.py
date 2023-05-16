T = 1

for test_case in range(1, T+1):
    n = 100000
    days = [1, 0, 0, 0, 1, 0, 1]
    count = 0

    stack = []
    for i in range(n):
        for j in days:
            stack.append(j)
            if j == 1:
                count += 1
            if count == n:
                answer = len(stack) 
                break
                
    print("#{} {}".format(test_case, answer))


T = 1

for test_case in range(1, T+1):
    n = 2
    days = [0, 1, 0, 0, 0, 0, 0]
    count = 0

    stack = []
    for i in range(n):
        for j in days:
            stack.append(j)
            if j == 1:
                count += 1
            if count == n:
                answer = len(stack) 
                break
                
    print("#{} {}".format(test_case, answer))

T = 1

for test_case in range(1, T+1):
    n = 1
    days = [1, 0, 0, 0, 0, 0, 0]
    count = 0

    stack = []
    for i in range(n):
        for j in days:
            stack.append(j)
            if j == 1:
                count += 1
            if count == n:
                answer = len(stack) 
                break
                
    print("#{} {}".format(test_case, answer))


T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = 2
    A = [1, 0, 0, 0, 0, 0, 0]
    firstDayList = []
    
    for i in range(len(A)) :
        if A[i] == 1 :
            firstDayList.append(i)
            
    
    for day in firstDayList :
        dayCnt = 0
        classCnt = 0
        while classCnt < N :
            if A[day] == 1 :
                classCnt += 1
            dayCnt += 1
            if day > 5 :
                day = 0
            else :
                day += 1
        answer = min(dayCnt)
        
    print(f'#{test_case} {answer}')