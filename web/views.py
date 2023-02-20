from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse
from .models import admins,make,model,years,addcar,addpart,sellpart
# Create your views here.

def homeview(request):
    return render(request, 'web/home.html')

def landview(request):
    return render(request, 'web/landing.html')

def registerview(request):
    if request.method == 'POST':
        member = admins(full_name=request.POST['full_name'],email=request.POST['email'],mobile_no=request.POST['mobile_no'],username=request.POST['username'],password=request.POST['password'],national_id=request.POST['national_id'],role=request.POST['role'])
        member.save()
        return redirect('/web/dashboard/')
    else:
        return render(request, 'web/index.html')

def loginview(request):
    # if request.method == 'POST':
    #     if admins.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
    #         member = admins.objects.get(username=request.POST['username'], password=request.POST['password'])
    #         return redirect('/web/dashboard/')
    #     else:
    #         context = {'msg': 'Invalid username or password'}
    #         return render(request, 'web/1login.html', context)
    return render(request, 'web/dashboard.html')

def dashboardview(request):
    return render(request, 'web/dashboard.html')

def makeview(request):
    if request.method == 'POST':
        name = request.POST.get('make_name')
        # project_id = request.POST.get('full_name')
        # a = admins.objects.get(username=project_id)
        task = make.objects.create(make_name=name)
        return JsonResponse({'success': True})
    else:
        return render(request, 'web/make.html', {'projects': admins.objects.all()})

def modelview(request):
    if request.method == 'POST':
        name = request.POST.get('make_name')
        project_id = request.POST.get('model_name')
        a = make.objects.get(make_name=name)
        # b = admins.objects.get(pk=1)
        task = model.objects.create(model_name=project_id,  make=a)
        return render(request, 'web/model.html', {'projects': make.objects.all()})
    else:
        return render(request, 'web/model.html', {'projects': make.objects.all()})

def yearview(request):
    if request.method == 'POST':
        member = years(year=request.POST['year'])
        member.save()
        return redirect('/web/year/')
    else:
        return render(request, 'web/year.html')

def addcarview(request):
    if request.method == 'POST':
        name1 = request.POST.get('purchaser_name')
        name2 = request.POST.get('make_name')
        name3 = request.POST.get('model_name')
        name4 = request.POST.get('year')
        project_id1 = request.POST.get('purchasing_price')
        # project_id2 = request.POST.get('purchasing_date')
        a1 = admins.objects.get(username=name1)
        a2 = make.objects.get(make_name=name2)
        a3 = model.objects.get(model_name=name3)
        a4 = years.objects.get(year=name4)
        task = addcar.objects.create(purchase_price=project_id1,year=a4,model=a3,make=a2,admin=a1)
        # p_name = {'p1': admins.objects.all()}
        # ma = {'p2': make.objects.all()}
        # mo = {'p3': model.objects.all()}
        # ye = {'p4': years.objects.all()}
        # return render(request, 'web/addcar.html',{'p4': years.objects.all(),'p3': model.objects.all(),'p2': make.objects.all(),'p1': admins.objects.all()})
    else:
        p_name = {'p1': admins.objects.all()}
        ma = {'p2': make.objects.all()}
        mo = {'p3': model.objects.all()}
        ye = {'p4': years.objects.all()}
    return render(request, 'web/addcar.html',{'p4': years.objects.all(),'p3': model.objects.all(),'p2': make.objects.all(),'p1': admins.objects.all()})

# def addcarview(request):
#     if request.method == 'POST':
#         member = admins(full_name=request.POST['full_name'],email=request.POST['email'],mobile_no=request.POST['mobile_no'],username=request.POST['username'],password=request.POST['password'],national_id=request.POST['national_id'],role=request.POST['role'])
#         member.save()
#         return redirect('/web/addcar/')
#     else:
#         return render(request, 'web/addcar.html')

def addpartview(request):
    if request.method == 'POST':
        name1 = request.POST.get('purchaser_name')
        name2 = request.POST.get('make_name')
        name3 = request.POST.get('model_name')
        name4 = request.POST.get('year')
        project_id1 = request.POST.get('partname')
        project_id2 = request.POST.get('partnumber')
        project_id3 = request.POST.get('isscrap')
        project_id4 = request.POST.get('partsellingprice')
        project_id5 = request.POST.get('partlocatione')
        a1 = admins.objects.get(username=name1)
        a2 = make.objects.get(make_name=name2)
        a3 = model.objects.get(model_name=name3)
        a4 = years.objects.get(year=name4)
        task = addpart.objects.create(part_name=project_id1,part_no=project_id2,is_scrap=bool(project_id3),sell_price=project_id4,part_location=project_id5,year=a4,model=a3,make=a2,admin=a1)
        # p_name = {'p1': admins.objects.all()}
        # ma = {'p2': make.objects.all()}
        # mo = {'p3': model.objects.all()}
        # ye = {'p4': years.objects.all()}
        return render(request, 'web/addpart.html',{'p4': years.objects.all(),'p3': model.objects.all(),'p2': make.objects.all(),'p1': admins.objects.all()})
    else:
        p_name = {'p1': admins.objects.all()}
        ma = {'p2': make.objects.all()}
        mo = {'p3': model.objects.all()}
        ye = {'p4': years.objects.all()}
        return render(request, 'web/addpart.html',{'p4': years.objects.all(),'p3': model.objects.all(),'p2': make.objects.all(),'p1': admins.objects.all()})


# def addpartview(request):
#     if request.method == 'POST':
#         member = admins(full_name=request.POST['full_name'],email=request.POST['email'],mobile_no=request.POST['mobile_no'],username=request.POST['username'],password=request.POST['password'],national_id=request.POST['national_id'],role=request.POST['role'])
#         member.save()
#         return redirect('/web/addpart/')
#     else:
#         return render(request, 'web/addpart.html')

def sellpartview(request):
    return render(request, 'web/loggin.html')


# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Task,Project

def create_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        project_id = request.POST.get('project')
        task = Task.objects.create(name=name, project_id=project_id)
        return JsonResponse({'success': True})
    else:
        return render(request, 'web/fore.html', {'projects': Project.objects.all()})

