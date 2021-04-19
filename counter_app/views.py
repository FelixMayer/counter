from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1

    return render(request, "index.html")


def destroy(request):
    request.session.flush()

    return redirect('/')

def double(request):
    request.session['counter'] += 1

    return redirect('/')
