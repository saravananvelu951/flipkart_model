from django import template

register = template.Library()

@register.filter(name="incart")
def incart(product,cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return True
    return False

@register.filter(name="cart_quantaty")
def cart_quantaty(product,cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return cart.get(key)
    return False 
    
@register.filter(name="total_price")
def total_price(product,cart):
    return product.product_price * cart_quantaty(product,cart)
    
@register.filter(name="payable_amount")
def payable_amount(product,cart):
    total = 0
    for i in product: 
        total = total + total_price(i,cart)
    return total

@register.filter(name="order_total_price")
def order_total_price(price,quantity):
    
    return price * quantity  
