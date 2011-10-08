from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponse
import httplib, urllib

BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = 8080

def get_digest():
    conn = httplib.HTTPConnection(BACKEND_HOST, BACKEND_PORT, timeout=30)
    conn.request("GET", "/digest")
    res = conn.getresponse()
    data = res.read()
    conn.close()
    return data

def main(request):
    return render_to_response('index.html', eval(get_digest()))

def digest(request):
    return render_to_response('digest.html', eval(get_digest()))

def show_pattern(request, hash, minutes):
    conn = httplib.HTTPConnection(BACKEND_HOST, BACKEND_PORT, timeout=10)
    conn.request("GET", "/pattern?hash=%s&min=%s" % (hash, minutes))
    res = conn.getresponse()
    data = res.read()
    conn.close()
    context = eval(data)
    context.update({'minutes': minutes})
    return render_to_response('pattern.html', context)

def get_data(request, hash, host, minutes):
    conn = httplib.HTTPConnection(BACKEND_HOST, BACKEND_PORT, timeout=10)
    conn.request("GET", "/data?hash=%s&host=%s&min=%s" % (hash, host, minutes))
    res = conn.getresponse()
    data = res.read()
    conn.close()
    context = eval(data)
    return render_to_response('data.html', context)

def new_pattern(request):
    return render_to_response('new.html')

@csrf_exempt
def save_patterns(request):
    conn = httplib.HTTPConnection(BACKEND_HOST, BACKEND_PORT, timeout=30)
    data = request.POST['data']
    params = urllib.urlencode({'data': data.encode('utf-8')})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request("POST", "/patterns/save/", params, headers)
    res = conn.getresponse()
    res_data = res.read()
    conn.close()
    return HttpResponse('')

def all_patterns(request):
    conn = httplib.HTTPConnection(BACKEND_HOST, BACKEND_PORT, timeout=10)
    conn.request("GET", "/patterns/all/")
    res = conn.getresponse()
    res_data = res.read()
    conn.close()
    return render_to_response('all_patterns.html', {'data': res_data})
