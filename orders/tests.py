from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()
class OrdersTestCase(TestCase):    

    # Creates a new test database
    def setUp(self):
        # Creates a new user
        user_a = User(username="cfe", email='cfe@invalid.com')

        # The following line of code is essential the same as
        # User.objects.create() or User.objects.create_user()

        user_a_pw = 'some_123_password'
        
        # self. to make it available in the whole class. ex. in test_user_password()
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True        
        user_a.set_password(user_a_pw)
        user_a.save()

        self.user_a = user_a


    # def test_create_order(self):
    #   obj = Order.objects.create(user=self.user_a, product=product_a)
