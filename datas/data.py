from selenium.webdriver.common.by import By


input = {'element_pro': 'kw',
         'element_type': 'send_keys'}

click_css = {
         'element_pro': 'kw',
         'element_type': 'click'
            }


register_skip_click = {
         'element_pro': 'kw',
         'element_type': 'click'
            }


register_click = {
         'element_locator': By.CSS_SELECTOR,
         'element_pro': '#app > div > div > div.main > div > form > div:nth-child(4) > div > div',
         'element_type': 'click'
            }

click_p_text={
         'element_locator': By.PARTIAL_LINK_TEXT,
         'element_pro': 'kw',
         'element_type': 'click'
            }

click_xpath = {
        'element_locator': By.XPATH,
        'element_pro': 'kw',
        'element_type': 'click'
            }

click_Class = {
    'element_locator': By.CLASS_NAME,
    'element_pro': 'kw',
    'element_type': 'click'

}



if __name__ == '__main__':
    files = ['C:\\Users\\anban\\Desktop\\gujianhuizong\\test\\sun.img',
             'C:\\Users\\anban\\Desktop\\gujianhuizong\\test\\boot.img',
             'C:\\Users\\anban\\Desktop\\gujianhuizong\\test\\340g.bin']
    for file in files:
        print(file)