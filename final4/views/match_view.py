import sys
import json

from final4.config import app
from final4.db_helper import getDb
from final4.models import match
from final4.models import schedule

from flask import render_template
from flask import request

@app.route('/matches', methods=['GET'])
def matches_home():
    ''' This view page list all matches in matches table.
        This page doesn't allow editing.
    '''
    conn, cur = getDb()
    matches = match.Matches(conn, cur)
    shedules = shedule.Shedules(conn, cur)
    
    # limit, page and order args
    # required for each table page
    limit = int(request.args['limit']) if 'limit' in request.args else 10
    page = int(request.args['page']) if 'page' in request.args else 0
    offset = page*limit
    sortby = request.args['sortby'] if 'sortby' in request.args else 'name'
    order = request.args['order'] if 'order' in request.args else 'asc'
   
    # check search value
    if 'name' in request.args:
        search_name = request.args['name']
        l, total = matches.get_matches_search_by('name', search_name, limit=limit, offset=offset)
    else:
        l, total = matches.get_matches(limit=limit, offset=offset)
    return render_template('leagues_home.html', matchtable=match.matchtable, matches=l, total=total, 
                limit=limit, page=page, sortby=sortby)

@app.route('/matches/table', methods=['DEL','GET', 'POST'])
def match_page():
    '''Routing function for match-table page. 

    This page has session control. see *session controlled pages*

    This page lists matches and allows adding, deleting, and updating on them.
    '''
    conn, cur = getDb()
    matches = match.Matches(conn, cur)
    schedules = schedule.Schedules(conn, cur)
    print('MATCHES PAGE')
    if request.method == 'GET':
        # handle GET request
        print ('GET REQUEST', request.args)
        limit = int(request.args['limit']) if 'limit' in request.args else 10
        page = int(request.args['page']) if 'page' in request.args else 0
        
        offset = page*limit
        print('page:',page,'limit',limit,'offset',offset)
        sortby = request.args['sortby'] if 'sortby' in request.args else 'name'
        order = request.args['order'] if 'order' in request.args else 'asc'
 
        l, total = matches.get_matches(limit, offset)
        c, ts = schedules.get_schedules()
        sortby={'attr':'name', 'property':'asc'}
        return render_template('matches.html', matchtable=match.matchtable, matches=l, schedules=c, total=total, 
                limit=limit, page=page, sortby=sortby)
    elif request.method == 'POST':
        # handle POST request
        print('ADD MATCH')
        
        schedule_id = request.form['schedule'] #FK
        T1_3PT = request.form['T1_3PT']
        T1_2PT = request.form['T1_2PT']
        T1_block = request.form['T1_block']
        T1_reb = request.form['T1_reb']
        T1_rate = request.form['T1_rate']
        T2_3PT = request.form['T2_3PT']
        T2_2PT = request.form['T2_2PT']
        T2_block = request.form['T2_block']
        T2_reb = request.form['T2_reb']
        T2_rate = request.form['T2_rate']
        
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        order = request.form['sortby'] if 'sortby' in request.form else 'name'
        order = request.form['order'] if 'order' in request.form else 'asc'
        
        match_obj = match.Match(schedule_id, T1_3PT, T1_2PT, T1_block, T1_reb, T1_rate, T2_3PT, T2_2PT, T2_block, T2_reb, T2_rate)
        matches.add_match(match_obj)
        
        match_list, total = matches.get_matches(limit, offset)
        schedule_list, ts = schedules.get_schedules() # get list object
        sortby={'attr':'name', 'property':'asc'}
        return render_template('matches.html', matchtable=match.matchtable, matches=match_list,
			schedules=schedule_list, total=total, limit=limit, page=page, sortby=sortby)
			
    elif request.method == 'DEL':
        # handle DEL request
        print ('DELETE REQUEST:MATCHES PAGE')
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
            matches.delete_match(_id)
        return json.dumps({'status':'OK', 'idlist':idlist})

