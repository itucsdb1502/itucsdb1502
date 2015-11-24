from flask import render_template

from final4.config import app
from final4.db_helper import getDb
from final4.models import teamroster

# player views
@app.route('/teamrosters')
def teamroster_page():
    conn, cur = getDb()
    
    teamrosters = teamroster.Teamrosters(conn, cur)
    playerlist = players.get_players()
    return render_template('teamrosters.html', teamrostertable=teamroster.teamrostertable, teamrosters=teamrosterlist)


