from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def test():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import time
    contact = "Pearl"
    text = "Hey, this message was sent using Selenium"
    import os
    print(os.getcwd())
    driver = webdriver.Chrome('/chromedriver')
    driver.get("https://web.whatsapp.com")
    print("Scan QR Code, And then Enter")
    input()
    print("Logged In")
    inp_xpath_search = "//input[@title='Search or start new chat']"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact)
    time.sleep(2)
    selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
    selected_contact.click()
    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(2)
    input_box.send_keys(text + Keys.ENTER)
    time.sleep(2)

def first():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome() #options=chrome_options)
    chrome.get('https://api.whatsapp.com/send?phone=+2348140455828&text=hello testing')
    url = chrome.command_executor._url       #"http://127.0.0.1:60622/hub"
    session_id = chrome.session_id  
    #chrome.find_element()
    print(url)
    print(session_id)
    print(chrome)






#'+234 813 293 5554': 'Dr. Etiese Akpan Etuk', '??': 'Femi Odumabo ','+234 703 341 1961': 'Dr. Waheed-Adekojo Funmilayo Mary FNSE', '+234 803 511 4020': 'David, Gabby Okwudiri', '+234 803 343 6395': 'Ajibola Olubisi Isaac', '+234 803 311 1676': 'Samtanye Yerima Balla Dr(HC)', '+234 805 543 7330': 'Qaribullah A. Arabi', '+234 803 578 9986': 'BARR. CHUKWUEMEKA IFEANYI M. UMEORA', '+234 802 359 7526': 'Adeosun Edward Oludayo,', '+234 813 024 7447': 'Usman Aleshinloye', 


def second():
    url = "http://localhost:33655"
    count = 0
    session_id = "1bcfdefb67a65f190f5ac391701875d9"
    
    contacts =   {  '0801 223 4455': 'John Doe'}
    message = """Message goes here
"""





    driver = webdriver.Remote(command_executor=url,desired_capabilities={})
    driver.close()   # this prevents the dummy browser
    driver.session_id = session_id
    
    for contact in contacts.keys():
        phony = []
        chec = contact
        if ',' in chec:
            star = chec
            for chec in star.split(','):
                chec = ''.join(chec.split(' '))
                if '?' in chec:
                    phone = '??'
                elif '+234' in chec:
                    phone = chec
                elif chec[0] =='0':
                    phone = '+234'+chec[1:]
                elif '234' in chec[:3]:
                    phone = chec
                elif '+' not in chec:
                    phone = '+234'+chec
                else:
                    phone = chec
                
                phony.append(phone)
            #phone = ','.join(phony)
        else:
            chec = ''.join(chec.split(' '))
            if '?' in chec:
                phone = '??'
            elif '+234' in chec:
                phone = chec
            elif chec[0] =='0':
                phone = '+234'+chec[1:]
            elif '234' in chec[:3]:
                phone = chec
            elif '+' not in chec:
                phone = '+234'+chec
            else:
                phone = chec
            phony.append(phone)
        for phone in phony:
            mess = message.format(contacts[contact])
            count += 1
            try:
                driver.get("https://api.whatsapp.com/send?phone={}&text={}".format(phone, mess))
                driver.find_element(By.ID,'action-button').send_keys(Keys.RETURN)
                #driver.find_element_by_partial_link_text("use WhatsApp Web").click()
                import time
                time.sleep(2)
                #/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a").click()
                #driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a").click()
                #driver.click()
                import time
                time.sleep(10)
                #inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
                driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
                #driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
                print(count, 'send  {} {}'.format(contact, contacts[contact]))
                time.sleep(2)
                #input_box.send_keys(Keys.ENTER)
            except:
                print(count, 'check {} {}'.format(phone, contacts[contact]))
        
        
        
#test()
#second()
first()

