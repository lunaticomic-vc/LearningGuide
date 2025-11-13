Conditional statements with the "if" keyword

Question 1 of 18
As compared with the regular test notation, the extended test notation allows us to _____.


have a single test with more than one condition

see a return status indicating whether the result of the evaluation is true or false

compare the value of numbers instead of just strings

There is no difference between regular and extended test.

1

Question 2 of 18
What do you use to return the result of a mathematical operation, without modifying the value of any variables involved?


arithmetic evaluation

brace expansion

arithmetic expansion

parameter expansion

3

Question 3 of 18
In order to compare the numeric values of two variables using the test notation, you might write _____.


[ $a < $b ]

[ $a -lt $b ]

$(( $a < $b ))

`$(( $a -lt $b ))

2

Question 4 of 18
What do you use to change the value of an numeric variable?


brace expansion

arithmetic expansion

parameter expansion

arithmetic evaluation

4

Question 5 of 18
Which of these uses extended test notation to compare values?


[ $a -lt $b ]

$( $a -lt $b )

$(( $a -lt $b ))

[[ $a -lt $b && $b -gt 0 ]]

4

Question 6 of 18
Which of these is a test to determine whether the value of the variable myvar is empty?


[ $myvar -eq "" ]

[ $myvar = "" ]

[ -z myvar ]

[ -z $myvar ]

4

Question 7 of 18
To output text, you'll often use which command?


print

echo

stdout

screen

2

Question 8 of 18
Bash should be written _____.


only using Vim or Emacs

only in nano

in any plain-text editor or IDE of your choice

in Microsoft Word

3

Question 9 of 18
This is an example of setting and using a variable _____.


myvar="hello" echo myvar

myvar="hello" echo $myvar

myvar="hello" echo $(myvar)

myvar = "hello" echo $myvar

2

Question 10 of 18
Variables are an example of _____.


arithmetic evaluation

command substitution

parameter expansion

brace expansion

3

Question 11 of 18
To write the word "bright" in red (color code 31), you would write _____.


echo -e "[31mHello[0m"

echo -e "\033[31mHello\033[0m"

echo -e "\031[0mHello\031[0m"

echo "\033[31mHello\033[0m"

2

Question 12 of 18
Using printf instead of echo allows us to _____.


output text to an actual printer instead of the screen

create strings of text without a trailing newline

tokenize values used in the string for easier management and editing, and provide format strings to control the display of text

use variables in a text string

3

Question 13 of 18
While ANSI color codes are more or less standard across various terminal emulators,_____.


you still shouldn't use them

many other escape sequences, like tab and the bell are not

the way you access them varies by platform

displaying them may be disabled by default

4

Question 14 of 18
In Bash, you can use two types of arrays, which are called _____.


flat arrays and tall arrays

lists and hash tables

linear arrays and square arrays

indexed arrays and associative arrays

4

Question 15 of 18
The placeholder for a string value in a printf statement is _____.


%t

%d

%s

%

3

Question 16 of 18
A best-practice shebang line for running Bash scripts is _____.


#/usr/bin/env Bash

#!/usr/bin/env Bash

#!/usr/bin/Bash

#!/bin/Bash

2

Question 17 of 18
The line at the top of a script that tells the shell which interpreter to run is called _____.


a comment

a shebang

the header

the run command

2

Question 18 of 18
If I create an array called myarr with declare -a myarr=("cat" "dog" "bird"), how would I retrieve the value dog from it?


echo $(myarr{1})

echo ${myarr[1]}

echo $myarr[1]

echo ${myarr[2]}

2
