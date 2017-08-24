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
```
powershell -Command "&{&'filebot.launcher' -script fn:amc --output '"E:\\"' --action 'move' --conflict 'skip' -non-strict --log-file 'amc.log' --def unsorted=y subtitles=en clean=y '"ut_dir=%F"' '"ut_kind=multi"' '"ut_title=%N"' '"ut_label=%L"' '"seriesFormat=E:\TV Shows\{n}\{''Season ''+s}\{s00e00} - {t}"' '"exec=@\path\to\args.txt"'}"; "&{&'\path\to\Notification_Processor.py'}"
```

An extensive log of filebot scripts I went through is present in [Filebot_Logs](../master/Filebot_Logs.MD) file

**NOTE**: The TVDb API v1, which is used by Filebot for fetching Series info [will be disabled](https://forums.thetvdb.com/viewtopic.php?f=3&t=36557) on **1st October 2017** in favour of [TVDb API v2.](https://api.thetvdb.com/swagger)

As a result, all older versions of Filebot cannot be used for Series renaming after 1st Oct. 2017. Therefore, you must update Filebot to the latest version from Filebot.net 

The newer versions of Filebot are paid for Windows, were always paid for Mac OS, and are free as of now for Linux. The dev works very hard on the software and provides excellent support on [his Forum](https://www.filebot.net/forums/), which helped me make this guide in such detail for everyone. If you cannot afford it, the dev is considerate enough to upload the binaries to [SourceForge](https://sourceforge.net/projects/filebot/files/filebot/) where you can download the installer for free. But please consider donating to him for his hardwork and prompt support.

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
There are two main ways to receive push notifications on your mobile devices: Pushbullet & Telegram (Filebot supports e-mail notifications by default. Check out `--def mailto=email ` and `--def mail=host:port:from[:username:password]`).
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
pushbullet.py -key YOUR_API_KEY -title {quote("* $n *")} -message {quote("The $type _ ${any{episode; s00e00 + ' - ' + t}{movie}} _ is ready.")}
```

Add this script to your environment variable OR a folder which is in your environment variable (Except C:\Windows\System32, never do that.)

#### Telegram:
----
For Telegram, you can use a script I made, [available here](https://github.com/ArionMiles/Filebot-To-Telegram/). Look at the instructions on the git repo. Be sure to edit the `creds.ini` with your Bot's `token` and `CHAT_ID`.

In `args.txt` paste the below line:
```
echo {quote("$n")} | Out-File -Encoding UTF8 SeriesName.txt; echo {quote("<b>${any{episode; s00e00 + ' - ' + t}{movie}}</b>")} | Out-File -Encoding UTF8 EpisodeDet.txt -append
```
also create a `SeriesName.txt` & `EpisodeDet.txt` in the same directory.

## Tips & Common Issues
1. If you're on Windows and cannot run the telegram/pushbullet script from the command line after adding it to env. variables, do the following:

    Regedit > `HKEY_CLASSES_ROOT\Applications\python.exe\shell\open\command`
   
    And change the value from : `"C:\Python27\python.exe" "%1"`
   
    To: `"C:\Python27\python.exe" "%1" %*`

    Similarly, set `HKEY_CLASSES_ROOT\py_auto_file\shell\open\command` to the same value.

    **adjust the path to your specific Python version.**

    Read more about this [here.](http://eli.thegreenplace.net/2010/12/14/problem-passing-arguments-to-python-scripts-on-windows/)	

2. Things will hardly go right in the first run, it took me 20 days to get the basic setup working as intended. So it's handy to have the Filebot's AMC log file close to your working directory. As for me, I keep it in my downloads folder (which I've named NEW). The file logs every step Filebot takes while processing new downloads and throws errors which are useful for troubleshooting, it still helps me when things don't go as planned.

    The Filebot AMC log can be found at `C:\Users\%USERPROFILE%\AppData\Roaming\FileBot\logs\amc.log` on Windows.
    Create a shortcut to this file in your downloads directory.

3. Create a manual.bat/manual.sh file in your downloads dir with the Filebot script with a little modification. Sometimes Filebot may fail to process the file, citing the file is already in use by another process. In that case, this batch/bash file will help immensely.
    
    For example, for my current script, I'd paste the below **as a single line** into a text file and save it as `Manual.bat` or `Manual.sh` in the downloads directory.
    ```
    filebot -script fn:amc --output "output/dir" --action move --conflict skip -
    non-strict "path/to/downloads/directory" --log-file amc.log --def unsorted=y clean=y 
    subtitles=en "seriesFormat=/TV Shows/{n}/{'Season 
    '+s}/{s00e00} - {t }" --def "exec=@path/to/args.txt"
    ```
     Change the output/dir, path/to/args.txt, and "E:/New" with what you put in the filebot script above. For testing/trial purposes, just paste already processed file in your downloads directory, rename it in a format the torrent uploaders do, like `Netflix.Daredevil.S02E04.x264.720p.aac` and run the batch file from command line. You'll be able to see every error easily, also the logs for this will be stored in the same `amc.log` file.

4. If even on torrent completion, Filebot doesn't run the script, you must make sure all the three main components, i.e., qBittorrent, Java JRE, and Filebot installed are of similar system architecture (i.e., either all 32-bit or 64-bit depending on your system architecture).

5. Newer filebot versions use PowerShell to execute the `--def exec="@path/to/file"` hooks, meaning executing Python scripts with PowerShell leads to opening new Python window from PowerShell and then executing our script. This can be distracting for users if they download in the background and while processing the file, they see a shell pop-up on their screens. If you'd like to do this silently, then append `;.py` at the end of your `PATHTEXT` in your Environment Variables (for help, [see this answer on StackOverflow](https://superuser.com/a/437853)). Now PowerShell will execute Python files from within itself.

## Further Reading

Read [this](https://www.filebot.net/forums/viewtopic.php?t=215) comprehensive guide on Filebot arguments/parameters by Rednoah (Filebot dev) to further improve and customize your script according to your needs.

## CONTRIBUTING

This setup is largely platform agnostic, but there might be a few times where certain things don't work for other systems. In that case, fork the repo, add instructions for specific OS, and send a PR.

For issues, enhancements, feature requests, use the issue tracker.