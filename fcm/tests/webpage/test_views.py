from flask import url_for


class TestWebpage(object):
    def test_dashboard_page(self, client):
        r = client.get(url_for('webpage.dashboard'))
        assert r.status_code == 200

    def test_customers_page(self, client):
        r = client.get(url_for('webpage.customers'))
        assert r.status_code == 200

    def test_products_page(self, client):
        r = client.get(url_for('webpage.products'))
        assert r.status_code == 200

    def test_orders_page(self, client):
        r = client.get(url_for('webpage.orders'))
        assert r.status_code == 200
