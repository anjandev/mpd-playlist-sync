import sys
import shutil
import os

def main(playlist, mus_fol, and_fol, name):
    mus_fol = os.path.expanduser(mus_fol)
    and_fol = os.path.expanduser(and_fol)
    playlist = os.path.expanduser(playlist)
    songs = []
    song_fs = []

    with open(playlist) as fin:
        songs = fin.readlines()

    play_dir = and_fol + '/' + name
    if not os.path.exists(play_dir):
        os.mkdir(play_dir)
    os.chdir(play_dir)

    for song in songs:
        """
        song.replace(" ","\ ")
        song.replace("(","\(")
        song.replace(")","\)")
        song.replace("[","\]")
        song.replace("]","\]")
        """
        fold,song_f = song.split('/',1)
        song_fs.append(song_f)
        if not os.path.isdir(fold):
            os.mkdir(fold)

        if not os.path.exists(song)
            shutil.copyfile(mus_fol + '/' + song,'./' + song)    

        print(song_f + " has been copied")

    print("deleting stuff")
    for dirpath, dirnames, song_f in os.walk('./'): 
        if len(song_f) == 1:
            if not song_f in song_fs:
                # notifiaction message here
                os.remove(dirpath + '/' + song_f)

    


if __name__=="__main__":
    print("The playlist file is " + sys.argv[1])
    print("The music root folder is " + sys.argv[2])
    print("The android root folder is " + sys.argv[3])
    print("The playlist name is " + sys.argv[4])
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

