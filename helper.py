from graphics import *
from random import choice

def get_int(window, entry_obj, error_msg):
    while True:
        window.getMouse()
        input_str = entry_obj.getText()
        try:
            value = int(input_str)
            break
        except:
            entry_obj.setText("")
            error_msg.setText("Error. Enter an integer. ")

    entry_obj.undraw()
    error_msg.setText("")
    return value

def get_n_points(window, msg, n):
    i = 1
    points = []
    while i < n:
        msg.setText("Enter point: " + str(i))
        point = window.getMouse()
        circle = Circle(point, 5)
        circle.draw(window)
        points.append(point)
        i += 1
    msg.setText("")
    return points


def x_values(points_list):
    return [i.getX() for x in points_list]


def tuples(points_list):
    tuples = []
    for point in points_list:
        tuples.append((point.getX(),point.getY()))
    return tuples

def sort_tuples_x(points_list):
    list_ = tuples(points_list)
    list_.sort(key=lambda x: x[0])
    return list_

def random_tuples(n):
    list_ = []
    for i in range(n):
        x = choice(range(10,380))
        y = choice(range(10,380))
        list_.append([x,y])
    return list_

def draw_lines(window,points):
    i = 0
    while i < len(points) - 1:
        p1 = Point(points[i][0],points[i][1])
        p2 = Point(points[i+1][0],points[i+1][1])
        line = Line(p1,p2)
        line.draw(window)

        i+=1

    p1 = Point(points[0][0],points[0][1])
    p2 = Point(points[-1][0],points[-1][1])
    line = Line(p1,p2)
    line.draw(window)

def draw_points(window,points,ch):
    for point in points:
        p1 = Point(point[0],point[1])
        p = [point[0],point[1]]
        circle = Circle(p1,5)
        if p in ch:
            circle.setFill("blue")
        circle.draw(window)

