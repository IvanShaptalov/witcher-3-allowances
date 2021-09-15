import random

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .utilities import sign_form_data
from payment import constant, utilities


def donations(request):
    rand_num = random.randint(0, 99999999999)
    merchant_id = constant.merchant_id
    context = {'merchant': merchant_id,
               'externalid': rand_num}
    return render(request, 'main/pre_payment.html', context)


def handle_donation(request):
    data = request.POST
    key = constant.sci_key
    pre_result_data = dict(data)
    result_dict = utilities.prepare_dictionary_to_sign(pre_result_data)
    sign = sign_form_data(key=key, data=result_dict)
    #  todo this part

    print('handled')
    context = result_dict
    context['sign'] = sign
    return render(request, 'main/payment.html', context=context)


def donation_done(request):
    return render(request, 'main/payment_done.html')
