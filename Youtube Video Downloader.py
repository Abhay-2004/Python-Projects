from pytube import YouTube

link = input("Enter the link here: ")
yt_l = YouTube(link)

print("Title:",yt_l.title)

resolution = yt_l.streams.get_highest_resolution()

print("Your video is getting ready")
print("Downloading...")
resolution.download()
print("Download Finished")