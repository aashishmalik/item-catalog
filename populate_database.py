from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="imashishmalik.45@gmail.com")
session.add(User1)
session.commit()

restaurant1 = Restaurant(name="Fine Dining", user_id="1")
session.add(restaurant1)
session.commit()
menuItem1 = MenuItem(name="Italian Food",
                     description="Italian cuisine",
                     price="80", restaurant=restaurant1, user_id=1)
session.add(menuItem1)
session.commit()

restaurant2 = Restaurant(name="The Imperial Spice")
session.add(restaurant2)
session.commit()
menuItem1 = MenuItem(name="paneer Tikka pizza",
                     description="Combo of Panner and Pizza",
                     price="500", restaurant=restaurant2)
session.add(menuItem1)
session.commit()
menuItem2 = MenuItem(name="PRAWN AND LEMON GRASS SOUP",
                     description="Thai clear soup for seafood lovers",
                     price="250",  restaurant=restaurant2)
session.add(menuItem2)
session.commit()

print("Database Polpulated!")
