from flask import url_for

teamtable = ['id', 'name','coach_id', 'coach_name','coach_surname']

class Team:
    def __init__(self, name,coach_id, coach_name=None,coach_surname=None, _id=None):
        self._id = _id
        self.name = name
        self.coach_id = coach_id
        self.coach_name = coach_name
        self.coach_surname = coach_surname
    def img_path(self, _id=None):
        if _id==None and self._id==None:
            return url_for('static',filename='.') + 'data/img/teams/not_available.png'
        if _id:
            return url_for('static',filename='.') + 'data/img/teams/' + str(_id) + '.png'
        else:
            return url_for('static',filename='.') +'data/img/teams/' + str(self._id) + '.png'

    def getAttrs(self):
        return (dict(zip(teamtable, (self._id, self.name, self.coach_id, self.coach_name,self.coach_surname))))

class Teams:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
        self.last_key = None

    def add_team(self, team):
        print("addteam ", team)
        query = """INSERT INTO teams (name,coach_id) 
                                    values (%s,%s) RETURNING id""" 

        self.cur.execute(query, (team.name, team.coach_id))
        insert_id = self.cur.fetchone()[0]
        self.conn.commit()
        return insert_id

    def delete_team(self, _id):
        query = """DELETE FROM teams WHERE id=%s"""
        self.cur.execute(query, (_id,))
        self.conn.commit()

    def update_team(self, _id, new):
        print('update_team')
        query = """UPDATE teams SET name=%s, coach_id=%s
                    WHERE id=%s"""
        self.cur.execute(query, (new.name, new.coach_id, _id))
        self.conn.commit()

    def get_team(self,_id):
        query = """SELECT teams.id, teams.name, coaches.id, coaches.name,coaches.surname
                        FROM teams,coaches
                        WHERE teams.id=%s AND coaches.id=teams.coach_id
                        ORDER BY teams.name
                        """
        self.cur.execute(query, (_id,))
        t = self.cur.fetchone()
        if t:
            td = dict(zip(teamtable, t[:len(teamtable)]))
            team = Team(td['name'], td['coach_id'], td['coach_name'], td['coach_surname'], td['id'])
            return team
        else:
            return None

    def get_teams(self, limit=100, offset=0):
        query = """SELECT count(teams.id)
                        FROM teams,coaches WHERE coaches.id=teams.coach_id
                          """
        self.cur.execute(query)
        total = self.cur.fetchone()[0]

        query = """SELECT teams.id, teams.name, coaches.id, coaches.name,coaches.surname 
                        FROM teams,coaches WHERE coaches.id=teams.coach_id
                          ORDER BY teams.name LIMIT %s OFFSET %s"""
        self.cur.execute(query, (limit, offset))
        teams = self.cur.fetchall()
        teamlist = []
        for t in teams:
            td = dict(zip(teamtable, t))
            team = Team(td['name'], td['coach_id'], td['coach_name'], td['coach_surname'],td['id'])
            teamlist.append(team)
        return teamlist, total

    def get_teams_by(self, attrib, search_key, limit=100, offset=0):
        skey = str(search_key)
        
        query = """SELECT count(teams.id)
                        FROM teams,coaches WHERE teams.{attrib}=%s AND 
                            coaches.id=teams.coach_id""".format(attrib=attrib)
        self.cur.execute(query, (skey,))
        total = self.cur.fetchone()[0]
        
        query = """SELECT teams.id, teams.name, teams.coach_id, coaches.name,coaches.surname
                        FROM teams,coaches WHERE teams.{attrib}=%s AND 
                            coaches.id=teams.coach_id ORDER BY teams.name 
                            LIMIT %s OFFSET %s""".format(attrib=attrib)
        self.cur.execute(query, (skey, limit, offset))
        teams = self.cur.fetchall()
        print('teams:', teams)
        teamlist = []
        for t in teams:
            td = dict(zip(teamtable, t))
            team = Team(td['name'],  td['coach_id'], td['coach_name'], td['coach_surname'],td['id'])
            teamlist.append(team)
        return teamlist, total

    def get_teams_search_by(self, attrib, search_key, limit=100, offset=0):
        skey = str(search_key) + '%'
        
        query = """SELECT count(teams.id)
                        FROM teams,coaches WHERE teams.{attrib} LIKE %s AND 
                            coaches.id=teams.coach_id""".format(attrib=attrib)
        self.cur.execute(query, (skey,))
        total = self.cur.fetchone()[0]
        
        query = """SELECT teams.id, teams.name, teams.coach_id, coaches.name,coaches.surname
                        FROM teams,coaches WHERE teams.{attrib} LIKE %s AND 
                            coaches.id=teams.coach_id ORDER BY teams.name 
                            LIMIT %s OFFSET %s""".format(attrib=attrib)
        self.cur.execute(query, (skey, limit, offset))
        teams = self.cur.fetchall()
        print('teams:', teams)
        teamlist = []
        for t in teams:
            td = dict(zip(teamtable, t))
            team = Team(td['name'], td['coach_id'], td['coach_name'], td['coach_surname'],td['id'])
            teamlist.append(team)
        return teamlist, total

