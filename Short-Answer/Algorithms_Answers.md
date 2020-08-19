#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

b) O(n log n)

c) O(n)

## Exercise II

To solve this problem I would use iterative binary search which has O(log n) time complexity.

So I would start on the middle floor and drop the egg

if it breaks, throw egg from mid floor in the top half

elif doesn't break, throw an egg from middle of lower half

using pointers I would keep track of the top and bottom of the narrowed down range until I determine the highest floor at which the egg does not break
