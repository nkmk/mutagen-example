from mutagen.easyid3 import EasyID3


def set_id3_tag(file_path, title=None, artist=None, albumartist=None, album=None, genre=None,
                track_num=None, total_track_num=None, disc_num=None, total_disc_num=None):
    tags = EasyID3(file_path)

    if title:
        tags['title'] = title
    if artist:
        tags['artist'] = artist
    if albumartist:
        tags['albumartist'] = albumartist
    if album:
        tags['album'] = album
    if genre:
        tags['genre'] = genre
    if total_track_num:
        if track_num:
            tags['tracknumber'] = '{}/{}'.format(track_num, total_track_num)
        else:
            tags['tracknumber'] = '/{}'.format(total_track_num)
    else:
        if track_num:
            tags['tracknumber'] = '{}'.format(track_num)
    if total_disc_num:
        if disc_num:
            tags['discnumber'] = '{}/{}'.format(disc_num, total_disc_num)
        else:
            tags['discnumber'] = '/{}'.format(total_disc_num)
    else:
        if track_num:
            tags['discnumber'] = '{}'.format(disc_num)

    tags.save()


def show_id3_tags(file_path):
    tags = EasyID3(file_path)
    print(tags.pprint())


def delete_id3_tag(file_path, target_tag):
    tags = EasyID3(file_path)
    tags.pop(target_tag, None)
    tags.save()


def delete_all_id3_tag(file_path):
    tags = EasyID3(file_path)
    tags.delete()
    tags.save()


path = 'example.mp3'
tags = EasyID3(path)
tags['title'] = 'new_title'
tags.save()

set_id3_tag(path, albumartist='new_artist')
delete_id3_tag(path, 'discnumber')
show_id3_tags(path)

for key in EasyID3.valid_keys.keys():
    print(key)
# album
# bpm
# compilation
# composer
# copyright
# encodedby
# lyricist
# length
# media
# mood
# title
# version
# artist
# albumartist
# conductor
# arranger
# discnumber
# organization
# tracknumber
# author
# albumartistsort
# albumsort
# composersort
# artistsort
# titlesort
# isrc
# discsubtitle
# language
# genre
# date
# originaldate
# performer:*
# musicbrainz_trackid
# website
# replaygain_*_gain
# replaygain_*_peak
# musicbrainz_artistid
# musicbrainz_albumid
# musicbrainz_albumartistid
# musicbrainz_trmid
# musicip_puid
# musicip_fingerprint
# musicbrainz_albumstatus
# musicbrainz_albumtype
# releasecountry
# musicbrainz_discid
# asin
# performer
# barcode
# catalognumber
# musicbrainz_releasetrackid
# musicbrainz_releasegroupid
# musicbrainz_workid
# acoustid_fingerprint
# acoustid_id
