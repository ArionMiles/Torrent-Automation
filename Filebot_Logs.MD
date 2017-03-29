## FILEBOT LOGS

* **APPLICATION:** Filebot CLI (not a separate program.)
	* NOTES: Add filebot to Environment Path to make execution convenient. Add "filebot.launcher.exe" in the environment path in the previous step if you want to prevent the console from popping up.
* **AUTHOR:** Arion Miles

### qBittorrent

**Date: 07 Jan, 2017:**
After KickAss Torrents went down on July 20 last year, I had to make do with ExtraTorrent's RSS Feeds. The feeds would work fine if they utilized HTTPS only functionality which ExtTorrents didn't, because my ISP blocked access to HTTP versions of most torrent sites, so the past six months have been a chore and mildly inconvenient for my setup. Also, qBit's ability to auto execute scripts upon torrent completion didn't work after v3.3.4 that is, until someone on Github recently taught me a solution to the problem. So here's a new script:

*NOTES:* Use RSS Feeds from zooqle.com now. They are HTTPS only and hence RSS Feed Downloader works seamlessly with it.
	The `args.txt` file contains the same arguments as with the previous versions, which is given in the below log (DATE:19 MAY).
**EDIT (11 MAR, 2017):** I now use a Telegram bot for push notifications, instead of Pushbullet.

SCRIPT:
```
filebot -script fn:amc --output "E:/" --action move --conflict auto -non-strict --log-file amc.log --def unsorted=y subtitles=en clean=y "ut_dir=%F" 
"ut_kind=multi" "ut_title=%N" "ut_label=%L" "seriesFormat=E:/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" exec="@E:\New\args.txt"
```

----

**Date: 12 Jul, 2016:**
After more than a month of using uTorrent, I hardly found myself using their "uTorrent Remote" feature as the Android version of the app hasn't even been updated since Dec,2013 and it's very slow and infested with bugs, not to mention the bad history uTorrent has with malwares. So here I am, back to qBittorrent v3.3.4. I've added some of the modifications from the utorrent script to my last qBittorrent script so that I can have the same functionality on a more reliable environment.

*NOTES:* The `args.txt` file contains the same arguments as with the previous versions, which is given in the below log (DATE:19 MAY).

SCRIPT:
```
"C:\Program Files\FileBot\filebot.launcher.exe" -script fn:amc --output "path/to/media" --action move --conflict auto -non-strict --log-file amc.log 
--def unsorted=y subtitles=y clean=y "ut_dir=%F" "ut_kind=multi" "ut_title=%N" "ut_label=%L" "seriesFormat=S:/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" 
exec="@E:/path/to/args.txt"
```

----
### μtorrent
**Date: 19 May, 2016:**
I wasn't satisfied with the previous Pushbullet because there were not dynamic. The Pushbullet message preset in the previous log's script is only good enough for TV Series. But when it comes to Movies, it's not the optimal choice. Also, writing long lines with multiple quotations in them can be pretty confusing and a mess to debug because of escape characters, so I put the pushbullet message line inside a text file and called it with: `--def "exec=@path/to/args.txt"` for ease of access and understanding.

**USAGE:** Look at the below log's 'USAGE' section.
*NOTES:* This is the pushbullet message line:
```
pushbullet -apikey "apikey" -title "{movie}{episode; n}" -message "{movie; 'The movie'}{episode; s00e00}{episode; ' - '}{episode; t} is ready."
```

SCRIPT:
```
filebot -script fn:amc --output "E:/" --action move --conflict auto -non-strict --log-file amc.log --def unsorted=y clean=y subtitles=en 
"ut_file=%F" "ut_dir=%D" "ut_kind=multi" "ut_title=%N" "ut_label=%L" --def "seriesFormat=/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" 
--def excludeList=amc.txt --def "exec=@path/to/args.txt"
```

----

