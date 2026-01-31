import sqlite3

def create_database():
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()

   
    cur.execute('''CREATE TABLE IF NOT EXISTS movie (
                    mname TEXT,
                    mrelease TEXT,
                    cost INTEGER,
                    hero TEXT,
                    profit INTEGER
                )''')

   
    conn.close()

def add_movie():
    
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()

    mname = input("Enter the name of the movie: ")
    mrelease = input("Enter the release date of the movie: ")
    cost = int(input("Enter the budget of the movie: "))
    hero = input("Enter the hero of the movie: ")
    profit = int(input("Enter the earning of the movie: "))

    cur.execute("INSERT INTO movie (mname, mrelease, cost, hero, profit) VALUES (?, ?, ?, ?, ?)", (mname, mrelease, cost, hero, profit))

    
    conn.commit()
    conn.close()

def display_movies():
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie ORDER BY profit DESC")
    movies = cur.fetchall()
    for movie in movies:
        print(movie)

    conn.close()

def main():
    create_database()
    add_movie()
    display_movies()

if __name__ == "__main__":
    main()
