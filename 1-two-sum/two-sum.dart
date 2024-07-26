class Solution {
  List<int> twoSum(List<int> nums, int target) {
    for (int i = 0; i < nums.length; i++) {
      for (int j = nums.length - 1; j > i; j--) {
        if (nums[i] + nums[j] == target) {
          return [i, j];
        }
      }
    }
    throw ArgumentError('No two sum solution');
  }
}