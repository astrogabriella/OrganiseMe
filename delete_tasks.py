
def check_id_exists(task_id, dbCursor):
    dbCursor.execute("SELECT task_id FROM Tasks WHERE task_id = ?", (task_id,))
    result = dbCursor.fetchone()
    return result is not None


def delete_data(dbCursor, task_id, dbCon):
    dbCursor.execute("DELETE FROM Tasks WHERE task_id = ?", (task_id,))
    dbCon.commit()

