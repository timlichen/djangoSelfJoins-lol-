from django.shortcuts import render, redirect
from .models import Person, Merges

def index(request):
    circle_of_friends = Person.personManager.get_em()
    pity_party = Merges.objects.all()
    hay = {'party': circle_of_friends,
           'LAN_PARTY': pity_party
          }
    return render(request, 'friends_app/index.html', hay)

def createFriend(request):
    data = { 'name': request.POST['name'] }
    notice_me = Person.personManager.createFriend(data)
    if notice_me[0]:
        print "yay friend"
    else:
        print "forever alone"
    return redirect('/')

def Bonding(request):
    print request.POST['friend1']
    print request.POST['friend2']
    data = { '1': request.POST['friend1'],
             '2': request.POST['friend2']
           }
    t1 = Person.objects.filter( pk = data['1'] )
    t2 = Person.objects.filter( pk = data['2'] )
    if t1 and t2:
        Merges.objects.create(templar1 = t1[0], templar2 = t2[0])
    return redirect('/')
