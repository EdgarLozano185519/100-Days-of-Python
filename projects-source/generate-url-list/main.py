import os

BASE_URL = "https://audio-game-recordings.s3.us-east-2.amazonaws.com/Brandon+Cole/Brandon+Cole"

file = open("main.html", "a")
#dir = os.getcwd().split("\\")[-1]

file.write(f"<h2>Misc</h2>\n")
file.write("<ul>\n")

with os.scandir('./') as iterator:
    for entry in iterator:
        if entry.name == "main.py" or entry.name == "main.html": continue
        if entry.is_file():
            url = f"{BASE_URL}/{entry.name}"
            url = url.replace(' ', '+')
            link_name = f"{entry.name[:len(entry.name)-4]}"
            file.write(f'<li><a href="{url}">{link_name}</a></li>\n')

file.write("</ul>\n")
file.close()