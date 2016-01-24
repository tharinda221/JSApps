from config import *
from JSApps import *
from backend.database.Operations import *
if __name__ == '__main__':
    # app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host=host, port=port, debug=True, threaded=True)