**Date: 12 May, 2016:**
The native pushbullet feature can't be modified to change the display message so I asked on the Filebot forum for a way and the dev said I could either make a donation to him and get it done by him or run an external program which would handle Pushbullet messages from CLI so I opted for running an external program to handle the pushbullet alerts. I'm using an unofficial CLI tool built by [dendory.](https://github.com/dendory/pushbullet_cli) 
It basically allows me to modify the pushbullet message.

**USAGE:** Add the pushbullet.exe in `./Tools` or your System32 dir (for testing only. Add it to a folder which is in your env. path) and use the below script.

SCRIPT:
```
filebot -script fn:amc --output "E:/" --action move --conflict auto -non-strict "E:/New" --log-file amc.log 
--def unsorted=y clean=y subtitles=en --def "seriesFormat=/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" 
--def excludeList=amc.txt 
--def "exec=pushbullet -apikey \"apikey\" -title \"New episode of {n} is here! \" -message \"{s00e00} - {t} has been downloaded.\""
```

----

**Date: 07 May, 2016:**
μTorrent's Remote view feature caught my eye. I could the progress of my torrents remotely and also add/remove torrents while away from home. But, μTorrent's RSS Downloader had caused me issues in the past which is the reason I switched from μTorrent to qBittorent. But unfortunately, qBittorrent didn't have remote feature similar to μTorrent. Fortunately, with a little bit of help from reddit, I forced myself to try it one more time but it didn't work until several tries. Here's the script I'm using currently.

This script does all the things my previous qBittorrent script used to. Apart from that, now it also sends a Pushbullet notification each time a torrent is finished processing by Filebot and it's accompanied by a HTML file that gives a summary of changes made.

**USAGE:** Add this below script to μtorrent to execute it after a torrent is finished.
`μtorrent > Preferences > Advanced > Run Program > Run this program when a torrent finishes`

*NOTE:* * ALWAYS USE Forward-slash (/) WHEN DENOTING FOLDERS\FILES IN THE SCRIPT TO AVOID CONFLICTS.
* Change `apikey` & path/to/media with your own Pushbullet apikey and media path respectively.

SCRIPT:
```
filebot -script fn:amc --output "path/to/media" --action move --conflict skip -non-strict --log-file amc.log --def unsorted=y clean=y subtitles=en 
"ut_file=%F" "ut_dir=%D" "ut_kind=multi" "ut_title=%N" "ut_label=%L" --def "seriesFormat=/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" 
--def excludeList=amc.txt --def pushbullet=apikey
```

----

## qBittorrent
**Date: 29 Apr, 2016:**
The last script gave me another issue. It would run renaming for all the folders present in the directory and messing up with active/incomplete downloads. This should hopefully solve all problems for now. 

SCRIPT:
```
filebot -script fn:amc --output "/path/to/media/" --action move 
--conflict skip -non-strict --log-file amc.log 
--def unsorted=y clean=y subtitles=en "ut_dir=%F" "ut_kind=multi" 
"ut_title=%N" "ut_label=%L" --def "seriesFormat=/TV Shows/{n}/{'Season '+s}/{s00e00} - {t }" --def excludeList=amc.txt
```

----
**Date: 22 Apr, 2016:**
Hopefully, this should be the last modification I'll be making in a long time. I finally got the subtitles to download properly. Fixed the error with Seasons folder being named in the manner of "Season 02". Now it can handle multiple files pretty well, be it movies or tv show or both. Doesn't leave a Excludes.list after renaming and organizing. Also set it to *MOVE* the files rather than COPY them, and reduce disk space. Yes, that makes me a leecher. You can create symlinks/hardlinks to keep seeding them after moving them, I haven't tested them. This version also cleans the leftover folders with ease, making human intervention minimum.

SCRIPT:
```
filebot -script fn:amc --output "E:/" --action move -non-strict "E:/New"
--log-file amc.log --def "seriesFormat=/TV Shows/{n}/{'Season '+s}/{s00e00} - {t
}" --def subtitles=en clean=y --conflict skip
```

----
**DATE: 21 APR, 2016:**
The new script utilizes filebot's native AMC (Automated Media Center) groovy script to automate the process. Moreover, the process is more fluent with the script executing right after a new torrent is finished downloading. I've got to add the feature to fetch subtitles (it's really easy, --get-subtitles). The script renames and moves the renamed file to the movies folder.
NOTE: For the purpose of convenience, movies are now directly stored in the "Movies" folder and not in ".\Movies\Blu-Ray & DVDs\Hollywood".

USAGE: Add this below script to qBittorrent to execute it after a torrent is finished.
```qBittorrent > Tools > Downloads > Run external program on torrent completion.```
NOTE: ALWAYS USE Forward-slash (/) WHEN DENOTING FOLDERS\FILES IN THE SCRIPT TO AVOID CONFLICTS.

**!NOW OBSOLETE!**
SCRIPT:
```
filebot -script fn:amc --output "/downloadsFolder/" --action symlink --conflict skip -non-strict 
--log-file amc.log unsorted=n music=n artwork=n "ut_dir=%F" "ut_kind=multi" "ut_title=%N" 
"ut_label=%L" --def "seriesFormat={s00e00} - {t}"
```

----
**DATE: 19 APR, 2016:**
USAGE: Save this as a batch file in the folder where new media is downloaded. Add the batch to Task Scheduler's list to execute it at every startup.

**!NOW OBSOLETE!**
SCRIPT:
```
@ECHO OFF
cls
ECHO #############RENAME#############

ECHO Renaming in progress...
@ECHO OFF
filebot -rename <path\to\media>
```

----