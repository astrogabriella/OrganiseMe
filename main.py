from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
import get_all_tasks, add_tasks, delete_tasks, amend_tasks, search_tasks
from delete_tasks import check_id_exists
from amend_tasks import check_id_exists

dbCon = sql.connect("database/organise_me.db",check_same_thread=False)
dbCursor = dbCon.cursor()

app = Flask(__name__)



@app.route('/')
def index():
   
    return render_template('index.html')
 
@app.route('/menu')
def options():
    
    req = request.args.get("option")
    if req == "list":
        return redirect(url_for('get_tasks'))
    elif req == "add":  
        return render_template("add_task.html")
    elif req == "delete":
        return render_template("delete_task.html")
    elif req == "amend":
        return render_template("amend_task.html")
    elif req == "search":
         return redirect(url_for('search'))
    else:
        return render_template("index.html")



@app.route('/get_tasks', methods = ["POST","GET"])
def get_tasks():   
    tasks = get_all_tasks.read_tasks(dbCursor)
    return render_template("list_tasks.html", entries = tasks)

@app.route('/add_task', methods = ["POST"])
def add():
    task =request.form['task_name'].title()
    date = request.form['due_date']
    priority = request.form['priority'].title()
    status = request.form['status'].title()
    error_message = "Task added successfully"
    add_tasks.add_record(dbCursor, dbCon, task, date, priority, status)
    return render_template('add_task.html',error_message=error_message)

@app.route('/amend_task', methods = ["POST"])
def amend():
    error_message = None
    task_id = request.form['taskID']
    task =request.form['task_name'].title()
    date = request.form['due_date']
    priority = request.form['priority'].title()
    status = request.form['status'].title()

    if not check_id_exists(dbCursor,task_id):
        error_message = "Task ID does not exist."
    else:
        amend_tasks.amend_data(dbCursor, dbCon, task_id,task, date, priority, status)
        error_message = "Task updated successfully"
    return render_template("amend_task.html", error_message=error_message)

@app.route('/delete_task', methods = ["POST","GET"])
def delete():  
    error_message = None
    task_id = request.form['taskID']
    if not check_id_exists(dbCursor,task_id):
        error_message = "Task ID does not exist."
    else:
        delete_tasks.delete_data(dbCursor,task_id, dbCon)
        error_message = "Task deleted successfully"
    return render_template("delete_task.html", error_message=error_message)

@app.route('/search_task', methods = ["POST","GET"])
def search():   
    return render_template("search_task.html")
    

@app.route('/execute_search', methods = ["POST","GET"])
def search_results():   

    error_message = None
    query = request.form.get("search_query")
    res= search_tasks.find(dbCursor,query)
    if not res:
        error_message = "No records found."
        return render_template('search_task.html',error_message=error_message)
    else:
        return render_template("list_tasks.html", entries = res)


if __name__ == "__main__":
    app.run(debug=True)
    css_url = url_for('static', filename='CSS/styles.css')


