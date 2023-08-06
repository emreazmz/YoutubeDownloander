
import pytube

url = input("enter url: ")
path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)