from flask import (Blueprint, render_template, redirect)
import os
import sqlite3
from datetime import datetime
from .forms import AppointmentForm

bp = Blueprint('main', __name__, '/')
DB_FILE = os.environ.get("DB_FILE")

def convert_date(data):
  id = data[0]
  name = data[1]
  start_datetime = datetime.strptime(data[2], '%Y-%m-%d %H:%M:%S')
  end_datetime = datetime.strptime(data[3], '%Y-%m-%d %H:%M:%S')
  return (id, name, start_datetime, end_datetime)


@bp.route("/", methods=['GET', 'POST'])
def main():
  form = AppointmentForm()
  if form.validate_on_submit():
    with sqlite3.connect(DB_FILE) as conn:
      curs = conn.cursor()
      #print(form.private.data)
      params = {
        'name': form.name.data,
        'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
        'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
        'description': form.description.data,
        'private': form.private.data
      }
      #print(params)
      sql_command = f"""INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
      VALUES (
      '{params['name']}',
      '{params['start_datetime']}',
      '{params['end_datetime']}',
      '{params['description']}',
      {str(params['private']).lower()});"""
      print(sql_command)
      curs.execute(sql_command)
      return redirect('/')
  with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    sql_command = f"""SELECT id, name, start_datetime, end_datetime
    FROM appointments
    ORDER BY start_datetime;"""
    curs.execute(sql_command)
    rows = curs.fetchall()
    rows = list(map(convert_date, rows))
    #print(rows)
    return render_template('main.html', rows=rows, form=form)