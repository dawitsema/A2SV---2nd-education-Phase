class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        heap = []

        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                ind = len(self.tweetmap[followeeId]) - 1
                count, tweetId = self.tweetmap[followeeId][ind]
                heap.append([count, tweetId, followeeId, ind - 1])
        heapq.heapify(heap)
        
        while heap and len(ans) < 10:
            count, tweetId, followeeId, ind = heapq.heappop(heap)
            ans.append(tweetId)
            if ind >= 0:
                count, tweetId = self.tweetmap[followeeId][ind]
                heapq.heappush(heap, [count, tweetId, followeeId, ind - 1])
        
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)