import os
import twitter
import markov
import sys

# Use Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# This will print info about credentials to make sure they're correct
print api.VerifyCredentials()

# Generate Markov text and print to screen to see if it is worth posting.
filenames = sys.argv[1:]
generator = markov.MarkovMachine()
generator.read_files(filenames)


# Control flow
print "Welcome to the Markov Tweeter!"
print "Enter yes to post to Twitter."
print "Enter no to get another random tweet."
print "Enter q to exit."

user_input = "no"

while user_input != "yes":
    possible_tweet = generator.make_text()
    print possible_tweet

    user_input = raw_input("Do you want to post this on Twitter?").lower()

    if  user_input == "yes": #send tweet
        status = api.PostUpdate(possible_tweet)
        print status.text
    elif user_input == "q":
        break
    else:
        print "Please choose yes, no or q."
