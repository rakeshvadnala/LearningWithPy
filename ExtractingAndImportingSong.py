
import eyed3,sys,os
import mysql.connector
import os,sys
from os import listdir
from os.path import isfile, join
folder=r'G:\Music'

mydb = mysql.connector.connect(host='localhost', database='marvel',
                              user='root',
                              password='root@123',
                              port='3307')
mycursor = mydb.cursor()

a=eyed3
#fp=r'G:\Music\[iSongs.info] 01 - Pagale Vennela.mp3'
fp=r'G:\Music'
dp=r'G:\Musicdata.csv'
for file in os.listdir(folder):
    if isfile(join(folder, file)):
        try:
            filepath=fp+'\\' + file
            af = eyed3.load(filepath)
            a2=af.tag

            genre=str(a2._getGenre())

            album=str(a2._getAlbum())

            artist=str(a2._getAlbumArtist())
            composer=str(a2._getComposer())
            bpm=str(a2._getBpm())
            all=genre+','+album+','+artist+','+composer+','+bpm
            with open(dp,'a+') as data:
                data.write('Title,Genre,Comments,Artist,Composer,Bpm\n')
                data.write(all)
            mycursor.execute('create table if not exists MusicList(album varchar(100),artist varchar(100),composer varchar(100),bpm varchar(100))')
            val=[album,artist,composer,bpm]
            sql='insert into MusicList(album,artist,composer,bpm) values(%s,%s,%s,%s);'
            mycursor.execute(sql, val)
        except Exception:
            print(Exception)


mycursor.execute("select * from MusicList")
rs=mycursor.fetchall()
for r in rs:
    print(r)
mydb.commit()

