from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/postjobs', methods=["GET", "POST"])
def postjobs():
    if request.method == "POST":
        try:
            title = request.form['title']
            category = request.form['category']
            jobnature = request.form['jobnature']
            vacancy = request.form['vacancy']
            salary = request.form['salary']
            Location = request.form['Location']
            description = request.form['description']
            qualifications = request.form['qualifications']
            keywords = request.form['keywords']
            company_name = request.form['company_name']
            company_location = request.form['company_location']
            website = request.form['website']

            # Establish a connection to the SQLite database
            sqlconnection = sqlite3.connect('adept.db')
            cur = sqlconnection.cursor()

            # Execute the SQL INSERT query
            cur.execute("""
                INSERT INTO user (title, category, jobnature, vacancy, salary, Location, description, qualifications, keywords, company_name, company_location, website)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (title, category, jobnature, vacancy, salary, Location, description, qualifications, keywords, company_name, company_location, website))

            # Commit the changes to the database
            sqlconnection.commit()

            flash("Record added Successfully", "success")
        except Exception as e:
            flash(f"Error in Insert Operation: {str(e)}", "danger")
        finally:
            # Close the database connection
            sqlconnection.close()
            return redirect('/login')

    # Handle the GET request, you might want to render a template or perform other actions
    # ...

if __name__ == '__main__':
    app.run(debug=True)
