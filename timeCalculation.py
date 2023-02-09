# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:19:02 2022
入力された時刻同士の時間差を測る
endtimeがfirsttimeより早い場合,日をまたいだとして処理する.
"""
def oclock2min(string):
    timelist=string.split(',')
    timelist=[int(i) for i in timelist]
    minutes=timelist[0]*60
    if len(timelist)>1:
        minutes+=timelist[1]
    return minutes

def min2oclock(minutes):
    hours=minutes/60
    minutes=minutes%60
    return f"{int(hours)}:{minutes:0<2d}"

print("ex：9:30→9,30")
while True:
    firsttime=oclock2min(input("firsttime?:"))
    endtime=oclock2min(input("endtime?:"))
    if firsttime>endtime:
        endtime+=12*60
    print(f">>{min2oclock(endtime-firsttime)} later")
    string=input("continue?(y/n):")
    if string=='n':
        break
