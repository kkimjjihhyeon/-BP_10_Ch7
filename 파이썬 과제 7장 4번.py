def draw_line(): #draw_line라는 이름의 함수 정의
    t.fd(100) #100픽셀 전진
    t.fd(-100) #100픽셀 후진


import turtle #터틀 그래픽 모듈을 포함한다.
t = turtle.Turtle() #turtle대신 t를 쓴다.
t.shape("turtle") #turtle 모듈의 아이콘을 거북이 모양으로 설정

for i in range(12): #코드 12번 반복
    draw_line() #draw_line 함수 호출
    t.lt(30) #왼쪽으로 30도 회전
