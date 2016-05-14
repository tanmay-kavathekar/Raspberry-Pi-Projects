from twython import Twython
excefile('init_keys.py')

tweet_obj= Twython.(APP_KEY, APP_SECRET_KEY)
tweet_status=raw_input("Enter a tweet to update: ")
tweet_obj.update_status(status=tweet_status)