"""
문제 7] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

    *
   ***
  *****
 *******
*********

"""
for i in range(5, 0, -1):
    count = 0
    for j in range(1, 6):
        if i <= j:
            count += 1
            print("*", end="")
            if count >= 2:
                print("*", end="")
        else:
            print(" ", end="")
    print()

# 선생님 풀이
for j in range(5):
    for i in range(4 - j):
        print(" ", end="")
    # for i in range((2 * j) + 1):
    for i in range(2 * (j + 1) - 1):
        print("*", end="")
    print()
