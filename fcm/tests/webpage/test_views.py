from flask import url_for
import re

# Checking if there is in all pages the title tag
tag_ptrn = re.compile(r'.*<title>.+</title>.*', re.S)


class TestWebpage(object):
    def test_dashboard_page(self, client):
        r = client.get(url_for('webpage.dashboard'))
        assert r.status_code == 200
        assert re.search(tag_ptrn, str(r.data))

    def test_customers_page(self, client):
        r = client.get(url_for('webpage.customers'))
        assert r.status_code == 200
        assert re.search(tag_ptrn, str(r.data))

    def test_products_page(self, client):
        r = client.get(url_for('webpage.products'))
        assert r.status_code == 200
        assert re.search(tag_ptrn, str(r.data))

    def test_orders_page(self, client):
        r = client.get(url_for('webpage.orders'))
        assert r.status_code == 200
        assert re.search(tag_ptrn, str(r.data))
