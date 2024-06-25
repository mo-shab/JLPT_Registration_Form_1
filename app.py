#!/usr/bin/python3
from flask import Flask, request, redirect, url_for, render_template, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import os
import csv
import plotly.express as px
import pandas as pd

app = Flask(__name__)
app.secret_key = 'This_is_not_my_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

users = {
    'shab': {'password': 'shab'}
}

# User class for Flask-Login (replace with your actual User model if using a database)
class User(UserMixin):
    pass

# Load user function for Flask-Login (replace with your actual user loading logic)
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user = User()
        user.id = user_id
        return user
    return None


temp_data = {}


jlpt_counters = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
for level in ['1', '2', '3', '4', '5']:
    file_path = f"data_N{level}.csv"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            last_row = None
            for row in reader:
                last_row = row
            if last_row is not None:
                jlpt_counters[level] = int(last_row[4])
    else:
        jlpt_counters[level] = 0


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    if request.method == 'POST':
        return redirect(url_for('registration'))
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'], strict_slashes=False)
def registration():
    if request.method == 'POST':
        temp_data['jlpt_level'] = request.form.get('jlpt_level', '')
        temp_data['test_center'] = request.form.get('test_center', '')
        temp_data['full_name'] = request.form.get('full_name', '').upper()
        temp_data['gender'] = request.form.get('gender', '')
        dob = request.form.get('dob', '')
        temp_data['dob_day'], temp_data['dob_month'], \
            temp_data['dob_year'] = dob.split('-')
        temp_data['pass_code'] = request.form.get('pass_code', '')
        temp_data['native_language'] = request.form.get('native_language', '')
        temp_data['nationality'] = request.form.get('nationality', '')
        temp_data['adress'] = request.form.get('adress', '')
        temp_data['country'] = request.form.get('country', '')
        temp_data['zip_code'] = request.form.get('zip_code', '')
        temp_data['phone_number'] = request.form.get('phone_number', '')
        temp_data['email'] = request.form.get('email', '')
        temp_data['institute'] = request.form.get('institute', '')
        temp_data['place_learn_jp'] = request.form.get('place_learn_jp', '')
        temp_data['reason_jlpt'] = request.form.get('reason_jlpt', '')
        temp_data['occupation'] = request.form.get('occupation', '')
        temp_data['occupation_details'] = request.form.get(
            'occupation_details', '')
        temp_data['media_jp'] = ''.join(choice if choice in request.form.getlist(
            'media_jp') else ' ' for choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        temp_data['communicate_teacher'] = ''.join(choice if choice in request.form.getlist(
            'communicate_teacher') else ' ' for choice in ['1', '2', '3', '4'])
        temp_data['communicate_friends'] = ''.join(choice if choice in request.form.getlist(
            'communicate_friends') else ' ' for choice in ['1', '2', '3', '4'])
        temp_data['communicate_family'] = ''.join(choice if choice in request.form.getlist(
            'communicate_family') else ' ' for choice in ['1', '2', '3', '4'])
        temp_data['communicate_supervisor'] = ''.join(choice if choice in request.form.getlist(
            'communicate_supervisor') else ' ' for choice in ['1', '2', '3', '4'])
        temp_data['communicate_colleagues'] = ''.join(choice if choice in request.form.getlist(
            'communicate_colleagues') else ' ' for choice in ['1', '2', '3', '4'])
        temp_data['communicate_CUSTOMERS'] = ''.join(choice if choice in request.form.getlist(
            'communicate_CUSTOMERS') else ' ' for choice in ['1', '2', '3', '4'])
        temp_data['jlpt_n1'] = ' ' if request.form.get(
            'jlpt_n1', '0') == '0' else request.form.get('jlpt_n1', ' ')
        temp_data['jlpt_n2'] = ' ' if request.form.get(
            'jlpt_n2', '0') == '0' else request.form.get('jlpt_n2', ' ')
        temp_data['jlpt_n3'] = ' ' if request.form.get(
            'jlpt_n3', '0') == '0' else request.form.get('jlpt_n3', ' ')
        temp_data['jlpt_n4'] = ' ' if request.form.get(
            'jlpt_n4', '0') == '0' else request.form.get('jlpt_n4', ' ')
        temp_data['jlpt_n5'] = ' ' if request.form.get(
            'jlpt_n5', '0') == '0' else request.form.get('jlpt_n5', ' ')
        temp_data['n1_result'] = request.form.get('n1_result', ' ')
        temp_data['n2_result'] = request.form.get('n2_result', ' ')
        temp_data['n3_result'] = request.form.get('n3_result', ' ')
        temp_data['n4_result'] = request.form.get('n4_result', ' ')
        temp_data['n5_result'] = request.form.get('n5_result', ' ')

        return render_template('confirm.html', form_data=temp_data)

    return render_template('registration.html')


@app.route('/confirm', methods=['POST'])
def confirm():
    jlpt_level = temp_data['jlpt_level']
    test_center = temp_data['test_center']
    full_name = temp_data['full_name']
    gender = temp_data['gender']
    dob_year = temp_data['dob_year']
    dob_month = temp_data['dob_month']
    dob_day = temp_data['dob_day']
    pass_code = temp_data['pass_code']
    native_language = temp_data['native_language']
    nationality = temp_data['nationality']
    adress = temp_data['adress']
    country = temp_data['country']
    zip_code = temp_data['zip_code']
    phone_number = temp_data['phone_number']
    email = temp_data['email']
    institute = temp_data['institute']
    place_learn_jp = temp_data['place_learn_jp']
    reason_jlpt = temp_data['reason_jlpt']
    occupation = temp_data['occupation']
    occupation_details = temp_data['occupation_details']
    media = temp_data['media_jp']
    teacher = temp_data['communicate_teacher']
    friends = temp_data['communicate_friends']
    family = temp_data['communicate_family']
    supervisor = temp_data['communicate_supervisor']
    colleagues = temp_data['communicate_colleagues']
    customers = temp_data['communicate_CUSTOMERS']
    jlpt_n1 = temp_data['jlpt_n1']
    jlpt_n2 = temp_data['jlpt_n2']
    jlpt_n3 = temp_data['jlpt_n3']
    jlpt_n4 = temp_data['jlpt_n4']
    jlpt_n5 = temp_data['jlpt_n5']
    n1_result = temp_data['n1_result']
    n2_result = temp_data['n2_result']
    n3_result = temp_data['n3_result']
    n4_result = temp_data['n4_result']
    n5_result = temp_data['n5_result']

    # Increment JLPT counter for the level
    jlpt_counters[jlpt_level] += 1

    # Process and store data as needed (e.g., write to files, send email)

    with open(f"data_N{jlpt_level}.csv", 'a') as f:
        f.write(f"\"{jlpt_level.strip()}\",\"24B\",\"8210101\",\"{jlpt_level.strip()}\",\"{str(jlpt_counters[jlpt_level]).zfill(4)}\",\"{full_name.strip()}\",\"{gender.strip()}\",\"{dob_year.strip()}\",\"{dob_month.strip()}\",\"{dob_day.strip()}\",\"{pass_code.strip()}\",\"{native_language.strip()}\",\"{place_learn_jp.strip()}\",\"{reason_jlpt.strip()}\",\"{occupation.strip()}\",\"{occupation_details.strip()}\",\"{media}\",\"{teacher}\",\"{friends}\",\"{family}\",\"{supervisor}\",\"{colleagues}\",\"{customers}\",\"{jlpt_n1}\",\"{jlpt_n2}\",\"{jlpt_n3}\",\"{jlpt_n4}\",\"{jlpt_n5}\",\"{n1_result}\",\"{n2_result}\",\"{n3_result}\",\"{n4_result}\",\"{n5_result}\"\n")

    with open(f"infos_N{jlpt_level}.csv", 'a') as f:
        f.write(f"\"{jlpt_counters[jlpt_level]}\",\"{jlpt_level}\",\"{test_center}\",\"{full_name}\",\"{gender}\",\"{dob_year}\",\"{dob_month}\",\"{dob_day}\",\"{pass_code}\",\"{native_language}\",\"{nationality}\",\"{adress}\",\"{country}\",\"{zip_code}\",\"{phone_number}\",\"{email}\",\"{institute}\"\n")

    # Function to send Email to the JLPT candidate
    # send_email(full_name, email)

    # Clear temporary data after processing
    temp_data.clear()

    # Render success page after confirmation
    return render_template('success.html')

@app.errorhandler(500)
def exception_handler(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def exception_handler(e):
    return render_template('404.html'), 404

def jlpt_stats():
    """Function that open the cvs file, read it, calcul the number of people
    who register, and who register on each level"""
    levels = ['N1', 'N2', 'N3', 'N4', 'N5']
    jlpt_count = {'N1': 0, 'N2': 0, 'N3': 0, 'N4': 0, 'N5': 0} 
    jlpt_rev = {'N1': 0, 'N2': 0, 'N3': 0, 'N4': 0, 'N5': 0}
    total = 0
    for level in levels:
        file_name = f'data_{level}.csv'
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                reader = csv.reader(f)
                last_row = None
                for row in reader:
                    last_row = row
                if last_row is not None:
                    jlpt_count[level] = int(last_row[4])
        else:
            jlpt_count[level] = 0
    for jlpt in jlpt_count:
        if jlpt == 'N1':
            jlpt_rev[jlpt] = jlpt_count[jlpt] * 450
        else:
            if jlpt == 'N2':
                jlpt_rev[jlpt] = jlpt_count[jlpt] * 400
            else:
                if jlpt == 'N3':
                    jlpt_rev[jlpt] = jlpt_count[jlpt] * 350
                else:
                    if jlpt == 'N4':
                        jlpt_rev[jlpt] = jlpt_count[jlpt] * 300
                    else:
                        if jlpt == 'N5':
                            jlpt_rev[jlpt] = jlpt_count[jlpt] * 250
                            
        total += jlpt_count[jlpt]
    
    return jlpt_count, total


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('jlpt'))  # Redirect to 'jlpt' endpoint
        else:
            error = 'Invalid username/password combination'
    return render_template('login.html', error=error)

@app.route('/logout', methods=['POST'])
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        logout_user()
        session.pop('logged_in', None)
        session.pop('username', None)
        return redirect(url_for('login'))
    
@app.route('/jlpt', methods=['GET', 'POST'])
def jlpt():
    jlpt_count, total = jlpt_stats()
    print(jlpt_count)
    print(total)
    return render_template('jlpt_data.html', total=total, jlpt_count=jlpt_count)


@app.route('/jlpt/N<level>', strict_slashes=False)
def get_data(level):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        data_file = f"data_N{level}.csv"
        infor_file = f"infos_N{level}.csv"
        data = []
        infor = []
        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    data.append(row)
        if os.path.exists(infor_file):
            with open(infor_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    infor.append(row)
        return render_template('data.html', data=data, infor=infor, level=level)
    

@app.route('/delete/<level>/<int:row_number>', methods=['POST', 'GET'], strict_slashes=False)
def delete_row(level, row_number):
    data_file = f"data_N{level}.csv"
    data_file_2 = f"infos_N{level}.csv"
    deleted_info = f"deleted_info_N{level}.csv"

    if os.path.exists(data_file) and os.path.exists(data_file_2):
        with open(data_file, 'r') as f:
            rows = list(csv.reader(f))
        
        with open(data_file_2, 'r') as f:
            rows_2 = list(csv.reader(f))

        if 0 <= row_number < len(rows):
            name = rows[row_number][5]  # Assuming name is in the 6th column
            rows.pop(row_number)
            deleted_row = rows_2.pop(row_number)

            # store the deleted row in a separate file for logging
            with open(deleted_info, 'a') as f:
                f.write(','.join(deleted_row) + '\n')
            

            # Decrement JLPT counter for remaining rows
            for i in range(row_number, len(rows)):
                rows[i][4] = f"{int(rows[i][4]) - 1:04}"  # Assuming JLPT counter is in the 5th column
                rows_2[i][0] = f"{int(rows_2[i][0]) - 1:04}"
           

            new_raws = []
            for row in rows: # Join elements of the row with commas and wrap them in double quotes
                row_string = ','.join([f'"{i}"' for i in row])
                new_raws.append(row_string)
            
            with open(data_file, 'w', newline='') as f:
                for row in new_raws:
                    f.write(row + '\n')
            
            with open(data_file_2, 'w', newline='') as f:
                for row in rows_2:
                    f.write(','.join(row) + '\n')
            
            flash(f"{name} deleted successfully!")
            return redirect(url_for('get_data', level=level))  # Return the deleted row surrounded by double quotes
        else:
            flash("Row number out of range!")
    else:
        flash("Data file not found!")
    
    return redirect(url_for('get_data', level=level))


@app.route('/base')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
