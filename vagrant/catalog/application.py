from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import SportCategory, Base, SportItems

app = Flask(__name__)

engine = create_engine('sqlite:///sportcategorysportitems.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog')
def catalog():
    catalog = session.query(SportCategory).all()
    return render_template('catalog.html', SportCategory = SportCategory, SportItems = SportItems )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded = False)
