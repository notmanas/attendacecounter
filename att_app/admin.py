from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import teacher 
from .models import Class , student , attendence , theorysubject , lab
from .models import timetable


# Teacher {.............
class teacherAdmin(admin.ModelAdmin):
    fields = (('name','mobile_number'),('image','college'),)

#..............}


# Class , Student and Timetable  {.............

class timetableTabularInline(admin.TabularInline):
    model = timetable
    extra = 0

class studentTabularInline(admin.TabularInline):
    model = student
    extra = 0

class theorysubjectInline(admin.TabularInline):
    model = theorysubject
    extra = 0

class labInline(admin.TabularInline):
    model = lab
    extra = 0    

class ClassAdmin(admin.ModelAdmin):
    fields = (('name','room_number'),)
    inlines = [studentTabularInline , timetableTabularInline, theorysubjectInline, labInline]

class studentAdmin(admin.ModelAdmin):
    #This will display all the fields which are in one tuple in one row if possible
    list_display = ('enrollment_number','branch','name','roll_number',)

class timetableAdmin(admin.ModelAdmin):
    fields = (('day','lec1','lec2','lec3','lec4','lec5','lec6','lec7'))

class theorysubjectAdmin(admin.ModelAdmin):
    list_display = ('name' , 'Class')
    fields = (('name','code','teacher_teaching',),)

class labAdmin(admin.ModelAdmin):
    list_display = ('name' , 'Class')
    fields = (('name','teacher_teaching',),)    

#..............}

# Student and Attendence {...........
class attendenceTabularInline(admin.TabularInline):
    model = attendence
    extra = 0


class studentAdmin(admin.ModelAdmin): 
    inlines = [attendenceTabularInline,]
    search_fields = ('enrollment_number',)
    list_display = ('enrollment_number','branch','name','roll_number',)

class attendenceAdmin(admin.ModelAdmin):

    search_fields = ('date',)
    list_display = ('date','day','Class','student')
    fields = (('date','day','lec1','lec2','lec3','lec4','lec5','lec6','lec7'),)
    
admin.site.site_header = 'Attendence Administration'
admin.site.site_title ='Attendence Administration'
admin.site.index_title = 'Attendence Administration'
admin.site.register(teacher , teacherAdmin)
admin.site.register(Class , ClassAdmin)
admin.site.register(student , studentAdmin)
admin.site.register(theorysubject , theorysubjectAdmin)
admin.site.register(attendence , attendenceAdmin)
admin.site.register(lab , labAdmin)
admin.site.register(timetable , timetableAdmin)
