from django.test import TestCase
from .models import Data
# Create your tests here.
class NewTest(TestCase):
    @classmethod
    def setUpTestuerData(cls):
        data=Data.objects.create(X=5,Y=10)
        data.save()

    def TESTER(self):
        data=Data.objects.get(id=1)
        data1=data.X
        data2=data.Y
        self.assertEqual(data1,5)
        self.assertEqual(data2,10)


