import requests
import os 
from PIL import Image

base_url = "https://api.mangadex.org"

def get_manga_id(title):
    response = requests.get(f"{base_url}/manga?title={title}")
    data = response.json()
    manga = data["data"][0]
    manga_id = manga["id"]
    return manga_id

def get_chapter_id(manga_id, chapter_number):
    response = requests.get(
        f"{base_url}/manga/{manga_id}/feed",
        params={
            "translatedLanguage[]": "en",
            "order[chapter]": "asc",
            "limit": 500
        }
    )
    data = response.json()
    for chapter in data["data"]:
        if chapter["attributes"]["chapter"] == str(chapter_number):
            return chapter["id"]
    return None

def download_chapter(chapter_id, folder_name):
    response = requests.get(f"{base_url}/at-home/server/{chapter_id}")
    data = response.json()
    server_url = data["baseUrl"]
    chapter_hash = data["chapter"]["hash"]
    images = data["chapter"]["data"]
    os.makedirs(folder_name, exist_ok=True)
    for i, image in enumerate(images):
        image_url = f"{server_url}/data/{chapter_hash}/{image}"
        img_response = requests.get(image_url)
        with open(f"{folder_name}/page_{i+1}.jpg", "wb") as f:
            f.write(img_response.content)
        print(f"Downloaded page {i+1}")

def create_pdf(folder_name, output_filename):
    images = []
    files = sorted(os.listdir(folder_name))
    for file in files:
        if file.endswith(".jpg"):
            img = Image.open(f"{folder_name}/{file}")
            rgb_img = img.convert("RGB")
            images.append(rgb_img)
    if not images:
        print(f"No images found in {folder_name}, skipping PDF")
        return
    first_image = images[0]        
    rest_images = images[1:]
    first_image.save(output_filename, save_all=True, append_images=rest_images)
    print(f"PDF saved as {output_filename}")

manga_id = get_manga_id("berserk")

start_chapter = input("From which chapter? ")
end_chapter = input("To which chapter? ")

for chapter_number in range(int(start_chapter), int(end_chapter) + 1):
    print(f"\nDownloading chapter {chapter_number}...")
    chapter_id = get_chapter_id(manga_id, chapter_number)
    if chapter_id:
        folder = f"berserk_chapter_{chapter_number}"
        download_chapter(chapter_id, folder)
        create_pdf(folder, f"berserk_chapter_{chapter_number}.pdf")
    else:    
        print(f"Chapter {chapter_number} not found, skipping...")