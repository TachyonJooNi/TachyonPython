"""
문제 3] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.

*
**
***
****
*****

"""

for i in range(5):
    for j in range(5):
        if i >= j:
            print("*", end="")
    print()

# 선생님 풀이
for j in range(5):
    # j의 크기만큼 i를 반복할 수 있도록 한다.
    for i in range(j + 1):
        print("*", end="")
    print()
