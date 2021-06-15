# MarketoMonitor "Marketo leaked data marketplace" 
Find them on TOR: http://marketojbwagqnwx.onion/

They provide the dump data on TOR and on the Web. This script uses the NON TOR option. 


This python script checks all the marketto dumps and updates to a text tile listing all the available dumps. 

The purpose of this is to get alerts of companies that you may have as a vendor or 3rd party relationship with. With the increase of 3rd party vendors and Business Email compromises it is important to get this information as soon as possible. Many times, especially smaller companies don't know how to handle breaches or loss of data and probably wont think about notifying business partnerships during a dumpster file. However, there are some that won't notify and you may find out after the fact via news. This is not the best time. So use or modify this script and get alerted as soon as you can. 

I also implement a telegram bot push to get notified of any new dumps that they post. 

**Note: It is probably wise to run this on a seperate cloud server on a daily cron.** 

## Requirements

pip install beautifulsoup4

pip install requests

pip install lxml


Works on my machine Windows 10. I will work on getting it to run on Linux. 