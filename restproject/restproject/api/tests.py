from django.test import TestCase
from api.models import Bucketlist


# Create your tests here.


class ModelTestCase(TestCase):

    def SetUp(self):
        self.bucketlist_name = "Write World class Code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_crate_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
