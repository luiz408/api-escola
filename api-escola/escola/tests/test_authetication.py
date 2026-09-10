from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste para verificar a autenticação com credenciais corretas."""
        usuario = authenticate(username='admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)     
    def test_autenticacao_user_username_incorreto(self):
            """Teste para verificar a autenticação com credenciais incorretas."""
            usuario = authenticate(username='wrong_user', password='admin')
            self.assertFalse((usuario is not None) and usuario.is_authenticated)
    def test_autenticacao_user_senha_incorreto(self):
            """Teste para verificar a autenticação com credenciais incorretas."""
            usuario = authenticate(username='admin', password='wrong_password')
            self.assertFalse((usuario is not None) and usuario.is_authenticated)
    def test_requisicao_get_autorizada(self):
        """Teste para verificar a requisição GET autorizada."""
        self.client.login(username='admin', password='admin')
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
                                                                                                                                                                                                                                                           