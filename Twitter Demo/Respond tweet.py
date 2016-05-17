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

stream.statuses.filter(track="Ian G. Harris")
	
