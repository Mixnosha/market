from itertools import product

from django.http import HttpResponse
from django.shortcuts import redirect, render
from market.models import BuyProduct, Profile, Product, Basket, Delivery, Category


def deliv_delete(request):
    try:
        buy_prod = BuyProduct.objects.filter(delivery__delivery='Delivered')
        buy_prod.delete()
        return redirect('profile')
    except Exception:
        pass


def add_basket(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = Profile.objects.get(user=request.user)
            product = Product.objects.get(id=request.GET.get('add_product_id'))
            try:
                new_amount = Basket.objects.get(user=user, product=product)
                new_amount.amount = new_amount.amount + 1
                new_amount.save()
            except Exception:
                Basket.objects.create(user=user, product=product, status='доставка через 3 дня')
        else:
            return HttpResponse('Сначало нужно войти')
    return redirect('basket')


def buy_product_def(request):
    all_product = []
    for id in get_all_product_id(request):
        all_product.append(Product.objects.get(id=id))
    delivery = Delivery.objects.get(id=1)
    user = Profile.objects.get(user=request.user)
    for product in all_product:
        amount = get_amount(request, product)
        BuyProduct.objects.create(user=user, product=product, delivery=delivery, amount=amount)
    return redirect('profile')


def get_sum_product_price_basket(request):
    user = Profile.objects.get(user=request.user)
    try:
        all_basket = Basket.objects.filter(user=user)
        all_price = 0
        for obj in all_basket:
            all_price += obj.product.product_price*obj.amount
        return all_price
    except Exception:
        return False


def get_amount(request, product):
    return Basket.objects.get(user=Profile.objects.get(user=request.user), product=product).amount


def get_all_product_id(request):
    user = Profile.objects.get(user=request.user)
    all_product = Basket.objects.filter(user=user)
    all_product_id = []
    for product in all_product:
        all_product_id.append(product.product.id)
    return all_product_id


def buy_all(request):
    all_product = []
    for id in get_all_product_id(request):
        all_product.append(Product.objects.get(id=id))
    all_amount = {}
    for product in all_product:
        all_amount[product.product_name] = (get_amount(request, product))
    all_price = 0
    for p in all_product:
        all_price += p.product_price * all_amount[p.product_name]
    context = {
        'title': 'Buy_product',
        'all_product': all_product,
        'all_amount': all_amount,
        'all_price': all_price
    }
    return render(request, 'market/buy_product.html', context=context)