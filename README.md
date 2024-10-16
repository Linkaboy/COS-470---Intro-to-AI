This file takes a desired string string from a text file, formats the text by removing any new line characters, and then creates a random ascii string of parents/children based off the length of the desired string.
Afterwards the program then sees which parents/children are most similar to the desired string, and makes a list based off that sorted list.
Then it takes the most fit and least fit parent/child, combines the two by spicing the data, and then makes a child based off that spiced data
Splicing happens by adding the correct characters from the first parent into a string. Then it fills in the rest of the data from the second parent with a potential mutation at a fixed rate.
After a new children are made they then are checked to see who is the best fit.
The program then prints out who is best fit in that generation, the fitness score of the child, and the generation number.
The program proceeds to repeat until the desired string is met. Once the string is met the program prints out the string, the fitness score, and the generation number.


Fun notes:
- The program generations operate based off a log(n) number complexity.
- At large numbers the program usually takes between 2400 and 2800 generations.
- This has been tested at an interval of a 75,000 character text file for fun.
