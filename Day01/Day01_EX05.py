temp = 40

#기온 >= 40 이면, 출력 : 매우 덥습니다.
#40 > 기온 >= 30 이면, 출력 : 덥습니다.
#30 > 기온       이면, 출력 : 살만합니다.

if temp >= 40:    # 조건 1
    print("매우 덥습니다.")   # 조건 1이 참이면,
elif temp >= 30:  # 조건 1을 부정 당하고, 조건 2를 확인
    print("덥습니다.")       # 조건 2가 참이면,
else:             # 조건 1, 조건 2도 부정 당했어요
    print("살만합니다.")

print("여기~")