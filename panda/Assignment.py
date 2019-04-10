from flask import Flask, render_template, request, url_for, redirect, session
from flask_mail import Mail, Message
import pymysql
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'any random string'

mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pandaericassignment@gmail.com'
app.config['MAIL_PASSWORD'] = 'Assignment123456'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/',methods = ['POST', 'GET'])
def main():
   return render_template('main.html')

@app.route('/registor_page',methods = ['POST', 'GET'])
def registor():
   if "Userid" in session:
      return redirect(url_for("profile"))
   else:
      return render_template('registor.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      
      FN = request.form["FirstN"]
      LN = request.form["LastN"]
      Gender = request.form["Gender"]
      Phone = request.form["Phone"]
      Email = request.form["Email"]
      username = request.form["username"]
      password = request.form["password"]
      

      email_list=[]
      email_count=0
      phone_list=[]
      phone_count=0
      usrn_list=[]
      usrn_count=0

      email_mail=[]
      email_mail.append(Email)



      db_check= pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
      with db_check.cursor() as cursor:
         cursor.execute( """SELECT COUNT(Email) from customer Where Email = '"""+str(Email)+"""'""")
         email_list=(cursor.fetchall())
         cursor.execute( """SELECT COUNT(Phone) from customer Where Phone = '"""+str(Phone)+"""'""")
         phone_list=(cursor.fetchall())
         cursor.execute( """SELECT COUNT(username) from customer Where username = '"""+str(username)+"""'""")
         usrn_list=(cursor.fetchall())

      db_check.close()
      for row in email_list:
         email_count+=(int(row[0]))

      for row in phone_list:
         phone_count+=(int(row[0]))

      for row in usrn_list:
         usrn_count+=(int(row[0]))
      
      if (email_count==0) and (phone_count==0) and (usrn_count==0):


         db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")

         cursor = db.cursor() 

         x= str(FN)
         
         sql = """INSERT INTO customer (FirstN, LastN, Gender, Phone, Email, username, password, comming_date, upcomming_booking) VALUES ('%s','%s','%s',%d,'%s','%s','%s','11-11-2011','NA')"""\
         %(str(FN),str(LN),str(Gender),int(Phone),str(Email),str(username),str(password))
         try:
            cursor.execute(sql)
            db.commit()
            
         except:

            db.rollback() 

            return redirect(url_for("login"))
         db.close()
         msg = Message('Welcome to become a member of us!', sender = 'Pandaericassignment@gmail.com', recipients = email_mail[0].split())
         msg.html = render_template("register_mail.html",fir_nam=str(FN), las_nam=str(LN), sex_choice=str(Gender), email_address=str(Email), phone_no=str(Phone), usrn=str(username))
   
         mail.send(msg)
         return redirect(url_for("login"))

      elif email_count!=0:
         return render_template("registor_error.html", fir_nam=str(FN), las_nam=str(LN), sex_choice=str(Gender), email_address=str(Email), phone_no=str(Phone), usrn=str(username),uspw=password, error_email="This email has been registered" )
      elif phone_count!=0:
         return render_template("registor_error.html", fir_nam=str(FN), las_nam=str(LN), sex_choice=str(Gender), email_address=str(Email), phone_no=str(Phone), usrn=str(username),uspw=password, error_phone="This phone number has been registered" )
      elif usrn_count!=0:
         return render_template("registor_error.html", fir_nam=str(FN), las_nam=str(LN), sex_choice=str(Gender), email_address=str(Email), phone_no=str(Phone), usrn=str(username),uspw=password, error_usrn="This username has been registered" )

@app.route('/login_page',methods = ['POST', 'GET'])
def login_page():
   if "Userid" in session:
      return redirect(url_for("profile"))
   else:
      return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():

      if request.method == 'POST':

      
         login = request.form
         usrn = request.form["un_login"]
         uspw = request.form["pw_login"]
      
         db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
         with db.cursor() as cursor:
            found=False
            a = """SELECT password from customer WHERE username='""" + usrn+"""'"""
            cursor.execute(a)
            x=(cursor.fetchall())
            len_x =len(str(x))
            y= str(x)
            cursor.execute("""SELECT Phone from customer WHERE username='""" + usrn+"""'""")
            cusid_db=(cursor.fetchall()[0])

         if uspw ==  y[3:len_x-5] and ((y[3:len_x-5])!= ""):
            str_cusid_db = str(cusid_db)
            len_cusid_db = len(str(cusid_db))
            session["Userid"] = str_cusid_db[1:len_cusid_db-2]
            return redirect(url_for("profile"))
         else:
            return render_template("log_in.html",incorrect = "Incorrect username or password")
         db.close()

@app.route('/profile',methods = ['POST', 'GET'])
def profile():
   if "Userid" in session:
      userid = session["Userid"]
      db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
      with db.cursor() as cursor:
         cursor.execute( """SELECT * from customer Where Phone = '"""+userid+"""'""")
         personal_detail=(cursor.fetchall())
      db.close()
      try:  
         return render_template("profile.html",personal_detail = personal_detail)
      except:
         return render_template("profile.html",personal_detail = personal_detail)
   else:
      return redirect(url_for("login_page"))
      
@app.route('/logout')
def logout():
   session.pop('Userid', None)
   return redirect(url_for('login_page'))

@app.route('/house',methods = ['POST', 'GET'])
def house():
   
   db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
   with db.cursor() as cursor:
      cursor.execute( """SELECT * from house""")
      house_list=(cursor.fetchall())
     
      return render_template("house.html",house_list =house_list)
   db.close()

   houseid = request.form["pid"]
   date = request.form["book"]
   now = datetime.datetime.now()
   today = now.strftime("%Y-%m-%d")
   if date <= today:
      return render_template("house.html",error ="Please pick a date start from today")
   elif date > today:
      userid = session["Userid"]
      db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
      with db.cursor() as cursor:
         cursor.execute("""UPDATE customer SET comming_date = '%s', upcomming_booking = '%s' WHERE Phone = %d""")\
         %(str(date),str(pid),int(userid))
         db.commit()
      
      db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
      with db.cursor() as cursor:
         cursor.execute( """SELECT * from customer Where Phone = '"""+userid+"""'""")
         personal_detail=(cursor.fetchall())
      db.close()

      return render_template("profile.html",personal_detail = personal_detail)
   else:
      return redirect(url_for('login'))
   db.close()

@app.route('/admin',methods = ['POST', 'GET'])
def adminlogin():
   return render_template('admin.html')

@app.route('/staff_login',methods = ['POST', 'GET'])
def sflogin():

      if request.method == 'POST':
         sfn = request.form["username"]
         sfpw = request.form["password"]
      
         db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
         with db.cursor() as cursor:
            found=False
            a = """SELECT sfusername, sfpassword from admin """
            cursor.execute(a)
            staffu.append(row[0])
            staffp.append(row[1])
            x = len(staffu)
            
            flag = 0

            while x == 0:
               if str(sfn) ==  str(staffu[x]) and str(sfpw) == str(staffp[x]):
                  flag = 1
                  x = 0
               else:
                  x = x - 1


         if flag == 1:
            
            return redirect(url_for("sfmain"))
         else:
            return render_template("admin.html",incorrect = "Incorrect username or password")
         db.close()

@app.route('/sfmain',methods = ['POST', 'GET'])
def sfmain():
   return render_template('sfmain.html')

@app.route('/sfcustomer',methods = ['POST', 'GET'])
def sfcustomer():
   return render_template('admin_customer.html')

@app.route('/sfcustomer_page',methods = ['POST', 'GET'])
def sfcustomer_page():

   db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
   with db.cursor() as cursor:
      cursor.execute( """SELECT * from customer""")
      customer_list=cursor.fetchall()
   db.close()

   return render_template('admin_customer.html', result = customer_list)

@app.route('/sfhouse',methods = ['POST', 'GET'])
def sfhouse():
   return render_template('admin_house.html')

@app.route('/sfhouse1',methods = ['POST', 'GET'])
def sfhouse1():
   db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
   with db.cursor() as cursor:
      cursor.execute( """SELECT * from house""")
      house_list=cursor.fetchall()
   return render_template('admin_house.html', result = house_list)

@app.route('/sfhouse_page',methods = ['POST', 'GET'])
def sfhouse_page():
   db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
   
   if request.method == 'POST':
         houseid = request.form["houseid"]
         Avaliable = request.form["Avaliable"]
         brno = request.form["brno"]
         csnb = request.form["csnb"]
         wrno = request.form["wrno"]
         bkno = request.form["bkno"]

         db = pymysql.connect("localhost", "pmauser", "123456aaa", "assignment")
         cursor = db.cursor() 

         sql = """INSERT INTO house(house_id, avaliable, bedroom, common_spaces, washroom, booking_no) VALUES ('%s', '%s', %d, %d, %d, %d)"""\
            %(str(houseid), str(Avaliable), int(brno), int(csnb), int(wrno), int(bkno))
            
         try:
            cursor.execute(sql)
            db.commit()

         except:

            db.rollback() 

            return redirect(url_for("sfhouse"))
         db.close()
 


if __name__ == '__main__':
   app.run(debug = True)

