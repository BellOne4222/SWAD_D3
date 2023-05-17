# 1493. 수의 새로운 연산

# 2차원 평면 제 1사분면 위의 격자점 (x,y)에 위 그림과 같이 대각선 순서로 점에 수를 붙인다.

# 점 (x,y)에 할당된 수는 #(x,y)로 나타낸다.

# 예를 들어 #(1,1) = 1, #(2,1)=3, #(2,2) = 5, #(4,4) = 25이다.

# 반대로 수 p가 할당된 점을 &(p)로 나타낸다.

# 예를 들어 &(1) = (1,1), &(3) = (2,1), &(5) = (2,2), &(25) = (4,4)이다.

# 두 점에 대해서 덧셈을 정의한다. 점 (x,y)와 점 (z,w)를 더하면 점 (x+z, y+w)가 된다.

# 즉, (x,y) + (z,w) = (x+z, y+w)로 정의한다.

# 우리가 해야 할 일은 수와 수에 대한 새로운 연산 ★를 구현하는 것으로, p★q는 #(&(p)+&(q))으로 나타난다.

# 예를 들어, &(1)=(1,1), &(5) = (2,2)이므로, 1★5 = #(&(1)+&(5)) = #((1,1)+(2,2)) = #(3,3) = 13이 된다.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 두 정수 p,q(1 ≤ p, q ≤ 10,000)가 주어진다.


# [출력]

# 각 테스트 케이스마다 ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 각 테스트 케이스마다 p★q의 값을 출력한다.

# 좌표를 값으로, 값을 좌표로 변환하는 문제


# [풀이 1] dict 사용
dct = {}
r_dct = {}
i, j = 1, 1
for n in range(1, 50000):   # 10000까지의 숫자를 좌표에 저장할때, 그 4배 크기 삼각형 (예상)
    dct[n] = (i,j) # 값을 좌표로 바꿔주는 딕셔너리
    r_dct[(i,j)] = n # 좌표를 값으로 바꿔주는 딕셔너리
    i, j = i-1, j+1 # 좌표 한칸 이동함에 따라 i,j값 변화
    if i<1: # i가 1보다 작을때 i,j 좌표
        i, j = j, 1
 
T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
 
    pi, pj = dct[p]                 # [1] p, q값의 좌표로 변환
    qi, qj = dct[q]
 
    ans = r_dct[(pi+qi, pj+qj)]     # [2] 좌표를 값으로 변환
    print(f'#{test_case} {ans}')

##################################################

# https://florescene.tistory.com/399

def numToXy(num):	#숫자->좌표 변환 함수
    p_cnt = 0 # 그룹 확인 변수
    xyArr = [0, 0] # x, y 저장
    total_p = 0 # 1~ p_cnt 까지 총합을 저장한 변수, 그룹의 마지막수		
    num2 = num
    while True: # p_cnt 값을 늘려나가며 num2에서 p_cnt를 뺀다. 
        p_cnt += 1
        total_p += p_cnt
        num2 -= p_cnt	
        if num2 <= 0: # num2의 값이 0 이나 음수이면 해당 p_cnt가 num의 그룹이 된다.
            xyArr[0] = p_cnt-(total_p-num) # x 좌표, x 좌표값은 1~ i까지 증가, i에서 그룹 내 가장 큰수 - 구하고자 하는 숫자
            xyArr[1] = 1+(total_p-num) # y 좌표, y 좌표값음 i에서 1씩 감소, 1에 그룹 내 가장 큰수와 구하고자 하는 수의 차이를 더해서 구함
            break
    return xyArr
def xyToNum(x, y):	#좌표->숫자 변환 함수
    group = (x+y)-1 #  각 그룹 =  두 좌표의 합 -1
    total = 0 # 최댓값
    for i in range(1, group+1):
        total += i 
#         좌표가 속한 값을 구하고 y의 좌표 값이 1부터 커지는 원리를 이용해 그룹의 최댓값을 구한다.
# y좌표는 그룹의 최댓값에서부터 1씩 감소하는 특징이 있기 때문에 최댓값과 현재 좌표를 이용하면 num을 구할 수 있다.
#         total += i
    return total - (y-1) # 최댓값 - (y-1) = 현재 좌표가 가리키는 num
T = int(input())
for test_case in range(1, T+1):
    p, q = map(int, input().split())
    a = numToXy(p)
    b = numToXy(q)
    x = a[0] + b[0]
    y = a[1] + b[1]
    print("#{} {}".format(test_case, xyToNum(x, y)))

# 숫자와 좌표간의 상관관계는 위의 표와 같다.

# 색깔로 구분한 숫자들을 하나의 그룹이라고 표현할 때 각 그룹에 속한 숫자의 갯수 i는 1, 2, 3, 4개로 순차적으로 늘어남을 알 수 있다.

