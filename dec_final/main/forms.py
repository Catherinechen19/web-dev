from django.forms import ModelForm
from review.models import Review
from refunds.models import Refund
from customer.models import Request
from review.models import Post

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'created_at', ]

        
class RefundForm(ModelForm):
    class Meta:
        model = Refund
        exclude = ['user', 'status',]

class RequestForm(ModelForm):
     class Meta:
        model = Request
        exclude = ['user', ]

# class PostForm(ModelForm):
#      class Meta:
#         model = Post
#         exclude = ['user1', 'post_id', 'timestamp',]