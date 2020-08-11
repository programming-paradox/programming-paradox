import os

files = os.listdir()

def CreateIfNOtExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


CreateIfNOtExists("Images Files")
CreateIfNOtExists("Text Files")
CreateIfNOtExists("Media Files")

ImgFormat = [".jpg", ".png", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in ImgFormat]

DocsFormat = [".log", ".txt", ".pdf", ".doc", ".docx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in DocsFormat]

MediaFormat = [".mp3", ".mp4", ".flv"]
media = [file for file in files if os.path.splitext(file)[1].lower() in MediaFormat]

Others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if ext not in images and ext not in DocsFormat and ext not in MediaFormat and os.path.isfile(file):
        Others.append(file)

move("Images Files", images)
move("Text Files", docs)
move("Media Files", media)
