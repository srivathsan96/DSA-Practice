// Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array?envType=problem-list-v2&envId=array

// *********************************************************************************************************************************
// 26. Remove Duplicates from Sorted Array

// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

// Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

// * Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
// * Return k.

// Custom Judge:

// The judge will test your solution with the following code:

// int[] nums = [...]; // Input array
// int[] expectedNums = [...]; // The expected answer with correct length

// int k = removeDuplicates(nums); // Calls your implementation

// assert k == expectedNums.length;
// for (int i = 0; i < k; i++) {
//     assert nums[i] == expectedNums[i];
// }
// If all assertions pass, then your solution will be accepted.


// Example 1:

// Input: nums = [1,1,2]
// Output: 2, nums = [1,2,_]
// Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
// It does not matter what you leave beyond the returned k (hence they are underscores).
// Example 2:

// Input: nums = [0,0,1,1,1,2,2,3,3,4]
// Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
// Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
// It does not matter what you leave beyond the returned k (hence they are underscores).

// Constraints:

// 1 <= nums.length <= 3 * 104
// -100 <= nums[i] <= 100
// nums is sorted in non-decreasing order.
// *********************************************************************************************************************************

/**
 * @param {number[]} nums
 * @return {number}
 */

// Time Complexity: O(n)
// Space Complexity: O(1)

// Solution Using Two Pointers
var removeDuplicates = function(nums) {

    // Initialize a pointer 'p1' to track the position where the next unique element should be placed.

    // We are starting at index 1 since the first element is always unique.
    let p1 = 1;

    // Loop through the array starting from index 1 using the pointer 'p2'.
    for(let p2 = 1; p2 < nums.length; p2++) {
        // Check if the current element is different from the previous unique element.
        if(nums[p2] != nums[p1 - 1]) {
            // If it's unique, place it at position 'p1' in the array.
            nums[p1] = nums[p2];
            // Move the 'p1' pointer forward to the next position for the next unique element.
            p1++;
        }

        // We skip if "nums[p2]" is a duplicate.
    }

    // Return the length of the array without duplicates (up to index 'p1')
    return p1;
};