from config import db

class Course(db.Model):

    __tablename__="courses"

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False,unique=True)
    instructor_id=db.Column(db.Integer,db.ForeignKey("instructors.user_id"))

    instructor=db.relationship("Instructor",back_populates="courses")

class User(db.Model):

    __tablename__="users"
    __table_args__=(db.CheckConstraint("age","age>=18 and age<=65",name="age_check_constraint"))

    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String,nullable=False)
    lname=db.Column(db.String,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    profile_pic=db.Column(db.String)


class Instructor(User):

    __tablename__="instructors"

    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),primary_key=True)
    tenured=db.Column(db.Boolean, default=False)

    courses=db.relationship("Course",back_populates="instructor")
