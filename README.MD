# Torrent Automation
**Author:** Arion Miles

## How it works:
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

\- [FileBot.net](http://www.filebot.net/)

This is my current script ([qBittorrent](https://www.filebot.net/forums/viewtopic.php?t=215#p9774)).
```text
filebot -script fn:amc --output "/path/to/media" --action move --conflict auto -non-strict --log-file amc.log --def unsorted=y subtitles=en clean=y "ut_dir=%F" "ut_kind=multi" "ut_title=%N" "ut_label=%L" "seriesFormat=path/to/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" exec="@path/to/args.txt"
```

An extensive log of filebot scripts I went through is present in [Filebot_Logs](../master/Filebot_Logs.MD) file

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
There are two main ways to receive push notifications on your mobile devices: Pushbullet & Telegram (I'm working on e-mail notifications).
First, create a text file in the torrent download directory (ease of access/debugging).

e.g: My download dir is `E:\New` and the file is named `args.txt` and its path is `E:\New\args.txt`.
This is what the `--def exec="@path/to/args.txt"` in the above script is for.

The format of the push notification is as follows:

**Movies:**
```
Title: Doctor Strange (2016)
Message: The Movie is ready.
```
**TV Shows:**
```
Title: Game of Thrones
Message: S06E09 - The Battle of Bastards is ready.
```
#### Pushbullet:
----
For pushbullet, you need the API key, and [a python script](https://raw.githubusercontent.com/dendory/scripts/091692bb07c685f5222e8d1f9e783db5b82c4f9f/pushbullet.py) made by Dendory. You can get the [Pushbullet API Key here](https://www.pushbullet.com/#settings/account).

Now, in `args.txt` paste the below line:
```
pushbullet.py -key YOUR_API_KEY -title "{movie}{episode; n}" -message "{movie; 'The movie'}{episode; s00e00}{episode; ' - '}{episode; t} {movie; 'is ready.'}{episode; "is ready."}"
```

Add this script to your environment variable OR a folder which is in your environment variable (Except C:\Windows\System32, never do that.)

#### Telegram:
----
For Telegram, you can use a script I made, [available here](https://github.com/ArionMiles/Filebot-To-Telegram/). Look at the instructions on the git repo. Be sure to edit the `creds.ini` with your Bot's `token` and `CHAT_ID`.

In `args.txt` paste the below line:
```
telegram.py -t "*{movie}{episode; n}*" -m "{movie; 'The movie'}_{episode; s00e00}{episode; ' - '}{episode; t}_ {movie; 'is ready.'}{episode; "is ready."}"
```

## Tips & Common Issues
1. If you're on Windows and cannot run the telegram/pushbullet script from the command line after adding it to env. variables, do the following:

    Regedit > HKEY\_CLASSES\_ROOT\Applications\python27.exe\shell\open\command
   
    And change the value from : `"C:\Python27\python27.exe" "%1"`
   
    To: `"C:\Python27\python27.exe" "%1" *%`

    **adjust the path to your specific Python version.**

    Read more about this [here.](http://eli.thegreenplace.net/2010/12/14/problem-passing-arguments-to-python-scripts-on-windows/)	

2. Things will hardly go right in the first run, it took me 20 days to get the basic setup working as intended. So it's handy to have the Filebot's AMC log file close to your working directory. As for me, I keep it in my downloads folder (which I've named NEW). The file logs every step Filebot takes while processing new downloads and throws errors which are useful for troubleshooting, it still helps me when things don't go as planned.

    The Filebot AMC log can be found at `C:\Users\%USERPROFILE%\AppData\Roaming\FileBot\logs\amc.log` on Windows.
    Create a shortcut to this file in your downloads directory.

## Further Reading

Read [this](https://www.filebot.net/forums/viewtopic.php?t=215) comprehensive guide on Filebot arguments/parameters by Rednoah (Filebot dev) to further improve and customize your script according to your needs.

## CONTRIBUTING

This setup is largely platform agnostic, but there might be a few times where certain things don't work for other systems. In that case, fork the repo, add instructions for specific OS, and send a PR.

For issues, enhancements, feature requests, use the issue tracker.