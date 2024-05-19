import oracledb
import os
from dotenv import dotenv_values

def connect():
    config = dotenv_values("config/.env")
    
    dsn_str = oracledb.makedsn(
        config.get("DB_HOST"),
        config.get("DB_PORT"),
        config.get("DB_SID"),
    )
    try:
        conn = oracledb.connect(
            user=config.get("DB_USER"),
            password=config.get("DB_PASSWORD"),
            dsn=dsn_str,
        )
        
        return True, conn.cursor(), conn
    except Exception as e:
        print(e)
    
    return False, None, None


def select(db_inst, table_name, fields, where=None):
    query = f"SELECT {fields} FROM {table_name}"
    
    if where:
        query += f" WHERE {where}"
    
    db_inst.execute(query)
    return db_inst.fetchall()

def insert(conn, db_inst, table_name, fields, values):
    query = f"INSERT INTO {table_name} ({fields}) VALUES ({values})"
    db_inst.execute(query)
    conn.commit()

    return db_inst

def update(conn, db_inst, table_name, fields_to_update, where):
    fields = ", ".join([f"{key} = '{value}'" for key, value in fields_to_update.items()])
    query = f"UPDATE {table_name} SET {fields} WHERE {where}"
    db_inst.execute(query)
    conn.commit()

    return db_inst

def delete(conn, db_inst, table_name, where):
    query = f"DELETE FROM {table_name} WHERE {where}"
    db_inst.execute(query)
    conn.commit()

    return db_inst