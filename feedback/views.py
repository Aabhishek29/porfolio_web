from django.shortcuts import render
from .models import FeedBackClass
import uuid
import datetime


# Create your views here.


def genrateUUId():
    return uuid.uuid4().hex[:15]

def getfeed(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['msg']
        userId = genrateUUId()
        createdAt = datetime.datetime.now()
        print(f"{name}  {mail}  {subject}  {msg}  {userId}  {createdAt}")
        feed = FeedBackClass(name = name, mail = mail, subject = subject,
                msg = msg, fid = userId, createdAt = createdAt)
        try:
            feed.save()
            print("data saved sucessfully...")
        except Exception as e:
            print("There is some issue in saving feedback",e)
        return render(request,'contactme.html')


