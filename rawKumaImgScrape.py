import os
import requests as req

def imgScrape(source_url: str) -> None:
    """
    Downloads manga chapter images from the given source URL.
    Args:
        source_url (str): The URL of the manga chapter page to scrape and download images from.
    Returns:
        None
    """

    # Manga Storage:
    manga_folder = "のあ先輩はともだち"
    url = source_url
    chapter_start_index = url.find("chapter")
    chaper_end_index = url.find("/", chapter_start_index + 7)
    chapter_number = url[chapter_start_index:chaper_end_index]
    chapter_folder = os.path.join(manga_folder, chapter_number)
    os.makedirs(chapter_folder, exist_ok=True)
    
    # Iterate over all files in the mangaPages folder and delete .jpg files
    for file_name in os.listdir(chapter_folder):
        if file_name.endswith(".jpg"):
            os.remove(os.path.join(chapter_folder, file_name))
            print(f"Deleted {file_name}")

    reponse = req.get(url)
    # with open("rawkuma.html", "w", encoding="utf-8") as file:
    #     file.write(reponse.text)
    
    # print("File saved as rawkuma.html")  
    parts = reponse.text.split("noscript")[1]
    # Cleaning the front end
    parts = parts[4:]
    # Cleaning the back end
    parts = parts[:-6]
    parts = parts.split("<img src=")
    parts = parts[1:]
    # cleaning the img urls
    parts = [a.split("'")[1] for a in parts]

    for i, a in enumerate(parts):
        image_data = req.get(a).content
        filepath = os.path.join(chapter_folder, f"{i}.jpg")
        with open(filepath, "wb") as file:
            file.write(image_data)
        print(f"Image {i} saved as {filepath}")