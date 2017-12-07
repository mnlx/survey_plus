import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'survey_plus.settings')
import random
import django
django.setup()
from forms.models import Category, Page, User
from conversations.models import *



s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

def sing_sen_maker():
    return random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
def populate():
# First, we will create lists of dictionaries containing the pages
# we want to add into each category.
# Then we will create a dictionary of dictionaries for our categories.
# This might seem a little bit confusing, but it allows us to iterate
# through each data structure, and add the data to our models.
    python_pages = [
    {"title": "Official Python Tutorial",
    "url":"http://docs.python.org/2/tutorial/"},
    {"title":"How to Think like a Computer Scientist",
    "url":"http://www.greenteapress.com/thinkpython/"},
    {"title":"Learn Python in 10 Minutes",
    "url":"http://www.korokithakis.net/tutorials/python/"} ]

    django_pages = [
    {"title":"Official Django Tutorial",
    "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
    {"title":"Django Rocks",
    "url":"http://www.djangorocks.com/"},
    {"title":"How to Tango with Django",
    "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
    {"title":"Bottle",
    "url":"http://bottlepy.org/docs/dev/"},
    {"title":"Flask",
    "url":"http://flask.pocoo.org"} ]

    cats = {"Python": {"pages": python_pages},
    "Django": {"pages": django_pages},
    "Other Frameworks": {"pages": other_pages},
    "Py":{	"pages": django_pages },
	"Practice":{"pages": django_pages},
	}

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views= random.randrange(100)
    p.save()
    return p
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = random.randrange(100)
    
    c.save()
    return c
# Start execution here!

def create_users(*number):
    import names
    for i in range(number[0]):
        lname= names.get_last_name()
        fname = names.get_first_name()
        User.objects.create_user(username= fname+'_'+ lname +str(random.randrange(1,99)),password="Frenetico1",first_name=fname,last_name=lname).save()
        print('User created:' + fname + ' ' + lname)

def make_friends(*number):


    for usr in User.objects.all():
        r_l = random.sample(range(1, User.objects.all().count() + 1), User.objects.all().count())
        count = User.objects.all().count()
        for i in r_l[1:round(count*random.random())]:
            print(usr.username + str(i))
            if i != usr.id:
                frd = Friends.objects.create(friend_id = i,is_blocked = round(random.random()),user = usr)
                frd.save()

import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)


def messaging(*number):

    for usr in User.objects.all():

        for frd in usr.friends_set.all():

            print(int(frd.friend_id))

            for i in range(random.randrange(1,1000)):
                text = ''.join(sing_sen_maker())
                msg = Messages.objects.create(pub_date = randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random()))
                print(str(text), usr,User.objects.get(pk = int(frd.friend_id)))
                msg.add(str(text),usr,User.objects.get(pk = frd.friend_id))
                msg.save()

if __name__ == '__main__':
    print("Starting Rango population script...")
    # populate()
    # create_users(20)
    # make_friends()
    messaging()