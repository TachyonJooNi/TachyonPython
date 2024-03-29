"""
문제 6] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

*****
 ****
  ***
   **
    *
    
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
"""
for i in range(5):
    for j in range(5):
        if i <= j:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 선생님 풀이
for j in range(5):
    # 스페이스는 정비례한다.(행이 증가할때 같이 증가한다.)
    for i in range(j + 1):
        print(" ", end="")
    # *(아스트리크)는 반비례 한다.(행이 증가할때 감소한다.)
    for i in range(5 - j):
        print("* ", end="")
        # print("*", end="")
    print()
