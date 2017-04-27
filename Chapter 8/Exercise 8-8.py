def make_album(artist, album):
    new_dict = {artist: album}
    return new_dict

    while True:
        print("\nPlease tell me your favourite Artist and Album: ")
        print("(enter 'q' at any time to quit)")
        new_artist = input("Artist name: ")
        if new_artist == 'q':
            break
        new_album = input("Last name: ")
        if new_album == 'q':
            break

make_album('Me', 'You')