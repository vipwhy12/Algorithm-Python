import time

#모든 경우에 제일 좋은 자료구조는 없다. 
#각 방법에 맞는 자료구조를 사용하자.

# 0 ~ 1000000를 리스트에 저장한다.
test_list = [x for x in range(1000001)]

# 0 ~ 1000000를 set에 저장한다.
test_set = set([x for x in range(1000001)])

# 특정 데이터가 리스트에 있는지 확인할 때 걸리는 시간 파악
t_0 = time.time()
print(100000 in test_list)
t_1 = time.time()

print("리스트에서 걸린시간: {}".format(t_1 - t_0))

#특정 데이터가 set에 있는지 확인할 때 걸리는 시간 파악
t_0 = time.time()
print(10000000 in test_set)
t_1 = time.time()

print("set에서 걸린 시간{}".format(t_1 - t_0))

