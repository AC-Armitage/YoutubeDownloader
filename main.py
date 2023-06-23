from __future__ import unicode_literals
import yt_dlp

class YTdown:
	def __init__(self, link, dirict):
		self.link = link
		self.dir = dirict
		self.audiopts = {
				'outtmpl': self.dir + '/%(title)s.%(ext)s',
		        'playliststart': "0",
        		'playlistend': "5000",
        		'ignoreerrors': 3,
	       		'format': 'bestaudio/best',
	        	'postprocessors': [{
	            	'key': 'FFmpegExtractAudio',
	            	'preferredcodec': 'mp3',
	            	'preferredquality': '192',
				}],
			}

	def video(self):
		vidopt = {'outtmpl': self.dir + '/%(title)s.%(ext)s'}
		try:
			with yt_dlp.YoutubeDL(vidopt) as ydl:
				ydl.download([self.link])
		except Exception as e:
			print(f"Error: {e}")
	def audio(self):
		try:
			with yt_dlp.YoutubeDL(self.audiopts) as ydl:
				ydl.download([self.link])

		except Exception as e:
			print(f"Error: {e}")
if __name__ == "__main__":
	link = input("Insert the link: ")
	dirict = input("Insert the download folder directory: ")
	ytd = YTdown(link, dirict)
	choix = int(input("Chose the coresponding number for the following:\n(1) for downloading in video format\n(2) for downloading in mp3 format\n> "))
	if choix == 1:
		ytd.video()
	elif choix == 2:
		ytd.audio()
	else: 
		print("invalid")
