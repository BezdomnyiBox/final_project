import sqlite3

def get_db_connection():
        conn = sqlite3.connect("furniture_company.sqlite")
        return conn

def init_db():
        conn = get_db_connection()
        # открываем файл с дампом базой двнных
        f_damp = open('furniture.db','r', encoding ='utf-8')
        # читаем данные из файла
        damp = f_damp.read()
        # закрываем файл с дампом
        f_damp.close()
        # запускаем запросы
        conn.executescript(damp)
        # сохраняем информацию в базе данных
        conn.commit()
        conn.close()
    
def close_db_connection(conn):
        conn.close()
        



