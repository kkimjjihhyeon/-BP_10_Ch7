def draw_f(): #draw_f라는 이름의 함수 정의
    for i in range(150):  #코드 150번 반복
        t.goto(i,(i**2+1)*0.01) #(x, y+100)좌표로 이동


import turtle #터틀 그래픽 모듈을 포함한다.
t = turtle.Turtle() #turtle대신 t를 쓴다.
t.shape("turtle") #turtle 모듈의 아이콘을 거북이 모양으로 설정


t.fd(250) #250픽셀 전진
t.fd(-250) #250픽셀 후진
t.lt(90) #왼쪽으로 90도 회전


t.fd(250) #250픽셀 전진
t.fd(-250) #250픽셀 후진
t.rt(90) #오른쪽으로 90도 회전


draw_f() #draw_f() 함수 호출
