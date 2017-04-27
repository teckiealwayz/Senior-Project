from django.shortcuts import render

# Create your views here.
def product_list(request, category_slug=None)
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	context = {'category': category,
				'categories': categories,
				'products': products,
				}
	template = 'list.html'
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, template, context)


def product_detail(request,id, slug):
	product = get_object_or_404(Product,id=id, slug=slug, available=True)
	cast_product_form = CartAddProductForm()
	template = 'detail.html'
	context = {'product': product,
				'cast_product_form': cast_product_form
				}
	return render(request, template, context)