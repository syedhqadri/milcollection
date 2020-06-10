from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     # with open('database.csv', mode='a') as database:
#     with open('database.txt', mode='a') as database:
#         first_name = data["firstname"]
#         last_name = data["lastname"]
#         email = data["email"]
#         contact_num = data["telephone"]
#         dob = data["dob"]
#         gender = data["gender"]
#         days_of_week = data["availability"]
#         num_of_desired_hours = data["hours"]
#         # csv_writer = csv.writer(database, delimiter=',', quotechar='',quoting=csv.QUOTE_MINIMAL)
#         # csv_writer.writerow([first_name,last_name,email,contact_num,dob,gender,days_of_week,num_of_desired_hours])
#         file = database.write(f'\n{first_name},{last_name},{email},{contact_num},{dob},{gender},{days_of_week},{num_of_desired_hours}')

def write_to_csv(data):
    with open('job_applications.csv', mode='a') as database:

        first_name = data["firstname"]
        last_name = data["lastname"]
        email = data["email"]
        contact_num = data["telephone"]
        dob = data["dob"]
        gender = data["gender"]
        days_of_week = data["availability"]
        num_of_desired_hours = data["hours"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([first_name,last_name,email,contact_num,dob,gender,days_of_week,num_of_desired_hours])

@app.route('/submit_application', methods=['POST','GET'])
def submit_application():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou_apply.html')
        except:
            return redirect('/tryagain.html')
    else:
        return 'Something went wrong. Try again!'


def write_to_csv2(data2):
    with open('messages.csv', mode='a') as database2:

        name = data2["name"]
        email = data2["email"]
        message = data2["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_message', methods=['POST','GET'])
def submit_message():

    if request.method == 'POST':
        try:
            data2 = request.form.to_dict()
            write_to_csv2(data2)
            return redirect('/thankyou_message.html')
        except:
            return redirect('/tryagain.html')
    else:
        return 'Something went wrong. Try again!'
