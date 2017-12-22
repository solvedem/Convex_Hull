
from helper import *

# global variables for board size and
# location of graphical objects

WIDTH = 400
HEIGHT = 400
message_point = Point(int(WIDTH/2.),int(HEIGHT/8.))
err_message_point = Point(int(WIDTH/2.),int(HEIGHT/6.))
entry_point = Point(int(WIDTH/2.),int(HEIGHT/2.))
error_message = Text(err_message_point, "")
message = Text(message_point, "")


def orientation(p1, p2, p3):
    i = (p2[1] - p1[1]) * (p3[0] - p2[0])
    j = (p2[0] - p1[0]) * (p3[1] - p2[1])
    if i - j > 0:
        return 0 # clockwise
    return 1  # counterclockwise

def convex_hull(p, gametype):
    # algorithm convex_hull(p)
    # input - a set p of points on the plane
    # output - a list containing the vertices of convex_hull of p in clockwise order

    # sort the points by x coordinate
    if gametype == "user":
        points = sort_tuples_x(p)
    else:
        points = p
        points.sort(key=lambda x: x[0])

    # compute upper hull    
    n = len(p)
    upper_hull = [points[0],points[1]]
    for i in range(2,n):
        upper_hull.append(points[i])
        while len(upper_hull) > 2 and orientation(upper_hull[-3],upper_hull[-2],upper_hull[-1]) == 1:
            upper_hull.remove(upper_hull[-2])

    # compute lower hull
    lower_hull = [points[-1],points[-2]]
    for i in range(0,n)[::-1]:
        lower_hull.append(points[i])
        while len(lower_hull) > 2 and orientation(lower_hull[-3],lower_hull[-2],lower_hull[-1]) == 1:
            lower_hull.remove(lower_hull[-2])

    # remove first and last point from lower_hull to avoid
    # duplication of the points where the upper and lower hull meet
    lower_hull.pop(0)
    lower_hull.pop(-1)

    # return complete hull
    return upper_hull + lower_hull

        
def main():
    win = GraphWin("Convex Hull", WIDTH, HEIGHT)
    win.setCoords(0,0,WIDTH,HEIGHT)
    input_box = Entry(entry_point, 10)
    input_box.draw(win)
    message.setText("Simulation (s) or user input(u)")
    message.draw(win)
    win.getMouse()
    
    if input_box.getText() == "s":
        points = random_tuples(50)
        input_box.undraw()
        draw_lines(win,convex_hull(points, "simulation"))
        draw_points(win, points,convex_hull(points, "simulation"))
    else:   
        message.setText("How many points?" )
        input_box.setText("")
        error_message.draw(win)
        points = get_n_points(win, message, get_int(win, input_box, error_message) + 1)
        draw_lines(win,convex_hull(points, "user"))

    
    message.setText("Click to close")
    win.getMouse()
    win.close()
main()
