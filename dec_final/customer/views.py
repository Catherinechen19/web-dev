# from django.shortcuts import render, redirect
# from .forms import RequestForm

# # Create your views here.
# def request(request):
#     request = Request.objects.all()
#     if request.method == "POST":
#         form = RequestForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = request.user
#             form.save()
#             return redirect("requests-page")
#     else:
#         form = RequestForm()
#         context = {
#         'requests': requests,
#         'form': form,
#     }
#     return render(request, 'request/request.html', {'form': form})