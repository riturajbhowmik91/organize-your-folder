import os


def CreatIFNotExit(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":
    files = os.listdir()
    files.remove("clasterclene.py")

    
    CreatIFNotExit("Imeges")
    CreatIFNotExit("Docs")
    CreatIFNotExit("Movies")
    CreatIFNotExit("Media")
    CreatIFNotExit("Others")

    imgExts=[".png",".jpg",".jpeg"]
    imeges = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts=[".doc",".docx",".txt",".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    movieExts=[".mkv",".avi",".mp4"]
    movies = [file for file in files if os.path.splitext(file)[1].lower() in movieExts]

    mediaExts=[".mp3",".mp4"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]


    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()

        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in movieExts) and (os.path.isfile(file)) :
            others.append(file)
            
    

    move("Images", imeges)
    move ("Docs", docs)
    move ("Movies", movies)
    move ("Media", medias)
    move ("Others", others)
