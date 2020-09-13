from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
import datetime , calendar
from decimal import *
from .models import teacher , Class , student , timetable , attendence , theorysubject , lab

def home(request):
    n = datetime.datetime.now()
    date = str(n)[0:10] 
    time = str(n)[11:19]
    context = {
        'dat' : date ,
        'tim' : time ,
    }

    return render(request , 'index.html' , context)


@staff_member_required
def selection_sheet(request):

    classes = Class.objects.all()
    context = {
        'class' : classes
    }
    return render(request , 'selection_sheet.html' , context)

@staff_member_required
def attendence_sheet(request , pk):

    
    #To render date on att_sheet
    n = datetime.datetime.now()
    today_date = str(n)[0:10]

    #To render day on att_sheet
    m = datetime.date.today
    today = calendar.day_name[n.weekday()]
    today = today.capitalize()


    #THIS DATA IS TO BE UPLOADED TO ATTENDENCE DB
    student_list = []
    daten = ''
    dayn = ''
    lec = ''
    c_id = 0

    if request.method == 'POST':
        for key, value in request.POST.items():
            #print('Key:',key) 
            #print('Value:',value)

            if key == 'csrfmiddlewaretoken':
                continue

            if key == 'date':
                daten = value
                continue

            if key == 'day':
                dayn = value
                continue
            
            if key == 'class_id':
                c_id = int(value)
                continue

            if key == 'lecture_number':
                lec = value
                continue
            
            if key == 'teacher_name':
                continue

            if key == 'subject':
                continue

            l = [key,value]
            student_list.append(l)
        
        print(student_list)

        if dayn == 'Sunday':
            return HttpResponse("<h1>You  Got no Chill Sir/Ma'am ,Its Sunday Today</h1> ")

        if not attendence.objects.filter(day = dayn , date = daten , Class_id =  pk):
            
            for x in student_list:
                
                if lec == 'lec1':

                    att = attendence(
                        student_id = int(x[0]) , lec1 = x[1] , date = daten , day = dayn , Class_id = c_id)
                    att.save() 

                elif lec == 'lec2':

                    att = attendence(
                        student_id = int(x[0]) , lec2 = x[1] , date = daten , day = dayn , Class_id = c_id)
                    att.save()
            

                elif lec == 'lec3':

                    att = attendence(
                        student_id = int(x[0]) , lec3 = x[1] , date = daten , day = dayn , Class_id = c_id)
                    att.save()


                elif lec == 'lec4':

                    att = attendence(
                        student_id = int(x[0]) , lec4 = x[1] , date = daten , day = dayn , Class_id = c_id)
                    att.save()
    

                elif lec == 'lec5':

                    att = attendence(
                        student_id = int(x[0]) , lec5 = x[1] , date = daten , day = dayn , Class_id = c_id)
                    att.save()
    

                elif lec == 'lec6':

                    att = attendence(
                        student_id = int(x[0]) , lec6 = x[1] , date = daten , day = dayn , Class_id = c_id)
                    att.save()
    
                
                elif lec == 'lec7':

                    att = attendence(
                        student_id = int(x[0]) , lec7 = x[1] , date = daten , day = dayn , Class_id = c_id)
                    att.save()
        
        else:

            for x in student_list:

                if lec == 'lec1':

                    attendence.objects.filter(student_id = int(x[0]) , Class_id = c_id ).update(lec1 = x[1])

                elif lec == 'lec2':

                    attendence.objects.filter(student_id = int(x[0]) , Class_id = c_id ).update(lec2 = x[1])
            

                elif lec == 'lec3':

                    attendence.objects.filter(student_id = int(x[0]) , Class_id = c_id ).update(lec3 = x[1])


                elif lec == 'lec4':

                    attendence.objects.filter(student_id = int(x[0]) , Class_id = c_id ).update(lec4 = x[1])
    

                elif lec == 'lec5':

                    attendence.objects.filter(student_id = int(x[0]) , Class_id = c_id ).update(lec5 = x[1])
    

                elif lec == 'lec6':

                    attendence.objects.filter(student_id = int(x[0]) , Class_id = c_id ).update(lec6 = x[1])
    
                
                elif lec == 'lec7':

                    attendence.objects.filter(student_id = int(x[0]) , Class_id = c_id ).update(lec7 = x[1])


    classes = Class.objects.filter(id = pk)
    theorysubjects = theorysubject.objects.filter(Class_id = pk)
    labs = lab.objects.filter(Class_id = pk) 
    students = student.objects.filter(Class_id = pk)
    teachers = teacher.objects.all()
    
    #To render date on att_sheet
    n = datetime.datetime.now()
    today_date = str(n)[0:10]

   
    context = {
        'class' : classes ,
        'student' : students ,
        'date' : today_date ,
        'day' : today,
        'teacher' : teachers ,
        'subject' : theorysubjects ,
        'lab' : labs ,
        'class_id' : int(pk) ,
    }
    return render(request , 'att_sheet.html' , context)

