from django.shortcuts import render
from .models import Host,HostGroup,AnsiModule,ModArg
# Create your views here.
def home(request):
    return render(request,'home.html')
def addhosts(request):
    if request.method=='POST':
        hostname = request.POST.get('host')
        ipaddr = request.POST.get('ipaddr')
        groupname = request.POST.get('hostgroup')
        if hostname and ipaddr and groupname:
            HostGroup.objects.get_or_create(groupname=groupname)
            group = HostGroup.objects.get(groupname=groupname)
            Host.objects.create(hostname=hostname,ipaddr=ipaddr,group_id=group.id)
        else:
            pass

    hostgroup = HostGroup.objects.all()
    hostnames = Host.objects.all()
    # return render(request,'addhosts.html',{'hostnames':hostnames})
    return render(request,'addhosts.html',{'hostgroup':hostgroup})
