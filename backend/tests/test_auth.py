import pytest
from app import create_app, db
from app.models.user import User

def setup_module(module):
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.drop_all()
        db.create_all()
        user = User(email='test@example.com')
        user.set_password('testpass')
        db.session.add(user)
        db.session.commit()

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.drop_all()
        db.create_all()
        user = User(email='test@example.com')
        user.set_password('testpass')
        db.session.add(user)
        db.session.commit()
    return app.test_client()

def test_register(client):
    response = client.post('/auth/register', json={
        'email': 'newuser@example.com',
        'password': 'newpass'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Usuário criado com sucesso.'

def test_login_success(client):
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert 'token' in response.data.decode()

def test_login_fail(client):
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    data = response.get_json()
    assert data['error'] == 'Credenciais inválidas'
