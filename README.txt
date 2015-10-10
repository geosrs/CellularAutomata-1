Cellular automata in a lion-antelope world

The file CellularAutomata.py implements the basic requirements as stipulated in the project requirements.
Lions and antelopes live in a grid and interact with each other and their environment as specified by the rules.

When the program stars the user is asked for parameters for the grid:
Size, rows by colomns
Ratio of empty space to lions to antelopes
The number of generations that should pass, by default the generations pass indefinately until interrupted.
When it finishes it prints some info and stops.

Features:
The user can choose between running with or with the features in the checkbox.
The file GenerationFeat.py implements some features I was playing around with.
It contains a menu for choosing whether you want to view the next generation of the one you just finished,
also whether you want to continue with that grid, and for starting a new one.
The antelopes now also have random deaths, and more likely than lions.
Also the lions can rove around now, if they are overcrowded and there a space nearby, they move to it.

Recording and file compression:
The user states whether he wants to record by the checkbox on the window.
When the simulation is finished the user can replay the recording by pressing the button.


