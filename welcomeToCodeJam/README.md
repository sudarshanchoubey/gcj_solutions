##Welcome to code jam

###To run the program
Type the following on your cmd prompt:

python3 welcomematrix.py < input.in >output.out

The problem can be found at 
https://code.google.com/codejam/contest/90101/dashboard#s=p2


###The solution involves 2 steps.
 * We create a  3-D array size 19,500,2 so we can store the index and the counts for each of the 19 positions in the string "welcome to code jam".We go through the input and populate the indexes at which each character of "welcome to code jam" occurs. e.g.

In an input "wweellccoommee to code qps jam"
'w' is found at 1 and 2 ' ' is found at 15 18 23 27.
I am using 0 index as sentinel implying entry not found.

* In the next step we go through each character 'e' onwards and add the counts for all indexes of the previous character i.e 'w' which are found at an index lower than the index at which a particular 'e' was found.
