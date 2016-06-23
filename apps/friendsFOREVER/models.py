from __future__ import unicode_literals
from django.db import models

class PersonManager(models.Manager):
    def createFriend(self, data):
        try:
            buddy = Person.objects.create(name = data['name'])
            buddy.save()
            return (True, {'yay': 'yeeee'} )
        except:
            raise
            return (False, {'boo': 'u suck'})
    def get_em(self):
        friends = Person.objects.all()
        return friends
        # print friends

class Person(models.Model):
    name = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    personManager = PersonManager()
    objects = models.Manager()

class Merges(models.Model):
    templar1 = models.ForeignKey(Person, related_name='initiator')
    templar2 = models.ForeignKey(Person, related_name='halp_me')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()