# 또한 각 그룹의 x좌표는 1에서 시작해 i까지 증가하고 y좌표는 i에서 시작해 1씩 감소하는 양상을 보인다.

# 이를 이용해 두 개의 함수를 만들었다

# p_cnt 그룹을 확인할 변수, 그룹을 늘려나가며 해당 수가 어떤 그룹에 속하는지 확인

# xyArr x, y좌표를 담을 배열

# total_p 1부터 p_cnt까지의 총합을 저장할 변수. 만약 p_cnt가 4라면 total_p는 1+2+3+4=10이고, 이는 그룹4의 마지막 수이다.

 

# p_cnt 값을 늘려나가며 num2에서 p_cnt를 빼준다.

# num2의 값이 음수거나 0이라면 해당 p_cnt가 num의 그룹이 된다.

# 만약 num의 값이 5였다면
# num2 - 1 - 2 - 3일때 num2의 값이 음수가 된다.
# 따라서 5의 그룹은 3 (p_cnt = 3) 이다.

# i = 그룹값일 때, 

# 각 그룹의 x좌표는 1에서 시작해 i까지 증가하고 y좌표는 i에서 시작해 1씩 감소하므로 해당 원리를 이용해 x, y 좌표를 구한다.

# x좌표는 i에서 그룹 내 가장 큰 숫자와 구하고자 하는 숫자의 차이를 빼서 구할 수 있다.

# 예를 들어 9의 x좌표를 구하고 싶다면 먼저 9의 그룹을 구한다.(=4)

# 이후 해당 그룹의 최댓값(1+2+3+4=10)에서 num 값(=9)을 뺀 결과(=1)를 그룹값에서 빼주면 x좌표가 된다.

# y좌표는 1에 그룹 내 가장 큰 숫자와 구하고자 하는 숫자의 차이를 더해서 구할 수 있다.

# 9의 y좌표를 구하려면 y값이 시작되는 1에 해당 그룹의 최댓값(1+2+3+4=10)에서 9를 뺀 값(=1)을 더해주면 된다.

# 위 표에서 보면 각 그룹은 (두 좌표의 합-1)의 값과 같다.

# 이를 이용해 좌표가 속한 값을 구하고 y의 좌표 값이 1부터 커지는 원리를 이용해 그룹의 최댓값을 구한다.

# y좌표는 그룹의 최댓값에서부터 1씩 감소하는 특징이 있기 때문에 최댓값과 현재 좌표를 이용하면 num을 구할 수 있다.


# 위의 표에서 규칙을 찾은 결과, 최댓값-(y-1)을 해주면 현재 좌표가 가리키는 num값을 찾을 수 있다.

 

# 만약 (x, y) = (2,3)이라면

# 2(=x)+3(=y)-1 = 4이므로 해당 좌표의 그룹값은 4이다. 

# 해당 그룹의 최댓값은 1+2+3+4=10이다.

# 최댓값 10에서 (y-1)를 진행하면 10-(2-1)=9로 num을 찾을 수 있다.




# 참고 코드

def make_list(start_list, target):
    while start_list[-1] <= target:
        start_list.append(len(start_list)+start_list[-1])
    gap = (target-start_list[-2])
    x, y = 1+ gap, (len(start_list)-1) - gap
    return x, y
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number_list = list(map(int, input().split()))
    number_list.sort()
    start_list = [1]
    x1, y1 = make_list(start_list, number_list[0])
    x2, y2 = make_list(start_list, number_list[1])
    x = x1+x2
    y = y1+y2
    
    while len(start_list) < (x+y):
        start_list.append(len(start_list)+start_list[-1])
    answer = start_list[-2] + (x-1)
    print(f"#{test_case} {answer}")


# 풀이

# 1 -> 2,3 -> 4,5,6 이런식으로 생각해보자.

# 각 줄의 첫번째 값들의 x좌표는 무조건 1, y좌표는 n번째 줄이므로 (1,n) 좌표라 생각하면 된다.

# 옆으로 갈때 x좌표는 +1 y좌표는 -1 이기 때문에 좌표값들의 합산은 같은 줄에서는 모두 같다.

 

# 즉 (4,4) 좌표의 값을 찾고자 한다면? ->4+4 인 8이며 n-1을 한 7번째줄의 4번째 값을 출력하면 된다.

# n에 1을 뺀 이유는 맨 첫번째 x값이 1로 고정되었기 때문에 1+n이 x+y값이 되기 때문이다.

 

# 즉 메인값들 (계차수열 형태를 가진다.)을 가진 리스트를 구하고자하는 값을 포함할 정도로 만든 후

# 좌표를 찾으면 된다.

 

# 내가 만든 코드는 메인 값들에서 두번째로 큰 수와 같은 줄에 찾고자하는 값이 있기 때문에 [-2]를 사용하게 되었다.
