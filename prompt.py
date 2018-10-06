from sys import argv

script, username = argv
prompt='>'

print "Do you like me,%s?" % username
like=raw_input(prompt)

print "What's your favorite food %s?" % username
food=raw_input(prompt)

print "What's your computer type %s?" % username
computer=raw_input(prompt)

print """
ALright,%s so you said %s is about liking me.
Your favorite food is %s.
And your computer type is %s.
""" % (username,like,food,computer) 
