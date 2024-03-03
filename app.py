import sqlite3
from flask import Flask,url_for, render_template,flash,session,request,redirect

app=Flask(__name__)
app.secret_key="123"

sqlconnection =sqlite3.connect("adept.db")
#sqlconnection.execute("create table if not exists signin(id integer primary key,Name text, Email text,Password integer,Comfirm integer,cname text,cemail text,cmnumber integer,csubject text,cmessage text)")
sqlconnection.execute("create table if not exists user(Name text,Email text,Password text,Confirm text)")
sqlconnection.execute("create table if not exists apply(firstname text,lastname text,email text,mobile text,city text,jobrole text,pincode text,date text)")
sqlconnection.execute("CREATE TABLE if not exists jobs(title text,category text,jobnature text,vacancy text,salary text,location text,description text,qualifications text,keywords text,name text, companylocation tect,website text)")

sqlconnection.close()

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))
@app.route('/')
def home():
    if 'email' in session:
        sqlconnection = sqlite3.connect('adept.db')
        cur = sqlconnection.cursor()
        cur.execute("""select * from jobs""")
        sqlconnection.commit()
        find = cur.fetchall()
        sqlconnection.close()
        return render_template('index.html', findjobs=find, email=session['email'], password=session['psswd'])
    sqlconnection = sqlite3.connect('adept.db')
    cur = sqlconnection.cursor()
    cur.execute("""select * from jobs""")
    sqlconnection.commit()
    find=cur.fetchall()
    return render_template('index.html',findjobs=find)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register',methods=["GET","POST"])
def register():
    if request.method =="POST":
        try:
            name=request.form['Name']
            mail=request.form['Email'] 
            psswd=request.form['Password']
            confirm=request.form['Confirm']
            sqlconnection=sqlite3.connect('adept.db')
            cur=sqlconnection.cursor()
            cur.execute("insert into user(Name,Email,Password,Confirm)values(?,?,?,?)",(name,mail,psswd,confirm))
            sqlconnection.commit()
            flash("Record added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:   
           return redirect('/login')
           sqlconnection.close()
    return render_template("register.html")
@app.route('/log',methods =["GET","POST"])
def log():
    if 'email' in session:
        return redirect(url_for('home'))
    if request.method =="POST":
        email=request.form['email']
        psswd=request.form['password']
        sqlconnection= sqlite3.connect('adept.db')
        sqlconnection.row_factory=sqlite3.Row
        cur=sqlconnection.cursor()
        
        cur.execute("select * from user where Email =? and Password =?",(email,psswd))
        data=cur.fetchone()
        if (data):
          session['email']=data["email"] 
          session['psswd']=data["password"] 
          flash("Welcome to  ","logged")
          return redirect("/")
        else:
            flash("Invalid Username and Password","danger")
            return redirect('/login')
    return redirect('/')


@app.route('/Findjobs')
def Findjobs():
    sqlconnection = sqlite3.connect('adept.db')
    cur = sqlconnection.cursor()
    cur.execute("""select * from jobs""")
    sqlconnection.commit()
    find=cur.fetchall()
    return render_template('jobs.html',findjobs=find)
@app.route('/postjobs', methods=["GET", "POST"])
def postjobs():
    if request.method =="POST":
        try:
            Title=request.form['title']
            Category=request.form['category'] 
            Jobnature=request.form['jobnature']
            Vacancy=request.form['vacancy']
            Salary=request.form['salary']
            Location=request.form['location']
            Discription=request.form['description']
            Qualifications=request.form['qualifications']
            Keywords=request.form['keywords']
            Name=request.form['name']
            Companylocation=request.form['companylocation']
            Website=request.form['website']
            sqlconnection = sqlite3.connect('adept.db')
            cur = sqlconnection.cursor()
            cur.execute("INSERT INTO jobs(title, category, jobnature, vacancy, salary, location, description, qualifications, keywords, name, companylocation, website) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(Title, Category, Jobnature, Vacancy, Salary, Location, Discription, Qualifications, Keywords, Name, Companylocation, Website))
            sqlconnection.commit()
            flash("Record added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
           return redirect('/postjobs')
           sqlconnection.close()
    return render_template("post-job.html")

@app.route('/jobapply',methods=["GET", "POST"])
def jobapply():
    if request.method == "POST":
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            mobile = request.form['mobile']
            city = request.form['city']
            jobrole = request.form['jobrole']
            pincode = request.form['pincode']
            date = request.form['date']
           

            sqlconnection = sqlite3.connect('adept.db')
            cur = sqlconnection.cursor()
            cur.execute("INSERT INTO apply(firstname, lastname, email, mobile, city, jobrole, pincode,  date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (firstname, lastname, email, mobile, city, jobrole, pincode,  date))
            sqlconnection.commit()
            flash("Record added Successfully", "success")
        except Exception as e:
            flash(f"Error in Insert Operation: {str(e)}", "danger")
        finally:
            sqlconnection.close()
            return redirect('/')

    return render_template("job-apply.html")
    
@app.route('/applications')
def applications():
    sqlconnection = sqlite3.connect('adept.db')
    cur = sqlconnection.cursor()
    cur.execute("""select * from apply""")
    sqlconnection.commit()
    applys=cur.fetchall()
    return render_template("application.html",application=applys)
@app.route('/govtblob')
def govtblob():
    return render_template("blob.html")
@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")
@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")
@app.route('/jobapplied')
def jobapplied():
    return render_template('job-applied.html')
@app.route('/mail')
def mail():
    return render_template('mail.html')
@app.route('/savedjobs')
def savedjobs():
    return render_template('saved-jobs.html')
@app.route('/jobdetail')
def jobdetail():
    sqlconnection = sqlite3.connect('adept.db')
    cur = sqlconnection.cursor()
    cur.execute("""select * from jobs""")
    sqlconnection.commit()
    find=cur.fetchall()
    return render_template('job-detail.html',findjobs=find)
    return render_template('job-detail.html')


if __name__=="__main__":
    app.run(debug=True)