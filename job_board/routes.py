from flask import render_template, url_for, flash, redirect, flash
from job_board import app
from job_board.forms import RegistrationForm, LoginForm
# from job_board.models import User

adverts = [
    {
        'recruiter': 'GeoPro',
        'vacancy': 'Data Engineer',
        'job_type': 'Full time',
        'description': 'Twiga is a B2B e-commerce company that builds fair and reliable markets for agricultural producers, food manufacturers and retailers based on transparency and efficiency. Our Mission is to build a closed ecosystem for the African retail, anchored on affordable access to food and grocery across urban cities. Our Ambition is to leverage technology, the ubiquity of mobile phones, modern distribution and logistics to modernize African retail.',
        'key_responsibilities': 'Develop data collection toolkits using e.g., PowerApps or Flutter.\nCreate a data lake for the business.\nTroubleshoot data-related technical issues and support data infrastructure needs.\nDevelop BI technical documentation; data dictionaries, data flows, database schemas, data model diagrams, Entity Relationship Diagrams (ERDs), etc.\nCreate data back-ups.',
        'minimum_qualifications_and_requirements': 'Experience in writing complex queries especially Big Query\nSolid knowledge of Python, SQL, and scripting\nProficiency in Power BI and Data Studio\nFamiliarity with PowerApps and/or Flutter\nOpen to change and flexible in a fast-paced environment, effectively adapts own approach to suit changing circumstances or requirements\nExperience working in an Agile/Scrum development process\nTime management skills',
        'deadline': '18/10/2024',
        'date_posted': '02/10/2024',
        'number_of_vacancies': '4',
        'location': 'Nairobi, Kenya',
        'category': 'Tech'
    },
    {
        'recruiter': 'Safaricom',
        'vacancy': 'Data Engineer',
        'job_type': 'Contract',
        'description': 'Safaricom is a B2B e-commerce company that builds fair and reliable markets for agricultural producers, food manufacturers and retailers based on transparency and efficiency. Our Mission is to build a closed ecosystem for the African retail, anchored on affordable access to food and grocery across urban cities. Our Ambition is to leverage technology, the ubiquity of mobile phones, modern distribution and logistics to modernize African retail.',
        'key_responsibilities': 'Develop data collection toolkits using e.g., PowerApps or Flutter.\nCreate a data lake for the business.\nTroubleshoot data-related technical issues and support data infrastructure needs.\nDevelop BI technical documentation; data dictionaries, data flows, database schemas, data model diagrams, Entity Relationship Diagrams (ERDs), etc.\nCreate data back-ups.',
        'minimum_qualifications_and_requirements': 'Experience in writing complex queries especially Big Query\nSolid knowledge of Python, SQL, and scripting\nProficiency in Power BI and Data Studio\nFamiliarity with PowerApps and/or Flutter\nOpen to change and flexible in a fast-paced environment, effectively adapts own approach to suit changing circumstances or requirements\nExperience working in an Agile/Scrum development process\nTime management skills',
        'deadline': '19/11/2024',
        'date_posted': '20/10/2024',
        'number_of_vacancies': '5',
        'location': 'Kitale, Kenya',
        'category': 'Tech'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', adverts=adverts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@post.com' and form.password.data == 'password':
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', title='Login', form=form)