from django.shortcuts import render

# Create your views here.
counter = 0

def counter_view(request):
    global counter
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increment':
            counter += 1
        elif action == 'decrement':
            counter -= 1
    return render(request, 'mycounter/counter.html', {'counter': counter})