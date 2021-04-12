from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy
from catalog.models import Product, Category


class CategoryListTestCase(TestCase):

    def setUp(self) -> None:
        self.category = mommy.make(Category)
        self.url = reverse('catalog:category', kwargs={'slug': self.category.slug})
        self.client = Client()

    def tearDown(self) -> None:
        self.category.delete()

    def test_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "catalog/category.html")

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('current_category' in response.context)


class ProductListTestCase(TestCase):
    # The pagination tests are based on products created by models_mommy

    def setUp(self) -> None:
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = mommy.make(Product, _quantity=10)

    def tearDown(self) -> None:
        map(lambda product: product.delete(), self.products)

    def test_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "catalog/product_list.html")

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('product_list' in response.context)

    def test_number_of_products_per_page(self):
        response = self.client.get(self.url)
        product_list = response.context['product_list']
        self.assertEquals(product_list.count(), 2)

    def test_number_of_pages(self):
        response = self.client.get(self.url)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 5)

    def test_page_not_found(self):
        response = self.client.get('{}?page=6'.format(self.url))
        self.assertEquals(response.status_code, 404)
