from django.urls import path
from events.views import event_list,event_creat,event_update,event_delete,event_details,category_create,category_update,category_delete,category_list,participant_add,participant_delete,participant_list
urlpatterns = [
    

    path('event-list/',event_list,name='event-list'),
    path('event-creat/',event_creat,name='event-creat'),
    path('event-details/<int:id>/',event_details,name="event-details"),
    path('event-update/<int:id>/',event_update,name="event-update"),
    path('event-delete/<int:id>/',event_delete,name="event-delete"),

    path('category-creat/',category_create,name="category-creat"),
    path('category-update/<int:id>/',category_update,name="category-update"),
    path('category-delete/<int:id>/',category_delete,name="category-delete"),
    path('category-list/',category_list,name="category-list"),

    path('participant-add/<int:id>/',participant_add,name="participant-add"),
    path('participant-delete/<int:id>/',participant_delete,name="participant-delete"),
    path('participant-list/',participant_list,name="participant-list"),
]
