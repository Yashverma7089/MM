from django.shortcuts import render
from . import Pool
import uuid
import random
import os

def EmployeeInterface(request):
    return render(request, 'EmployeeInterface.html')

def EmployeeSubmit(request):
    try:
       firstname = request.POST['firstname']
       lastname = request.POST['lastname']
       gender = request.POST['gender']
       birthdate = request.POST['birthdate']
       paddress = request.POST['paddress']
       state = request.POST['state']
       city = request.POST['city']
       caddress = request.POST['caddress']
       emailaddress = request.POST['emailaddress']
       mobilenumber = request.POST['mobilenumber']
       designation = request.POST['designation']
       
       picture = request.FILES['picture']
       filename = str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
       password = "".join(random.sample(['1','j','d','@','#','9','$'],k=7))

       q = "insert into employee (firstname, lastname, gender, birthdate, paddress, stateid, cityid, caddress, emailaddress, mobilenumber, designation, picture, password) values ('{}', '{}', '{}', '{}', '{}', {}, {}, '{}','{}', '{}', '{}', '{}', '{}')".format(firstname, lastname, gender, birthdate, paddress, state, city, caddress, emailaddress, mobilenumber, designation, filename, password)
       print(q)
       dbe, cmd = Pool.ConnectionPolling()
       cmd.execute(q)
       dbe.commit()
       F = open("D:/MM/assets/"+filename,"wb")
       for chunk in picture.chunks():
           F.write(chunk)
       F.close()
       dbe.close()
       return render(request, "EmployeeInterface.html",{'msg':'Record Successfully Submitted'})
    except Exception as e:
       print("Error :",e)
       return render(request, "EmployeeInterface.html",{'msg':'Fail to Submit Record'})

def DisplayAll(request):
    try:
        dbe, cmd = Pool.ConnectionPolling()
        q = "select E.*,(select C.cityname from Cities C where C.cityid = E.cityid), (select S.statename from States S where S.stateid = E.stateid) from employee E"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return render(request,"DisplayAllEmployee.html",{'rows' : rows})
    except Exception as e:
        print(e)
        return render(request,"DisplayAllEmployee.html",{'rows' : []})

def DisplayById(request):
    empid = request.GET['empid']
    try:
        dbe, cmd = Pool.ConnectionPolling()
        q = "select E.*,(select C.cityname from Cities C where C.cityid = E.cityid), (select S.statename from States S where S.stateid = E.stateid) from employee E where employeeid = {}".format(empid)
        cmd.execute(q)
        row = cmd.fetchone()
        dbe.close()
        return render(request,"DisplayEmployeeById.html",{'row' : row})
    except Exception as e:
        print(e)
        return render(request,"DisplayEmployeeById.html",{'row' : []})

def EditDeleteRecord(request):
    btn = request.GET['btn']
    empid = request.GET['empid']
    if(btn == "Edit"):
        firstname = request.GET['firstname']
        lastname = request.GET['lastname']
        gender = request.GET['gender']
        birthdate = request.GET['birthdate']
        paddress = request.GET['paddress']
        state = request.GET['state']
        city = request.GET['city']
        caddress = request.GET['caddress']
        emailaddress = request.GET['emailaddress']
        mobilenumber = request.GET['mobilenumber']
        designation = request.GET['designation']

        try:
            dbe, cmd = Pool.ConnectionPolling()
            q = "update employee set firstname = '{}', lastname = '{}', gender='{}', birthdate='{}', paddress='{}', stateid={}, cityid={}, caddress='{}', emailaddress='{}', mobilenumber='{}', designation='{}' where employeeid = {}".format(firstname, lastname, gender, birthdate, paddress, state, city, caddress, emailaddress, mobilenumber, designation, empid)
            cmd.execute(q)
            dbe.commit()
            row = cmd.fetchone()
            dbe.close()
            return DisplayAll(request)
        except Exception as e:
            print(e)
            return DisplayAll(request)

    elif(btn == "Delete"):
        try:
            dbe, cmd = Pool.ConnectionPolling()
            q = "delete from employee  where employeeid = {}".format(empid)
            cmd.execute(q)
            dbe.commit()
            row = cmd.fetchone()
            dbe.close()
            return DisplayAll(request)
        except Exception as e:
            print(e)
            return DisplayAll(request)
 
def EditEmployeePicture(request):
    try:
        empid = request.GET['empid']
        firstname = request.GET['firstname']
        lastname = request.GET['lastname']
        picture = request.GET['picture']
        row = [empid,firstname,lastname,picture]
        return render(request,"EditEmployeePicture.html",{'row':row})
    except Exception as e:
        return render(request,"EditEmployeePicture.html",{'row':[]})
        
def SaveEditPicture(request):
    try:
       empid = request.POST['empid']
       oldpicture = request.POST['oldpicture']
       picture = request.FILES['picture']
       filename = str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]

       q = "update employee set picture = '{}' where employeeid = {}".format(filename,empid)
       print(q)
       dbe, cmd = Pool.ConnectionPolling()
       cmd.execute(q)
       dbe.commit()
       F = open("D:/MM/assets/"+filename,"wb")
       for chunk in picture.chunks():
           F.write(chunk)
       F.close()
       dbe.close()
       os.remove('D:/MM/assets/'+oldpicture)
       return DisplayAll(request)
    except Exception as e:
       print("Error :",e)
       return DisplayAll(request)
