Cellular automata in a lion-antelope world

The file CellularAutomata.py implements the basic requirements as stipulated in the project requirements. Lions and antelopes live in a grid and interact with each other and their environment as specified by the rules.

When the program stars the user is asked for parameters for the grid:
First the size, rows by colomns
then the ratio of empty space to lions to antelopes. It then asks the user to enter the number of generations that should pass, but if the user enters nothing the generations pass indefinably until the user interrupts it.
When it finishes it prints some info and stops.

Problems:
Problems were initially finding an efficient algorithm to solve the problem. Implementing the rules and avoiding errors were laborious.
Optimising the code also took some time, but I did change some of the programming and the results were good, the biggest time consumer was the output. I was surprised that the simple method of printing each element in a for-loop took so much time, and that adding all the elements into one string saved so much time
Also when I added some features and made the program more modular a lot of editing with respect to undefined variables and global names had to be done.
To solve the problem of the marginal animals I added an edge to the whole grid, it is never printed out and any animals in it never get accessed, but it helps to keep the evaluation of the animal’s area constant. This is just a lazy solution to a problem with many other ways to fix.

Features:
The user can choose between running with or with the features in the checkbox.
The file GenerationFeat.py implements some features I was playing around with.
It contains a menu for choosing whether you want to view the next generation of the one you just finished, also whether you want to continue with that grid, and for starting a new one.
The antelopes now also have random deaths, and more likely than lions, it seems logical that antelopes will die more regularly of random stuff than lions.
Also the lions can rove around now, if they are overcrowded and there a space nearby, they move to it.

GUI
With the GUI I had a few more problems, frankly I was unable to learn the ins and outs of Tkinter in one week, hopefully I will improve this week. I got Tkinter to run the very basic of the Cellular Automata. It takes the specs in entry boxes, and runs the grid, and thats that. It just runs the basic requirements, no room made for the features, yet.
I stuggled initially with printing the grid onto canvas, actually I still am cause it only prints text, not images, yet. Then i just couldn't figure out a way to make to loop stop when the user wanted it to, but I finally made this cumbersome way of defining an Interrupt class, and changing it's state when the user pressed the stop button, and then the while loop getting it's boolean from there, but I figured that out about an hour before hand-in, and it works, so.
I am planning to improve the GUI this week, graphically and in performance, hopefully file compression won't be that hard.

Recording and file compression:
The user states whether he wants to record by the checkbox on the window. When the simulation is finished the user can
replay the recording by pressing the button. Unfortunately this does not give the desired result, some random lions and antelopes
are display on the canvas after a wait, but the grid seems to be correctly saved on the record.txt file. So this was a bit
hard.

