from queue import PriorityQueue


class Tweet:

    def __init__(self, time: int, id: int):
        self.time = time
        self.id = id


class User:

    def __init__(self):
        self.tweets = []
        self.following = set()

        
class Twitter:

    def __init__(self):
        self.users = dict()
        self.time = 0

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        if user_id not in self.users:
            self.users[user_id] = User()

        user = self.users[user_id]
        user.tweets.append(Tweet(self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id: int) -> list:
        if user_id not in self.users: return []

        min_heap = PriorityQueue()

        user = self.users[user_id]
        for followee in user.following:
            if followee not in self.users: continue

            for tweet in self.users[followee].tweets:
                min_heap.put((tweet.time, tweet.id))
                if min_heap.qsize() > 10:
                    min_heap.get()

        for tweet in user.tweets:
            min_heap.put((tweet.time, tweet.id))
            if min_heap.qsize() > 10:
                min_heap.get()

        feed = []
        while not min_heap.empty():
            feed.append(min_heap.get()[1])

        return feed[::-1]

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id not in self.users:
            self.users[follower_id] = User()

        self.users[follower_id].following.add(followee_id)
        
    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.users:
            self.users[follower_id].following.discard(followee_id)
