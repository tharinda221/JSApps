from config import *
from JSApps import *
from backend.database.Operations import *
if __name__ == '__main__':
    app.run(host=host, port=port, debug=True, threaded=True)