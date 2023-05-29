import json
import sys
import pytest
import os

# Add the project directory to the sys path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api(client):
    response = client.get('/allBerryStats')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'berries_names' in data
    assert 'min_growth_time' in data
    assert 'median_growth_time' in data
    assert 'max_growth_time' in data
    assert 'variance_growth_time' in data
    assert 'mean_growth_time' in data
    assert 'frequency_growth_time' in data
