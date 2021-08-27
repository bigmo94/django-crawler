import requests
from bs4 import BeautifulSoup

base_url = 'https://timcheh.com'


def get_categories(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    categories = soup.find_all('a', class_='nav_item_link')
    name_link = []
    for category in categories:
        name_link.append((category.get_text(), category.attrs['href']))
    return name_link


def get_product_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_html_tag = soup.select(
        '#__next > div.category_styles_main_body__O756o > div.container.clearfix > div.category_styles_content_page__3ew5u > div.row.category_styles_products_holder__2ZCFy > ul > li > a')
    products_link = []
    for tag in product_html_tag:
        products_link.append(base_url + tag.attrs['href'])
    return products_link


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')


def crawl_product_name(soup_page):
    try:
        name = soup_page.select_one(
            '#__next > div.product_styles_main_body__1Btj6 > div > div.product_styles_product_wrapper__1AnKQ > div.product_styles_product_info_holder__9IC6k > h1').get_text()
    except:
        name = ''
    return name


def crawl_product_price(soup_page):
    try:
        price = soup_page.select_one(
            '#__next > div.product_styles_main_body__1Btj6 > div > div.product_styles_product_wrapper__1AnKQ > div.product_styles_product_info_holder__9IC6k > div.product_styles_info_price__3P4Ei > div > span.product_styles_price__3Ws3t').get_text()
    except:
        price = ''
    return price


def crawl_product_color(soup_page):
    try:
        color = soup_page.select_one(
            '#__next > div.product_styles_main_body__1Btj6 > div > div.product_styles_product_wrapper__1AnKQ > div.product_styles_product_info_holder__9IC6k > div.product_styles_info_variant__tBbvU > div.product_styles_item__JnLL- > span.product_styles_value__1oJcf').get_text()
    except:
        color = ''
    return color


def crawl_product_seller(soup_page):
    try:
        seller = soup_page.select_one(
            '#__next > div.product_styles_main_body__1Btj6 > div > div.product_styles_product_wrapper__1AnKQ > div.product_styles_info_seller__3Q-Wg > div.product_styles_seller_table__19qhL > div > div.product_styles_cell_table__2pzhT.product_styles_head__-844O > a').get_text()
    except:
        seller = ''
    return seller


def crawl_product():
    categories = get_categories(base_url)
    all_products_option = []
    for category in categories:
        products_links = get_product_link(base_url + category[1])
        for link in products_links:
            soup = get_soup(link)
            name = crawl_product_name(soup)
            price = crawl_product_price(soup)
            color = crawl_product_color(soup)
            seller = crawl_product_seller(soup)
            all_products_option.append((category[0], name, price, color, seller))

    return all_products_option





