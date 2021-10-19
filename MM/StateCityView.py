from django.http import JsonResponse
from . import Pool


def FetchAllStates(request):
    try:
        dbe, cmd = Pool.ConnectionPool()
        q = "select * from states"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)


def FetchAllCities(request):
    try:
        dbe, cmd = Pool.ConnectionPool()
        stateid = request.GET['stateid']
        q = "select * from cities where stateid = {}".format(stateid)
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)
