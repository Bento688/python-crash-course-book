def make_album(album_name: str, artist: str, num_songs: int | None = None):
    dict = {}

    if num_songs is None:
        dict[album_name] = {
            "artist": artist,
        }
    else:
        dict[album_name] = {
            "artist": artist,
            "num_songs": num_songs,
        }

    return dict

# print(make_album("Pablo Honey", "Radiohead"), "\n")
# print(make_album("The Bends", "Radiohead", 12), "\n")

albums = {}
while True:

    album_name = input("Input album: ")
    if album_name == "q":
        break
    artist = input("Input artist: ")
    if artist == "q":
        break

    albums = {**albums, **make_album(album_name, artist)} 

    print(f"Here is your album collection: {albums}")


