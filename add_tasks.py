def add_record(dbCursor, dbCon, task, date, priority, status):
            priority = priority.title()
            status = status.title()

            dbCursor.execute("INSERT INTO Tasks(task_name,due_date,priority,status) VALUES (?,?,?,?)", (task,date,priority,status))
            dbCon.commit()

