"""
문제 4] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

*****
****
***
**
*
"""

for i in range(5):
    for j in range(5):
        if i <= j:
            print("*", end="")
    print()

# 선생님 풀이
for j in range(5):  # 0, 1, 2...
    # 행(j)에 반비례 하므로 전체 행에서 j를 빼준다.
    for i in range(5 - j):  # 5, 4, 3...
        print("*", end="")
    print()
