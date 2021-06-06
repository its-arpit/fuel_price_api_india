Fuel Price API India 
=============
![alt text](https://images.hindustantimes.com/auto/img/2021/05/31/600x338/20210529189L_1622429410483_1622429432528.jpg)

An API for the latest fuel prices in India for all the major towns and cities. 
It is a Flask based lean app. 

To run it on your own server, you will need [Python][] with the [Flask][] microframework and [BS4][]. 
Use can use either `easy_install` or `pip` to install the libraries. 

Start the server with : 

    $ python -m flask run

[Python]: http://python.org/
[Flask]: http://flask.pocoo.org/
[Beautifulsoup4]: https://pypi.org/project/beautifulsoup4/

REST webservice calls
---------------------

- /states - returns a Dict of all states. 
- /state/district?state=Delhi - returns a Dict of all districts of paramaeter passed state. 
- /price/state/district?state=Delhi&district=South%20Delhi - It will give diesel price passed district along with state. 

In free time I'll upgrade this API.
Photo Credit [https://auto.hindustantimes.com/auto/news/new-day-new-high-petrol-diesel-price-hiked-for-the-16th-day-in-may-41622429310566.html]

--
I <3 scraping. 
