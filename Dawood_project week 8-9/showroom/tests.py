from django.contrib.auth.models import Group, User
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APITestCase


class ShowroomRoleTests(APITestCase):
	def setUp(self):
		self.manager = User.objects.create_user(username='manager', password='test-password')
		self.manager.groups.add(Group.objects.create(name='Managers'))
		self.customer = User.objects.create_user(username='customer', password='test-password')
		self.customer.groups.add(Group.objects.create(name='Customers'))

	def test_dashboard_page_renders(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'showroom/index.html')

	def test_manager_can_create_update_and_delete_showrooms(self):
		self.client.force_authenticate(self.manager)
		response = self.client.post('/api/showrooms/', {
			'name': 'Central Motors',
			'location': 'Lahore',
			'certified_dealership': True,
			'phone_no': '03001234567',
		}, format='json')
		self.assertEqual(response.status_code, 201)
		showroom_url = f"/api/showrooms/{response.data['id']}/"
		self.assertEqual(self.client.patch(showroom_url, {'location': 'Karachi'}, format='json').status_code, 200)
		self.assertEqual(self.client.delete(showroom_url).status_code, 204)

	def test_customer_can_read_but_not_change_inventory(self):
		self.client.force_authenticate(self.customer)
		self.assertEqual(self.client.get('/api/showrooms/').status_code, 200)
		self.assertEqual(self.client.get('/api/cars/').status_code, 200)
		self.assertEqual(self.client.post('/api/showrooms/', {
			'name': 'Not allowed',
			'location': 'Lahore',
			'certified_dealership': False,
			'phone_no': '03001234567',
		}, format='json').status_code, 403)
		self.assertEqual(self.client.get('/api/customers/').status_code, 403)

	def test_token_contains_admin_configured_role(self):
		response = self.client.post('/api/token/', {
			'username': 'manager',
			'password': 'test-password',
		}, format='json')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(AccessToken(response.data['access'])['role'], 'manager')
