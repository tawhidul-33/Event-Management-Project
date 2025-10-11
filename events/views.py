from django.shortcuts import render,redirect
from events.forms import EventModelForm,CategoryModelForm,ParticipantModelForm
from django.contrib import messages
from events.models import Category,Event,Participant
from django.utils import timezone
from django.db.models import Count, Q
# Create your views here.
# def home(request):
#     return render(request,'home.html')

def event_list(request):
     # Filter type from GET parameter
    type = request.GET.get('type', 'all')
    today = timezone.now().date()  

    # Event counts
    counts = Event.objects.aggregate(
        total=Count("id"),
        upcoming=Count('id', filter=Q(start_date__gt=today)),
        past=Count('id', filter=Q(end_date__lt=today)),
        today=Count('id', filter=Q(start_date__lte=today, end_date__gte=today)),
    )

    # Base query
    Base_query = Event.objects.select_related("category").prefetch_related("participants")
    # specific akti event er total perticipent
    # participant_count = Event.objects.annotate(specific_total_participants=Count('participants'))
    
    # Conditional filtering
    if type == 'upcoming':
        events = Base_query.filter(start_date__gt=today)
    elif type == 'past':
        events = Base_query.filter(end_date__lt=today)
    elif type == 'today':
        events = Base_query.filter(start_date__lte=today, end_date__gte=today)
    else:
        events = Base_query.all()
    # protita event er moddeh "participant_count" name akta attribute baniye tar moddeh participant count raktechi
    for event in events:
        event.participant_count = event.participants.count()

    context = {
        "events": events,
        "counts": counts,
    }
    return render(request, 'event/event_list.html', context)



def event_details(request, id):
    event = Event.objects.get(id=id)
    participants = event.participants.all()

    context = {
        "event": event,
        "participants": participants,
    }
    return render(request, 'event/event_details.html', context)

def event_creat(request):
    form = EventModelForm()
    if request.method == 'POST':
        form = EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Event Created Successfuly")
            return redirect('event-creat')
    
    context={
        "event_form":form,  
    }
    return render(request, 'event/event_creat.html',context)

def event_update(request,id):
    event=Event.objects.get(id=id)
    form = EventModelForm(instance=event)
    if request.method == 'POST':
        form = EventModelForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            messages.success(request,"Update Successfuly")
            return redirect('event-update',id)
    context={
        "event_form":form,
    }
    return render(request, 'event/event_creat.html',context)

def event_delete(request, id):
        event= Event.objects.get(id=id)
        event.delete()
        messages.success(request,"Event Deleted Successfuly")
        return redirect("event-list")

    
"""For Category"""
def category_create(request):
    form = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully!")
            return redirect('category-creat')

    context = {
        'category_form': form
    }
    return render(request, 'category/category_creat.html', context)

def category_update(request,id):
    category=Category.objects.get(id=id)
    form = CategoryModelForm(instance=category)
    if request.method == 'POST':
        form = CategoryModelForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Updated successfully!")
            return redirect('category-update',id)

    context = {
        'category_form': form
    }
    return render(request, 'category/category_creat.html', context)

def category_delete(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    messages.success(request,"Event Deleted Successfuly")
    return redirect('category-list')

def category_list(request):
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    return render(request, 'category/category_list.html',context)

""" for Participants"""

def participant_add(request, id):
    event =Event.objects.get(id=id)
    form = ParticipantModelForm()
    if request.method == "POST":
        form = ParticipantModelForm(request.POST)
        if form.is_valid():
            participant = form.save()
            event.participants.add(participant)  # sudhu oi event e add
            messages.success(request, f"{participant.name} is now participating in {event.name}!")
            return redirect('participant-add',id)  

    context = {
        'form_participate': form,
        'event': event,
    }
    return render(request, 'participant/participate_add.html', context)


def participant_list(request):
    participants = Participant.objects.all()
    context={
        'participants': participants
    }
    return render(request, 'participant/participate_list.html',context)

def participant_delete(request, id):
    participant = Participant.objects.get(id=id)
    participant.delete()
    return redirect('participant-list')

"""Search list for event"""
def search_event_list(request):
    search_query = request.GET.get('search', '')  # Input theke string neya
    events = Event.objects.all()

    if search_query:  # Khali na thakle filter koro
        events = events.filter(
            Q(name__icontains=search_query) | Q(location__icontains=search_query)
        )

    context = {
        "events": events,
        "search_query": search_query,
    }
    return render(request, 'home.html', context)

