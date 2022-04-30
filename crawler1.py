import re
import requests as req

s = 'hi'
print(re.match(r'hey', s))

s1 = '이 영화는 F등급 입니다'
print(s1.split('이 영화는 ')[1].split('등급')[0])
print(re.findall(r'이 (..)는 ([ABCF])등급 입니다', s1))


url = "https://finance.naver.com/marketindex/"
res = req.get(url)
body = res.text


r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)
print(captures)

for c in captures:
    print(c[0] + " : " + c[1])

print()
usd = float(captures[0][1].replace(",", ""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해주세요 : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar}달러 환전되었습니다.")
