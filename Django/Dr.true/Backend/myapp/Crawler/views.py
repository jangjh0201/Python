import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

def score_board(request):
    # 크롤링 할 웹 주소
    url = "https://sports.news.naver.com/kbaseball/schedule/index.nhn?date=20200825&month=08&year=2020&teamCode="
    
    # pip install requests 를 사용한다.
    req = requests.get(url)
    
    # 전체 페이지 html 가지고 오기
    soup = BeautifulSoup(req.text, 'html.parser')
	    
    
    # ul 태그를 가지고 오려고 하는데 ul 태그의 id 가 todaySchedule이고
    # ul 태그 안에 있는 모든 li를 today_schedule변수 안에 넣는다.
    today_schedule = soup.find('ul', {'id': 'todaySchedule'}).findAll('li')
    
    # 가지고 온 li를 반복문을 돈다.
    for schedule in today_schedule:
    	
        #  상태를 가지고 온다
        # <em class="state">종료</em> 라는 태그 안에 있는 종료 값을 가지고 오고
        # .strip()을 이용해서 앞 뒤 공백을 제거한다.
        state = schedule.find('em', class_='state').text.strip()

        # <div class="vs_lft"></div> 태그를 찾는다
        left = schedule.find('div', class_='vs_lft') 

        # 팀 이름을 찾는다
        left_team = left.p.strong.text.strip()

        # 팀 점수를 찾는다.
        left_team_score = left.find('strong', class_='vs_num').text

        # 왼쪽과 동일하다. 
        right = schedule.find('div', class_='vs_rgt')
        right_team = right.p.strong.text.strip()
        right_team_score = right.find('strong', class_='vs_num').text

        print(state)
        print(left_team, left_team_score)
        print(right_team, right_team_score)
        print('----------------------------------')

    return HttpResponse('')