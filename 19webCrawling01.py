# 웹 크롤링 : 웹사이트의 정보를 가져오는 방법 (동행복권사이트에 있는 로또 번호 자동으로 가져오기)
# 가져올 웹사이트를 requests 로 크롤링으로 긁어오고 BeautifulSoup 으로 원하는 정보를 파싱하는 것
# pip3 list 하면 설치한 목록들을 볼 수 있다.
# (C:\01Developkits\Python\Python310\Lib\site-packages 에 깔리고 파이썬으로 작성되어있다.)

# 주석처리를 해가면서 출력내용을 확인함.

"""
웹크롤링을 위해 두가지 라이브러리 설치가 필요하다
pip3 install requests
pip3 install beautifulsoup4
"""
# 모듈 임포트
import requests
from bs4 import BeautifulSoup

# 크롤링 할 웹사티으의 URL 및 접속
url = "https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
# 접속을 위해 requests 모듈을 사용한다.
response = requests.get(url)

# 응답코드가 200이면 접속에 성공한 것이므로 크롤링을 시작한다.
if response.status_code == 200:
    # HTML코드 전체를 받아온다.
    html = response.text
    # 파싱하기 위해 soup 객체로 변환한다.
    soup = BeautifulSoup(html, "html.parser")

    # CSS셀렉터를 통해 원하는 엘리먼트를 추출한다.(크롬 or 엣지)
    title1_1 = soup.select_one(
        "#s_content > div.section > ul > li:nth-child(1) > dl > dt"
    )
    ##print("추출1_1:", title1_1)

    # 파이어폭스에서의 셀렉터를 통해 추출
    """title1_2 = soup.select_one("크롬과 다르게 표현되지만 크롤링은 똑같이 된다.")
    print("추출1_2:", title1_2)"""

    # 텍스트만 추출
    text = title1_1.get_text()
    ##print("추출2:", text)

    # 검색결과 부분에서 <li>태그로 반복되는 부분 크롤링
    ul = soup.select_one("ul.basic1")
    print("추출3:", ul)

    # print("추출4")
    titles2 = ul.select("li > dl > dt > a")
    for tit in titles2:
        print(tit.get_text())
else:
    # 접속에 실패했을때 응답코드를 확인한다.
    print(response.status_code)
