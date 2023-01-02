from django.shortcuts import render

def looping(request):
    d={'name':'sreenivasaramanujan','profession':'mathematician'}
    return render(request,'looping.html',d)
