from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from review.models import Review
from transaction.models import Transaction
from refunds.models import Refund
from review.models import Post
from review.models import Replie
from customer.models import Request
from .forms import ReviewForm, RefundForm, RequestForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main/home.html', context)

def history(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions
    }
    return render(request, 'main/history.html', context)

def catalogue(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main/catalogue.html', context)

def request(request):
    requests = Request.objects.all()
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("requests-page")
    else:
        form = RequestForm()
    context = {
        'requests': requests,
        'form': form,
    }
    return render(request, 'main/request.html', context)

def registration(request):
    return render(request, 'main/registration.html', {})

def refund(request):
    refunds = Refund.objects.all()
    if request.method == "POST":
        form = RefundForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("refund-page")
    else:
        form = RefundForm()
    context = {
        'refunds': refunds,
        'form': form,
    }
    return render(request, 'main/refund.html', context)

def review(request):
    reviews = Review.objects.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("review-page")
    else:
        form = ReviewForm()
    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'main/review.html', context)

def forum(request):
    if request.method=="POST":   
        user = request.user
        content = request.POST.get('content','')
        post = Post(user1=user, post_content=content)
        post.save()
        alert = True
        return render(request, "review/forum.html", {'alert':alert})
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, "review/forum.html", {'posts':posts})

def discussion(request, myid):
    post = Post.objects.filter(id=myid).first()
    replies = Replie.objects.filter(post=post)
    if request.method=="POST":
        user = request.user
        desc = request.POST.get('desc','')
        post_id =request.POST.get('post_id','')
        reply = Replie(user = user, reply_content = desc, post=post)
        reply.save()
        alert = True
        return render(request, "review/discussion.html", {'alert':alert})
    return render(request, "review/discussion.html", {'post':post, 'replies':replies})