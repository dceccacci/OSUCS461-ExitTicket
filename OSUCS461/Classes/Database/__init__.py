from OSUCS461.Config import MySQL as DatabaseConfig
from OSUCS461.ThirdParty.MySQL import MySQL
from OSUCS461.Models import UserCreate, UserPostCreate

# ---- For testing ----
import sys
import sys

# Function to log an error message to standard error
def log_error(message):
    print(f"ERROR: {message}", file=sys.stderr)

log_error(os.environ.get("DB_HOST"))
log_error(int(os.environ.get("DB_PORT")))
# ---------------------

DB = MySQL(**DatabaseConfig)

def create_user(user: UserCreate):
    query = f"INSERT INTO user (uuid, name, time_created) VALUES ('{user.uuid}', '{user.name}', {user.time_created})"
    DB.query(query)

def create_user_post(user_post: UserPostCreate):
    query = f"INSERT INTO user_post (uuid, user_uuid, post_9char, text, time_created) VALUES ('{user_post.uuid}', '{user_post.user_uuid}', '{user_post.post_9char}', '{user_post.text}', {user_post.time_created})"
    DB.query(query)
    
def get_user(user_uuid: str):
    query = f"SELECT uuid, name, time_created FROM user WHERE uuid = '{user_uuid}'"
    result = DB.get_row(query)
    return result

def get_user_posts(user_uuid: str):
    query = f"SELECT uuid, user_uuid, post_9char, text, time_created FROM user_post WHERE user_uuid = '{user_uuid}'"
    results = DB.get_results(query)
    return results