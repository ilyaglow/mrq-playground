from mrq import context
from mrq.job import queue_job

context.setup_context()

result = queue_job("crawler.Fetch", {
    "url": "http://docs.python-requests.org",
    "from": "whatever.com"
    }, queue="crawl")

print(result)
