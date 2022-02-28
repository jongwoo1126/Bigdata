"""
날짜 : 2022/02/28
이름 : 박종우
내용 : 파이썬 HTML 페이지 요청 실습
"""

import requests as req

html = req.get('https://naver.com').text
print(html)

print("-"*100)

test = req.get("http://chhak.or.kr/test.html").text
print(test)
