'''
파일명 : 05set.py

집합(Set)
  : 객체를 참조하기 위한 순서가 없는 Colletion으로 원소를
  쉽게 추가, 삭제할 수 있다.
  딕셔너리에서 value를 제거하고, key만 남은 상태와 같다.
'''
# set() 함수를 통해 새로운 set을 생성한다.
empty_set = set()
print(empty_set)  # set()

# set()의 인자로 리스트를 전달하여 set으로 변환한다.
even_set = set([0, 2, 4, 6, 8])
print(even_set)  # {0, 2, 4, 6, 8}

# 생성과 동시에 초기화 한다. 이때 중복값은 제거된다.
odd_set = {1, 3, 5, 7, 9, 7, 5, 3, 1}
print(odd_set)  # {1, 3, 5, 7, 9}

# 새로운 set 초기화
myset = {1, 3, 5}  # 초기화

# 추가(add()) : 새로운 원소를 추가한다.
myset.add(7)
print("myset1=", myset)  # {1, 3, 5, 7}

# update() : 여러개의 원소 추가
myset.update({4, 6, 8})
print("myset2=", myset)  # {1, 3, 4, 5, 6, 7, 8}

# 삭제. 단 여러개를 삭제할 수 없다.
myset.remove(1)
print("myset3=", myset)  # {3, 4, 5, 6, 7, 8}

# 모든 원소를 한꺼번에 삭제한다.
myset.clear()
print("myset4=", myset)  # set()

# 집합 연산이 가능하다.
set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 5}
print("합집합", set_a | set_b)  # {1, 2, 3, 5, 7, 9}
print("교집합", set_a & set_b)  # {1, 5}
print("차집합", set_a - set_b)  # {3, 7, 9} (a에서 b를 뺸 결과를 출력한다.)

'''
set()
{0, 2, 4, 6, 8}
{1, 3, 5, 7, 9}
myset1= {1, 3, 5, 7}
myset2= {1, 3, 4, 5, 6, 7, 8}
myset3= {3, 4, 5, 6, 7, 8}
myset4= set()
합집합 {1, 2, 3, 5, 7, 9}
교집합 {1, 5}
차집합 {9, 3, 7}
'''
