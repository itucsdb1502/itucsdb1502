teamtable = ['id', 'name', 'coach_id']

class Team:
    def __init__(self, name, coach_id, _id=None):
	    self._id=_id        
	    self.name = name
	    self.coach_id = coach_id
       		
class Teams:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
        self.last_key = None

    def add_team(self, team):
        print("addplayer",player)
        query = """INSERT INTO players (name, coach_id) 
                                    values ('%s','%s')"""
        self.cur.execute(query,(team.name,team.coach_id))
        self.conn.commit()

    def delete_team(self, _id):
        query = "DELETE FROM teams WHERE id='%s"""
        self.cur.execute(query,(_id,))
        self.conn.commit()

    def update_team(self,_id,new_team):
        
        query = """UPDATE teams SET name=%s, coach_id=%s, 
                    id=%s""" 

        self.cur.execute(query,(new_team.name,new_team.coach_id,_id))
        self.conn.commit()

    def get_team(self, _id):
        query = "SELECT * FROM teams WHERE id=%s" 
        self.cur.execute(query,(_id))
        t = self.cur.fetchone()
        if t:
            
            td = dict(zip(teamtable, t)) # team dict
            team = Team(td['name'], td['coach_id'],td['id'])
            print (team.age)
            return team
        else:
            return None

    def get_teams(self):
        query = "SELECT * FROM teams;"
        self.cur.execute(query)
        teams = self.cur.fetchall()
        teamlist = []
        for t in Teams:
            td = dict(zip(teamtable, t))
            team = Team(ld['name'], ld['country'],ld['id'])
            teamlist.append(team)
        return teamlist
