# Convex_Hull
Graphical Convex Hull Program

2 modes-

User - User clicks determine input

Simulation - Random points decided by computer

[![ch1.jpg](https://s14.postimg.org/6ne2nwgyp/ch1.jpg)](https://postimg.org/image/dqly3ime5/) [![ch2.jpg](https://s14.postimg.org/lw401oq2p/ch2.jpg)](https://postimg.org/image/e3dc9pk3h/)

Inpired by M. de Berg, M. van Krevald, M. Overmars, & O. Schwarzkopf's Computational Geometry - Algorithms and Applications

In simple terms, this function checks combinations of 3 consecutive points and tests whether three consecutive points make a right turn. If not, the middle one is not part of the hull. (de Berg)

Pseudocode (de Berg)

    CONVEXHULL(P)
    Input. A set of P Points in the plane
    Ouput. A list containing the vertices of CH(P) in clockwise order
    1.    Sort the points by x-coordinate, resulting in a sequence p1,...,pn
    2.    Put the points p1 and p2 in a list Lupper, with p1 as the first point
    3.    for i <- 3 to n
    4.        do Append pi to Lupper
    5.            while Lupper contains more than two points and the last three points in Lupper do not make a right turn
    6.                do Delete the middle of the last three points from Lupper
    7.    Put the points p1 and pn-1 in a list Llower with pn as the first point
    8.    for i <- n - 2 downto 1
    9.        do Append pi to Llower
    10.            while Llower contains more than two points and the last three points in Llower do not make a right turn
    11.                do Delete the middle of the last three points from Llower
    12.    Remove the first and last point from Llower to avoid duplication of the points where the upper and lower hull meet
    13.    Append Llower to Lupper, call the resulting list L
    14.    return L
    
After running this function on a set of inputted or random points, for all of the points on the hull, the program colors them blue and draws lines between them.

This function uses an incremental algorithm to compute the result in O(n log n) time.
