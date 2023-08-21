
def check_id_exists(dbCursor,task_id):
    dbCursor.execute("SELECT * FROM Tasks WHERE task_id = ?", (task_id,))
    result = dbCursor.fetchone()
    return result is not None

def amend_data(dbCursor, dbCon, task_id,task, date, priority, status):
    update_query = """
    UPDATE Tasks
    SET task_name = ?, due_date = ?, priority = ?, status = ?
    WHERE task_id = ?
    """
    dbCursor.execute(update_query, (task, date, priority, status, task_id))
    dbCon.commit()

