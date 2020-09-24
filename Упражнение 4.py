import turtle

(t_final, a_y, v_x, v_y) = list(map(float, input().split()))
t = 0

turtle.shape('circle')
for steps_of_time_number in range(100):
    t = t + t_final/100
    turtle.goto(v_x*t, v_y*t+a_y*(t**2)/2)
