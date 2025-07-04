class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)

        balls = 0
        cost = 0
        for i in range(len(boxes)):
            answer[i] += cost
            if boxes[i] == '1':
                balls += 1
            cost += balls

        
        balls = 0
        cost = 0
        for i in range(len(boxes) -1, -1, -1):
            answer[i] += cost
            if boxes[i] == '1':
                balls += 1
            cost += balls


        return answer
