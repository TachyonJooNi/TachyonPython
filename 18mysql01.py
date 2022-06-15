# MySQL를 좀더 가볍게 만든게 MariaDB 이다. 하지만 명령어의 99%가 같다.
# 좀더 가벼운 MariaDB를 많이 사용한다. 어디가서 꿀리지 않게 다뤄보는 맛만 본다.
# 웹호스팅(cafe24등..) : 전세 (단독서버를 운영하려면 비용문제가 발생)
# 웹호스팅에서 비싼 오라클을 쓰는 경우는 없다.

# 오라클의 시스템계정과 같이 MySQL은 루트계정이 있다 (123456 설정)
# MySQL은 TCP port : 3306 사용 (오라클은 1521이였다.)
# 오라클과 MySQL이 접속에 있어 다른점이 MySQL은 DB,ID,Pass 가 필요하다.
# 오라클은 계정만 생성하여 접속하는 형태지만, MariaDB는 DB계정을 생성하여 접속해야 한다.
# 계정으로만 접근하는 오라클과 다르게 특정한 계정으로 특정한 DB에 접근해야 사용가능하다.
# 사용자 권한 주기
# 코스모디비에 생성된 모든 테이블에 대한 모든 권한에 대해 TO~~에게 준다.
# show tables; : 접속해있는 DB에 있는 모든 테이블을 보겠다.

# 시퀀스가 없는대신 AUTO_INCREMENT, 그래서 시퀀스 하나만들어서 여러테이블에서 쓰는게 안됨.
# 음수가 필요없는 경우 UNSIGNED 를 사용하면 음수범위를 양수범위로 늘려서 사용가능
# 실수사용시 표현범위를 (정수표현범위, 소수점아래표현범위) 로 지정가능

# MariaDB 실습.sql 교안을 봐라.
# MySQL은 commit이 필요없다.
# 에디터마다 => 찾기 : Ctrl + f / 바꾸기 : Ctrl + h


"""
파이썬에서는 MySQL(MariaDB)를 사용하기 위해 PyMySQL 모듈을 설치해야한다.
c:> pip3 install pymysql
"""
# 모듈 임포트
import pymysql

# MariaDB 연결
conn = pymysql.connect(
    host="localhost", user="kosmo_user", password="1234", db="kosmo_db", charset="utf8"
)
"""
    , cursorclass=pymysql.cursors.DictCursor
    => 위 설정이 없는 경우에는 레코드를 튜플로 출력한다.
    해당 설정을 통해 딕셔너리로 출력할 수 있다.
    
    만약 중복설치되어 기본포트인 3306을 사용할 수 없는 상태라면
    connect() 함수를 통해 연결시 port=0000 과 같이 항목을 추가한다.
    포트번호는 문자열("")이 아닌 숫자(int)로 기술해야 한다.
"""
# 커서 생성
curs = conn.cursor()

try:
    sql = "SELECT * FROM board"
    curs.execute(sql)

    # select한 모든 레코드 인출. 반복문 없이 전체를 출력한다.
    rows = curs.fetchall()
    print(rows)

    # 행(레코드)단위로 출력한다.
    print("출력1", "-" * 40)
    for row in rows:
        print(row)

    # 행 단위로 출력하되 각 컬럼의 인덱스를 지정하여 출력한다.
    print("출력2", "-" * 40)
    for row in rows:
        print(row[0], row[1], row[2], end=" ")
        id = row[3]
        pdate = row[4]
        vcnt = row[5]
        print("%s, %s, %s" % (id, pdate, vcnt))

    # format() 함수를 통해 쿼리문에 사용자가 입력한 검색어를 추가한다.
    print("출력3", "-" * 40)
    sql = sql + " WHERE title like '%{0}%' ".format(input("검색어입력:"))
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)

except Exception as e:
    print("쿼리 실행시 오류발생", e)

print("-" * 40)
conn.close()
print("자원반납")
