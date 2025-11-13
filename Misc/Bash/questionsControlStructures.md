Question 1 of 12
How should you decide whether to use a while or an until loop?


Until loops always test a logical value, and while loops always test a numeric value.

You should decide based on how your test condition works, and how you want to think about the loop operation.

Until loops are timers, and while loops are for infinite operations.

While loops can only count upwards, and until loops can only count downward.

2

Question 2 of 12
Which of these is valid syntax for a basic if statement?


if [ $a -lt $b ]; then echo "yes" end

if [ $a -lt $b ] echo "yes" fi

if [ $a -lt $b ]; then echo "yes" fi

if [ $a -lt $b ]; then echo "yes" done

3

Question 3 of 12
If a loop never reaches an exit condition, it can run forever. If this happens to your program, what's the best way to tell the program to stop?


wait until the computer gets tired of running the program

press Esc

press Ctrl-C

close the terminal window

3

Question 4 of 12
This program will read lines from my.txt and print them to the screen _____.


while my.txt; do echo $line done

for line in my.txt; do echo $line done

while read l; do echo $l done < my.txt

read my.txt; do echo $line done

3

Question 5 of 12
To read and write text files from a script, what operation(s) do you use?


pipes

Bash's sophisticated file-handling library, Bash.read

input and output redirection

command substitution, where you call a text editor to communicate with a file

3

Question 6 of 12
To count to five using a for loop, you might write _____.


for i in {1..5} echo $i done

for i in {1..5}; do echo $i done

for i in 5; do echo $i done

for i in 1-5; do echo $i done

2

Question 7 of 12
A for loop allows us to _____.


loop over a set of items, either provided explicitly or through expansion or substitution

quickly make a loop that only ever cycles 4 times

test a value and determine whether to continue or end the loop

make a loop that runs for the period of time when a condition returns success

1

Question 8 of 12
In order to capture or match a value that isn't included in a case statement's list of entries, which of these can you use?


*)

&)

!)

There is no way to respond to an unexpected value.

1

Question 9 of 12
Which of these might you use to respond to the value of $var?


case $var in car) echo "Vroom!";; bike) echo "Zoom!";; done

if $var in car) echo "Vroom!";; bike) echo "Zoom!";; fi

case $var in car) echo "Vroom!" bike) echo "Zoom!" esac

case $var in car) echo "Vroom!";; bike) echo "Zoom!";; esac

4

Question 10 of 12
To define a function that accepts and uses arguments, you might write _____.


myfunc() { echo ${myfunc[1]} ${myfunc[2]} }

myfunc() { echo $1 $2 }

myfunc($1, $2) { echo $1 $2 }

myfunc { echo $1 $2 }

2

Question 10 of 12
To define a function that accepts and uses arguments, you might write _____.


myfunc() { echo ${myfunc[1]} ${myfunc[2]} }

myfunc() { echo $1 $2 }

myfunc($1, $2) { echo $1 $2 }

myfunc { echo $1 $2 }

2

Question 12 of 12
A function allows us to _____.

create a reusable piece of code, which can optionally take input

Correct

As a script becomes more complex, it can be useful to break up code into functions, if appropriate.


run a program; without it, the program wouldn't function.

define a value to be used later in the script.

repeatedly run a piece of code while a condition evaluates as true

1



