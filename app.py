#!/usr/bin/python3
from flask import Flask, request, redirect, url_for, render_template
import os
import csv

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
