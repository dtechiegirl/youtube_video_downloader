# from pickle import FALSE
from pytube import YouTube
# import re


input1 = int(input("how any videos do you want to download"))
input2 = input("input the url, to start downloading")
result = None
while result == None:
    try:
        url = input2
        for i in range(0, input1):
            video = YouTube(url)
        
        forDownload = video.streams.get_highest_resolution()
        print("download in progress...")

        
        forDownload.download()
        


        
     

    except:
        pass



