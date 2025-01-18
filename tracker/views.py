from django.shortcuts import render, get_object_or_404, redirect
from .models import Activity
from .forms import ActivityForm


# Home page: List all activities with filtering and sorting

def activity_list(request):
    # Get priority filter from query parameters
    priority_filter = request.GET.get('priority', '')

    # Fetch activities with possible priority filtering
    activities = Activity.objects.all()

    if priority_filter:
        activities = activities.filter(priority=priority_filter)

    # Optionally sort by start_time
    activities = activities.order_by('start_time')

    return render(request, 'tracker/activity_list.html', {'activities': activities})


# Add a new activity
def activity_add(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm()
    return render(request, 'tracker/activity_form.html', {'form': form})


# Mark an activity as completed
def mark_completed(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    activity.is_completed = True
    activity.save()
    return redirect('activity_list')