'''@staff_member_required
def clone(request , pk):

    #print(pk)

    #To render date on att_sheet
    n = datetime.datetime.now()
    today_date = str(n)[0:10]

    #To render day on att_sheet
    m = datetime.date.today
    today = calendar.day_name[n.weekday()]
    today = today.capitalize()

    if not attendence.objects.filter(day = today , date = today_date , Class_id = pk):
        return HttpResponse('<h1 style = "margin-top: 10px;"> To Clone attendence, first you have to record attendence of any lecture of today </h1>')

    if request.method == 'POST':
        
        clone_from = ''
        clone_to = ''

        for key, value in request.POST.items():
            
            if key == 'clone_from':
                clone_from = value
                continue

            if key == 'clone_to':
                clone_to = value
                continue

        for x in attendence.objects.filter(day = today , date = today_date , Class_id = pk ):
            

    context = {

        'date' : today_date , 
        'day' : today ,
    }

    return render(request , 'clone.html' , context)  ''' 


def student_profile(request):

    c_id = 0
    s_id = 0

    #To render date on att_sheet
    n = datetime.datetime.now()
    today_date = str(n)[0:10]

    #To render day on att_sheet
    m = datetime.date.today
    today = calendar.day_name[n.weekday()]
    today = today.capitalize()
    

    if request.method == 'POST':
        enroll = []
        
        for key, value in request.POST.items():
            l = (key,value)
            enroll.append(l)
        print(enroll)
        enroll.pop(0)

        # OBJECTS OF DB {...............
        students = student.objects.filter(enrollment_number = enroll[0][1].lower())
        
        if not students:
            return HttpResponse('<h1 style = margin: 50% > No Record Exist for This Entry....Sorry :( </h1>') 

        else:
            for x in students:
                c_id = x.Class_id
                s_id =  x.id
        
            theorysubjects = theorysubject.objects.filter(Class_id = c_id)
            labs = lab.objects.filter(Class_id = c_id)
            timetables = timetable.objects.filter(Class_id = c_id , day = today)
            current_attendences = attendence.objects.filter(date = today_date , student_id = s_id)
            total_attendence = attendence.objects.filter(student_id = s_id)
    
            # ...............}
            
            total_p = 0
            count = 0
            for x in total_attendence:
                if x.lec1 == 'P':
                    total_p += 1
                if x.lec2 == 'P':
                    total_p += 1
                if x.lec3 == 'P':
                    total_p += 1
                if x.lec4 == 'P':
                    total_p += 1
                if x.lec5 == 'P':
                    total_p += 1
                if x.lec6 == 'P':
                    total_p += 1
                if x.lec7 == 'P':
                    total_p += 1
                count += 1
            
            #print(count*7 , total_p)
            per = (total_p / (count*7)) * 100

            perc = "{:.2f}".format(per)
            
            percent = str(perc) + ' ' + '%'
            #.....................}
            
            if students:
            
                context = {
                    'student' : students ,
                    'timetable' : timetables ,
                    'att' : current_attendences ,
                    'percentage' : percent ,
                    'percentageI' : perc ,
                    'subject' : theorysubjects ,
                    'lab' : labs ,
                }
    

    return render(request , 'student_profile.html' , context)

 