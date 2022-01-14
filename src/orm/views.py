from django.shortcuts import render
from . models import *
from django.db import connection
from django.db.models import Q
# Create your views here.


##-----------------------------------part 1---------------------------------

def index(request):

    student = Student.objects.all()
    print('student--------------', student)
    # print('student query--------------', student.query)
    print('connection query--------------', connection.queries)
    #data base can understant sql, not python.
    # so python to sql, sql to databasedata. so data will comde by sql language 
 
    return render(request, 'index.html',{'student':student})

# def student_list(request):
#     # post = Student.objects.filter(surname__startswith = 'Ah') | Student.objects.filter(surname__startswith = 'S')
#     post = Student.objects.filter(Q (surname__startswith = 'Ah') | Q (surname__startswith = 'S')) 
#     # the both line above do same job. If ~Q it would not come out 

#     print('student query--------------', post.query)


#     return render(request, 'index.html', {'data':post} )



##-----------------------------------part 2---------------------------------
# def student_list(request):
#     post = Student.objects.exclude(classroom = 3) & Student.objects.exclude(firstname__startswith = 'R')
#     #exclude will exclude the record
#     print('student query--------------', post.query)

#     return render(request, 'index.html', {'data':post} )


##-----------------------------------part 3 data union---------------------------------
# def student_list(request):
#     post = Student.objects.all().values_list('firstname').union(Teacher.objects.all().values_list('firstname')) #for object
#     # post = Student.objects.all().values('firstname').union(Teacher.objects.all().values('firstname')) #for dictionary
   
#     print('student query--------------', post.query)

#     return render(request, 'index.html', {'data':post} )





# ##-----------------------------------part 4 Not query---------------------------------
# # not example
# # exclude(condition)
# #filter(~Q(condition))

# def student_list(request):
#     # post = Student.objects.exclude(surname = 'Islam')
#     post = Student.objects.filter(Q(age__gt = 22))
#     # gt = greater than
#     # gte = Greater than or equal to
#     # lt = Less than
#     #lte = Less than or equal to

#     print('student query--------------', post.query)

#     return render(request, 'index.html', {'data':post} )




# ##-----------------------------------part 5 select and output---------------------------------


# def student_list(request):

#     post = Student.objects.filter(classroom = 4).only('firstname')
#     # here firstname is brought so prosseing time will be saved
   

#     print('student query--------------', post.query)

#     return render(request, 'index.html', {'data':post} )




# ##----------------------------------- part 6 raw queries ---------------------------------


def student_list(request):

    # post = Student.objects.all() 
    # post = Student.objects.raw("SELECT * FROM orm_student") # all()
    post = Student.objects.raw("SELECT * FROM orm_student WHERE age=22") # filter()


    print('student query--------------', post.query)

    return render(request, 'index.html', {'data':post} )




##----------------------------------- part 7 model inheritance ---------------------------------


# def student_list(request):
#     cursor = connection.cursor()
#     cursor.execute("SELECT count(*) FROM orm_student")
#     r = cursor.fetchone()
#     print(r)


#     return render(request, 'index.html', {'data':r} )



