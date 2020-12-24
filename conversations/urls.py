from django.urls import path
from . import views

app_name = "converstations"

urlpatterns = [
    path("go/<int:a_pk>/<int:b_pk>", views.go_converstation, name="go"),
    path("<int:pk>/", views.ConversationDetailView.as_view(), name="detail"),
    
    
]