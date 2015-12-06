playertable = ['id', 'name','age','country_id', 'country']

class Player:
    def __init__(self, name,age, country_id, country=None, _id=None):
        self._id = _id
        self.name = name
        self.age=age
        self.country_id = country_id
        self.country = country

    def getAttrs(self):
        return (dict(zip(playertable, (self._id, self.name,self.age, self.country_id, self.country))))

class Players:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
        self.last_key = None

    def add_player(self, player):
        print("addplayer ", player)
        query = """INSERT INTO players (name,age, country_id) 
                                    values (%s,%s,%s)""" 

        self.cur.execute(query, (player.name,player.age, player.country_id))
        self.conn.commit()

    def delete_player(self, _id):
        query = """DELETE FROM players WHERE id=%s"""
        # variables should be in tuple object
        self.cur.execute(query, (_id,))
        self.conn.commit()

    def update_player(self, _id, new):
        '''
        new : player object
        '''
        print('update_player')
        query = """UPDATE players SET name=%s,age=%s, country_id=%s,
                    WHERE id=%s"""
        self.cur.execute(query, (new.name,new.age, new.country_id, _id))
        self.conn.commit()

    def get_player(self,_id):
        query = """SELECT players.id, players.name,players.age countries.id, countries.name
                        FROM players,countries
                        WHERE players.id=%s AND countries.id=players.country_id
                        ORDER BY players.name
                        """
        self.cur.execute(query, (_id,))
        l = self.cur.fetchone()
        if l:
            ld = dict(zip(playertable, l[:len(playertable)]))
            player = Player(ld['name'],ld['age'], ld['country_id'], ld['country'], ld['id'])
            return player
        else:
            return None

    def get_players(self, limit, offset):

        query = """SELECT count(players.id)
                        FROM players,countries WHERE countries.id=players.country_id
                          """
        self.cur.execute(query)
        total = self.cur.fetchone()[0]

        query = """SELECT players.id, players.name,players.age, countries.id, countries.name 
                        FROM players,countries WHERE countries.id=players.country_id
                          ORDER BY players.name LIMIT %s OFFSET %s"""
        self.cur.execute(query, (limit, offset))
        players = self.cur.fetchall()
        playerlist = []
        for l in players:
            ld = dict(zip(playertable, l))
            player = Player(ld['name'],ld['age'], ld['country_id'], ld['country'],ld['id'])
            playerlist.append(player)
        return playerlist, total

    def get_players_by(self, key, var, limit, offset):
        skey = str(key) + '%'

        query = """SELECT count(players.id)
                        FROM players,countries WHERE players.name LIKE %s AND 
                            countries.id=players.country_id"""
        self.cur.execute(query, (skey,))
        total = self.cur.fetchone()[0]

        query = """SELECT players.id, players.name,players.age , players.country_id,countries.name
                        FROM players,countries WHERE players.name LIKE %s AND 
                            countries.id=players.country_id ORDER BY players.name
                            LIMIT %s OFFSET %s"""
        self.cur.execute(query, (skey,limit, offset))
        players = self.cur.fetchall()
        print('players:', players)
        playerlist = []
        for l in players:
            ld = dict(zip(playertable, l))
            player = Player(ld['name'],ld['age'], ld['country_id'],ld['country'],ld['id'])
            playerlist.append(player)
        return playerlist, total

