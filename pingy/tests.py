from django.test import TestCase
from django.utils import timezone
from .models import Website
from users.models import CustomUser
import datetime

class WebsiteModelTest(TestCase):
    def setUp(self):
        # Stwórz testowego użytkownika
        self.user = CustomUser.objects.create(email="testuser@user.user", password="testpass123")

        # Stwórz obiekt Website
        self.website = Website.objects.create(
            owner=self.user,
            address='https://example.com',
            status='offline',
            last_checked=timezone.now()
        )

    def test_website_creation(self):
        """Testuje, czy obiekt Website został prawidłowo utworzony."""
        self.assertEqual(self.website.owner, self.user)
        self.assertEqual(self.website.address, 'https://example.com')
        self.assertEqual(self.website.status, 'offline')
        self.assertIsNotNone(self.website.last_checked)

    def test_website_str(self):
        """Testuje metodę __str__."""
        expected_object_name = f"{self.website.address} (status: {self.website.status})"
        self.assertEqual(str(self.website), expected_object_name)

    def test_status_change(self):
        """Testuje zmianę statusu Website."""
        self.website.status = 'online'
        self.website.save()
        self.assertEqual(self.website.status, 'online')

    def test_address_change(self):
        """Testuje zmianę adresu URL Website."""
        new_address = "https://examplechanged.com"
        self.website.address = new_address
        self.website.save()
        updated_website = Website.objects.get(id=self.website.id)
        self.assertEqual(updated_website.address, new_address)

    def test_last_checked_update(self):
        """Testuje aktualizację daty ostatniego sprawdzenia Website."""
        new_time = timezone.now() + datetime.timedelta(days=1)
        self.website.last_checked = new_time
        self.website.save()
        updated_website = Website.objects.get(id=self.website.id)
        self.assertEqual(updated_website.last_checked.replace(microsecond=0), new_time.replace(microsecond=0))

    def test_related_name(self):
        """Testuje, czy related_name działa prawidłowo."""
        self.assertEqual(self.user.urls.count(), 1)
        self.assertEqual(self.user.urls.first(), self.website)
