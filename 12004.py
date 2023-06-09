# 12004. 구구단 1

# 정수 N이 주어졌을 때, N 이 1 이상 9 이하의 두 수 a, b의 곱으로 표현될 수 있는지 판단하라.
 

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.

#     ∙ 하나의 정수 N이 주어진다. (1≤N≤100)
 

# [출력]

# 각 테스트 케이스마다
#     ∙ N 이 1 이상 9 이하의 두 수 a, b의 곱으로 표현될 수 있으면 “Yes”, 아니면 “No” 를 출력하라.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ans = "No"
    for i in range(1, 10):
        if N % i == 0 and 1<= N / i <=9: # 딱 나누어 떨어지는 수이고 몫이 1~9 범위 내라면 yes, 아니라면 no 반환
            
            ans = "Yes"
    
    print("#{} {}".format(test_case, ans))
        