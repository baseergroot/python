import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    author_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(author_id) REFERENCES users(id)
)
""")

conn.commit()

current_user = None
def register():
    global current_user 
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password == confirm_password:

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            user = cursor.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
            current_user = {
                "id": user[0],
                "username": username,
            }
            print(f"Registration successful; {current_user}")

        except sqlite3.IntegrityError:
            print("Username already exists")

        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Passwords do not match")


def login():
    global current_user 
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    if user:
        current_user = {
                "id": user[0],
                "username": username,
            }
        print(f"Login successful", current_user)
    else:
        print("Invalid username or password")
    
def create_post():
    global current_user
    title = input("Enter title: ")
    content = input("Enter content: ")
    
    cursor.execute("INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)", (title, content, current_user["id"]))
    conn.commit()

    posts = cursor.execute("SELECT * FROM posts WHERE author_id = ?", (current_user["id"],)).fetchall()

    print("Post created successfully")

def  list_posts():
    global current_user
    posts = cursor.execute("SELECT * FROM posts WHERE author_id = ?", (current_user["id"],)).fetchall()
    # print(posts)
    print()
    for post in posts:
        print(f"Post Number: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Content: {post[2]}")
        print(f"Created at: {post[4]}")
        print()


while True:
    if not current_user:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
    else:
        print("1. Create Post")
        print("2. List Posts")
        print("3. Logout")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_post()
        elif choice == "2":
            list_posts()
        elif choice == "3":
            current_user = None
        elif choice == "4":
            break
