from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
from django.db.models import Min, Max

def index(request):
    products = Product.objects.all()

    # Get minimum and maximum discounted prices (as integers)
    min_price = products.aggregate(Min('discounted_price'))['discounted_price__min']
    max_price = products.aggregate(Max('discounted_price'))['discounted_price__max']

    # Ensure minimum price is not None (in case no products exist)
    if min_price is None:
        min_price = 0

    min_price = int(min_price)
    max_price = int(max_price)

    price_step = 10000

    price_ranges = [(price, price + price_step) for price in range(0, max_price + 1, price_step)]

    # Get unique values for dropdown menus
    processors = Product.objects.values_list('processor', flat=True).distinct()
    rams = Product.objects.values_list('ram', flat=True).distinct()
    oss = Product.objects.values_list('os', flat=True).distinct()
    ssds = Product.objects.values_list('ssd', flat=True).distinct()
    displays = Product.objects.values_list('display', flat=True).distinct()

    context = {
        'products': products,
        'price_ranges': price_ranges,
        'processors': processors,
        'rams': rams,
        'oss': oss,
        'ssds': ssds,
        'displays': displays,
    }
    return render(request, 'index.html', context)


def search(request):
    price_range_str = request.GET.get('price_range', None)
    processor = request.GET.get('processor', '')
    ram = request.GET.get('ram', '')
    os = request.GET.get('os', '')
    ssd = request.GET.get('ssd', '')
    display = request.GET.get('display', '')

    products = Product.objects.all()

    if price_range_str:
        price_range = [int(x) for x in price_range_str.strip().split('_')]
        min_price, max_price = price_range
        products = products.filter(discounted_price__gte=min_price, discounted_price__lte=max_price)
    elif processor:
        products = products.filter(processor__icontains=processor)
    elif ram:
        products = products.filter(ram__icontains=ram)
    elif os:
        products = products.filter(os__icontains=os)
    elif ssd:
        products = products.filter(ssd__icontains=ssd)
    elif display:
        products = products.filter(display__icontains=display)

    context = {
        'products': products,
        'price_range': price_range if price_range_str else [],  # Empty list if no price range
        'processor': processor,
        'ram': ram,
        'os': os,
        'ssd': ssd,
        'display': display,
    }
    return render(request, 'results.html', context)