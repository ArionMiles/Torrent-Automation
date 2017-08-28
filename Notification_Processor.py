# -*- coding: utf-8 -*-
from telegraph_post import telegraph_submit
from telegram import telegram

__author__ = 'Kanishk Singh (Arion Miles)'
__license__ = "MIT"

def line_no(fname):
    '''Count number of lines in a text file.'''
    i =- 1
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def FileBot():
    with open("SeriesName.txt", 'r') as sr: #Use absolute paths
        seriesTitle = sr.read().strip('\n')
    with open("EpisodeDet.txt", 'r+') as file: #Use absolute paths
        episodeNames = file.read()

    #Send message depending upon number of files processed (checked with number of lines)
    if line_no("EpisodeDet.txt") > 2: #Use absolute paths
        telegraph_submit(seriesTitle, episodeNames)
    else:
        seriesTitle = '<b>' + seriesTitle + '</b>'
        telegram(seriesTitle, episodeNames)
    #Empty File contents
    with open("SeriesName.txt", 'w') as sr: #Use absolute paths
        pass
    with open("EpisodeDet.txt", 'w') as file: #Use absolute paths
        pass

if __name__ == '__main__':
    FileBot()
