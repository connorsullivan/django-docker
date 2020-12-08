from django.shortcuts import render


def error(request):
    '''Intentionally raise an exception.'''
    raise Exception('The error view was called!')


def headers(request):
    '''Display the HTTP headers on the incoming request.'''
    headers = sorted(request.META.items())
    return render(request, 'core/headers.html', {'headers': headers})
