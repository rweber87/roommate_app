import falcon
import pyscopg2

conn = psycopg2.connect("dbname=roommate_app user=postgres")

cur = conn.cursor()

class RoommateResource:
    def on_get(self, req, resp):
    	cur.execute("SELECT * FROM roommates;")
			roommates = cur.fetchall()
			resp.status = falcon.HTTP_200
			resp.body = roommates

app = falcon.API()

roommates = RoommateResource()

app.add_route('/roommate', roommates)