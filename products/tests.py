from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

# Test to see if a staff member and a non-staff member can create a product

User = get_user_model()

class ProductTestCase(TestCase):

# Creates a new test database
    def setUp(self):
        # Creates a new user
        user_a = User(username="akl", email='akl@invalid.com')

        # The following lines of code is essential the same as
        # User.objects.create() or User.objects.create_user()

        user_a_pw = 'password'
        
        # self. to make it awailable in the whole class. ex. in test_user_password()
        self.user_a_pw = user_a_pw
        self.user_a = user_a

        user_a.is_staff = True
        user_a.is_superuser = False        
        user_a.set_password(user_a_pw)
        user_a.save()
        

        # Create a second user
        user_b = User.objects.create_user("user_2", "user_2@invalid.com", "password")
        self.user_b = user_b


    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    
    # Test to see if user can create product
    def test_invalid_request(self):
        # User login
        self.client.login(username=self.user_b.username, password="password")
        response = self.client.post("/products/create/", 
        {"title": "This is an valid test"})        
        self.assertNotEqual(response.status_code, 200)
        
    # Test to see if user can create product
    def test_valid_request(self):
        # User login
        self.client.login(username=self.user_a.username, password="password")
        response = self.client.post("/products/create/", 
        {"title": "This is an valid test"})
        self.assertEqual(response.status_code, 200)

