import sys, twitter

from datetime import datetime


def main():
  user = sys.argv[1]
  friends = get_friends(user)
  frequencies = get_frequencies(friends)
  output_results(frequencies)


def get_friends(user):
  api = twitter.Api(
    consumer_key='x6loeD4LKC9WUJUuz94xZA',
    consumer_secret='uWE7HUeKQ5xTNBgY31QRrhORAzpd9KDl3wvjSQKsA',
    access_token_key='16024857-Eaf22XzYRbsb5AOTLibyycIiGMH9FG5K0K5xYd2Ts',
    access_token_secret='JPAMsSzqWsCoqLMLulRp3VD0nFfWYlmUa7DeqWy4Rk')
  
  return api.GetFriends(user)


def get_frequencies(friends):
  return dict((f.screen_name, get_tweets_per_day(f)) for f in friends)


def get_tweets_per_day(friend):
  created_at_unicode = friend.created_at.replace(' +0000', '') # http://bugs.python.org/issue6641
  created_at = datetime.strptime(created_at_unicode, "%a %b %d %H:%M:%S %Y")
  days_since_creation = (datetime.now() - created_at).days
  return friend.statuses_count / float(days_since_creation)


def output_results(frequencies):
  for (friend, frequency) in frequencies.items():
    print("%s\n%.1f tweets per day\n" % (friend, frequency))


#--------------------------
if __name__ == "__main__":
  if len(sys.argv) > 1:
    main()
  else:
    print 'Please provide an username.'
