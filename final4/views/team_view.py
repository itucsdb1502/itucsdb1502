from flask import render_template

from final4.config import app
from final4.db_helper import getDb
from final4.models import team

# team views
@app.route('/teams')
def team_page():
    conn, cur = getDb()
    
    teams = team.Teams(conn, cur)
    teamlist = team.get_teams()
    return render_template('teams.html', teamtable=team.teamtable, teams=teamlist)


