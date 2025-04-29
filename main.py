from rawKumaImgScrape import imgScrape as rawKuma

if __name__ == "__main__":
    print()
    print("Welcome to the RawKuma Image Scraper!")
    print("This program will download all images from a given manga chapter URL.")
    print("Please enter the URL of the manga chapter you want to download images from:")
    source_url = input("URL: ")
    print("Downloading images...")
    rawKuma(source_url)

    