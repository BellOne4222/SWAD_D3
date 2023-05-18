# 14361. 숫자가 같은 배수

# 자연수 N이 있다. N의 10진법 표기(단, 0으로 시작하지 않도록 표기해야 함)에서 나타나는 숫자들을 재배열하여 N보다 큰 N의 배수(즉 2N, 3N, …, k•N, …) 를 만들 수 있는지 판단하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 자연수 N (1 ≤N ≤ 106) 이 공백 하나를 사이로 두고 주어진다.
 

# [출력]
# 각 테스트 케이스마다, 주어진 자연수에 나타난 숫자들을 재배열하여 더 큰 배수를 만들 수 있다면 ‘possible’, 불가능하다면 ‘impossible’을 출력한다.

# testcase 108 중 62개만 정답


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    n = str(N)
    nums = []
    for i in n:
        nums.append(i)
    k = 1
    res = "impossible"
    while True:
        k += 1
        N *= k
        a = str(N)
        arr = []
        for num in a:
            arr.append(num)
        
        if len(n) < len(a):
            break 

        for b in nums:
            if b in arr:
                arr.remove(b)
        
        if len(arr) == 0:
            res = "possible"
            break
        
        arr.clear()
    
    print("#{} {}".format(test_case, res))

# 로직 : input 수로 이루어진 리스트와 k배한 숫자 리스트를 대조하여 앞의 리스트 안에 있는 숫자를 k배한 숫자 리스트에서 제거하고
# 반복문 종료후 리스트안에 아무것도 없으면 재배열로 배수를 만들수 있으므로 possible, 아니라면 impossible 반환








        


    

    
