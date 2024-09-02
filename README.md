# Shreenidhi
# Selection Sort Correctness

Algorithm
<br>
for i in 0 to arr.length - 1
    
    min = i
    for j in i+1 to arr.length - 1
        if arr[j] < arr[min]
           min = j
       endif
    endfor

   swap arr[i] with arr[min]
endfor

# Correctness of Selection Sort <br>
Description of Selection Sort<br>

Outer Loop <br>
Before each iteration of the outer loop, the first i-1 elements are sorted in ascending order
The elements in the subarray A[i..n] are greater or equal to the elements in A[1..i-1]
The elements of the array remain unchanged<br>
Inner Loop <br>
Before each iteration of the inner loop, min references the smallest element of the subarray A[i..j-1]
The loop finds the smallest element in the subarray A[i..j-1] and updates min accordingly<br>
Initialization of Inner Loop 
Before the start of the inner loop, min is assigned to be i and j starts at i+1
If A[k] < A[min], min is updated to be k, ensuring that min references the smallest element in the subarray A[i..k]
Upon termination, min references the smallest element of the subarray A[i..j-1] = A[i..n]
The swap done and the smallest element of A[i..n] at index i

<br>
Before the start of the outer loop, 
The first i-1 = 0 elements of the array are sorted in ascending order
The elements in the subarray A[i..n] = A[1..n] are greater or equal to the elements in A[1..i-1] = A[1..0] = ∅
The elements of the array remain unchanged

<br>
The swap ensures that A[i+1..n] are greater or equal to the elements in A[1..i]
<br>
Upon termination, the first n-1 elements of the array are sorted in ascending order
The elements in the subarray A[n..n] are greater or equal to the elements in A[1..n-1]
The elements of the array remain unchanged
