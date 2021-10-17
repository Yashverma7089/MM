from django.shortcuts import render, resolve_url
from . import PoolDict

def AdminLogin(request):
    try:
      result = request.session['ADMIN']
      return render(request,"AdminDashboard.html",{'result': result})
    except Exception as e:
       return render(request,'AdminLogin.html') 

def AdminLogout(request):
    del request.session['ADMIN'] 
    return render(request,'AdminLogin.html') 
 
def CheckAdminLogin(request):
  try:
    emailid = request.POST['emailid']
    password = request.POST['password']

    dbe,cmd = PoolDict.ConnectionPolling()
    q = "select * from admins where emailid = '{}' and password = '{}'".format(emailid,password)
    cmd.execute(q)
    result = cmd.fetchone()
    print(result) 
    if(result):
        request.session['ADMIN'] = result
        return render(request,"AdminDashboard.html",{'result': result})
    else:
        return render(request,"AdminLogin.html",{'result': result, 'msg': 'Invalid Email / Password '})
    dbe.close()
  except Exception as e:
    print(e)
    return render(request,"AdminLogin.html",{'result': {}, 'msg' : 'Server Error'})

def AdminDashboard(request):
  return render(request,"AdminDashboard.html")