import tweepy # for tweeting
import secrets # shhhh
import random


def random_modifier():
  # open text file
  text_file = open('modifiers.txt', 'r')
  text_string = text_file.read()
  return random.choice(text_string.split('\n'))

def get_next_chunk():
  # open text file
  text_file = open('names.txt', 'r+')
  text_string = text_file.read()
  chunk = text_string.split('\n')[0]

  # delete what we just tweeted from the text file
  text_file.seek(0)
  text_file.write(text_string[len(chunk) + 1:len(text_string)])
  text_file.truncate()
  text_file.close()

  return chunk

def desiderata_word():
  return random_modifier() + ' ' + get_next_chunk()

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  print("Posting message {}".format(message))
  api.update_status(status=message)

tweet(desiderata_word())
