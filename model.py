from config import get_db_connection

def create_user(username, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()

def get_user(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    conn.close()
    return user

def create_order(user_id, item):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (user_id, item) VALUES (%s, %s)", (user_id, item))
    conn.commit()
    conn.close()

def list_orders(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders WHERE user_id=%s", (user_id,))
    orders = cur.fetchall()
    conn.close()
    return orders

def save_message(user_id, message):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (user_id, message) VALUES (%s, %s)", (user_id, message))
    conn.commit()
    conn.close()
