from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from . import forms
from rooms import models as room_models

def create_review(request, room):
    if request.method =="POST":
        form = forms.CreateReviewForm(request.POST)
        room = room_models.Room.objects.get_or_none(pk=room)
        if not room:
            return redircet(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.room = room
            review.user = request.user
            review.save()
            messages.success(reqeust, "Room reviewed")
            return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))
