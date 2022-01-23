import driver as driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element(By.ID,"menu-item-50").click()
email_address = driver.find_element(By.ID,"username")
email_address.send_keys("Smit@bk.ru")
password = driver.find_element(By.ID,"password")
password.send_keys("Smit.007qq")
login = driver.find_element(By.CSS_SELECTOR,"[name=login]").click()
shop_btn = driver.find_element(By.ID,"menu-item-40").click()
book_html5 = driver.find_element(By.PARTIAL_LINK_TEXT,"HTML5 Forms").click()
time.sleep(3)
name_book = driver.find_element(By.CSS_SELECTOR,".product_title.entry-title")
book_text = name_book.text
assert book_text == "HTML5 Forms"
driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element(By.ID,"menu-item-50").click()
email_address = driver.find_element(By.ID,"username")
email_address.send_keys("Smit@bk.ru")
password = driver.find_element(By.ID,"password")
password.send_keys("Smit.007qq")
login = driver.find_element(By.CSS_SELECTOR,"[name=login]").click()
shop_btn = driver.find_element(By.ID,"menu-item-40").click()
html = driver.find_element(By.LINK_TEXT,"HTML").click()
products = driver.find_elements(By.CLASS_NAME,"attachment-shop_catalog")
if len(products) == 3:
    print("3 товара в категории HTML")
else:
    print("Ошибка. Количество товаров: ",str(len(products)))
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element(By.ID,"menu-item-50").click()
email_address = driver.find_element(By.ID,"username")
email_address.send_keys("Smit@bk.ru")
password = driver.find_element(By.ID,"password")
password.send_keys("Smit.007qq")
login = driver.find_element(By.CSS_SELECTOR,"[name=login]").click()
shop_btn = driver.find_element(By.ID,"menu-item-40").click()
default_sorting = driver.find_element(By.CSS_SELECTOR,"[value=menu_order]")
default_sorting = default_sorting.get_attribute("selected")
if default_sorting is None:
    print("Стоит другая сортировка")
else:
    print("Выбрана сортировка по умолчанию")
element_selector = driver.find_element(By.CLASS_NAME,"orderby")
select = Select(element_selector)
select.select_by_index("4")
low_to_high = driver.find_element(By.CSS_SELECTOR,"[value=price]")
low_to_high = low_to_high.get_attribute("selected")
if low_to_high is None:
    print("Стоит другая сортировка")
else:
    print("Сортировка от большего к меньшему")
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element(By.ID,"menu-item-50").click()
email_address = driver.find_element(By.ID,"username")
email_address.send_keys("Smit@bk.ru")
password = driver.find_element(By.ID,"password")
password.send_keys("Smit.007qq")
login = driver.find_element(By.CSS_SELECTOR,"[name=login]").click()
shop_btn = driver.find_element(By.ID,"menu-item-40").click()
android_qs = driver.find_element(By.PARTIAL_LINK_TEXT,"Android Quick Start Guide").click()
price = driver.find_element(By.CSS_SELECTOR,"del>.woocommerce-Price-amount")
price = price.text
assert price == "₹600.00"
price_new = driver.find_element(By.CSS_SELECTOR,"ins>.woocommerce-Price-amount")
price_new = price_new.text
assert price_new == "₹450.00"
wait = WebDriverWait(driver, 5)
cover = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME,"attachment-shop_single")))
cover.click()
close = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME,"pp_close")))
close.click()
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element(By.ID,"menu-item-40").click()
add_to_basket = driver.find_element(
    By.CSS_SELECTOR,"#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart"
).click()
time.sleep(3)
number_goods = driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
number_goods_text = number_goods.text
assert number_goods_text == "1 Item₹180.00"
number_goods.click()
wait = WebDriverWait(driver, 5)
element_subtotal= wait.until(
    EC.text_to_be_present_in_element((
    By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div.cart-collaterals > div > table > tbody > tr.cart-subtotal > td"
    ),"₹180.00"))
element_total= wait.until(
    EC.text_to_be_present_in_element((
    By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > form > table > tbody > tr.cart_item > td.product-subtotal > span"
    ),"₹180.00"))
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element(By.ID,"menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
to_basket_html = driver.find_element(
    By.CSS_SELECTOR,"#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart"
).click()
time.sleep(3)
to_basket_jsdata = driver.find_element(
    By.CSS_SELECTOR,"#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart"
).click()
basket = driver.find_element(By.CLASS_NAME,"wpmenucart-contents").click()
time.sleep(3)
delete_html = driver.find_element(
    By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a"
                                  ).click()
time.sleep(3)
undo_btn = driver.find_element(
    By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > div.woocommerce-message > a"
).click()
quantity_jsdata = driver.find_element(
    By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input"
)
quantity_jsdata.clear()
quantity_jsdata.send_keys("3")
update_basket  = driver.find_element(
    By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button"
).click()
time.sleep(3)
value_jsdata = driver.find_element(
    By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input"
)
value_jsdata = value_jsdata.get_attribute("value")
assert value_jsdata == "3"
apply = driver.find_element(
    By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button"
).click()
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > ul")
element_text = element.text
assert element_text == "Please enter a coupon code."
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element(By.ID,"menu-item-40").click()
to_basket_html = driver.find_element(
    By.CSS_SELECTOR,"#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart"
).click()
time.sleep(3)
basket = driver.find_element(
    By.CLASS_NAME,"wpmenucart-contents"
).click()
time.sleep(3)
wait = WebDriverWait(driver, 5)
checkout_btn= wait.until(
    EC.element_to_be_clickable((
    By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > div > a"))).click()
first_name= wait.until(
    EC.element_to_be_clickable((
    By.ID, "billing_first_name")))
first_name.send_keys("Mr")
last_name = driver.find_element(By.ID,"billing_last_name")
last_name.send_keys("Smit")
email = driver.find_element(By.ID,"billing_email")
email.send_keys("Smit@bk.ru")
phone = driver.find_element(By.ID,"billing_phone")
phone.send_keys("+79999999999")
sel = driver.find_element(By.CSS_SELECTOR,"#s2id_billing_country > a").click()
sel_open = driver.find_element(By.ID,"s2id_autogen1_search")
sel_open.send_keys("Russia")
Russia_btn = driver.find_element(By.ID,"select2-result-label-393").click()
address = driver.find_element(By.ID,"billing_address_1")
address.send_keys("street zero")
city = driver.find_element(By.ID,"billing_city")
city.send_keys("SPB")
county = driver.find_element(By.ID,"billing_state")
county.send_keys("Russia")
postcode = driver.find_element(By.ID,"billing_postcode")
postcode.send_keys("000")
check_pay = driver.find_element(By.ID,"payment_method_cheque").click()
place_order = driver.find_element(By.ID,"place_order").click()
wait = WebDriverWait(driver, 5)
element = wait.until(
    EC.text_to_be_present_in_element((
    By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received"
    ),"Thank you. Your order has been received."))
payment_method = wait.until(
    EC.text_to_be_present_in_element((
    By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td"
    ),"Check Payments"))
driver.quit()