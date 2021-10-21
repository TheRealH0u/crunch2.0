- [Crunch2.0](#crunch20)
	- [Math](#math)
		- [Equation](#equation)
	- [Conclusion](#conclusion)
	- [Usage with crunch using bash script](#usage-with-crunch-using-bash-script)
		- [Bash script](#bash-script)
		- [Usage with crunch](#usage-with-crunch)

# Crunch2.0
I love the crunch program in Kali Linux but it's really limited. 
Did you ever try to make a password that has capital and lover letters but it's a fixed word: `password, Password, pAssword` and so on.

Introducing the crunch2.0 that solves this problem. One little python script that does it all.
***
## Math

### Equation
So the equation is quite easy: $(numberOfStates)^{(numberOfLetters)}$  
So if we have two letters (**a** and **b**) and two states (**uppercase** and **lowercase**). 
***
## Conclusion
With two states, we can make uppercase letters be a binary state 1 and lowercase letters a binary state 0.  
We can see that if we start from `00` which is `aa` we can see that It's binary addition. So the final result with two letters should look like this:
```js
00 => ab
01 => aB
10 => Ab
11 => AB
```
***
## Usage with crunch using bash script

### Bash script

Primary script looks like this. Nothing special. For more letters we just insert them in the specified position and add `{letter,letter}`
```bash
for w in {a,A}{b,B};
do 
echo $w;
done
```

### Usage with crunch
To use the bash script with crunch we just replace the `echo $w` with a crunch payload.
```bash
for w in {a,A}{b,B};
do 
crunch 3 3 -t $w% >> outputToFile.lst
done
```