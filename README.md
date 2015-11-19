# slack + tweet = sleet!
#### A Very rudamentary Twitter plugin for Slack's python-rtmbot.
##### Requirements:

- [python-rtmbot] (https://github.com/slackhq/python-rtmbot)
- [tweepy] (https://github.com/tweepy/tweepy)

###### This project also makes use of simplejson.

##### Why?
Slack has the ability to send tweets out, but not to receive them for some reason. This will allow you to track users and keywords and view the resulting tweets directly in Slack chat.


# Usage
#### Setup
To use sleet, you will need Twitter API keys, a bot in Slack with relevant keys, and you will need to identify the channel(s) in which you'd like the bot to post tweets into.
#### Commands
- @botname !follow [@twitteruser] - *follow twitter account.*
- @botname !remove [@twitteruser] -  *stop following twitter account*
- @botname !add [keyword] - *add keyword to watchlist*
- @botname !delete [keyword] - *remove keyword from watchlist*

#### Warnings
- Keywords are *extremely* sensitive. These should be a last resort.
- Slack displays images and links that come through via Twitter, making certain material potentially NSFW.

#### To-Do
- Add situational error handling
- Stop using global variables
- Better message features (user icons, clickable user names, etc)
- Better persistence and data options.
