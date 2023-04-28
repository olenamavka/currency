from currency.models import Source


def test_get_api_rate_list(api_client):
    response = api_client.get('/v1/api/currency/rates/')
    assert response.status_code == 200


def test_post_api_rate_list_empty_form_status(api_client):
    response = api_client.post('/v1/api/currency/rates/')
    assert response.status_code == 400


def test_post_api_rate_list_empty_form(api_client):
    response = api_client.post('/v1/api/currency/rates/')
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_get_api_source_list_unauth(api_client):
    response = api_client.get('/v1/api/currency/source/')
    assert response.status_code == 401


def test_get_api_source_list_200(auth_client):
    response = auth_client.get('/v1/api/currency/source/')
    assert response.status_code == 200


def test_post_api_source_empty_form_status(auth_client):
    response = auth_client.post('/v1/api/currency/source/')
    assert response.status_code == 400


def test_post_api_source_empty_form(auth_client):
    response = auth_client.post('/v1/api/currency/source/')
    assert response.json() == {
        'source_url': ['This field is required.'],
        'name': ['This field is required.']
    }


def test_post_api_source_valid_data_status(auth_client):
    payload = {
        'source_url': 'https://api.monobank.ua',
        'name': 'mono'
    }
    response = auth_client.post('/v1/api/currency/source/', data=payload)
    assert response.status_code == 201


def test_post_api_source_valid_data(auth_client):
    initial_count = Source.objects.count()
    payload = {
        'source_url': 'https://api.monobank.ua',
        'name': 'mono'
    }
    response = auth_client.post('/v1/api/currency/source/', data=payload)  # noqa: F841
    assert Source.objects.count() == initial_count + 1


def test_put_api_source_empty_form_status(auth_client, test_source):
    response = auth_client.put(f'/v1/api/currency/source/{test_source.id}/')
    assert response.status_code == 400


def test_put_api_source_empty_form(auth_client, test_source):
    response = auth_client.put(f'/v1/api/currency/source/{test_source.id}/')
    assert response.json() == {
        'source_url': ['This field is required.'],
        'name': ['This field is required.']
    }


def test_put_api_source_valid_data_200(auth_client, test_source):
    payload = {
        'source_url': 'https://api.monobank.ua',
        'name': 'mono'
    }
    response = auth_client.put(f'/v1/api/currency/source/{test_source.id}/', data=payload)
    assert response.status_code == 200


def test_patch_api_source_valid_data_200(auth_client, test_source):
    payload = {
        'source_url': 'https://api.monobank.ua'
    }
    response = auth_client.patch(f'/v1/api/currency/source/{test_source.id}/', data=payload)
    assert response.status_code == 200


def test_patch_api_source_valid_data(auth_client, test_source):
    payload = {
        'source_url': 'https://api.monobank.ua'
    }
    response = auth_client.patch(f'/v1/api/currency/source/{test_source.id}/', data=payload)
    assert response.json() == {
        'id': test_source.id,
        'source_url': payload['source_url'],
        'name': test_source.name,
        'number': test_source.number
    }


def test_delete_api_source_status(auth_client, test_source):
    response = auth_client.delete(f'/v1/api/currency/source/{test_source.id}/')
    assert response.status_code == 204


def test_delete_api_source(auth_client, test_source):
    response = auth_client.delete(f'/v1/api/currency/source/{test_source.id}/')  # noqa: F841
    assert Source.objects.all().count() == 0
