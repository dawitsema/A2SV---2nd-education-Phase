class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queque = deque()
        for i in range(len(deck)-1, -1, -1):
            if len(queque) > 1:
                queque.appendleft(queque.pop())
                queque.appendleft(deck[i])
            else:
                queque.appendleft(deck[i])
        
        return queque