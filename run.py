from config import *
from JSapps import *
from backend.database.Operations import *
if __name__ == '__main__':
    #putAppsData()
    app.run(host=host, port=port, debug=True)