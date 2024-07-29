class Solution {
  bool containsDuplicate(List<int> nums) {
    Map<int, int> elements = {};
    for(var num in nums){
        if (elements.containsKey(num)){
            return true;
        }
        else{
            elements.putIfAbsent(num, () => 1);
        }
    }

    return false;
  }
}