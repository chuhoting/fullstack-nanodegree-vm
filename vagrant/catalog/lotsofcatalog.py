import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from databasecreate import SportCategory, Base, SportItems, User

engine = create_engine('sqlite:///sportcategorysportitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won"t be persisted into the database until you call
# session.commit(). If you"re not happy about the change, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


category1 = SportCategory(name = "Soccer")
session.add(category1)
session.commit()

item1 = SportItems(name = "Soccer ball", description = "For you to kick around", sportcategory = category1)
session.add(item1)
session.commit()

item2 = SportItems(name = "Soccer Gloves", description = "Save it", sportcategory = category1)
session.add(item2)
session.commit()


category2 = SportCategory(name = "Basketball")
session.add(category2)
session.commit()

item1 = SportItems(name = "Basketball the ball", description = "For you to shoot", sportcategory = category2)
session.add(item1)
session.commit()

item2= SportItems(name = "NBA Video Recording", description = "Watch Jordan Fly", sportcategory = category2)
session.add(item2)
session.commit()

category3 = SportCategory(name = "Frisbee")
session.add(category3)
session.commit()
item1 = SportItems(name = "The Frisbee", description = "Toss it and watch it return", sportcategory = category3)
session.add(item1)
session.commit()
item2 = SportItems(name = "Yellow Frisbee", description = "Only if you like Yellow", sportcategory = category3)
session.add(item2)
session.commit()

category4 = SportCategory(name = "Baseball")
session.add(category4)
session.commit()
item1 = SportItems(name = "Baseball Glove", description = "Pitch it like you mean it", sportcategory = category4)
session.add(item1)
session.commit()
item2 = SportItems(name = "Green Gloves", description = "For the GREEN boy", sportcategory = category4)
session.add(item2)
session.commit()

category5 = SportCategory(name = "Snowboarding")
session.add(category5)
session.commit()
item1 = SportItems(name = "Helmet", description = "You will need one", sportcategory = category5)
session.add(item1)
session.commit()
item2 = SportItems(name = "Snow Machine", description = "Otherwise what to board on", sportcategory = category5)
session.add(item2)
session.commit()

category6 = SportCategory(name = "Rockclimbing")
session.add(category6)
session.commit()
item1 = SportItems(name = "Chalk", description = "Hang on for your dear life", sportcategory = category6)
session.add(item1)
session.commit()
item2 = SportItems(name = "White Gloves (rock)", description = "For the GRIP", sportcategory = category6)
session.add(item2)
session.commit()

category7 = SportCategory(name = "Foosball")
session.add(category7)
session.commit()
item1 = SportItems(name = "What the shit is this", description = "Turn it twist it", sportcategory = category7)
session.add(item1)
session.commit()

category8 = SportCategory(name = "Hockey")
session.add(category8)
session.commit()
item1 = SportItems(name = "Hockey Stick", description = "Whack it wrath", sportcategory = category8)
session.add(item1)
session.commit()
item2 = SportItems(name = "Hockey Shoes", description = "Run like a dog", sportcategory = category8)
session.add(item2)
session.commit()

category9 = SportCategory(name = "Skating")
session.add(category9)
session.commit()
item1 = SportItems(name = "Skates", description = "Asian Pride", sportcategory = category9)
session.add(item1)
session.commit()
item2 = SportItems(name = "Skate Knee Pads", description = "Protect your kneecaps", sportcategory = category9)
session.add(item2)
session.commit()

print "added all these items!"
