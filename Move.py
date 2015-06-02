#!/usr/bin/python

import sys
import shutil
import os

def main(playlist, mus_fol, devicename, and_fol_name):
    
    playlist = "~/.mpd/playlists/" + playlist + ".m3u"
    
    if mus_fol.endswith("/"):
        mus_fol[:-1]

    mus_fol = os.path.expanduser(mus_fol)
    and_fol = os.path.expanduser(devicename + '/' + and_fol_name)
    playlist = os.path.expanduser(playlist)
    songs = []
    song_fs = []

    with open(playlist) as fin:
        songs = fin.readlines()

    if not os.path.exists(and_fol):
        os.mkdir(and_fol)
    os.chdir(and_fol)

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
        
        and_loc_artist = and_fol + '/' + artist
        and_loc_album = and_loc_artist + '/' + album
        and_loc_song = and_loc_album + '/' + song_fs
 

        if not os.path.isdir(and_loc_artist):
            os.mkdir(and_loc_artist)

        if not os.path.isdir(and_loc_album):
            os.mkdir(and_loc_album)

        if not os.path.exists(and_loc_song):
            songloc = mus_fol + "/" + artist + "/" + album + "/" + song_fs 
            shutil.copy2(songloc[:-1], and_loc_song)    
            print(song_fs + " By " + artist + " has been copied")


def device_manager():
    if not os.path.exists("~/.config/mpdsync"):
        os.mkdir("~/.mpdsync")

    if not os.path.exists("~/.mpdsync" + devicename):
        devicename = input("New Device? Please name this device. If not new device type no to see previously configured devices.")

        if devicename == no:
            os.chdir("~/.mpdsync")
            devicename = input("Enter a device name ")
            and_fol = "~/.mpdsync/" + devicename
        else:
            linktodevice = input("Where is this device? (Entire mount path ")
            os.symlink(linktodevice, "~/.mpdsync/" + devicename)
            and_fol = "~/.mpdsync/" + devicename 
    
    else:
        and_fol = "~/.mpdsync/" + devicename 

def del_not_in_playlist(): 
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
    print("Saving to folder " + sys.argv[4] + " on android device.")
    main(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4])