@app.route('/matches/g/<match_id>', methods=['GET','POST'])
def get_match_from_id(match_id):
    '''Routing function for getting match from its id.
    
    *GET request* returns JSON object.

    *POST request* updates match which has id equal to the *lid* with the 
    values recieved from the request.form. After all it renders matches.html

    :param lid: id of the match, int
    '''
    conn, cur = getDb()
    matches = match.Matches(conn, cur)
    schedules = schedule.Schedules(conn, cur)
    
    if request.method == 'GET':
        # handle GET request
        match_obj= matches.get_match(match_id)
        if match_obj:
            return json.dumps({'status':'OK', 'match':match_obj.getAttrs()})
        else:
            return json.dumps({'status':'FAILED'})
    elif request.method == 'POST':
        # handle POST request
        print("POST METHOD REQUEST")
        print(request.form)
        schedule_id = request.form['schedule'] #FK
        #T1_name = request.form['T1_name']
        #T2_name = request.form['T2_name']
        T1_3PT = request.form['T1_3PT']
        T1_2PT = request.form['T1_2PT']
        T1_block = request.form['T1_block']
        T1_reb = request.form['T1_reb']
        T1_rate = request.form['T1_rate']
        T2_3PT = request.form['T2_3PT']
        T2_2PT = request.form['T2_2PT']
        T2_block = request.form['T2_block']
        T2_reb = request.form['T2_reb']
        T2_rate = request.form['T2_rate']
 
        # limit: number of result showing each page
        # offset: selectedpage x limit
        limit = int(request.form['limit']) if 'limit' in request.form else 10
        page = int(request.form['page']) if 'page' in request.form else 0
        offset = page*limit
        order = request.form['sortby'] if 'sortby' in request.form else 'name'
        order = request.form['order'] if 'order' in request.form else 'asc'
        
        match_obj = match.Match(schedule_id, T1_3PT, T1_2PT, T1_block, T1_reb, T1_rate, T2_3PT, T2_2PT, T2_block, T2_reb, T2_rate)
        matches.update_match(match_id, match_obj)
        
        match_list, total = matches.get_matches(limit, offset)
        schedule_list, ts = schedules.get_schedules() # get list object
        sortby={'attr':'name', 'property':'asc'}
        return render_template('matches.html', matchtable=match.matchtable, matches=match_list,
			schedules=schedule_list, total=total, limit=limit, page=page, sortby=sortby)

@app.route('/matches/s/<key>', methods=['GET','POST'])
def search_match(key):
    '''Routing function for search match by its name.

    *GET request* renders the matches.html with matches comes from the search result.
    '''
    conn, cur = getDb()
    matches = match.Matches(conn, cur)
    schedules = schedule.Schedules(conn, cur)
    
    limit = int(request.args['limit']) if 'limit' in request.args else 10
    page = int(request.args['page']) if 'page' in request.args else 0

    sortby = request.args['sortby'] if 'sortby' in request.args else 'name'
    order = request.args['order'] if 'order' in request.args else 'asc'
    
    offset = page*limit

    match_list, total = matches.get_matches_search_by('name', key,  limit, offset)
    schedule_list, ts = schedules.get_schedules() # get list object
    sortby={'attr':'name', 'property':'asc'}
    return render_template('matches.html', matchtable=match.matchtable, matchs=match_list, 
			schedules=schedule_list, total=total, limit=limit, page=page, sortby=sortby)
			
@app.route('/matches/match/<match_id>')
def view_match(match_id):
    '''Routing function for match info page.
    
    It renders the match_page.html with related statistical information.
    '''
    conn, cur = getDb()
    
    matches = match.Matches(conn, cur)
    schedules = schedule.Schedules(conn, cur)
    
    l = matches.get_match(match_id)
    if l is None:
        # return not found error 
        return render_template('error.html', err_code=404)

    # else render country page with required args

    return render_template('match_page.html', match=l)

