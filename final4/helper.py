from final4.db_helper import getDb

import datetime

# HELPER FUNCS

def login_success(username, password):
    conn, cur = getDb()
    cur.execute("SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password) )
    user = cur.fetchone()

    if user:
        return True

    return False

def getCurrTimeStr():
    now = str(datetime.datetime.now())
    return now[:-7]


