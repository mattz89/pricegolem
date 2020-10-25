To configure: 

Prerequisites: Python3, pipenv

Mac / Linux commands (in order):

pipenv install -r requirements.txt
pipenv shell
python3
from app import db
db.create_all()
exit()
flask run

The app will now be viewable on localhost:5000

Currently any item URL on bhphotovideo.com or ulta.com can be added along with your desired buy price. 

Support for other sites can be added by modifying Scraper.py and PriceChecker.py.