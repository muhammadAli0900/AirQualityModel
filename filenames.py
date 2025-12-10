import os

folder = "C:\\Users\\HT COMPUTERS\\Desktop\\DS_presentation"   # <-- fixed

pictures = os.listdir(folder)

for pic in pictures:
    print(pic)
