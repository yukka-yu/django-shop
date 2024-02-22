from django.core.management.base import BaseCommand
from Orderapp.models import OrderModel, ProductModel, ClientModel

class Command(BaseCommand):
    help = "Delete order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = OrderModel.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()