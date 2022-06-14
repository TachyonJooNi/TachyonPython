"""
문제 8] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성 해보세요.

*********
 *******
  *****
   ***
    *

"""
for i in range(5):
    count = 0
    for j in range(5):
        if i <= j:
            count += 1
            print("*", end="")
            if count >= 2:
                print("*", end="")
        else:
            print(" ", end="")
    print()
