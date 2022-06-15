# SQLite 는 굉장히 가볍고  파이썬 표준 라이브러리로 별도의 설치없이 바로 사용가능하다....
# ...그러므로 import만 하면 데이터베이스를 사용할 수 있다.
# 자료형의 이름만 조금 다르고, 사용하는 쿼리문등은 대부분 비슷하다.
# 별도의 DB가 있는게 아니라?? .db 파일을 만들고 거기에 테이블만들고 저장하고 꺼내면서 사용하는것이다.
# .connect('~~~')했는데 해당 db가 없으면 자동으로 만들고 사용한다.
# Oracle처럼 sql browser라는 SQLite을 다루기 위한 툴이 있다. (.zip (no installer)다운 -> 03압축해제 -> 01잘라냄)

# Connection 객체 : DB와의 연결을 주로 처리한다.
# Cursor 객체 : 데이터를 저장 및 조회를 담당한다.
# 데이터베이스에 BLOB로 이미지와 같은 파일 자체를 저장은 가능하지만 용량이 어마어마해서 DB에 저장하지는 않는다.
# 그래서 넉넉한 서버에 그냥 두고 사용한다.
# 단, 몇 기가바이트가 되는 대용량은 쓸 수 없다.

# pip(핍) : pip는 기본적으로 명령프롬프트에는 없지만 Python을 설치할때 이미 같이 설치했다.
#  - pip란 Python으로 작성된 package software를 install & uninstall 하는 package management system이다.
# pip3의 3는 파이썬 버전을 의미한다.
# 추가적인 내용은 교안 02.개발환경설정 - Jupyter Notebook 을 참조

# sqlite를 사용하기 위한 모듈 임포트
import sqlite3

# 파일 형태로 존재하는 dbase1에 연결한다. 최초 실행이라면 파일이 생성된다.
conn = sqlite3.connect("dbase1")
# 연결한 후 DB작업을 위해 커서를 생성한다.
curs = conn.cursor()

# 테이블생성
"""
파일명 : 17sqlite.py

    첫 실행시에는 문제가 없으나 두번째 실행에서는 이미 테이블이
    존재하므로 예외처리를 해야 아래 문장이 실행된다.
"""
try:
    tblcmd = "create table people (name char, job char, pay int)"
    # 쿼리실행은 execute() 함수를 사용한다.
    curs.execute(tblcmd)
except Exception as e:
    print("[예외발생]테이블은 이미 생성되었습니다.", e)


"""
레코드가 실행할때마다 계속 생성되면 실습에 불편할 수 있어서 주석처리 후 진행

# 레코드삽입
# 방법 1 : 한개의 레코드를 삽입한다. 튜플을 이용해서 인파라미터를 설정한다.
curs.execute("insert into people values (?,?,?)", ("이순신", "장군", 500))

# 방법 2 : 2개 이상의 레코드를 삽입할때는 list를 활용한다.
#   여기서는 list의 원소가 tuple로 구성되어있다.
curs.executemany(
    "insert into people values (?,?,?)", [("강감찬", "장군", 700), ("홍길동", "의적", 800)]
)

# 방법 3 : for문을 이용해서 반복적으로 삽입한다.
rows = [["곽재우", "의병", 1100], ["유성룡", "재상", 1200], ["임꺽정", "의적", 1500]]
for row in rows:
    curs.execute("insert into people values (?,?,?)", row)

# 커밋
conn.commit()
"""


# 조회 1 : 조회된 레코드를 한꺼번에 출력한다.
curs.execute("select * from people")
print(curs.fetchall())
print("------------------------------------")

# 조회 2 : 조회된 결과를 한 행(row)씩 출력한다.
curs.execute("select * from people")
for row in curs.fetchall():
    print(row)
print("------------------------------------")

# 조회 3 : 각 컬럼별로 출력한다.
curs.execute("select * from people")
for (name, job, pay) in curs.fetchall():
    print(name, ":", job, ":", pay)
print("------------------------------------")


"""
연습문제] 이름이 '강감찬'인 레코드의 급여를 9999로 변경하시오. 
"""
curs.execute("update people set pay=? where name=?", (9999, "강감찬"))


"""
연습문제] 급여를 1200인 레코드를 삭제하시오. 
"""
curs.execute("delete from people where pay=?", (1200,))

# 변경된 레코드가 있으면 반드시 커밋해서 테이블에 적용한다.
conn.commit()
