from currency.models import ContactUs


def test_get_contact_us(client):
    response = client.get('/currency/contact-us/create/')
    assert response.status_code == 200


def test_post_empty_form_200(client):
    response = client.post('/currency/contact-us/create/')
    assert response.status_code == 200


def test_post_empty_form_errors(client):
    response = client.post('/currency/contact-us/create/')
    assert response.context_data['form']._errors == {
        'name': ['This field is required.'],
        'email_from': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


def test_post_invalid_email_200(client):
    payload = {
        'name': 'Olena',
        'email_from': 'INVALID EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.status_code == 200


def test_post_invalid_email_error(client):
    payload = {
        'name': 'Olena',
        'email_from': 'INVALID EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.context_data['form']._errors == {'email_from': ['Enter a valid email address.']}


def test_post_valid_data_status(client):
    payload = {
        'name': 'Olena',
        'email_from': 'olena@example.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.status_code == 302


def test_post_valid_data_redirect(client):
    payload = {
        'name': 'Olena',
        'email_from': 'olena@example.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response['location'] == '/currency/contact-us/list/'


def test_post_valid_data_object(client):
    initial_count = ContactUs.objects.count()
    payload = {
        'name': 'Olena',
        'email_from': 'olena@example.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)  # noqa: F841
    assert ContactUs.objects.count() == initial_count + 1


def test_post_valid_data(client, mailoutbox, settings):
    payload = {
        'name': 'Olena',
        'email_from': 'olena@example.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)  # noqa: F841
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
