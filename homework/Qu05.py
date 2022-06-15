"""
문제 5] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

    *
   **
  ***
 ****
*****

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""

for i in range(5, 0, -1):
    for j in range(1, 6):
        if i <= j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 선생님 풀이
# 3번문제와 동일한 로직으로 시작한다.
for j in range(5):
    # 앞 부분에 스페이스를 넣는 로직을 추가한다.
    # 스페이스는 행에 반비례 하므로 4에서 빼준다.
    for i in range(4 - j):
        print(" ", end="")
    for i in range(j + 1):
        print("* ", end="")
        # print("*", end="")
    print()
