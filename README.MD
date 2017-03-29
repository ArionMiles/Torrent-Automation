# Torrent Automation

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

### How it works:
I use Filebot's [AMC script](https://www.filebot.net/forums/viewtopic.php?t=215) for qBittorrent which automatically executes once a torrent has finished downloading, then the filebot script sorts them out into Movies/TV series and on the basis of that renames them into `SxxExx - Title` format and puts them into their respective `SeriesTitle/Season xx` folders.

For movies, it simply renames them to `MovieName (YEAR)` format and puts them in a folder of the same name.

Then I receive a Pushbullet/Telegram notification telling me if a Movie or a Series (with episode number and title) is ready and my [Plex](https://plex.tv) library is automatically updated.


Consists of 4 parts:
* [Torrent Client](#torrent-client)
* [FileBot](#filebot)
* [RSS Feeds](#rss-feeds)
* [Notifications](#notifications)

## Torrent Client
You can use any torrent client, but bear in mind that different clients have minor changes in the Filebot script depending upon their supported parameters. I'm using [qBittorrent](https://github.com/qbittorrent/qBittorrent). [Look at this guide](https://www.filebot.net/forums/viewtopic.php?t=215) from Rednoah on Filebot forums to choose proper script for your client.

For qBittorrent, paste the script here:
<kbd>Tools</kbd> 🡪 <kbd>Options (Alt + O)</kbd> 🡪 <kbd>Downloads</kbd> 🡪 <kbd>Run external program on torrent completion</kbd>

## Filebot
>Filebot is the ultimate tool for organizing and renaming your movies, tv shows or anime, and music well as downloading subtitles and artwork. It's smart and just works.

/- [FileBot.net](http://www.filebot.net/)

This is my current script ([qBittorrent](https://www.filebot.net/forums/viewtopic.php?t=215#p9774)).
```text
filebot -script fn:amc --output "/path/to/media" --action move --conflict auto -non-strict --log-file amc.log --def unsorted=y subtitles=en clean=y "ut_dir=%F" "ut_kind=multi" "ut_title=%N" "ut_label=%L" "seriesFormat=path/to/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" exec="@E:\New\args.txt"
```

An extensive log of filebot scripts I went through is present in [Filebot_Logs.MD](../master/Filebot_Logs.md) file

## RSS Feeds
1. Get a RSS feed link from your favourite Torrent Aggregator (I use Zooqle) for the desired tv show from a particular uploader of your choice. 

Use the following search parameters:

Search > `{TVSeriesName} {quality} {suffixes} DesiredUser`

where {suffixes} = LOL/Xvid-FUM/DIMENSION/RARBG. Leave it blank if your search with `seriesName`, 
`quality` & `DesiredUser` return satifactory results.

2. Add this link to your RSS subscription's list.

3. Set a new rule in the RSS Downloader for your particular TV Series (or user, in the case of Movies) and set it to contain a specific keyword and set the Episode filter according to the season and no. of episodes it has. Apply this rule to your particular subscribed feed.

4. Test it multiple times to make sure you're doing it right.

## Notifications

## Further Reading

Read [this](https://www.filebot.net/forums/viewtopic.php?t=215) comprehensive guide on Filebot arguments/paraments by Rednoah (Filebot dev) to further improve and customize your script according to your needs.