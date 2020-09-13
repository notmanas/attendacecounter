from django.db import models


# THIS IS TEACHER TABLE                   {.............................
class teacher(models.Model):
    name = models.CharField(max_length = 50)
    mobile_number = models.CharField(max_length = 10)
    image = models.ImageField(blank = True)
    college = models.CharField(max_length = 50)

    class Meta: 
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return (self.name)   

 #......................}   

 
 
 
 #THIS IS CLASS TABLE   {...........................................
class Class(models.Model):
    name = models.CharField(max_length = 10)
    room_number = models.CharField(max_length = 10 , unique = False)


    class Meta:
        verbose_name = "Class"
        verbose_name_plural = 'Classes'

    def __str__(self):
        return (self.name)

class theorysubject(models.Model):
    name = models.CharField(max_length = 30)
    code = models.CharField(max_length = 10)
    teacher_teaching = models.CharField(max_length = 50)
    Class = models.ForeignKey(Class , on_delete = models.CASCADE)

    def __str__(self):
        return (self.name)

class lab(models.Model):
    name = models.CharField(max_length = 30)
    teacher_teaching = models.CharField(max_length = 50)
    Class = models.ForeignKey(Class , on_delete = models.CASCADE)

    def __str__(self):
        return (self.name)


#THIS TABLE IS FOR STUDENTS WHO ARE STUDYING IN ABOVE CLASS
class student(models.Model):
    enrollment_number = models.CharField(max_length = 15 , unique = True)
    roll_number = models.IntegerField(unique = True)
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    branch = models.CharField(max_length = 30)
    dob = models.DateField()
    mobile_number = models.CharField(max_length = 10)
    Class = models.ForeignKey(Class , on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = 'students'

    def __str__(self):
        return (self.name)

 #......................} 


#THIS TABLE STORES TIMETABLE AND IS CHILD TABLE OF Class
class timetable(models.Model):
    day = models.CharField(max_length = 15)    
    lec1 = models.CharField(max_length = 50)
    lec2 = models.CharField(max_length = 50)
    lec3 = models.CharField(max_length = 50)
    lec4 = models.CharField(max_length = 50)
    lec5 = models.CharField(max_length = 50)
    lec6 = models.CharField(max_length = 50)
    lec7 = models.CharField(max_length = 50)
    Class = models.ForeignKey(Class , on_delete = models.CASCADE)
    class Meta:
        verbose_name = "Timetable"
        verbose_name_plural = 'Timetables'

    def __str__(self):
        return (self.day)

 #......................} 


class attendence(models.Model):
    date = models.CharField(max_length = 10)
    day = models.CharField(max_length = 10)
    lec1 = models.CharField(max_length = 30 , blank = True , default = 'Blank' )
    lec2 = models.CharField(max_length = 30 , blank = True , default = 'Blank' )
    lec3 = models.CharField(max_length = 30 , blank = True , default = 'Blank' )
    lec4 = models.CharField(max_length = 30 , blank = True , default = 'Blank' )
    lec5 = models.CharField(max_length = 30 , blank = True , default = 'Blank' )
    lec6 = models.CharField(max_length = 30 , blank = True , default = 'Blank' )
    lec7 = models.CharField(max_length = 30 , blank = True , default = 'Blank' )
    student = models.ForeignKey(student , on_delete = models.CASCADE)
    Class = models.ForeignKey(Class , on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Attendence Table"
        verbose_name_plural = 'Attendence Tables'

    def __str__(self):
        return (self.date)