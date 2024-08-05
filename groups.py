from db import db
from sqlalchemy.sql import text
import users

def get_list():
    sql = "SELECT G.name, U.username, G.created_at FROM groups G, users U WHERE G.user_id=U.id ORDER BY G.id"
    result = db.session.execute(text(sql))
    return result.fetchall()

def send(name):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO groups (name, user_id, created_at) VALUES (:name, :user_id, NOW())"
    db.session.execute(text(sql), {"name":name, "user_id":user_id})
    db.session.commit()
    return True
