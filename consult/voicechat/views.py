from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Chat, Contact, Message
from call.models import Call
from boards.models import Post
from django.utils.safestring import mark_safe
import json

# Create your views here.

# ===== stt.html test =====
def stt(request):
    return render(request, 'stt.html')
# =========================

@login_required
def voicechat(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user.voice_active = False
        user.save()
        
        counselor_list = User.objects.filter(member_type='Counselor')
        context = {
            'counselor_list': counselor_list
        }
        
        return render(request, 'voicechat.html', context)
    else:
        return redirect('accounts:login')
    
@login_required
def room(request, room_name):
    user = User.objects.get(username=request.user.username)
    user.voice_active = True
    user.save()
    
    # 상담사 정보
    counselor = User.objects.get(id=room_name)
    
    # 고객 정보  --> 수정 중
    customer = None
    if request.user.member_type == 'Customer':
        customer = User.objects.get(id=request.user.id)
    
    # message = Message.objects.latest('timestamp')
    # customer = User.objects.get(id=message.user_id)
        
    customers = User.objects.filter(member_type='Customer')
    chats = Chat.objects.all()
    calls = Call.objects.all()
    
    # FAQ
    faqs = Post.objects.filter(category='FAQ')
        
    return render(request, "room.html", {"room_name": mark_safe(json.dumps(room_name)),
                                                'username': request.user.username,
                                                'counselor':counselor, 'customer':customer, 
                                                'customers':customers, 'chats':chats, 'calls':calls,
                                                'faqs':faqs})
