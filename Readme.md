##Requirements for turtle crossing game.##

*Screen*
1.	Screen size (600, 600)
2.	Exit on click
3.	Background white

*Turtle*
4.	Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north
5.	Turtle shape
6.	Turtle size
7.	Starting position of turtle
8.	Pen up 
9.	Detect when the turtle player has reached the top edge of the screen (i.e., reached the finish_line_y). when this happens, return the turtle to the starting position and increase the speed of the cars. hint: think about creating an attribute and using the move_increment to increase the car speed.

*Cars*
10.	Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
11.	No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. 
12.	Shape of cars
13.	Random colour of cars 
14.	Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

*Scoreboard*
15.	

*Rules and scoring*
16.	A turtle moves forwards when you press the "Up" key. It can only move forwards.
17.	When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
18.	When the turtle collides with a car, it's game over and everything stops.
19.	Detect when the turtle player collides with a car and stop the game if this happens.
20.	Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.

*Miscellaneous*
21.	Possible sound of walking
22.	Sound of cars moving
23.	Sound of collision
