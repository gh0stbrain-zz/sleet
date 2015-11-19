import simplejson as json
import tweepy
from tweepy import Stream

################################# HOW TO USE ###############################
# ALL COMMANDS MUST START WITH @BOTNAME
# !follow <@TWITTERACCOUNT> - Follows Twitter User
# !remove <@TWITTERACCOUNT> - Removes Twitter User
# !add <KEYWORD> - Adds Keyword To Keyword Filter
# !delete <KEYWORD> - Deletes Keyword From Keyword Filter
# EXAMPLE: @chatbot !follow @twitteruser
############################## END HOW TO USE ##############################
################################# WARNING ##################################
# The keyword filter can be quite sensitive, as picking very "generic" words
# can cause the bot to spazz out, and can cause you a lot of stress in your
# channel. IE: Placing the word "the" in the filter will certainly flood the
# channel uncontrollably, and would cause you and the bot to lag heavily.
#               Please exercise caution when using them.
# Also, tweets regardless of filter could display NSFW content, so be very
#   careful about who and what you follow, especially in the workplace!
################################# END WARNING ##############################


########################## START USER CONFIGURATION ########################
#Twitter API Keys
consumer_key = "EXAMPLE"
consumer_secret = "EXAMPLE"
access_key = "EXAMPLE"
access_secret = "EXAMPLE"
#Slack Configuration - You will need to get your Channel ID and Bot User ID.
sChannel = "EXAMPLE"
sbID = "@EXAMPLE"
########################## END USER CONFIGURATION ##########################

#Twitter API stuff.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#Necessary User List Variables.
TwitterUserList = []
filehandle = open('plugins/sleet/users.txt', 'r')
data_from_file = filehandle.read()
TwitterUserList = json.loads(data_from_file)
filehandle.close()

#Necessary Keyword Variables.
KeyWordList = []
xfilehandle = open('plugins/sleet/keywords.txt', 'r')
xdata_from_file = xfilehandle.read()
KeyWordList = json.loads(xdata_from_file)
xfilehandle.close()

#Don't touch this.
FirstRun = 1

#Stream Listener.
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        outputs.append([sChannel, "New tweet from @" + status.author.screen_name + ": " + status.text])


    def on_error(self, status_code):
        if status_code == 420:
            return False

#Stream Authentication and Tracking.
myStreamListener = MyStreamListener()
def set_stream():
    global FirstRun
    global myStream
    if len(TwitterUserList) > 0 and len(KeyWordList) > 0:
        follow_str = ','.join(str(element) for element in TwitterUserList)
        track_str = ','.join(str(element) for element in KeyWordList)
        myStream = tweepy.Stream(auth = auth, listener=myStreamListener)
        myStream.filter(follow=[follow_str], track=[track_str], async=True)
        FirstRun = 0
    elif len(TwitterUserList) == 0 and len(KeyWordList) > 0:
        track_str = ','.join(str(element) for element in KeyWordList)
        myStream = tweepy.Stream(auth = auth, listener=myStreamListener)
        myStream.filter(track=[track_str], async=True)
        FirstRun = 0
    elif len(TwitterUserList) > 0 and len(KeyWordList) == 0:
        follow_str = ','.join(str(element) for element in TwitterUserList)
        myStream = tweepy.Stream(auth = auth, listener=myStreamListener)
        myStream.filter(follow=[follow_str], async=True)
        FirstRun = 0

set_stream()

#Slack Bot stuff.
def process_message(data):
    global filehandle
    global xfilehandle
    global KeyWordList
    global TwitterUserList
    global FirstRun
    global myStream
    if data["text"].find(sbID) != -1 and data["text"].find("!follow") != -1:
        initial_pos = data["text"].find("follow")
        next_pos = data["text"].find(" ", initial_pos)
        next_pos2 = next_pos + 1
        new_pos = data["text"].find(" ", next_pos2)
        if new_pos == -1:
            new_pos = len(data["text"])
        NewFollow = data["text"][next_pos2:new_pos]
        convid = api.get_user(NewFollow)
        if convid.id not in TwitterUserList:
            TwitterUserList.append(convid.id)
            my_json_data = json.dumps(TwitterUserList)
            filehandle = open('plugins/sleet/users.txt', 'w')
            filehandle.write(my_json_data)
            filehandle.close()
            if FirstRun != 1:
                try:
                    myStream.disconnect()
                except:
                    print "ERROR WITH DISCONNECTION AT FOLLOW"
            outputs.append([sChannel, "TWITTER - Now Following: %s" % NewFollow ])
            set_stream()
    elif data["text"].find(sbID) != -1 and data["text"].find("!remove") != -1:
        initial_pos = data["text"].find("remove")
        next_pos = data["text"].find(" ", initial_pos)
        next_pos2 = next_pos + 1
        new_pos = data["text"].find(" ", next_pos2)
        if new_pos == -1:
            new_pos = len(data["text"])
        NewFollow = data["text"][next_pos2:new_pos]
        convid = api.get_user(NewFollow)
        if convid.id in TwitterUserList:
            TwitterUserList.remove(convid.id)
            my_json_data = json.dumps(TwitterUserList)
            filehandle = open('plugins/sleet/users.txt', 'w')
            filehandle.write(my_json_data)
            filehandle.close()
            if FirstRun != 1:
                try:
                    myStream.disconnect()
                except:
                    print "ERROR WITH DISCONNECTION AT REMOVE"
            outputs.append([sChannel, "TWITTER - No longer following: %s" % NewFollow ])
            set_stream()
    elif data["text"].find(sbID) != -1 and data["text"].find("!add") != -1:
        initial_pos = data["text"].find("add")
        next_pos = data["text"].find(" ", initial_pos)
        next_pos2 = next_pos + 1
        new_pos = data["text"].find(" ", next_pos2)
        if new_pos == -1:
            new_pos = len(data["text"])
        NewFollow = data["text"][next_pos2:new_pos]
        if NewFollow not in KeyWordList:
            KeyWordList.append(NewFollow)
            my_json_data = json.dumps(KeyWordList)
            xfilehandle = open('plugins/sleet/keywords.txt', 'w')
            xfilehandle.write(my_json_data)
            xfilehandle.close()
            if FirstRun != 1:
                try:
                    myStream.disconnect()
                except:
                    print "ERROR WITH DISCONNECTION AT ADD KEYWORD"
            outputs.append([sChannel, "TWITTER - Now tracking keyword: %s" % NewFollow ])
            set_stream()
    elif data["text"].find(sbID) != -1 and data["text"].find("!delete") != -1:
        initial_pos = data["text"].find("delete")
        next_pos = data["text"].find(" ", initial_pos)
        next_pos2 = next_pos + 1
        new_pos = data["text"].find(" ", next_pos2)
        if new_pos == -1:
            new_pos = len(data["text"])
        NewFollow = data["text"][next_pos2:new_pos]
        if NewFollow in KeyWordList:
            KeyWordList.remove(NewFollow)
            my_json_data = json.dumps(KeyWordList)
            xfilehandle = open('plugins/sleet/keywords.txt', 'w')
            xfilehandle.write(my_json_data)
            xfilehandle.close()
            if FirstRun != 1:
                try:
                    myStream.disconnect()
                except:
                    print "ERROR WITH DISCONNECTION AT REMOVE"
            outputs.append([sChannel, "TWITTER - No longer tracking keyword: %s" % NewFollow ])
            set_stream()
