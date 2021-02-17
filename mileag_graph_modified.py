# %%
import numpy as np
import matplotlib.pyplot as plt


# 주어진 E(e)와 초기 마일리지에 대해, '초반' 전략가의 마지막 활동 라운드와 '후반' 전략가의 마지막 활동 라운드 리턴
def end_round(e, init_mileage):
    used_mileage_i = 0
    used_mileage_f = 0
    round_i, round_f = 0, 0
    for k in range(1, 100000000):
        if used_mileage_i + (k+e) > init_mileage:
            round_i = k-1
            break
        else:
            used_mileage_i += (k+e)
    for k in range(round_i+1, 1000000):
        if used_mileage_f + (k+e) > init_mileage:
            round_f = k-1
            break
        else:
            used_mileage_f += (k+e)
    return round_i, round_f


# 각 전략가 집단이 채역가는 총 파이 리턴
def get_pi(e, init_mileage, point_list):
    round_i, round_f = end_round(e, init_mileage)
    pi_i = sum(point_list[:round_i+1])
    pi_f = sum(point_list[round_i+1:round_f+1])
    return pi_i, pi_f

########################### 여기만 조절하면 됨 ##########################
INIT_MILEAGE = 100  # 초기에 각 플레이어에게 주어지는 마일리지
POINT_LIST = [0]  # POINT_LIST[k] = k라운드 보상 포인트
# 지수적으로 증가하는 보상
INCREASE_RATE = 1.1
for k in range(1, 100):
    POINT_LIST.append(100 * INCREASE_RATE**(k-1))
########################################################################

e_list = np.arange(0, 10, 0.01).tolist()
round_i_list, round_f_list = [], []
pi_i_list, pi_f_list = [], []
for e in e_list:
    ri, rf = end_round(e, INIT_MILEAGE)
    round_i_list.append(ri)
    round_f_list.append(rf)
    pi, pf = get_pi(e, INIT_MILEAGE, POINT_LIST)
    pi_i_list.append(pi)
    pi_f_list.append(pf)


plt.figure()

plt.subplot(1,2,1)
plt.title("E(e) - (End Round) Curve\nRed: i, Blue: f")
plt.xlim([0, 10])
plt.ylim([0, 20])
plt.plot(e_list, round_i_list, color="red")
plt.plot(e_list, round_f_list, color="blue")

plt.subplot(1,2,2)
plt.title("E(e) - (Total Pi) Curve\nRed: i, Blue: f, Black: total")
plt.xlim([0, 10])
plt.plot(e_list, pi_i_list, color="red")
plt.plot(e_list, pi_f_list, color="blue")
plt.plot(e_list, list(np.array(pi_i_list)+np.array(pi_f_list)), color="black")

plt.show()
