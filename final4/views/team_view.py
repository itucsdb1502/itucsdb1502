import sys
import json

from final4.config import app
from final4.db_helper import getDb
from final4.models import team
from final4.models import country

from flask import render_template
from flask import request

@app.route('/teams', methods=['DEL','GET', 'POST'])
def team_page():
    conn, cur = getDb()
    teams = team.Teams(conn, cur)
    countries = country.Countries(conn, cur)
    print('TEAMS PAGE')
    if request.method == 'GET':
        print ('GET REQUEST', request.args)
        limit = int(request.args['limit']) if 'limit' in request.args else 10
        page = int(request.args['page']) if 'page' in request.args else 0
        
        offset = page*limit
        print('page:',page,'limit',limit,'offset',offset)
        orderby = request.args['orderby'] if 'orderby' in request.args else 'asc'
        t, total = teams.get_teams(limit, offset)
        c = countries.get_countries()
        return render_template('teams.html', teamtable=team.teamtable, teams=t, countries=c, total=total, 
                                limit=limit, page=page)
    elif request.method == 'POST':
        print('ADD TEAM')
        name = request.form['name']
        country_id = request.form['country']
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        orderby = request.form['orderby'] if 'orderby' in request.form else 'asc'
        lg = team.Team(name, country_id)
        teams.add_team(lg)
        
        t, total = teams.get_teams(limit, offset)
        c = countries.get_countries()
        return render_template('teams.html', teamtable=team.teamtable, teams=t, countries=c, total=total, 
                                limit=limit, page=page)

    elif request.method == 'DEL':
        print ('DELETE REQUEST:TEAMS PAGE')
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
            teams.delete_team(_id)
        return json.dumps({'status':'OK', 'idlist':idlist})

@app.route('/teams/g/<tid>', methods=['GET','POST'])
def team_from_id(tid):
    conn, cur = getDb()
    teams = team.Teams(conn, cur)
    countries = country.Countries(conn, cur)
    
    if request.method == 'GET':
        t= teams.get_team(tid)
        if t:
            return json.dumps({'status':'OK', 'team':t.getAttrs()})
        else:
            return json.dumps({'status':'FAILED'})
    elif request.method == 'POST':
        print("POST METHOD REQUEST")
        tid = request.form['id']
        name = request.form['name']
        country_id = request.form['country']
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        orderby = request.form['orderby'] if 'orderby' in request.form else 'asc'
        lg = team.Team(name, country_id)
        teams.update_team(tid, lg)
        
        t, total = teams.get_teams(limit, offset)
        c = countries.get_countries()
        return render_template('teams.html', teamtable=team.teamtable, teams=t, countries=c, total=total, 
                                limit=limit, page=page)


@app.route('/teams/s/<key>', methods=['GET','POST'])
def search_team(key):
    conn, cur = getDb()
    teams = team.Teams(conn, cur)
    countries = country.Countries(conn, cur)

    limit = int(request.args['limit']) if 'limit' in request.args else 10
    page = int(request.args['page']) if 'page' in request.args else 0
    
    offset = page*limit

    result,total = teams.get_teams_search_by('name', key,  limit, offset)
    c = countries.get_countries()
    return render_template('teams.html', teamtable=team.teamtable, teams=result, countries=c, total=total, 
                            limit=limit, page=page)
