T = int(input())

for test_case in range(1, T+1):
    N = input()
    nums = sorted(list(N))
    res = False # 숫자가 같은지 체크한다
    k = 2
    
    while True:
        # 2부터 곱해서 자릿수 넘어가면 false
        # 곱한 것들을 정렬한 원소가 원래 원소와 같으면 참
        num = int(N) * k # num의 배수 2 ~
        
        # 원래 입력한 숫자의 길이보다, 곱한 결과의 길이가 길다면 자릿수가 늘어난거니까 종료
        if len(str(num)) > len(N):
            break
         # 배수를 문자열로 만들어 리스트로 만든걸 정렬, 그게 원래 숫자와 같으면
        if sorted(list(str(num))) == nums:
            res = True
            break
        k += 1
        
    if res:
        ans = "possible"
    else:
        ans = "impossible"
     
    print("#{} {}".format(test_case, ans))