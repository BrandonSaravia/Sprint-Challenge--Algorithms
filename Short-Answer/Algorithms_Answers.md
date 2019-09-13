#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0                     // O(1) 
    while (a < n * n * n):    // O(1)         // it is O(1) because n is a single value
        a = a + n * n           // O(1)

b) sum = 0                                   // O(1)
    for i in range(n):                        // O(1)
        i += 1                                  // O(1)
        for j in range(i + 1, n):               // O(1)            
        j += 1                                // O(1)       // it is O(1) we are looping over a range of numeric values not lists
        for k in range(j + 1, n):             // O(1)
            k += 1                              // O(1)
            for l in range(k + 1, 10 + k):      // O(1)
            l += 1                            // O(1)
            sum += 1                          // O(1)

c) def bunnyEars(bunnies):
        if bunnies == 0:                    // O(1)
        return 0                          // O(1)           // O(1) because even though it is recursive it only uses numeric values

    return 2 + bunnyEars(bunnies-1)       // O(1)



## Exercise II

proposed algorithim) 
    1st solution) first I would write a func that accepts a numeric value. then I would say for i in range(0, _n_): if i == _f_ then i would have it return the value of _i_.

    2nd solution) if _n_ is a list of floors. I would get the median of the list, check to see if _f_ was greater than the median if it is then i would recursivly recall the func with the list starting from the median up. if _f_ was less than the median i would recursivly recall the func with the list starting from the median down. I would also set a catch if _n_ == _f_ return _n_.

runtime)
    1st solution) O(1)

    2nd solution) O(logn)
