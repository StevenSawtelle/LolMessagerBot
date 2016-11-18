import time#time to ease reddit servers with calls
import praw

r = praw.Reddit('messame me about key LoL word mentions 1.0 by u/baconologist')
r.login()
already_done = []#to be used so that one post isnt mentioned multiple times

lolWords = ['bard', 'riot', 'pls', 'support']#words to look for
while True:
    subreddit = r.get_subreddit('leagueoflegends')
    for submission in subreddit.get_hot(limit=10):#get 10 hot posts from /r/lol
        op_text = submission.selftext.lower()#lower easier to deal with
        has_camille = any(string in op_text for string in lolWords)#any post where main body has one of the strings listed
        if submission.id not in already_done and has_camille:#also if not handled already
            msg = '[LOL related thread](%s)' % submission.short_link#msg to send to me, hyperlinked
            r.send_message('Baconologist', 'LOL Thread', msg)#user, title, body
            already_done.append(submission.id)# dont repeat post if multiple occurences of keywords
    time.sleep(1800)#wait 30 min
