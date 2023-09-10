from django.shortcuts import render,get_object_or_404
from .models import Item,Category
from django.db.models import Q

# Create your views here.
def items(request):
    query = request.GET.get('query','')
    items  =Item.objects.filter(is_sold =False)
    category_id =request.GET.get('category',0)
    categories = Category.objects.all()
    if category_id:
        items  = items.filter(category_id=category_id)
    if query: 
        items = items.filter(Q(name_icontains = query)| Q(description_icontains =query))
        
    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'category':categories,
        'category_id':int(category_id),
    })
def detail(request,pk):
    item =  get_object_or_404(Item,pk=pk)
    related_items  =Item.objects.filter(category=item.category,is_sold =False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
    'item':item,
    'related_item':related_items})