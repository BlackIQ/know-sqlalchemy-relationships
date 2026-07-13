# SQLAlchemy & SQLAlchemy ORM
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, Mapped, mapped_column

# Settings
from settings import config

# Engine
engine = create_engine(config.POSTGRES_NN)


# Base Model
class Base(DeclarativeBase):
    pass


# Session & Session Maker
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = Session()


# Table: StudentCourse
class StudentCourse(Base):
    __tablename__ = "student_course"

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        primary_key=True
    )
    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        primary_key=True
    )


# Table: Student
class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )

    courses: Mapped[list["Course"]] = relationship(
        "Course", back_populates="students", secondary="student_course"
    )


# Table: Course
class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )

    students: Mapped[list["Student"]] = relationship(
        "Student", back_populates="courses", secondary="student_course"
    )


# Create tables
# Base.metadata.create_all(engine)


# ---------- INSERT ---------- #

amir = Student(name="Amirhossein")
sina = Student(name="Sina")

CCNA = Course(name="CCNA")
CCNP = Course(name="CCNP")
MTCNA = Course(name="MTCNA")
MTCRE = Course(name="MTCRE")
MTCWE = Course(name="MTCWE")

amir.courses.append(CCNA)
amir.courses.append(CCNP)

sina.courses.append(MTCNA)
sina.courses.append(MTCRE)
sina.courses.append(MTCWE)

session.add_all([
    amir, sina
])
session.commit()

# ---------- SELECT ---------- #

students = session.query(Student).all()

for student in students:
    print(f"Student: {student.name}")
    for c in student.courses:
        print(f"Course: {c.name}")

    print("")

print("------------------------------------------------------")

courses = session.query(Course).all()

for course in courses:
    print(f"Course: {course.name}")
    for s in course.students:
        print(f"Student: {s.name}")

    print("")
