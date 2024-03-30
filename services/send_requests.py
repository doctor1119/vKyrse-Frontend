import requests

def send_requests(start_date="2024-01-01", end_date="2024-01-02"):
    url = "http://localhost:8000/get-articles-by-period"
    request_body = {
        "start_date": start_date,
        "end_date": end_date
    }

    with requests.Session() as session:
        response = session.get(url=url, json=request_body)
    return response.json()

