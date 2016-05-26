"""
The init_key.py file is used to assign values to the variables C_KEY,C_S_KEY,A_TOK and A_S_TOK which 
are used for authentication of the twitter application
"""
from twython import TwythonStreamer

exec(open('int_key.py').read())

count=0

class MyStreamer(TwythonStreamer):
	def on_success(self,data):
		global count
		if 'text' in data:
			count=count+1
			print(count)
			if count==3:
				print("Ian G. Harris is popular!")
				self.disconnect()

stream=MyStreamer(C_KEY,C_S_KEY,A_TOK,A_S_TOK)

stream.statuses.filter(track="Ian G. Harris") #the following function is used to check whether the track variable is found in the tweet  
	
