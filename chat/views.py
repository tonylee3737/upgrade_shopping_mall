from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden

def chat_room(request):
    return render(request,'chat/room.html')

