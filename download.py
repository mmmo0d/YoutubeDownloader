import pafy
url = input("url: ")
vid = pafy.new(url)
streams = vid.streams
stream_num = 1

print("video title: ", vid.title)
f = input("is it your video? (y/n) ").lower()
while f == "n":
    url = input("url: ")
    print("video title: ", vid.title)
    f = input("is it your video? (y/n) ")
print(" _____  __    __      _____   _ __")
print("|  _  \\ \\ \\  / /     |  _  \\ | /_/")
print("| (_) |  \\ \\/ /   _  | (_) | | |   ____")
print("|  ___/   \\  /   (*) |  ___/ |_|  |____|")
print("| |       / /        | |")
print("|_|      /_/         |_|")
if f == "y":
    print("video streams: ")
    for i in streams:
        print(stream_num, ":", i)
        stream_num += 1
    k = input("choose stream number: ")
    best = vid.getbest()
    if k == "best":
        best.download()
    else:
        k = int(k)
        streams[k - 1].download()
