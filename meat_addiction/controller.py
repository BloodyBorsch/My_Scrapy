from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from spiders.artplast import ArtplastSpider

if __name__ == "__main__":
    catalog_url = "/catalog/korobki-dly-piccy/"
    
    configure_logging()
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    process = CrawlerProcess(get_project_settings())
    process.crawl(ArtplastSpider, query=catalog_url)
    process.start()