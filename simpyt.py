from pytube import YouTube
from pytube import Channel

def YoutubeVideo():

    try:
        url = input("URL: ")
        yt_vid = YouTube(url)

        print(f"Title        : {yt_vid.title}")
        print(f"Thumbnail URL: {yt_vid.thumbnail_url}")

    except:
        pass

def YoutubeChannel():

    ch = input("Channel: ")
    
    if ch.find("/@"):
        ch = ch.replace('/@', '/c/')
        
    yt_ch = Channel(ch)

    print(yt_ch.channel_name)

if __name__ == "__main__":

    # YoutubeVideo()
    YoutubeChannel()