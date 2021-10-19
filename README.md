# GithubCrawler
Crawls Github Search Results for repository Urls

A Simple Github Crawler that can be imported as a module to another applicaiton

If you would like to use it as a module to another application, clone the repository to your project folder and:

    import Githubcrawler

    dictionary = {
            "keywords": ["nova", "css"],
            "proxies": ["154.202.121.124:3128"],
            "type": "Repositories"
        }
    
    a = Githubcralwer.Crawler(**dictionary)
    
    a.search()

requirements

    requests
    coverage
    pytest
    bs4

To run test coverage:

    coverage run -m pytest
    coverage report