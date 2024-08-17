from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=Eppn8jQhTVI")
yt = yt.streams.get_highest_resolution()
yt.download('C:\\Users\jayes\\Downloads')
