from django.shortcuts import render
from mytable.models import Buser, Jikwon, Gogek
from django.db.models.aggregates import Count

# Create your views here.
def MainFunc(request):
    buser = Buser.objects.all()
    
    return render(request, 'main.html', {'blist': buser})

def JikwonFunc(request):
    i=0
    no = request.GET.get('buser_no')

    empData = Jikwon.objects.filter(buser_num = no).order_by('-jikwon_no')


    datas = []
    '''
    강사님 코드
#     customerData = Gogek.objects.values('gogek_damsano').annotate(count = Count('gogek_no')).values('gogek_damsano', 'count')
#     for eData in empData:
#         cnt = 0
#         for cData in customerData:
#             if eData.jikwon_no == cData["gogek_damsano"]:
#                 cnt = cData["count"]
#  
#         newEmpData = {}
#         newEmpData["jikwon_no"] = eData.jikwon_no
#  
#         newEmpData["jikwon_jik"] = eData.jikwon_jik
#         newEmpData["count"] = cnt
#         datas.append(newEmpData)
        '''
    for i in empData:
        gogeks = Gogek.objects.filter(gogek_damsano=i.jikwon_no).count()
        i.count= gogeks
            
    return render(request, 'jlist.html', {'jlist': empData})

def GogekFunc(request):
    jikwon = request.GET.get('jikwon_no')
    gogek = Gogek.objects.all().filter(gogek_damsano = jikwon).order_by('gogek_name')
    return render(request, 'glist.html', {'glist': gogek})
