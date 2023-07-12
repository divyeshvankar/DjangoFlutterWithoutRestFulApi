from django.shortcuts import render
from django.conf import settings
import stripe
# Create your views here.

from django.views.generic.base import TemplateView

stripe.api_key= settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs): #new
        context = super().get_context_data(**kwargs)
        context['key']=settings.STRIPE_PUBLISHABLE_KEY
        return context


# new to render charge.html and make payment using diffrent API : PaymentIntent without saving card info

# def charge(request):
#     if request.method == 'POST':
#         intent = stripe.PaymentIntent.create(
#             amount=500,
#             currency='inr',
#             description='Payment Gateway',
#             payment_method_data={
#                 'type': 'card',
#                 'card': {
#                     'token': request.POST['stripeToken'],
#                 },
#             },
#             confirm=True,
#         )
#         return render(request, 'charge.html')

def charge(request):
    if request.method == 'POST':
        # Create a new customer
        customer = stripe.Customer.create(
            email=request.POST['stripeEmail'],
            source=request.POST['stripeToken']
        )

        # Use the customer's stored card details for the payment intent
        intent = stripe.PaymentIntent.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            customer=customer.id,
            payment_method=customer.default_source,
            confirm=True,
        )
        # print(response.card)
        # customer_ID=customer_id
        print("customer id is:"+customer.id)

        return render(request, 'charge.html')




# below code for deduct money from credit again

# def charge(request):
#     if request.method == 'POST':
#         # Use the customer's stored card details for the payment intent
#         intent = stripe.PaymentIntent.create(
#             amount=500,  # Set this to the new charge amount
#             currency='inr',
#             description='Further Deduction',
#             customer='cus_XXXXX',  # The customer's ID
#         )

#         return render(request, 'charge.html')




