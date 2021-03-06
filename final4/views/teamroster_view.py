import sys
import json

from final4.config import app
from final4.db_helper import getDb
from final4.models import teamroster
from final4.models import player
from final4.models import team

from flask import render_template
from flask import request
from flask import session

@app.route('/teamrosters', methods=['GET'])
def teamrosters_home():
    conn, cur = getDb()
    teamrosters = teamroster.Teamrosters(conn, cur)
    print('TEAMROSTERS PAGE')
    if request.method == 'GET':
        print ('GET REQUEST', request.args)
        limit = int(request.args['limit']) if 'limit' in request.args else 10
        page = int(request.args['page']) if 'page' in request.args else 0
        
        offset = page*limit
        
        

    # check search value
    if 'team_name' in request.args:
        search_name = request.args['team_name']
        teamroster_list,total = teamrosters.get_teamrosters_search_by('name', search_name,  limit, offset)        
        
    else:

        teamroster_list, total = teamrosters.get_teamrosters(limit, offset)
    
    return render_template('teamrosters_home.html', teamrostertable=teamroster.teamrostertable, 
			teamrosters=teamroster_list, 
			total=total, limit=limit, page=page)


    return render_template('leagues_home.html', leaguetable=league.leaguetable, leagues=l, total=total, 
                limit=limit, page=page, sortby=sortby)


@app.route('/teamrosters/table', methods=['DEL','GET', 'POST'])
def teamroster_page():
    if 'username' not in session:
        return render_template('error.html', err_code=401)
    conn, cur = getDb()
    teamrosters = teamroster.Teamrosters(conn, cur)
    players = player.Players(conn, cur)
    teams = team.Teams(conn, cur)
    print('TEAMROSTERS PAGE')
    if request.method == 'GET':
        print ('GET REQUEST', request.args)
        limit = int(request.args['limit']) if 'limit' in request.args else 10
        page = int(request.args['page']) if 'page' in request.args else 0
        
        offset = page*limit
        print('page:',page,'limit',limit,'offset',offset)
        
 
        teamroster_list, total = teamrosters.get_teamrosters(limit, offset)
        player_list, pp = players.get_players(100,0)
        team_list,tp = teams.get_teams(100,0)
        
        return render_template('teamrosters.html', teamrostertable=teamroster.teamrostertable, 
			teamrosters=teamroster_list, players=player_list, teams=team_list, 
			total=total, limit=limit, page=page)
    elif request.method == 'POST':
        print('ADD TEAMROSTER')
        player_id = request.form['player']
        team_id = request.form['team']
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        teamroster_obj = teamroster.Teamroster(player_id, team_id)
        teamrosters.add_teamroster(teamroster_obj)
        
        teamroster_list, total= teamrosters.get_teamrosters(limit,offset)
        player_list,pp = players.get_players(100,0)
        team_list,tp = teams.get_teams(100,0)
        
        return render_template('teamrosters.html', teamrostertable=teamroster.teamrostertable, 
			teamrosters=teamroster_list, players=player_list, teams=team_list, 
			total=total, limit=limit, page=page)

    elif request.method == 'DEL':
        print ('DELETE REQUEST:TEAMROSTERS PAGE')
        print (request.form)
        idlist = request.form.getlist('ids[]')
        print ('IDS: ', idlist)
        if idlist == []:
            try:
                idlist = [request.form['id']]
                print ('IDS: ', idlist)
            except:
                return json.dumps({'status':'OK', 'idlist':idlist})

        print ('IDS: ', idlist)
        print(json.dumps({'status':'OK', 'idlist':idlist}))
        for _id in idlist:
            print (_id)
            teamrosters.delete_teamroster(_id)
        return json.dumps({'status':'OK', 'idlist':idlist})
 


@app.route('/teamrosters/g/<teamroster_id>', methods=['GET','POST'])
def teamroster_from_id(teamroster_id):
    if 'username' not in session:
        return render_template('error.html', err_code=401)
    conn, cur = getDb()
    teamrosters = teamroster.Teamrosters(conn, cur)
    players=player.Players(conn,cur)
    teams=team.Teams(conn,cur)
    
    if request.method == 'GET':
        l = teamrosters.get_teamroster(teamroster_id)
        if l:
            return json.dumps({'status':'OK', 'teamroster':l.getAttrs()})
        else:
            return json.dumps({'status':'FAILED'})
    elif request.method == 'POST':
        print("POST METHOD REQUEST")
        lid = request.form['id']
        player_id = request.form['player']
        team_id = request.form['team']
        
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        
        teamroster_obj = teamroster.Teamroster(player_id,team_id)
       
        teamrosters.update_teamroster(lid,teamroster_obj)
        
        teamroster_list, total= teamrosters.get_teamrosters(limit,offset)
        player_list,pp = players.get_players(100,0)
        team_list,tp = teams.get_teams(100,0)
        
        return render_template('teamrosters.html', teamrostertable=teamroster.teamrostertable, 
			teamrosters=teamroster_list, players=player_list, teams=team_list, 
			total=total, limit=limit, page=page)

@app.route('/teamrosters/s/<key>', methods=['GET','POST'])
def search_teamroster(key):
    if 'username' not in session:
        return render_template('error.html', err_code=401)
    conn, cur = getDb()
    teamrosters = teamroster.Teamrosters(conn, cur)
    players=player.Players(conn,cur)
    teams=team.Teams(conn,cur)

    limit = int(request.args['limit']) if 'limit' in request.args else 10
    page = int(request.args['page']) if 'page' in request.args else 0
    
    offset = page*limit
    
    teamroster_list,total = teamrosters.get_teamrosters_search_by('name', key,  limit, offset)
    player_list,pp = players.get_players(100,0)
    team_list,tp = teams.get_teams(100,0)
    
    return render_template('teamrosters.html', teamrostertable=teamroster.teamrostertable, 
			teamrosters=teamroster_list, players=player_list, teams=team_list, 
			total=total, limit=limit, page=page)
		
