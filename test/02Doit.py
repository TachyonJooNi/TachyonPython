# Q1
# 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
kor, eng, math = 80, 75, 55
avg = (kor + eng + math) / 3
print("평균점수 : ", avg)


# Q2
# 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
num = 13
if num % 2 == 0:
    print("13은 짝수입니다.")
else:
    print("13은 홀수입니다.")


# Q3
# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD)
# 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# ※ 문자열 슬라이싱 기법을 사용해 보자.
juminnum = "881120-1068234"
datebirth = juminnum[:6]
uniquenum = juminnum[7:]
print("생년월일 :", datebirth)
print("주민번호 뒷 7자리 :", uniquenum)


# Q4
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을
# 나타내는 숫자를 출력해 보자.
juminnum = "881120-1068234"
sex = juminnum[7]
print("주민번호의 성별번호 :", sex)


# Q5
# 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로
# 바꿔서 출력해 보자.
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
