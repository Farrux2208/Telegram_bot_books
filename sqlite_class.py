import sqlite3

class Baza:
    conn = sqlite3.connect("Telegram.db")
    cur = conn.cursor()



    def baza_create(self):
        self.cur.execute(f"""create table if not exists users (
            telegram_id int,
            username varchar (50),
            phone_number varchar (20)
            ) """)


    def user_select_telegram_id(self,telegram_id):
        self.cur.execute("select * from users where telegram_id={}".format(telegram_id))
        return self.cur.fetchone()

    def user_insert(self, telegram_id,username, phon_number):
        self.cur.execute("insert into users values ({}, '{}', {})".format(telegram_id, username, phon_number))
        return self.conn.commit()



##
    def db_insert_books(self,book_name, book_discribtin):
        self.cur.execute(f"""insert into books values ('{book_name}','{book_discribtin}')""")
        conn.commit()

    def db_select_all_book(self):
        self.cur.execute("select * from books")
        return self.cur.fetchall()

    def db_select_one_book(self,book_name):
        self.cur.execute(f"select * from books where book_name='{book_name}' ")
        return self.cur.fetchone()

    def db_update_where_book(self,book_name, book_discribtin):
        self.cur.execute(f"apdate books set book_discribtin='{book_discribtin}' where book_name='{book_name}' ")

    def category_create(self):
        self.cur.execute(f"""create table if not exists category (
            id integer PRIMARY KEY AUTOINCREMENT,
            category_name varchar (250)
            ) """)

    def books_select(self):
        self.cur.execute("select * from category")
        return self.cur.fetchall()



    def books_create(self):
        self.cur.execute(f"""create table if not exists books (
            id integer PRIMARY KEY AUTOINCREMENT,
            category_id int,
            book_name varchar (250),
            book_file text,
            book_img text,
            book_dict text
            ) """)

    def books_select_by_category(self,id):
        self.cur.execute("select * from books where category_id={}".format(id))
        return self.cur.fetchall()

    def books_select_by_id(self, id):
        self.cur.execute("select * from books where id={}".format(id))
        return self.cur.fetchone()


    
    def search_book(self, bookname):
        self.cur.execute("SELECT * from books  where book_name like '{}%' ".format(bookname))
        return self.cur.fetchall()
