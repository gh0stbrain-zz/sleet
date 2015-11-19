# slack + tweet = sleet!
#### A Very rudamentary Twitter plugin for Slack's python-rtmbot.
##### Requirements:

- [python-rtmbot] (https://github.com/slackhq/python-rtmbot)
- [tweepy] (https://github.com/tweepy/tweepy)
- Twitter API Keys (for sleet.py)
- A Slackbot w/ Keys (for python-rtmbot, see their docs for setup)
- Relevant Slack channel ID and Slackbot User ID (for sleet.py)

###### This project also makes use of simplejson.

##### Why?
Slack has the ability to send tweets out, but not to receive them for some reason. This will allow you to track users and keywords and view the resulting tweets directly in Slack chat. I also needed a project to learn how to program with.


# Usage
#### Setup
- Install python-rtmbot.
- Install tweepy.
- Clone sleet into rtmbots "plugins" folder.
- Edit **sleet.py** with the relevant information.
- Run **rtmbot.py** and sleet will automatically load.

#### Commands
- @botname: !follow [@twitteruser] - *follow twitter account.*
- @botname: !remove [@twitteruser] -  *stop following twitter account*
- @botname: !add [keyword] - *add keyword to watchlist*
- @botname: !delete [keyword] - *remove keyword from watchlist*

#### Warnings
- Keywords are *extremely* sensitive. These should be a last resort.
- Slack displays images and links that come through via Twitter, making certain material potentially NSFW.

#### To-Do
- Add situational error handling
- Stop using global variables
- Better message features (user icons, clickable user names, etc)
- Better persistence and data options.
