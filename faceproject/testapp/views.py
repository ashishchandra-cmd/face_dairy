from django.shortcuts import render,redirect
from testapp.models import face
from testapp.forms import faceForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def show_face_views(request):
    face_details=face.objects.all()
    paginator=Paginator(face_details,2)
    page_number=request.GET.get('page')
    try:
        face_details=paginator.page(page_number)
    except  PageNotAnInteger:
        face_details=paginator.page(1) 
    except EmptyPage:
        face_details=paginator.page(paginator.num_pages)  
    return render(request,'show.html',{'face_details':face_details})

def insert_face_views(request):
    form=faceForm()
    if request.method=='POST':
        form=faceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'insert.html',{'form':form})