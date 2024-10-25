from datetime import datetime, timezone
from job_board import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship('Role', backref='user_role', lazy=True)
    organisation = db.Column(db.String(60), nullable=True, unique=False)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Role({self.id} - {self.role_name})"
    
class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    applicant_name = db.Column(db.String(30), nullable=False)
    applicant_email = db.Column(db.String(60), nullable=False)
    applicant_resume = db.Column(db.String(20), nullable=False)
    other_attachments = db.Column(db.String(20), nullable=True)
    application_dt = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"Application('{self.applicant_name}' - '{self.application_dt}')"
    
class Advert(db.Model):
    __tablename__ = 'adverts'

    id = db.Column(db.Integer, primary_key=True)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recruiter = db.relationship('User', backref='advert_recruiter', lazy=True)
    number_of_vacancies = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(40), nullable=False)
    job_type = db.Column(db.String(10), nullable=False)
    town = db.Column(db.String(40), nullable=True)
    country = db.Column(db.String(40), nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    category = db.relationship('JobCategory', backref='job_category', lazy=True)
    deadline = db.Column(db.DateTime, nullable=False)
    posted_dt = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"Advert('{self.position}' at '{self.recruiter}' before '{self.deadline}')"
    
class JobCategory(db.Model):
    __tablename__ = 'job_categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"JobCategory('{self.id}' - '{self.category_name}')"


