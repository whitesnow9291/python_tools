from outscraper import ApiClient

api_client = ApiClient(api_key='SECRET_API_KEY')

# Search for businesses in specific locations:
result = api_client.google_maps_search('restaurants brooklyn usa', limit=20, language='en')

# Get data of the specific place by id
result = api_client.google_maps_search('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', language='en')

# Search with many queries (batching)
result = api_client.google_maps_search([
    'restaurants brooklyn usa',
    'bars brooklyn usa',
], language='en')

print(result)