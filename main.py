from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Playlist
import os
perm_mas = ("144","360","720")

#запрашиваем разрешение от юзера
def perm():
        while True:
            raz =  input("разрешение:").strip()
            # метод strip() удалает все пробелы
            if raz not in perm_mas:
                print("разрешение не верно")
                continue
            if raz in perm_mas:
                break
            # pytubefix принимает не числа , а строку с р
        return(raz+"p")    

def dow_Yo():
    while True:

        url = input("url pleas:").strip()

        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            print("downlad -",yt.title,"ВЕРНО?","y/n")
            #title - заголовок
            if(input().lower() != "y"):
                continue

            stream = yt.streams.filter(progressive=True, res=perm()).first()

            if not stream :
                itog = input("разрешение не найденно \n y-скачать максимальное\n n - попробывать другим разришением\n\n y/n").lower()
                if itog != "y":
                    while True:
                        stream = yt.streams.filter(progressive=True, res=perm()).first()
                        if stream:
                            break
                        if input("может хватит ? y/n") == "y":
                            stream = yt.streams.get_highest_resolution()
                            break
                else:
                    stream = yt.streams.get_highest_resolution()  
            stream.download(output_path="./downloads")  

        except Exception as error:
            print(error)

if("downloads" not in os.listdir()):
    #listdir - рабочая дириктория
    os.makedirs("./downloads")
dow_Yo()
