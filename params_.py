from tempfile import TemporaryFile

import requests
import xlwt
from bs4 import BeautifulSoup


class Product:
    def __init__(self):
        self.payload = {
            'type': 'requestNewProductList',
            'colId': '',
            'productsPerPage': '15',
            'sort': 'az',
            'lang': 'eng',
        }

# Parsing links to product technical description on each page
    def _parse_links(self, number_of_pages=None):
        print('parsing links from %s...' % self.file_name)
        links = []
        if number_of_pages == None:
            links = self._parse_links_all_pages(links)
        else:
            links = self._parse_links_selected_pages(links, number_of_pages)
        return links

    def _forming_links(self, current_page, links):
        self.payload['page'] = current_page
        r = requests.get(self.product_url + 'selector.php', params=self.payload)
        soup = BeautifulSoup(r.text, 'lxml')
        page_stuff = soup.find_all('td', {'class': 'desc'})
        for a in page_stuff:
            if a.find('a') != None:
                links.append(self.product_url + a.find('a').attrs['href'])
        return links

    def _parse_links_all_pages(self, links):
        current_page = 1
        while True:
            print('parsing links from %s ... page nmbr.%d' % (self.file_name, (current_page)))
            links = self._forming_links(current_page, links)
            r = requests.get(self.product_url + 'selector.php', params=self.payload)
            soup = BeautifulSoup(r.content, 'lxml')
            button_next = soup.find(class_='for btn icon_btn forward_btn ')
            if button_next == None:
                return links
            current_page += 1

    def _parse_links_selected_pages(self, links, number_of_pages):
        for current_page in range(1, number_of_pages + 1):
            links = self._forming_links(current_page, links)
            print('parsing links from %s ...%d%%' % (self.file_name, (current_page / number_of_pages * 100)))
        return links

# Parsing full technical description from each link
    def _parse_data(self, links):
        data = []
        i = 1
        for link in links:
            print('parsing technical descriptions from %s ...%d%%' % (self.file_name, i / len(links) * 100))
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'lxml')
            table = soup.find('table', id='pd_master_data')
            rows = table.find_all('tr')
            model = rows[0].find('td')
            article = rows[1].find('td')
            content = soup.find('li', id='techfeatures')
            items = content.find_all('li', class_='item')
            d = {
                'Model': model.text.split(' -')[0],
                'Article': article.text
            }
            for item in items:
                # If same key already exist save to (key + j)
                if item.find('em', class_='title').text in d:
                    for j in range(2, len(items)):
                        if item.find('em', class_='title').text + ' ' + str(j) in d:
                            continue
                        d[item.find('em', class_='title').text + ' ' + str(j)] = item.find('span').text
                        break
                else:
                    d[item.find('em', class_='title').text] = item.find('span').text
            i += 1
            data.append(d)
        return data

    def _save_to_excel(self, data):
        print('saving to %s...' % self.file_name)
        book = xlwt.Workbook()
        sheet = book.add_sheet(self.file_name)
        for col, c in enumerate(self.characteristics):
            sheet.write(0, col, c)
        for row, d in enumerate(data):
            for col, c in enumerate(self.characteristics):
                sheet.write(row + 1, col, d.get(c))
        name = self.file_name + '.xls'
        book.save(name)
        book.save(TemporaryFile())
        print('Saved to Excel! file ' + name)

    def parse(self, number_of_pages=None):
        # if number_of_pages == None:
        #    number_of_pages = self.pages()
        links = self._parse_links(number_of_pages)
        data = self._parse_data(links)
        self._save_to_excel(data)