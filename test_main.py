from . import Crawler
import pytest

dictionary = {
        "keywords": ["nova", "css"],
        "proxies": ["154.202.121.124:3128"],
        "type": "Repositories"
    }

def test_crawler_properties_proxies():
    a = Crawler(**dictionary)
    assert a.proxies == ["154.202.121.124:3128"]

def test_crawler_properties_keyword():
    a = Crawler(**dictionary)
    assert a.keywords == ["nova", "css"]

def test_crawler_properties_type():
    a = Crawler(**dictionary)
    assert a.type == "Repositories"

def test_crwaler_type_none():
    dictionary = {
        "keywords": ["nova", "css"],
        "proxies": ["154.202.121.124:3128"],
    }
    a = Crawler(**dictionary)
    assert a.type == "repositories"


def test_crawler_search():
    a = Crawler(**dictionary)
    assert type(a.search()) == list

def test_random_proxy():
    a = Crawler(**dictionary)
    assert a.random_proxy() == "154.202.121.124:3128"

def test_crawler_properties():
    a = Crawler(**dictionary)
    assert a.supported_types == ["repositories", "issues", "wikis"]