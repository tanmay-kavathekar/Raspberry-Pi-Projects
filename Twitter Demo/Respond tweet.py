from twython import Twython
class MyStreamer(TwythonStreamer):
	def on_success(self,data):
		if 'text' in data:
			print("Found "+"text")

stream=MyStreamer(C_KEY,C_SECRET,A_TOKEN,A_SECRET)

stream.statuses.filter(track="xyz")