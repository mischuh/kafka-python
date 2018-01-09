import os
import tweepy
import threading, logging, time
from confluent_kafka import Producer
import string

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_SECRET')

mytopic='kafka-twitter-test'


class StdOutListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    producer = Producer({'bootstrap.servers': 'localhost:29092'})

    def on_status(self, status):

        print("{}, {}, {}, {}, {}".format(
                status.user.followers_count,
                status.user.friends_count,
                status.user.statuses_count,
                status.text,
                status.user.screen_name
            ))

        message =  status.text + ',' + status.user.screen_name
        msg = filter(lambda x: x in string.printable, message)
        try:
            StdOutListener.producer.produce(mytopic,str(message))
            StdOutListener.producer.poll(0.5)
        except (KeyboardInterrupt, Exception) as e:
            print(str(e))
            return True

        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening


if __name__ == '__main__':

    listener = StdOutListener()

    #sign oath cert
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #uncomment to use api in stream for data send/retrieve algorythms
    #api = tweepy.API(auth)

    stream = tweepy.Stream(auth, listener)
    # stream.sample()
    stream.filter(track=['machinelearning', 'kafka', 'python'])


    producer.flush(30)
