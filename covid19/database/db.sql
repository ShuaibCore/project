CREATE TABLE courses(
id int not null AUTO_INCREMENT,
    matric varchar(100) not null,
    passport varchar(100) not null,
    levelName varchar(50),
    semester varchar(50),
    courseCode1 varchar(50),
    courseCode2 varchar(50),
    courseCode3 varchar(50),
    courseCode4 varchar(50),
    courseCode5 varchar(50),
    courseCode6 varchar(50),
    courseCode7 varchar(50),
    courseCode8 varchar(50),
    courseCode9 varchar(50),
    courseCode10 varchar(50),
    date_time datetime(6),
    PRIMARY key(id)
)

CREATE TABLE studentInfo(
id int not null AUTO_INCREMENT,
    matric varchar(100) not null,
    surname varchar(100) not null,
    firstname varchar(100) not null,
    othername varchar(100),
    school varchar(150),
    department varchar(150),
    program varchar(150),
    date_time datetime(6),
    PRIMARY key(id)
)


create TABLE enrolledFaces(
id int not null AUTO_INCREMENT,
    matric varchar(100) not null,
    faceName varchar(100) not null,
    date_time datetime(6),
    PRIMARY key(id)
)


CREATE table passports(
id int not null AUTO_INCREMENT, PRIMARY KEY(id),
    matric varchar(100),
    filename varchar(100)
    )

    CREATE table course_registration(
    id int not null AUTO_INCREMENT, PRIMARY KEY(id),
    matric varchar(100),
    surname varchar(100),
    firstname varchar(100),
    othername varchar(100),
    program varchar(100),
    department varchar(100),
    school varchar(100),
    levelName varchar(50),
    semester varchar(50),
    sessionName varchar(50),
    courseCode varchar(50),
    courseTitle varchar(150),
    courseUnit varchar(50),
    date_time datetime (6),
    )