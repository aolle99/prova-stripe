import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

stripe.api_key  = settings.STRIPE_SECRET_KEY

@csrf_exempt
def procesar_pago(request):
    if request.method == 'GET':
        total_amount = request.POST.get('total_amount')
        productos = [
            {
                'nombre': 'Una cris',
                'precio': 1000,
                'cantidad': 2
            },
            {
                'nombre': 'Otra criiis',
                'precio': 1500,
                'cantidad': 1
            }
        ]

        line_items = []
        for producto in productos:
            item = {
                'price_data': {
      'currency': 'eur',
      'unit_amount': producto["precio"],
      'product_data': {
        'name': producto["nombre"],
        'description': 'Comfortable cotton t-shirt',
        'images': ['https://static.wikia.nocookie.net/kingdomrushtd/images/5/56/Frontiers_Logo.png'],
      },
    },
    'quantity': producto["cantidad"],
            }
            line_items.append(item)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='http://tu-sitio.com/pago-exitoso',
            cancel_url='http://tu-sitio.com/pago-cancelado'
        )
        return redirect(session.url)
        """return render(request, 'procesar_pago.html', {
            'session_url': session.url,
            'total_amount': 2000,
            'productos': productos
        })"""

    return render(request, 'procesar_pago.html')


def pago_exitoso(request):
    return render(request, 'pago_exitoso.html')

def pago_cancelado(request):
    return render(request, 'pago_cancelado.html')