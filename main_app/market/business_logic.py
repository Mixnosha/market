from django.http import HttpResponse
from django.shortcuts import redirect
from market.models import BuyProduct, Profile, Product, Basket, Delivery


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
    deliv = Delivery.objects.get(id=1)
    pr_id = request.GET.get('change_profile')
    user = Profile.objects.get(user=request.user)
    try:
        product = Product.objects.get(id=pr_id)
    except Exception:
        return HttpResponse('Данный продукт уже не продается :(')
    try:
        del_bas = Basket.objects.get(user=user, product=product)
        BuyProduct.objects.create(user=user, product=product, delivery=deliv, amount=del_bas.amount)
        del_bas.delete()
    except Exception as es:
        return HttpResponse(':(')
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


