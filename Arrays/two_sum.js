// Source: https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array

// *********************************************************************************************************************************
// 1. Two Sum

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
// *********************************************************************************************************************************

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Time Complexity: O(n)
// Space Complexity: O(n)

var twoSum = function (nums, target) {
    const numMap = new Map(); // Map to keep track of numbers visited and their indices.

    // Loop through the array
    for (let i = 0; i < nums.length; i++) {
        const desiredNum = target - nums[i]; // Calculate the complement.
        if (numMap.has(desiredNum)) {
            // If complement exists, return its index and the current index.
            return [numMap.get(desiredNum), i];
        }
        // Add the current number and its index to the Map.
        numMap.set(nums[i], i);
    }

    // If no valid pair is found, return an empty array.
    return [];
};