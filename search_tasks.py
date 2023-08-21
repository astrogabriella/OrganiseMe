
def find(dbCursor, query):
    query = f"%{query}%"
    dbCursor.execute("SELECT * FROM Tasks WHERE LOWER(task_name) LIKE LOWER(?) OR due_date LIKE LOWER(?) OR LOWER(priority) LIKE LOWER(?) OR LOWER(status) LIKE LOWER(?)", (query, query, query, query))

    taskRecords = dbCursor.fetchall()
    print(taskRecords)
    return taskRecords
