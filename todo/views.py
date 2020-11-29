from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

def view_list(request):
    form = TaskForm(request.POST or None)
    # Retrieve all the products and render index.html with the data
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)

def add(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_list page
        return redirect('view_list')
    # Retrieve all the products and render index.html with the data
    context = {'form': form}
    return render(request, 'todo/index.html', context)

def update_task(request, id):
    # Get the task based on its id
    task = Task.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance= task allows to update the record rather than creating a new record when save method is called
    form = TaskForm(request.POST or None, instance=task)
    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_task page
        return redirect('view_list')
    else:
        # if the request does not have post data, render the page with the form containing the task's info
        return render(request, 'todo/update.html', {'form': form, 'task': task})

def delete_task(request, id):
    # Get the task based on its id
    task = Task.objects.get(id=id)
    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        task.delete()
        # after deleting redirect to view_list page
        return redirect('view_list')
    else:
        # if the request is not post, render the page with the task's info
        return render(request, 'todo/delete.html', {'task': task})

def complete(request, id):
    # Get the task based on its id
    task = Task.objects.get(id=id)
    task.complete = True
    task.save()
    return redirect('view_list')