# Shreenidhi Deepak Pai
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

   swap arr[i] with arr[min]<br>
endfor

# Correctness of Selection Sort <br>
To establish that the Selection Sort algorithm is correct, we can use mathematical induction and induction invariants. <br>

Selection Sort Algorithm<br>

Selection Sort sorts an array by separating the array into two sub-arrays; a sorted array and an unsorted array. The algorithm repeatedly finds the smallest element from the unsorted sub-array and swaps it into the first index of the unsorted array. The next iteration finds the minimum element from the unsorted sub-array this increases the number of swaps by 1.
 <br>
Here's a high-level description of the algorithm to help understand the process of the algorithm in general: <br>
1. Start with the first element at index 0 as the first sorted element of the array.
2. For each element in the unsorted portion of the array, find the minimum element.
3. Swap the minimum element into the first element of the unsorted portion of the array. Swap. 
4. The sorted portion now has one more element added, and the process can continue to repeat until the entire array has been sorted. <br>

To demonstrate the correctness of Selection Sort, we utilize a proof by loop invariant, which is a property that must be true both before and after each iteration of the loop.<br>

Loop Invariant<br>

Before each iteration of the main loop, we will have the following invariant.<br>

Invariant: At the beginning of iteration i, the subarray A[0..i-1] contains the i smallest elements and is sorted, and the subarray A[i..n-1] contains the unsorted elements.<br>

Initialization<br>

Base Case (Initialization step): Before the first iteration (i=0), the sorted part of the subarray is A[0..-1], which satisfies the invariant because it is trivially true (no elements in it). The unsorted part of the subarray is A[0..n-1].<br>

Maintenance<br>

Induction (Maintenance step): Assume the invariant holds at the beginning of iteration i. During iteration i, we do the following:
1. Find the minimum of the unsorted part (A[i..n-1]).
2. Swap it with A[i]. <br>

After the swap,
- A[i] is now the i+1th smallest element in the entire array.
- A[0..i] is now sorted and contains the smallest (and sorted) i+1 elements.
- A[i+1..n-1] is still unsorted. <br>

Thus, we have maintained the invariant dynamically.<br>

Termination<br>

Termination (Termination step): The loop finishes when i=n-1. At this point, the sorted part is A[0..n-1] (the entire array), which now means we have a sorted array. The invariant guarantees that all the elements in the sorted part are in order, meaning we are guaranteed to have a sorted array when the loop is finished.<br>

Conclusion<br>

Since the invariant is true in the initialization step, we maintained it, and this leads to the entire array being sorted when the loop terminates. Hence, Selection Sort is correct. 
