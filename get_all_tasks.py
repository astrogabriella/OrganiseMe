def read_tasks(dbCursor):
    dbCursor.execute("SELECT * FROM Tasks")
    taskRecords = dbCursor.fetchall()
    return taskRecords    
    
