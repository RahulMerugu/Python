#import sys
#print (sys.argv)
#name = sys.argv[1]
#print ("Hello " + name)


#in output, if i type python CLI.py beau 39, the output is: ['CLI.py', 'beau', '39']
#thus essentially a list is created
#argv stands for arguement values. 

import argparse

parser = argparse.ArgumentParser(
    description = 'This program prints the name of my dogs!'
)

parser.add_argument('-c' , '--color', metavar = 'color' , required = True , choices = {'red' , 'yellow'} , help = 'the color to srarch for')
args = parser.parse_args()
print (args.color)


#Here, we can set the requirements as to what has to be inputted, so if not done correctly, we get:
#usage: CLI.py [-h] -c color
#CLI.py: error: the following arguments are required: -c/--color

#if the input is done as python CLI.py -c red then the output is: red

#when choices is there, then one can only select a color from the given dictionary. In this case scenario, that is red and yellow.
#if the inputted color is not there in the dictionary, we get the output:
#usage: CLI.py [-h] -c color
#CLI.py: error: argument -c/--color: invalid choice: 'blue' (choose from yellow, red)