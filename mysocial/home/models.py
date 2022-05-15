from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from .utils import *



# user post model 
class Postmodel(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    likeCount=models.IntegerField(default=0,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Postmodel, self).save(*args, **kwargs)


# followsystem model
class Followmodel(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE)
    following=models.IntegerField()
    state=models.BooleanField(default=True)

    def __str__(self):
        f1=self.follower.username
        f2=self.following
        val= f1 + " follows " + str(f2)
        return val

    def getstate(self):
        return self.state



# likes model 
class likes(models.Model):
    likerUser=models.ForeignKey(User,on_delete=models.CASCADE)
    likedPost=models.ForeignKey(Postmodel,on_delete=models.CASCADE)
    state=models.BooleanField(default=True)

    def __str__(self):
        myuser=self.likerUser.username
        mypost=self.likedPost.title
        val=mypost+" liked by "+myuser
        return val

    def getstate(self):
        return self.state



#comment model
class comments(models.Model):
    commenter=models.ForeignKey(User, on_delete=models.CASCADE)
    commentedPost=models.ForeignKey(Postmodel, on_delete=models.CASCADE)
    commentText=models.CharField(max_length=2000)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.commentText

