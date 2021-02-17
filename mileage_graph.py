# %%
import numpy as np
import matplotlib.pyplot as plt


# 주어진 E(e)에 대해, 예상되는 진행 라운드 수를 대강 예상한 것.
def max_round(e):
    cost = 0
    for k in range(1, 1000):
        if cost + (k+e) > 100:
            return k-1
        else:
            cost += (k+e)


# 총 라운드 진행 수 K와, 라운드별 보상 point_list를 받아서, 총 파이 리턴
def get_pi(K, point_list):
    return sum(point_list[:K+1])


########################### 여기부터 보면 됨 ##########################
INIT_MILEAGE = 100  # 초기에 각 플레이어에게 주어지는 마일리지
POINT_LIST = [0]  # POINT_LIST[k] = k라운드 보상 포인트
# 지수적으로 증가하는 보상
for k in range(1, 100):
    POINT_LIST.append(100 * 2**(k-1))
e_list = np.arange(0, 10, 0.01).tolist()
K_list = []
for e in e_list:
    K_list.append(max_round(e))
pi_list = []
for K in K_list:
    pi_list.append(get_pi(K, POINT_LIST))

plt.figure()

plt.subplot(1,2,1)
plt.title("E(e) - #Round Curve")
plt.xlim([0, 10])
plt.ylim([0, 20])
plt.plot(e_list, K_list)

plt.subplot(1,2,2)
plt.title("E(e) - Total Pi Curve")
plt.xlim([0, 10])
plt.plot(e_list, pi_list)

plt.show()

