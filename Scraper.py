import PriceChecker, requests
from bs4 import BeautifulSoup


class MainScraper():

    def __init__(self, url):

        #use link to pull site content
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        page = requests.get(url, headers=headers) #headers=headers
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def title(self):
        raise NotImplementedError

    def price_finder(self):
        raise NotImplementedError

    def image_url(self):
        raise NotImplementedError

class BHPhoto(MainScraper):

    def __init__(self, url):
        MainScraper.__init__(self, url)

    def title(self):
        title = self.soup.find(**{'data-selenium': 'productTitle'}).get_text()
        return title

    def price_finder(self):
        unformatted_price = self.soup.find(**{'data-selenium': 'pricingPrice'}).get_text()
        formatted_price = float(unformatted_price[1:].replace(',', ''))
        return formatted_price

    def image_url(self):
        image_data = self.soup.find(**{'data-selenium': 'inlineMediaMainImage'})
        image_url = image_data['src']
        return image_url

#working but low quality image - probably something to do with website being react based. 
class Ulta(MainScraper):

    def __init__(self, url):
        MainScraper.__init__(self, url)

    def title(self):
        title = self.soup.find('div', **{'class': 'ProductMainSection__productName'}).get_text()
        return title

    def price_finder(self):
        unformatted_price = self.soup.find('div', **{'class': 'ProductPricingPanel'}).get_text()
        formatted_price = float(unformatted_price[6:].replace(',', ''))
        return formatted_price

    def image_url(self):
        image_data = self.soup.find(**{'class': 'ProductDetail'})
        all_images = image_data.findAll('img')[1]
        image_url = all_images['src']
        return image_url
        
        
#must use bestbuy API to scrape https://bestbuyapis.github.io/api-documentation/#response-format
""" class BestBuy(MainScraper):

    def title(self, soup):
        title = soup.find(class='sku-title').get_text()
        return title

    def price_finder(self, soup):
        current_price = soup.find(class='sku-title').get_text()
        selling_price = float(current_price[1:].replace(',', ''))
        return current_price, selling_price

    def image_url(self, soup):
        image_data = soup.find(**{'data-selenium': 'inlineMediaMainImage'})
        image_url = image_data['src']
        return image_url  """

#walmart api should allow scraping: https://developer.walmartlabs.com/docs
# class Walmart(MainScraper):


#working except for price block - need to investigate if there is an API or workaround
#price block is in react stuffs :( - only way would be to use selenium likely
""" class Target(MainScraper):

    def __init__(self, url):
        MainScraper.__init__(self, url)

    def title(self):
        title = self.soup.find(**{'data-test': 'product-title'}).get_text()
        return title

    def price_finder(self):
        unformatted_price = self.soup.find('div', **{'class': 'h-padding-b-default'}).get_text()
        print(f'Unformatted Price: { unformatted_price }')
        formatted_price = float(unformatted_price[1:].replace(',', ''))
        print(f'Formatted Price: { formatted_price }')
        return 250.00

    def image_url(self):
        image_data = self.soup.find(**{'data-test': 'carousel-image'})
        # print(f'Image Data: { image_data }')
        image_url = image_data.img['src']
        # print(f'Image Url: { image_url }')
        return image_url """

#requires the passing of headers to scrape properly
#amazon blocks scraping requests frequently as well :( need to find more reliable way
#removing amazon scraping for now
""" class Amazon(MainScraper):

    def __init__(self, url):
        MainScraper.__init__(self, url)
        print(self.soup)

    def title(self):
        title = self.soup.find('span', **{'id': 'productTitle'}).get_text()
        print(title)
        return title

    def price_finder(self):
        unformatted_price = self.soup.find('span', **{'id': 'priceblock_ourprice'}).get_text()
        print(unformatted_price)
        formatted_price = float(unformatted_price[1:].replace(',', ''))
        return formatted_price

    def image_url(self):
        image_data = self.soup.find('img', **{'id': 'landingImage'})
        image_url = image_data['src']
        return image_url  """