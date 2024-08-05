class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = len(arr)
        distinct_strings = []

        # Iterate through each string in the array
        for i in range(n):
            current_string = arr[i]
            is_distinct = True

            # Check if the current string is distinct
            for j in range(n):
                if j == i:
                    continue  # Skip comparing with itself
                if arr[j] == current_string:
                    is_distinct = False
                    break

            # If the string is distinct, add it to the list
            if is_distinct:
                distinct_strings.append(current_string)

        # Check if there are enough distinct strings
        if len(distinct_strings) < k:
            return ""

        return distinct_strings[k - 1]