from pytube import YouTube
yt = YouTube()
yt.from_url("http://youtube.com/watch?v=v869YR_nTuU")
video = yt.get('mp4','360p')
#video = yt.filter('mp4')[0]
video.download(yt.filename)
        
