def draw_hexa(): #draw_hexa라는 이름의 함수 정의
    for i in range(6): #코드 6번 반복
        t.fd(50)  #50픽셀 전진
        t.rt(60)  #오른쪽으로 60도 회전


import turtle #터틀 그래픽 모듈을 포함한다.
t = turtle.Turtle() #turtle대신 t를 쓴다.
t.shape("turtle") #turtle 모듈의 아이콘을 거북이 모양으로 설정

for i in range(6): #코드 6번 반복
    t.fd(50)   #50픽셀 전진
    t.lt(60)   #왼쪽으로 60도 회전
    draw_hexa() #draw_hexa 함수 호출
