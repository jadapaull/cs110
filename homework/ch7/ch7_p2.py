def main():
    userartist=input("Enter an artist's name: ")
    spotify = r'/Users/jadapaul/Desktop/cs110/homework/ch7/p2_spotify.txt'
    artists= artistsread(spotify)
    checkartist = artistcheck(userartist, artists)

    print(checkartist)

def artistsread(spotify):
    openspotify= open(spotify,"r")
    artist = openspotify.readlines()
    artists = []
    for name in artist:
        artists.append(name.rstrip())
    return artists

def artistcheck(userartist, artists):
    if userartist in artists:
        for i in range(len(artists)):
            if userartist == artists[i]:
                place = i + 1
        return (f"{userartist} has the #{place} most monthly listeners on Spotify")
    else:
        return(f" {userartist} is not in the top 50")

main()

    
    