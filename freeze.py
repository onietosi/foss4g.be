#from app import app
# app.run(debug=True)

from flask_frozen import Freezer
from app import app
# from myapplication import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze() # destination='test_build')

