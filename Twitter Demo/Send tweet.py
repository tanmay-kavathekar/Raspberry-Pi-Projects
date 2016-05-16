from twython import Twython

exec(open('int_key.py').read())

tweet_obj= Twython(C_KEY,C_S_KEY,A_TOK,A_S_TOK)
tweet_status=input("Enter a tweet to update: ")
tweet_obj.update_status(status=tweet_status)
