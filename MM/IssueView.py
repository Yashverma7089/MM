from django.shortcuts import render
from . import Pool

def IssueInterface(request):
    try:
        result = request.session['EMPLOYEE']
        return render(request, "IssueInterface.html")
    except Exception as e:
        return render(request, 'EmployeeLogin.html')


def IssueProductSubmit(request):
    try:
        employeeid = request.POST['employeeid']
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        productid = request.POST['productid']
        finalproductid = request.POST['finalproductid']
        demand_employeeid = request.POST['demand_employeeid']
        dateissue = request.POST['dateissue']
        qtyissue = request.POST['qtyissue']
        remark = request.POST['remark']

        q = "insert into issue (employeeid, categoryid, subcategoryid, productid, finalproductid, demand_employeeid, dateissue, qtyissue, remark) values ({}, {}, {}, {}, {}, {}, '{}', {}, '{}' )".format(
             employeeid, categoryid, subcategoryid, productid, finalproductid, demand_employeeid, dateissue, qtyissue, remark)
        print(q)
        dbe, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return render(request, "IssueInterface.html", {'msg': 'Record Successfully Submitted'})
    except Exception as e:
        print("Error :", e)
        return render(request, "IssueInterface.html", {'msg': 'Fail to Submit Record'})

def DisplayAllIssueProduct(request):
    try:
        dbe, cmd = Pool.ConnectionPool()
        q = "select IP.*,(select C.categoryname from categories C where C.categoryid = IP.categoryid),(select S.subcategoryname from subcategory S where S.subcategoryid = IP.subcategoryid), (select P.productname from products P where P.productid = IP.productid), (select FP.finalproductname from finalproducts FP where FP.finalproductid = IP.finalproductid) from issue IP"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return render(request, "DisplayAllIssueProduct.html", {'rows': rows})
    except Exception as e:
        print(e)
        return render(request, "DisplayAllIssueProduct.html", {'rows': []})

def EditDeleteIssueProductRecord(request):
    btn = request.GET['btn']
    issueid = request.GET['issueid']
    if(btn == "Edit"):
        employeeid = request.GET['employeeid']
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        productid = request.GET['productid']
        finalproductid = request.GET['finalproductid']
        demand_employeeid = request.GET['demand_employeeid']
        dateissue = request.GET['dateissue']
        qtyissue = request.GET['qtyissue']
        remark = request.GET['remark']
        try:
            dbe, cmd = Pool.ConnectionPool()
            q = "update issue set employeeid = {}, categoryid = {}, subcategoryid = {}, productid = {}, finalproductid = {}, demand_employeeid = {}, dateissue = '{}', qtyissue = {}, remark = '{}' where issueid={}".format(
                employeeid, categoryid, subcategoryid, productid, finalproductid, demand_employeeid ,dateissue, qtyissue, remark, issueid)
            print(q)
            cmd.execute(q)
            dbe.commit()
            row = cmd.fetchone()
            dbe.close()
            return DisplayAllIssueProduct(request)
        except Exception as e:
            print(e)
            return DisplayAllIssueProduct(request)

    elif(btn == "Delete"):
        try:
            dbe, cmd = Pool.ConnectionPool()
            q = "delete from issue where issueid={}".format(
                issueid)
            cmd.execute(q)
            dbe.commit()
            row = cmd.fetchone()
            dbe.close()
            return DisplayAllIssueProduct(request)
        except Exception as e:
            print(e)
            return DisplayAllIssueProduct(request)
