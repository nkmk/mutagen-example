from mutagen.id3 import ID3, TIT2

path = 'example.mp3'
tags = ID3(path)
print(tags.pprint())

tags.add(TIT2(encoding=3, text="new_title"))
tags.save()
