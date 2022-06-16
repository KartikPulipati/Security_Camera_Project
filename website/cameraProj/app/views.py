from django.shortcuts import redirect, render
import json

def home(request):
    if request.method == 'GET':
        return render(request=request,template_name='app/index.html')
    else:
        dict = {}
        dict['send'] = request.POST['send']
        dict['time'] = request.POST['time']
        dict['sense'] = request.POST['sense']
        with open("data.json", "w") as outfile:
            json.dump(dict, outfile)
    return redirect('home')

