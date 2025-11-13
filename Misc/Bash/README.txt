$touch
$ls
$echo
$printf

$enable - disables builtin
$ enable -n
$ enable -V

Pipes - изпраща output от една команда като input на друга

$cat "lorem.txt" - access file

Redirection - насочва процес към друга програма
Работи със Standart Input 0; Standart Output 1; Standart Error 2
< takes input// ReadFrom
> override destination file// WriteOver
>> append destination file// WriteTo
<< "here document" - multiple lines //ReadFromMultipleLines

~ - Home Directory
~- - Just Visited Directory

$rm - delete
$clear - empty terminal
$head -n

-i - integer

-lt
-gt
-e

$a vs a

Arithmetic expansion
Arithmetic evaluation
Parameter expansion

extended test notation 

if [[]]
then script
elif (())
then
else script
fi

while condition
do
done

until
do
done

Ctrl + C to fix an infinite loop

for i in 1 2 3 / {1..100} / (( i=1; i<=10; i++)) // ${fruits[@]} // "${!arr[@]}" #access by keys
do // "${arr[$i]" #access the values of keys
done

for i in $(ls) // *
do
work with file
done

case variable in 
testingSetForWhetherItsIncluded) do something ;;
variable|smthelse|orsmthelse) do smth;;
*) #doesnt match# do smth;;
esac

functions:
fname() {
...
}

fname() {
 echo "$1"
}
fname ARG1

$@ - all arguments
$FUNCNAME - name of function

/* - files in directory

local schrodingersVar = "I only exist in a function"

#Write into file
for i in 1 2 3 4 5
do echo "This is line $i" >> textfile.txt
done

while read f
do echo "I read a line and it says: $f"
done < textfile.txt

sleep 1

$0 - name of script
$1 - first argument
for i in "$@" do smth done - all arguments no matter the amount
$# - number of arguments

Options
getops

while getopts :u:p:ab option; - the script expects -u and -p, ab optional, the : gives other options
do
case $option in
u) user=$optarg;;
p) pass=$optarg;;
a) smth;;
b) smht;;
esac
done

-s
-p

select

