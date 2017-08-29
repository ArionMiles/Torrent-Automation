# -*- coding: utf-8 -*-
import logging
from telegraph_post import telegraph_submit
from telegram import telegram

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

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
        logger.debug('Reading %s' % sr)
    with open("EpisodeDet.txt", 'r') as file: #Use absolute paths
        episodeNames = file.read()
        logger.debug('Reading %s' % file)

    #Send message depending upon number of files processed (checked with number of lines)
    logger.debug('Checking number of files processed...')
    if line_no("EpisodeDet.txt") > 2: #Use absolute paths
        logger.debug('More than one file processed. Sending to Telegra.ph')
        telegraph_submit(seriesTitle, episodeNames)
    else:
        logger.debug('One file processed. Sending directly.')
        seriesTitle = '<b>' + seriesTitle + '</b>'
        telegram(seriesTitle, episodeNames)

    #Empty File contents
    logger.debug('Clearing contents of the text files.')
    with open("SeriesName.txt", 'w') as sr: #Use absolute paths
        pass
    with open("EpisodeDet.txt", 'w') as file: #Use absolute paths
        pass

if __name__ == '__main__':
    FileBot()
