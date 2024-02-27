import turtle
t = turtle.Turtle()
t.speed(1000)
sum = 0
for i in range(5):
    num = int(input())
    sum += num
print(sum/5)
input()