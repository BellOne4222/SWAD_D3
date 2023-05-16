# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금

# 퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.

# 우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.

# 예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.

# 교환전>



# 처음에는 첫번째 숫자판의 3과 네 번째 숫자판의 8을 교환해서 8, 2, 8, 3, 8이 되었다.
 


# 다음으로, 두 번째 숫자판 2와 마지막에 있는 8을 교환해서 8, 8, 8, 3, 2이 되었다.



# 정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.

# 숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.

# 위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.

# 여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.

# 다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다.



# 94의 경우 2회 교환하게 되면 원래의 94가 된다.

# 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.

# [입력]


# 가장 첫 줄은 전체 테스트 케이스의 수이다.

# 최대 10개의 테스트 케이스가 표준 입력을 통하여 주어진다.

# 각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.

# 숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.

# [출력]

# 각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.

# 같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.

# DFS와 백트래킹
# 깊이 우선 탐색(DFS)

# DFS는 가능한 모든 경로(후보)를 탐색합니다. 따라서, 불필요할 것 같은 경로를 사전에 차단하거나 하는 등의 행동이 없으므로 경우의 수를 줄이지 못합니다.

# 따라서 N! 가지의 경우의 수를 가진 문제는 DFS로 처리가 불가능할 것입니다.

# 백트래킹(Backtracking)

# 해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 그 경로를 더이상 가지 않고 되돌아갑니다.

# 즉, 코딩에서는 반복문의 횟수까지 줄일 수 있으므로 효율적입니다.

# 이를 가지치기라고 하는데, 불필요한 부분을 쳐내고 최대한 올바른 쪽으로 간다는 의미입니다.

# 일반적으로, 불필요한 경로를 조기에 차단할 수 있게 되어 경우의 수가 줄어들지만, 만약 N!의 경우의 수를 가진 문제에서 최악의 경우에는 여전히 지수함수 시간을 필요로 하므로 처리가 불가능 할 수도 있습니다. 가지치기를 얼마나 잘하느냐에 따라 효율성이 결정되게 됩니다.

# 정리하자면, 백트래킹은 모든 가능한 경우의 수 중에서 특정한 조건을 만족하는 경우만 살펴보는 것입니다.

# 즉 답이 될 만한지 판단하고 그렇지 않으면 그 부분까지 탐색하는 것을 하지 않고 가지치기 하는 것을 백트래킹이라고 생각하면 됩니다.
# 주로 문제 풀이에서는 DFS 등으로 모든 경우의 수를 탐색하는 과정에서, 조건문 등을 걸어 답이 절대로 될 수 없는 상황을 정의하고, 그러한 상황일 경우에는 탐색을 중지시킨 뒤 그 이전으로 돌아가서 다시 다른 경우를 탐색하게끔 구현할 수 있습니다.
# 👍 백트래킹 기법의 유망성 판단
# 어떤 노드의 유망성, 즉 해가 될 만한지 판단한 후 유망하지 않다고 결정되면 그 노드의 이전(부모)로 돌아가(Backtracking) 다음 자식 노드로 갑니다.

# 해가 될 가능성이 있으면 유망하다(promising)고 하며, 유망하지 않은 노드에 가지 않는 것을 가지치기(pruning) 한다고 하는 것입니다.

# https://chanhuiseok.github.io/posts/baek-1/ : 참고 문제


# 풀이

# 시간 복잡도가 최대 6자릿수에서 2개를 교환하는 방식이므로 6C2 = 15 ^ 10 이므로 시간 복잡도가 매우 크다 -> 그래서 가지치기 필요

# 백트래킹 사용

# 종료 조건 : 교환 횟수가 끝날 때까지 최댓값 반환


def dfs(n):
    global ans
    if n==N: # 반복 횟수 끝이라면 ans를 ans와 리스트로 갱신
        ans = max(ans, int("".join(map(str,lst)))) # 최댓값 반환
        return
 
    # L개에서 2개뽑는 모든 조합(둘을 교환)
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]
 
            chk = int("".join(map(str,lst)))*10+n # 교환 횟수 + n
            if chk not in visited: # 중복 방지를 위해 visited에 없으면 dfs 호출 -> 중복 방지, 가지 치기 : 다 끝나고 올라오면서 체크를 하는 방식
                dfs(n+1) # 백트래킹 호출
                visited.append(chk)
 
            lst[i], lst[j] = lst[j], lst[i] # 반드시 원상복구!!
 
T = int(input())
for test_case in range(1, T + 1):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))     # lst => 정수값
    L = len(lst)
    ans = 0
    visited = []
    dfs(0)
    print(f'#{test_case} {ans}')


#D3 1244 최대상금
 
