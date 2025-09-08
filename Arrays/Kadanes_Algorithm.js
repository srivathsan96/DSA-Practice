// Source: https://www.algoexpert.io/questions/kadane's-algorithm

/*
Kadane's Algorithm

Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all of the integers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers (numbers next to each other in the input array).

Sample Input
array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

Sample Output
19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]
*/

// Time Complexity: O(n) - where n is the length of the input array
// Space Complexity: O(1)

function kadanesAlgorithm(array) {
  // Write your code here.
  let max_so_far = -Infinity;
  let curr_max = 0;

  for (let i = 0; i < array.length; i++) {
    curr_max += array[i];
    max_so_far = Math.max(curr_max, max_so_far);
    if (curr_max < 0) curr_max = 0;
  }

  return max_so_far;
}
