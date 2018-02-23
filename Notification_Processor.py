#! python3
# -*- coding: utf-8 -*-
import logging
from telegraph_post import telegraph_submit
from telegram import telegram

logger = logging.getLogger()
handler = logging.FileHandler('E:/New/config/notifications.log') #Use absolute paths
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

__author__ = 'Kanishk Singh (Arion Miles)'
__license__ = "MIT"

def line_no(fname):
    '''Count number of lines in a text file.'''
    i =- 1
    with open(fname, encoding='utf-8-sig') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def FileBot():
    with open("E:/New/config/SeriesName.txt", 'r', encoding='utf-8-sig') as sr: #Use absolute paths
        seriesTitle = sr.read().strip('\n')
        logger.debug('Reading %s' % sr)
    with open("E:/New/config/EpisodeDet.txt", 'r', encoding='utf-8-sig') as file: #Use absolute paths
        episodeNames = file.read()
        logger.debug('Reading %s' % file)

    #Send message depending upon number of files processed (checked with number of lines)
    logger.debug('Checking number of files processed...')
    if line_no("E:/New/config/EpisodeDet.txt") > 2: #Use absolute paths
        logger.debug('More than one file processed. Sending to Telegra.ph \n \n')
        telegraph_submit(seriesTitle, episodeNames)
    else:
        logger.debug('One file processed. Sending directly. \n \n')
        seriesTitle = '<b>' + seriesTitle + '</b>'
        telegram(seriesTitle, episodeNames)

    #Empty File contents
    logger.debug('Clearing contents of the text files.')
    with open("E:/New/config/SeriesName.txt", 'w', encoding='utf-8-sig') as sr: #Use absolute paths
        pass
    with open("E:/New/config/EpisodeDet.txt", 'w', encoding='utf-8-sig') as file: #Use absolute paths
        pass

if __name__ == '__main__':
    FileBot()
