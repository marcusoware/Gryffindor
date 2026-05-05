

import os
import shutil
import sys
import subprocess



def main():
    """
    scan files in Download and sort it out
    
    """


    out = program_main_logic()
    print(out)-1




def program_main_logic():
    
    

    header = f"*"*10 + " QuickFile Utility " + "*"*10

    message = input(
        f"\n{header}\n"
        "1: scan files \n"
        "2: Sort files in Download folder\n"
        "3: Youtube Downloader\n"
        "select option to continue or 'n' to exit program: \n"
    ).strip().lower()


    match message:
        case "n":
            sys.exit()
        case "1":
            return file_folder_scanner()
        case "2":
            return sorting_operations_Downloads()
        case "3":
            return downloader_files()
        case _:
            return "invalid user choice! "



def file_folder_scanner():

    messge = input (
        "\nselect the ROOT folder you want to scan it's content\n"
        "1: Documents\n"
        "2: Downloads \n"
        "3: Videos\n"
        "4: Pictures\n"
    )

    match messge:
        case "1":
            path = os.path.expanduser("~/Documents")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case "2":
            path = os.path.expanduser("~/Downloads")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case "3":
            path = os.path.expanduser("~/Videos")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case "4":
            path = os.path.expanduser("~/Pictures")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case _:
            return "invalid user choice"




def downloader_files():

    check = operating_system_checker()
    first_time_installer = input(
        "\nFirst time installer: \n"
        "[y]es or [n]o"
        "type 'y' or 'n' to continue\n"
    ).strip().lower()


    match check:
        case "Computer is a Debian OS(Ubuntu)":
            if first_time_installer in ["yes", "y"]:
                 working_with_debian_os()
                 youtube_downloader()
                 print()
            else:
                youtube_downloader()
            

           

        case "Computer is Windows":
            if first_time_installer in ["yes", "y"]:
                working_with_windows_os
                youtube_downloader
            else:
                youtube_downloader()
           
            






def youtube_downloader():
    import yt_dlp
    url = input(" enter URL here: \n")
    yt_options = {
        'format': 'best',
        'cookiefile': 'youtube_cookies.txt',
         'nocheckcertificate': True
    }
    try:
        with yt_dlp.YoutubeDL(yt_options) as stream:
            stream.download(url_list=[url])
            print("files downloaded successfully")
    except Exception as e:
        print(f"{e}...\n sorry DOWNLOAD FAILED ...")
     
        current_path = os.path.curdir
        root_folder = os.path.expanduser("~/Downloads")
        list_dir = os.listdir(current_path)
        for downloaded_file in list_dir:
            if downloaded_file.endswith((".mkv", ".mp4", ".avi", ".mov", ".wmv", ".flv", ".webm")):
                shutil.move(src=f"{current_path}/{downloaded_file}", dst=root_folder)
                print("downloaded file has been moved to Root Downloads Folder")
            
        print("no new video file downloaded")

    



    
def working_with_debian_os():

    print("Please wait while we update & upgrade US OS ....")
    command = ["sudo", "apt", "update"]
    command_2 = ["sudo","apt", "upgrade", "-y"]
    subprocess.run(command)
    subprocess.run(command_2)
   
   


    ffmpeg =shutil.which("ffmpeg")
    if ffmpeg == True:
        print("ffmpeg is Found on Pc Skipping to next Dependencies .\n")
    else:
        subprocess.run(["sudo", "apt", "install", "ffmpeg"])
        print("ffmpeg installed successfully")
    


    ytdlp = shutil.which("yt-dlp")
    if ytdlp == True:
        print("Proceeding to next ...\n")
    else:
        command_3 = ["sudo","add-apt-repository","https://github.com", "ppa:tomtomtom/yt-dlp"]
        subprocess.run(command_3)
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "yt-dlp"])

    


def working_with_windows_os():
    ffmpeg =shutil.which("ffmpeg")
    if ffmpeg == True:
        print("ffmpeg is Found on Pc Skipping to next Dependencies .\n")
    else:
        print("installing ffmpeg .... .")
        subprocess.run(["winget", "install", "ffmpeg"])
        print("ffmpeg installed successfully")
    
    ytdlp = shutil.which("yt-dlp")
    if ytdlp == True:
        print("Proceeding to next ...\n")
    else:
        subprocess.run(["winget", "install", "yt-dlp"])











def operating_system_checker():

    check = sys.platform
    if check == "linux":
        return "Computer is a Debian OS(Ubuntu)"
    
    elif check == "win32":
        return "Computer is Windows"

    elif check =="darwin":
        return "computer is a MacOS"
    
    return check







    
def file_sorter():

    root_downloads_folder = os.path.expanduser("~/Downloads")
    path = os.listdir(root_downloads_folder)

    
    try:
        if "MOVIE_FILES" not in path:
            movie = os.mkdir(f"{root_downloads_folder}/MOVIES_FILES")
        else:
            return "movie folder exist"
            
        if "MUSIC_FILES" not in path:
            music = os.mkdir(f"{root_downloads_folder}/MUSIC_FILES")
        else:
            return "music folder found"
        
        if "DOCUMENT_FILES" not in path:
            document = os.mkdir(f"{root_downloads_folder}/DOCUMENT_FILES")
        else:
            return "document folder found"
        
        if "SOFTWARE_FILES" not in path:
            software = os.mkdir(f"{root_downloads_folder}/SOFTWARE_FILES")
        else:   
            return "software  folder found "
        
        if "PICTURE_FILES" not in path:
            picture = os.mkdir(f"{root_downloads_folder}/PICTURE_FILES")
        else:
            return "picture folder found"
            
    except (FileExistsError):
        return "file exist"
    
    return movie ,music, document, software,picture, root_downloads_folder








def sorting_operations_Downloads():

    file_sorter()

    
    
    path = os.path.expanduser("~/Downloads")
    downloads  =os.listdir(path)
    # print(downloads)

    for file in downloads:
            if file.endswith((".mkv", ".mp4", ".avi", ".mov", ".wmv", ".flv", ".webm")):
                # print(file, "Moved Successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"{path}/MOVIES_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)
            elif file.endswith((".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a")):
                # print(file, "Moved Successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"{path}/MUSIC_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)

            elif  file.endswith((".zip", ".iso", ".msi", ".dmg", ".exe", ".rar", "7z")):
                # print(file, "Moved Successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"{path}/SOFTWARE_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)
            elif file.endswith((".pdf", ".txt", ".csv", ".docx", ".xlsx", ".pptx", ".odt")):
                # print(file, "move successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"{path}/DOCUMENT_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)
            elif file.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", "webp", ".tiff", ".svg")):
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"{path}/PICTURE_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)

    return "Files Movies Successfully"


    

     
    

if __name__== "__main__":
    main()