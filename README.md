# Item Catalog

An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system.

## QuickStart

1 Download and install [Python](https://www.python.org/)

2 Download and install [virtual box](https://www.virtualbox.org/)

3 Download and install [vagrant](https://www.vagrantup.com/)

4 Clone this repository

5 Place the Item Catalog folder in your Vagrant directory

6 Launch Vagrant

```
$ vagrnt up
```

7 Login to vagrant

```
$ vagrant ssh
```

8 Change directory to ```/vagrant```

```
$ cd /vagrant
```

9 Run ```database_setup.py``` file to initialize *Database*

```
$ python database_setup.py
```

10 Run ```populate_database.py``` to populate database with some initial data

```
$ python populate_database.py
```

11 Run ```app.py``` file to launch the project

```
$ python app.py
```

12 Open browser and visit [http://localhost:5000](http://localhost:5000)

## SCREENSHOTS

> Home Page:

![Create](https://github.com/theashishmalik/item-catalog/blob/master/static/home.png)

> Creating a new Restaurant:

![Create](https://github.com/theashishmalik/item-catalog/blob/master/static/AddedRestaurant.png)
> Editing an existing Restaurant: 

![Edit](https://github.com/theashishmalik/item-catalog/blob/master/static/AddedMenu.png)
> SignIn :

![Delete](https://github.com/theashishmalik/item-catalog/blob/master/static/SignIn.png)
