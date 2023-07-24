from config import app,db
from models import Course,User,Instructor


@app.route("/courses")
def courses():
    all=Course.query.all()
    courses=[]
    for course in all:
        courses.append(course.to_dict(rules=("-instructor",)))
        # instructor_to_dict={
        #     "fname":course.instructor.fname,
        #     "lname":course.instructor.lname,
        #     "age":course.instructor.age,
        #     "profile_pic":course.instructor.profile_pic
        # }
        # course_to_dict={
        #    "title":course.title,
        #    "instructor":instructor_to_dict
        # }
        # courses.append(course_to_dict)
    return courses
    # response="<h1>Our Courses</h1>"
    # for course in all:
    #     response+="<div>"
    #     response+=f"<p>{course.title}</p>"
    #     response+=f"<p>Instructor: {course.instructor.fname}</p>"
    #     response+="</div>"
    # return response

@app.route("/courses/<int:id>")
def course_by_id(id):
    course=Course.query.filter(Course.id==id).first()
    if course==None:
        return {}, 404
    return course.to_dict()

@app.route("/instructors")
def instructors():
    all=Instructor.query.all()
    instructors=[]
    for instructor in all:
        instructors.append(instructor.to_dict())
        # instructor_to_dict={
        #     "fname":instructor.fname,
        #     "lname":instructor.lname,
        #     "age":instructor.age,
        #     "profile_pic":instructor.profile_pic
        # }
        #instructors.append(instructor_to_dict)
    return instructors
    # response="<h1>Our Users</h1>"
    # for user in users:
    #     response+="<div>"
    #     response+=f"<p>{user.fname}"
    #     response+=f"<div><img src='{user.profile_pic}' width=200 height=200></div>"
    #     response+="</div>"
    # return response