#경우의 수 찾기, 매개변수로 몇번 바꿧는지 적는다.
def dfs(count):
    global answer
    #횟수를 다 사용했다면
    if not count:
        #숫자로 바꿔보고
        temp = int(''.join(values))
        #가지고 있는 최대수보다 크다면 갱신
        if answer < temp:
            answer = temp
        return
    # 바꿔야 하니까 이중 포문
    for i in range(length):
        #경우의 수를 찾는거니까 i보다 큰위치부터
        for j in range(i+1, length):
            #두개의 위치를 바꾸고 나서
            values[i], values[j] = values[j], values[i]
            #가지치기 해야하니까 일단 합쳐보고
            temp_key = ''.join(values)
            #어떤수가 몇회차에 나왔는지 체크 1이면 안나온거니까 경우의수에 넣어주기
            if visited.get((temp_key, count-1), 1):
                #이숫자는 몇회차에 사용했으니까 체크해주고
                visited[(temp_key, count-1)] = 0
                #dfs도 돌려주고
                dfs(count-1)
            #다 썻으면 원상복귀
            values[i], values[j] = values[j], values[i]
 
 
for t in range(int(input())):
    answer = -1
    value, change = input().split()
    #바꾸기 편하려고 리스트화시킴
    values = list(value)
    change = int(change)
    #계속 쓸꺼니까 캐스팅
    length = len(values)
    #가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print('#{} {}'.format(t+1, answer))

# 완전탐색으로 풀려고 하면 시간초과가 생기기때문에 백트래킹, 가지치기 작업이 필요하다.

# 제가 여기서 생각했던 가지치기는 '같은 교환회수일때 이미 나온 수라면 넘아가자' 다.

# 이러한 정보를 딕셔너리를 이용하여 저장해 문제를 풀어나갔다.

def dfs(cnt):
    global answer
    if cnt == t:	#최대 교환횟수에 도달하면
        temp = ''.join(num)	#문자열 변환
        answer = max(answer, temp)	#answer와 비교해 더 큰 숫자를 answer변수에 담기(문자열 타입의 숫자도 대소비교 가능)
        return	#종료
    for i in range(len(num)):
        for j in range(i+1, len(num)):
	        #하나씩 교환
            num[i], num[j] = num[j], num[i]
            temp = ''.join(num)
            #get(): visited에 (temp, cnt)라는 key가 존재하지 않으면 1리턴
            #방문한 적 있다면 재방문 금지->시간초과 방지
            #방문한 적 없다면 방문처리 후 방문
            if visited.get((temp, cnt), 1):
                visited[(temp, cnt)] = 0
                dfs(cnt+1)
            #dfs수행이 종료되었다면 다른 경로의 dfs 수행을 위해 num 원상복구
            num[i], num[j] = num[j], num[i]	
            
T = int(input())
for test_case in range(1, T + 1):
    num, t = input().split()
    num = list(num)
    t = int(t)	#교환횟수
    answer = "0"	#answer 초기화
    visited = {}	#방문했는지 확인하는 용도
    dfs(0)
    print("#{} {}".format(test_case, answer))


# 내 풀이

def dfs(change):
    global max_money 
    if change == max_change: # 교환 횟수가 최대 교환 횟수와 같아지면
        changed = ''.join(num_table) # 바꾼 숫자판을 문자열로 변환
        max_money = max(max_money, changed) # 금액 최댓값은 금액 최댓값과 바꾼 숫자판을 문자열로 변환한 것중 큰 것을 최댓값으로 갱신
        return 
    
    for i in range(len(num_table)): # 두 개씩 뽑아서 조합을 만들어 비교한다. 
        for j in range(i+1, len(num_table)):
            num_table[i], num_table[j] = num_table[j], num_table[i] # 교환
            changed = ''.join(num_table) # 숫자판을 바꾸면 합쳐서 문자열로 만들어서 비교
            if visited.get((changed, change), 1): # 가지치기 : visited에 (바꾼 숫자판, 교환 횟수) key가 없으면 1로 처리 -> 방문한 적이 없으면 1 
                visited[(changed, change)] = 0 # 방문을 하면 0으로 바꿔 다음에 다시 방문하지 않게 처리 (방문했던 곳 중복 방지)
                dfs(change+1) # 바꾼 횟수 +1해서 dfs 다시 호출
            num_table[i], num_table[j] = num_table[j], num_table[i] # 다른 경로 탐색을 위해 다시 i, j 돌려놓기


T = int(input())
for test_case in range(1, T + 1):
    num_table, max_change = input().split() # 숫자판, 교환 횟수
    num_table = list(num_table)
    max_change = int(max_change)
    max_money = "0" # 금액의 최댓값
    visited = {} # 방문했는지 확인하는 딕셔너리
    dfs(0)
    print("#{} {}".format(test_case, max_money))


