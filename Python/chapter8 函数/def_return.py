
# 练习：城市名
def city_country(city, country):
    info = '"'+country+','+city+'"'
    return info.title()


print(city_country('santiago', 'chile'))


# 练习：专辑
def make_album(album_artist, album_name, album_songs=''):
    album_info = {}
    album_info['artist'] = album_artist
    album_info['name'] = album_name

    if album_songs:
        # album_info = {
        #     'artist': album_artist,
        #     'name': album_name,
        #     'songs': album_songs
        # }
        album_info['songs'] = album_songs
    # else:
        # album_info = {
        #     'artist': album_artist,
        #     'name': album_name
        # }
    return album_info


print(make_album('Adele', '19'))
print(make_album('Taylor Swift', '1989', 15))


# 练习：用户的专辑
# #允许用户一直添加，超过5张，提示不能添加了
while True:
    times = 0
    albums = {}
    while times <= 5:
        times += 1
        artist = input('Please input artist:')
        if artist == 'quit':
            break
        name = input('Please input album name:')
        if name == 'quit':
            break
        songs = input('Please input songs number:')
        if songs == 'quit':
            break
        albums['album_'+str(times)] = make_album(artist, name, songs)
        print(albums)
    if times > 5:
        print('Only allow 5 albums,exited')
    else:
        print('You have exited')
    break
