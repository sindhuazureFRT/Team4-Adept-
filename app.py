from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/Findjobs')
def Findjobs():
    return render_template('jobs.html')
@app.route('/postjobs')
def postjobs():
    return render_template('post-job.html')
@app.route('/account')
def account():
    return render_template('account.html')
@app.route('/myjobs')
def myjobs():
    return render_template('my-jobs.html')
@app.route('/jobapplied')
def jobapplied():
    return render_template('job-applied.html')
@app.route('/savedjobs')
def savedjobs():
    return render_template('saved-jobs.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/jobdetail')
def jobdetail():
    return render_template('job-detail.html')


if __name__=="__main__":
    app.run(debug=True)