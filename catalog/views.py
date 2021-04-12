from django.shortcuts import render, get_object_or_404
from django.views import generic
from catalog.models import Product, Category


class ProductListView(generic.ListView):

    # the context name will be model_name + _list -> product_list
    model = Product
    template_name = 'catalog/product_list.html'
    # add a query named ?page=<number> to url
    paginate_by = 2


class CategoryListView(generic.ListView):

    # model = Product -> sobreescrevendo o model eu não preciso informar o model
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


class ProductView(generic.TemplateView):

    template_name = 'catalog/product.html'

    def get(self, request, **kwargs):
        current_product = Product.objects.get(slug=self.kwargs['slug'])
        context = {
            'current_product': current_product
        }
        return render(request, 'catalog/product.html', context=context)


product_list = ProductListView.as_view()
category = CategoryListView.as_view()
product = ProductView.as_view()


# old example
# def product(request, slug):
#     current_product = Product.objects.get(slug=slug)
#     context = {
#         'current_product': current_product
#     }
#     return render(request, 'catalog/product.html', context=context)