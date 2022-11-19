def draw_snowman(x, y): #x, y가 매개변수인 draw_snowman라는 이름의 함수 정의

    t.up()   #그림판에서 펜을 뗀다.
    t.goto(x, y+110) #(x, y+100)좌표로 이동
    t.down()  #그림판에 펜을 올려둔다.

    t.begin_fill() #내부색 채우기
    t.circle(35) #반지름이 35인 원 그리기
    t.end_fill() #내부색 채우기 끝

    t.up()
    t.goto(x, y+80) #(x, y+80)좌표로 이동
    t.down()

    t.lt(20) #왼쪽으로 20도 회전
    t.fd(90); t.fd(-90) #90픽셀 전진, 90픽셀 후진
    t.lt(115) #왼쪽으로 115도 회전
    t.fd(90); t.fd(-90)
    t.seth(0) #거북이의 방향을 동쪽으로 설정

    t.begin_fill()
    t.circle(25) #반지름이 25인 원 그리기
    t.end_fill()

    t.up()
    t.goto(x,y) #(x, y)좌표로 이동
    t.down()

    t.begin_fill()
    t.circle(50) #반지름이 50인 원 그리기
    t.end_fill()


import turtle  #터틀 그래픽 모듈을 포함한다.
t = turtle.Turtle() #turtle대신 t를 쓴다.
s = turtle.Screen() #그림이 그려지는 화면을 얻는다.

t.color('black', 'white') #펜의 테두리색 검은색, 내부색 하얀색으로 설정
s.bgcolor('skyblue') #배경화면을 하늘색으로 변경


for i in range(3):  #코드 3번 반복
    draw_snowman(200*i-200,0) #draw_snowman 함수호출 (200*i-200,0)를 인수로 설정


