from django.db import models

# Create your models here.
class HostGroup(models.Model):
    groupname=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.groupname

class Hosts(models.Model):
    hostname=models.CharField(max_length=50,unique=True)
    ipaddr=models.CharField(max_length=15,unique=True)
    group = models.ForeignKey(HostGroup,on_delete=models.CASCADE)

    def __str__(self):
        return '<%s : %s>' % (self.ipaddr,self.group)

class AnsiMod(models.Model):
    modulename = models.CharField(max_length=15)

    def __str__(self):
        return self.modulename

class ModArgs(models.Model):
    arg_text = models.CharField(max_length=300)
    mod = models.ForeignKey(AnsiMod,on_delete=models.CASCADE)

    def __str__(self):
        return '<%s "%s">' % (self.arg_text,self.mod)
