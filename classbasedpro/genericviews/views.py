from django.shortcuts import render
from django.views import generic
from .forms import PersonForm
from .models import Person

def makeentry(request):
    if request.method=='POST':
        form=PersonForm(request.POST)
        if form.is_valid():
                name=request.POST.get('name','')
                desc=request.POST.get('desc=desc','')
                person=Person(name=name,desc=desc)
                person.save()
                form=PersonForm()
                return render(request,'genericviews/makeentry.html',{'form':form})
        else:
            form=PersonForm()
            return render(request,'genericviews/makeentry.html',{'form':form})


class IndexView(generic.ListView):
    context_object_name='list'
    template_name='genericviews/index.html'

    def get_queryset(self):
        return Person.objects.all()

class DetailsView(generic.DetailView):
    model=Person
    template_name='genericviews/detail.html'














