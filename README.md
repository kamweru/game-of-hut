# game-of-hut

A simple analog game that involves finding unique paths to draw a hut with two conditions:
1. One cannot go through a path twice
2. The path has to be continous, that is, the end of one point is the beginning of the next
> Seeing that everytime I played I could come up with different paths/ways, I set out to create a program that would find all possible unique paths/ways.

## The hut
![Hut Image](https://github.com/notrexbias/game-of-hut/blob/master/hut.jpg)

## *(While ignoring point F)* An example of a complete path would be:
**_A B_ -> _B C_ -> _C D_ -> _D E_ -> _E A_ -> _A D_ -> _D B_ -> _B E_**

This path is pretty obvious and one can come up with a number of them by hand, but there are others that are not so obvious.

### I created a program in python that finds all possible unique paths/ways
> Using the two rules as listed above, the program came up with **88 unique paths/ways**

### When I added the point F, shown above in red...
> Using the same two rule listed above, the program came up with **240 unique paths/ways**

It is a fun game especially when played *without the help of a computer*, in contrast, with a computer, my mind was blown when I knew that there are so many other possibilities, different from the ones I could come up with on my own.
