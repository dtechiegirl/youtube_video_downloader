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
        


        #     print("download in progress")
        # else: print("download completed")

    except:
        pass



# result = None
# while result ==None:
#     try:



# from pytube import YouTube


# video = YouTube(url)
# print(video)
# def useRegex(video):
#     pattern = re.compile(r"https://www\\.youtube\\.com/watch\\?v=m8sjsUrJYSM")
#     return pattern.match(video, re.IGNORECASE)


# if url == 

# def useRegex(url):
#     pattern = re.compile(r"https://www\\.youtube\\.com/watch\\?v=m8sjsUrJYSM")
#     return pattern.match(url, re.IGNORECASE)
# print(useRegex('https://www.youtube.com/watch?v=m8sjsUrJYSM'))
# print(video.title)
# print(video.thumbnail_url)