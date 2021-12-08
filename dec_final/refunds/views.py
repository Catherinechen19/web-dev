#from django.shortcuts import render, redirect
#from .forms import RefundForm

# Create your views here.
#def refund(request):
#    if request.method == "POST":
#        form = RefundForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("refund")
#    else:
#       form = RefundForm()
#    return render(request, 'refund/refund.html', {'form': form})