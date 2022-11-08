# SNUsort

SNUSort is a hybrid sorting algorithm, which combines Randomized Quicksort with Insertion sort. 
In SNUSort, Randomized Quicksort runs recursively until the subarray’s size is less than some value, k.

<img width="786" alt="Screenshot 2022-11-08 at 12 41 03" src="https://user-images.githubusercontent.com/63445400/200469945-0d417dce-b24a-4e77-8d6f-60a0a822afb4.png">



In SNUSort, the average-case runtime of Partial-Quicksort is O(nlog(nk )), and the average-case runtime of Insertion-sort is O(nk). 
Thus, in total, SNUSort runs in O ( n k + n l o g ( nk ) ) .
