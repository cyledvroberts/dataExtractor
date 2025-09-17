Cyle Roberts
CS 485 Project 1
Dependencies:
regex library
This program extracts email address and phone numbers from
disk images or memory images that are in raw/dd format.
The program takes in 2 Command line arguments using the argparse library. 
A -phonenumber flag and a -email flag.
The program writes the list of phone numbers to a phonenumber.txt file and the
emails to an emails.txt file in the same directory as the program.
For example you can call the program with the command line input 
'python .\\dataExtractor -phonenumbers'.
This program writes to standard out the size of the lists for the total emails,
unique emails, total phone numbers, and unique phone numbers.
This program reads the input file 2 lines at a time to handle cases where a phone
number or email address is broken up by a new line character.
