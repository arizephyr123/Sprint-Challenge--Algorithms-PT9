# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n

# for n = 0 => 0 passes

# for n = 3 => 3 passes

# for n = 10 => 10 passes

# for n = 100 => passes

# so, O(n)

```

```
b)  sum = 0
    for i in range(n): # O(n)
      j = 1
      while j < n: # O(log n)
        j *= 2
        sum += 1


# while loop:

# for n = 0 => 0 passes

# for n = 3 => 2 passes

# for n = 5 => 3 passes

# for n = 10 => 4 passes

# for n = 100 => 7 passes

# each pass through the while loop reduces runtime complexity by double what was removed the previous time
# so, O(n) * O(log n) => O(n log n)
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:  # O(1)
        return 0

      return 2 + bunnyEars(bunnies-1)

# for n = 0 => 1 pass

# for n = 3 => 3 passes

# for n = 10 => 10 passes

# for n = 100 => 100 passes

# so, even though using recursion, still Runtime complexity = O(n)

```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
