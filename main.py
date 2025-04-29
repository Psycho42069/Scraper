import requests as req

if __name__ == "__main__":
    reponse = req.get("https://rawkuma.net/noa-senpai-wa-tomodachi-chapter-56/")
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
    # Cleaning the string
    parts = [a[1:] for a in parts]
    parts = [a[:-2] for a in parts]

    for i,a in enumerate(parts):
        print(f"\n\nfile {i}")
        print(a + "\n\n")