import sys
import json

from final4.config import app
from final4.db_helper import getDb
from final4.models import player
from final4.models import country

from flask import render_template
from flask import request

# player views
@app.route('/players', methods=['DEL','GET', 'POST'])
def player_page():
    conn, cur = getDb()
    players = player.Players(conn, cur)
    countries = country.Countries(conn, cur)
    print('PLAYERS PAGE')
    if request.method == 'GET':
        print ('GET REQUEST', request.args)
        limit = int(request.args['limit']) if 'limit' in request.args else 10
        page = int(request.args['page']) if 'page' in request.args else 0
        
        offset = page*limit
        print('page:',page,'limit',limit,'offset',offset)
        orderby = request.args['orderby'] if 'orderby' in request.args else 'asc'
        l, total = players.get_players(limit, offset)
        c = countries.get_countries()
        return render_template('players.html', playertable=player.playertable, players=l, countries=c, total=total, 
                                limit=limit, page=page)
    elif request.method == 'POST':
        print('ADD PLAYER')
        name = request.form['name']
        age = request.form['age']
        country_id = request.form['country']
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        orderby = request.form['orderby'] if 'orderby' in request.form else 'asc'
        lg = player.Player(name,age, country_id)
        players.add_player(lg)
        
        l, total = players.get_players(limit, offset)
        c = countries.get_countries()
        return render_template('players.html', playertable=player.playertable, players=l, countries=c, total=total, 
                                limit=limit, page=page)

    elif request.method == 'DEL':
        print ('DELETE REQUEST:PLAYERS PAGE')
        print (request.form)
        # concat json var with '[]' for calling array getted with request
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
            players.delete_player(_id)
        return json.dumps({'status':'OK', 'idlist':idlist})

@app.route('/players/g/<lid>', methods=['GET','POST'])
def player_from_id(lid):
    conn, cur = getDb()
    players = player.Players(conn, cur)
    countries = country.Countries(conn, cur)
    
    if request.method == 'GET':
        l= players.get_player(lid)
        if l:
            return json.dumps({'status':'OK', 'player':l.getAttrs()})
        else:
            return json.dumps({'status':'FAILED'})
    elif request.method == 'POST':
        print("POST METHOD REQUEST")
        lid = request.form['id']
        name = request.form['name']
        age = request.form['age']
        country_id = request.form['country']
        # limit: number of result showing each page
        # offset: selectedpage x limit
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        orderby = request.form['orderby'] if 'orderby' in request.form else 'asc'
        lg = player.Player(age, country_id)
        players.update_player(lid, lg)
        
        l, total = players.get_players(limit, offset)
        c = countries.get_countries()
        return render_template('players.html', playertable=player.playertable, players=l, countries=c, total=total, 
                                limit=limit, page=page)


@app.route('/players/s/<key>', methods=['GET','POST'])
def search_player(key):
    conn, cur = getDb()
    players = player.Players(conn, cur)
    countries = country.Countries(conn, cur)

    limit = int(request.args['limit']) if 'limit' in request.args else 10
    page = int(request.args['page']) if 'page' in request.args else 0
    
    offset = page*limit

    result,total = players.get_players_by(key, 'name', limit, offset)
    c = countries.get_countries()
    return render_template('players.html', playertable=player.playertable, players=result, countries=c, total=total, 
                            limit=limit, page=page)
