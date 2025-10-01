from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def story(request):
    return render(request, 'home/story.html')

def map(request):
    return render(request, 'home/map.html')

def about(request):
    return render(request, 'home/about.html')

def three_demo(request):
    return render(request, 'home/three_demo.html')
