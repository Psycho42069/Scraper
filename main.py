import requests as req

if __name__ == "__main__":
    reponse = req.get("https://rawkuma.net/noa-senpai-wa-tomodachi-chapter-56/")
    with open("rawkuma.html", "w", encoding="utf-8") as file:
        file.write(reponse.text)
    print("File saved as rawkuma.html")  