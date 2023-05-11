# 1208 Flatten  

T = int(input())

for test_case in range(10):
    boxes = list(map(int, input().split()))
    boxes.sort()
    for i in range(T):
        max[boxes] -= 1
        min[boxes] += 1
        if (max[boxes] - min[boxes]) <= 1:
            ans = max[boxes] - min[boxes]
            print("#{} {}".format(test_case, ans))
    print("#{} {}".format(test_case, (max[boxes] - min[boxes])))