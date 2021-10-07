from django.shortcuts import render
from . import Pool

def SupplierInterface(request):
    return render(request,"SupplierInterface.html")

def SupplierSubmit(request):
    try:
       suppliername = request.GET['suppliername']
       landlinenumber = request.GET['landlinenumber']
       mobilenumber = request.GET['mobilenumber']
       emailid = request.GET['emailid']
       address = request.GET['address']
       state = request.GET['state']
       city = request.GET['city']
       
       q = "insert into supplier (suppliername, landlinenumber, mobilenumber, emailid, address, stateid, cityid) values ('{}', '{}', '{}', '{}', '{}', {}, {})".format(suppliername, landlinenumber, mobilenumber, emailid, address, state, city)
       print(q)
       dbe, cmd = Pool.ConnectionPolling()
       cmd.execute(q)
       dbe.commit()
       dbe.close()
       return render(request, "SupplierInterface.html",{'msg':'Record Successfully Submitted'})
    except Exception as e:
       print("Error :",e)
       return render(request, "SupplierInterface.html",{'msg':'Fail to Submit Record'})

def DisplayAllSupplier(request):
    try:
        dbe, cmd = Pool.ConnectionPolling()
        q = "select SR.*,(select C.cityname from Cities C where C.cityid = SR.cityid), (select S.statename from States S where S.stateid = SR.stateid) from supplier SR"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return render(request,"DisplayAllSupplier.html",{'rows' : rows})
    except Exception as e:
        print(e)
        return render(request,"DisplayAllSupplier.html",{'rows' : []})