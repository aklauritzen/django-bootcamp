from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()
class UserTestCase(TestCase):    

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
        user_a.is_superuser = True        
        user_a.save()
        user_a.set_password(user_a_pw)
        

    # Test to see if user exists
    def test_user_exists(self):
        user_count = User.objects.all().count()

        # Test to see if user_count is equal to 1
        self.assertEqual(user_count, 1)

        # Test to see if user_account is NOT queal to 0
        self.assertNotEqual(user_count, 0)

    # Test to see if the test user password is correct
    def test_user_password(self):

        # Two solutions to test if password is correct

        # Solution 1
            # user_qs = User.objects.filer(username__iexact="akl")
            # user_exists = user_qs.exists() and user_qs.count() == 1
            # self.assertTrue(user_exists)
            # user_a = user_qs.first()

        # Solution 2
        # check_password is a build in method to check password
        self.assertTrue(
            self.user_a.check_password(self.user_a_pw)
        )


