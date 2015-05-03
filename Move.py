#!/usr/bin/python

import sys
import shutil
import os

def main(playlist, mus_fol, and_fol):

    if mus_fol.endswith("/"):
        mus_fol[:-1]
    if and_fol.endswith("/"):
        and_fol[:-1]

    mus_fol = os.path.expanduser(mus_fol)
    and_fol = os.path.expanduser(and_fol)
    playlist = os.path.expanduser(playlist)
    name = str(playlist)
    songs = []
    song_fs = []

    with open(playlist) as fin:
        songs = fin.readlines()

    play_dir = and_fol + '/' + name
    
    if not os.path.exists(play_dir):
        os.mkdir(play_dir)
    os.chdir(play_dir)

    for song in songs:
        
        # Remove \n from songs list
        if song.endswith("\n"):
            song[:-2]


        """
        song.replace(" ","\ ")
        song.replace("(","\(")
        song.replace(")","\)")
        song.replace("[","\]")
        song.replace("]","\]")
        """
        
        artist,other = song.split('/',1)
        album,song_fs= other.split('/',1)
        
        
        and_loc_artist = and_fol + artist
        and_loc_album = and_loc_artist + '/' + album
        and_loc_song = and_loc_album + '/' + song_fs
 

        if not os.path.isdir(and_loc_artist):
            os.mkdir(and_loc_artist)

        if not os.path.isdir(and_loc_album):
            os.mkdir(and_loc_album)

        if not os.path.exists(and_loc_song):
            print (mus_fol)
            songloc = mus_fol + "/" + artist + "/" + album + "/" + song_fs 
            shutil.copyfile(songloc[:-1], and_loc_song)    
            print(songloc + " has been copied")
    
    print("deleting stuff")

    music_formats = [".mp3",".flac"]

    for dirpath, dirnames, song_f in os.walk('./'): 
        if len(song_f) == 1:
            if not song_f in song_fs:
                for formats in music_formats:
                    if str(song_f).endswith(formats):
                        print(song_f)
                        os.remove(dirpath + '/' + song_f)


if __name__=="__main__":
    print("The playlist file is " + sys.argv[1])
    print("The music root folder is " + sys.argv[2])
    print("The android root folder is " + sys.argv[3])
    main(sys.argv[1],sys.argv[2],sys.argv[3])
