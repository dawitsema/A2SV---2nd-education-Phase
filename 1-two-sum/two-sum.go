func twoSum(nums []int, target int) []int {
	myMap := map[int]int{}

	for i := 0; i < len(nums); i++ {
		diff := target - nums[i]
		index, boolean := myMap[diff]
		if boolean {
			return []int{index, i}
		}
		myMap[nums[i]] = i
	}

	return []int{-1, -1}
}