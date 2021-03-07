from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.views.generic import View
from users import models as user_models
from . import models, forms

def go_converstation(request, a_pk, b_pk):
    host = user_models.User.objects.get_or_none(pk=a_pk)
    guest = user_models.User.objects.get_or_none(pk=b_pk)
    if host is not None and guest is not None:
        try:
            converstation = models.Conversation.objects.get(
            Q(participants=host) & Q(participants=guest)
         )
        except models.Conversation.DoesNotExist:
             converstation = models.Conversation.objects.create()
             converstation.participants.add(host, guest)

    return redirect(reverse("converstations:detail", kwargs={'pk': converstation.pk}))


class ConversationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))
