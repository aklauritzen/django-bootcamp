from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()
class UserTestCase(TestCase):    

    # Creates a new test database
    def setUp(self):
        # Creates a new user
        user_a = User(username="cfe", email='cfe@invalid.com')

        # The following lines of code is essential the same as
        # User.objects.create() or User.objects.create_user()

        user_a_pw = 'some_123_password'
        
        # self. to make it awailable in the whole class. ex. in test_user_password()
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True        
        user_a.set_password(user_a_pw)
        user_a.save()

        self.user_a = user_a
        
        

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
        user_a = User.objects.get(username="cfe")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )

    def test_login_url(self):
        # login_url = "/login/"
        # self.assertEqual(settings.LOGIN_URL, login_url)

        login_url = settings.LOGIN_URL
        
        # python requests - manage.py runserver
        # self.client.get, self.client.post
        # response = self.client.post(url, {}, follow=True)
        data = {"username": "cfe", "password": "some_123_password"}
        response = self.client.post(login_url, data, follow=True)
        # print(dir(response))
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")

        print(f"Redirect_path: {redirect_path}")
        print(f"settings.LOGIN_REDIRECT_URL: {settings.LOGIN_REDIRECT_URL}")

        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)
