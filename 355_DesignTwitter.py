'''
355. Design Twitter
'''

class Tweet(object):
    def __init__(self, index, tweetId):
        self.index = index
        self.tweetId = tweetId

class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = 0
        self.followers = dict()
        self.posts = dict()

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.index += 1
        tweet = Tweet(self.index, tweetId)
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append(tweet)

        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        followers = self.followers[userId]
        
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.followers:
            self.followers[followeeId] = set()
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followers[followeeId].remove(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)    


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

obj = Twitter()
obj.postTweet(1,5)
print(obj.getNewsFeed(1))
obj.follow(1,2)
obj.postTweet(2,6)
print(obj.getNewsFeed(1))
obj.unfollow(1,2)
print(obj.getNewsFeed(1))