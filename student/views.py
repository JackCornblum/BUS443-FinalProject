from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from student.models import Studentinfo, Courseinfo, Enrollmentinfo, Enrollment

# Create your views here.

@login_required
def home(request):
    cursorgpa = connection.cursor()
    cursorgpa.execute('SELECT AVG(gpa) FROM final_project.student_studentinfo;')
    cursorit = connection.cursor()
    cursorit.execute('SELECT COUNT(major) FROM final_project.student_studentinfo WHERE (major="I.T.");')
    average = cursorgpa.fetchone()
    avg = average[0]
    itmajor = cursorit.fetchone()
    itcount = itmajor[0]
    cursorphysics = connection.cursor()
    cursorphysics.execute('SELECT COUNT(major) FROM final_project.student_studentinfo WHERE (major="Physics");')
    physicsmajor = cursorphysics.fetchone()
    physicscount = physicsmajor[0]
    cursorstats = connection.cursor()
    cursorstats.execute('SELECT COUNT(major) FROM final_project.student_studentinfo WHERE (major="Stats");')
    statsmajor = cursorstats.fetchone()
    statsCount = statsmajor[0]
    cursorchem = connection.cursor()
    cursorchem.execute('SELECT COUNT(major) FROM final_project.student_studentinfo WHERE (major="Chemistry");')
    chemmajor = cursorchem.fetchone()
    chemcount = chemmajor[0]
    cursormarketing = connection.cursor()
    cursormarketing.execute('SELECT COUNT(major) FROM final_project.student_studentinfo WHERE (major="Marketing");')
    marketingmajor = cursormarketing.fetchone()
    marketingcount = marketingmajor[0]
    context = {'avgGpa':avg, 'totalIT':itcount, 'totalPhysics':physicscount, 'totalStats':statsCount, 'totalChem':chemcount, 'totalMarketing': marketingcount}
    return render(request, 'student/home.html', context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    
@login_required
def studentinfo(request):
    cursorobj = connection.cursor()
    cursorobj.execute("select * from student_studentinfo")
    studentdata = dictfetchall(cursorobj)
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data':minidata}
    return render(request, 'student/studentinfo.html', context)
    
@login_required
def courseinfo(request):
    cursorobj = connection.cursor()
    cursorobj.execute("select * from student_courseinfo")
    coursedata = dictfetchall(cursorobj)
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data':minidata}
    return render(request, 'student/courseinfo.html', context)

@login_required
def enrollment(request):
    coursedata = Courseinfo.objects.all()
    studentdata = Enrollmentinfo.objects.all()
    if ('studentname' in request.session):
        enrollmentdetails = Enrollment.objects.filter(student = request.session['studentname'])
    else:
        enrollmentdetails = Enrollment.objects.all()
    context = {'course': coursedata, 'student': studentdata, 'enrollment': enrollmentdetails,}
    return render(request, 'student/enrollment.html', context)

def saveenrollment(request):
    if ('sname' in request.GET and 'course' not in request.GET):
        request.session['studentname'] = request.GET.get('sname')
    if ('sname' and 'course' in request.GET):
        studentname = request.GET.get('sname')
        course = request.GET.get('course')
        dataobj = Enrollment(student = studentname, course = course)
        dataobj.save()
    return HttpResponse("Success")
        


