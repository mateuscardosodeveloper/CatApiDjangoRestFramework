# Challenge from Let's delivery 

<h3>Goal of this projects is I'm lerner more about django rest framework</h3>

* We have three endpoints

* First endpoint is a list to endpoint for a cats management

* Second endpoint is to create a new Cat

* Third endpoint is to update or delete one cat select for id

* Also have filter to search cats registered

* I have create one command in python manage.py to create three new cats

```sh
    python manage.py create_three_cat
```

<h3>About tests</h3>

* Test is based in models, cat and command

* Models have one test to create a new cat if have string representation

* Cat have six tests, to create new cat success, create new cat fail, update partial cat, update full cat, if update cat breeed with value already registered and filter with value negative.

* Command have one test, if command create three new cats correctly

<h3>how execute this project using docker</h3>


```sh
# into folder the project excute command

docker build .

# the next

docker-compose build

# now excute project

docker-compose up

# to see tests excute

docker-compose run --rm app sh -c 'python manage.py test && flake8' #flake8 is patterns clean code
```
