from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from todo.models import Tasks

@csrf_exempt
def TaskList(request):

    if request.method == 'GET':
        tasks = Tasks.objects.all()
        context = {'tasks':tasks}
        return render(request, 'index.html', context)

    if request.method == 'POST':
        id = request.POST.get('id')
        if id == '':
            task = Tasks.objects.create(
                name = request.POST.get('name'),
                desc = request.POST.get('desc')
            )
            task.save()
            return redirect('tasks')
        else:
            task = Tasks.objects.get(id=id)
            task.name = request.POST.get('name')
            task.desc = request.POST.get('desc')
            task.save()
            return redirect('tasks')

def TaskDelete(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return redirect('tasks')