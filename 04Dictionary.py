'''
파일명 : 04Dictionary.py

딕셔너리(Dictionary)
  : List와 비슷하며, 순서는 중요하지 않으나 :(콜론) 문자로 구분되는
  고유키(KEY)와 값(VALUE)으로 지정된다. 값은 변경할 수 있고,
  중괄호{}로 선언한다.
'''
# 생성 1 : dict() 함수를 이용해서 딕셔너리 생성
dic1 = dict(birth=1970, name="홍길동", size="100cm")
print(dic1)
# 생성 2 : 중괄호를 이용한 생성
dic2 = {'one': 1, 'two': 2, 'three': '3'}
print(dic2)

# 반복문을 이용한 딕셔너리 출력
fruits = {'apple': 100, 'grapes': 200, 'orange': 300, 'peach': 400}
print('for문을 이용한 출력')
# key를 먼저 얻어온 후..
for key in fruits:
    # 얻어온 key를 통해 value를 출력한다.
    val = fruits[key]
    # Java의 printf()와 유사한 형태의 출력방식으로 서식문자를 사용한다.
    print("%s : %d" % (key, val))

# len() : 딕셔너리의 크기를 반환
print("길이", len(fruits))
print("복숭아", fruits['peach'])  # 400출력

# key가 동일하면 기존의 값을 변경한다.
fruits['orange'] = 3500
print("오렌지", fruits['orange'])

# del(삭제) : key에 해당하는 값을 삭제한다.
del fruits['peach']
print('fruits=', fruits)

# keys() : 딕셔너리의 키로 된 dict_keys 객체를 반환한다.
get_keys = fruits.keys()
print(get_keys)
for k in get_keys:
    print(k)  # key를 출력한다.

# values() : 딕셔너리의 값들로 된 dict_values 객체를 반환한다.
get_values = fruits.values()
print(get_values)
for v in get_values:
    print(v)  # value를 출력한다.

'''
{'birth': 1970, 'name': '홍길동', 'size': '100cm'}
{'one': 1, 'two': 2, 'three': '3'}
for문을 이용한 출력
apple : 100
grapes : 200
orange : 300
peach : 400
길이 4
복숭아 400
오렌지 3500
fruits= {'apple': 100, 'grapes': 200, 'orange': 3500}
dict_keys(['apple', 'grapes', 'orange'])
apple
grapes
orange
dict_values([100, 200, 3500])
100
200
3500
'''
