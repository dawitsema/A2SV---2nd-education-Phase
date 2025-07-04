class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for i in range(len(boxes)):
            temp = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    temp += abs(i - j)
            
            answer.append(temp)
        

        return answer

        