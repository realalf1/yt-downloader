from pytube import YouTube
from pytube import Channel

def Youtube():

    url     = input ("Input URL    : ")
    channel = input ("Input Channel: ")
    
    if url.startswith("/watch?v="):
        yt = YouTube(url)
    else:
        print("Youtube video must be followed by /watch?v= after link url")

    if channel.startswith("@"):
        channel = channel.replace("@", "c/")
        ch = Channel(channel)
    else:
        print("Youtube channel must be followed by /c/ before channel name")
        exit()
    
    return yt,ch

def YoutubeVideo():

    yt_vid = Setup()

    print(f"Title        : {yt_vid.title}")
    print(f"Thumbnail URL: {yt_vid.thumbnail_url}")

def YoutubeChannel():

    yt_ch = Setup()

    print(f"Channel name : {yt_ch.channel_name}")
    print(f"Videos       :                     ")

    for c in c.video_urls[:3]:
        print(c)

if __name__ == "__main__":

    YoutubeVideo()
    YoutubeChannel()