"""
문제 5] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

    *
   **
  ***
 ****
*****

"""

for i in range(5, 0, -1):
    for j in range(1, 6):
        if i <= j:
            print("*", end="")
        else:
            print(" ", end="")
    print()