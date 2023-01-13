"""*Dear {}*%0a
%0a
%0a
Please, be reminded that the scheduled Certification/Induction for Chartered Management Status will hold as planned: There is provision for you to make payment and/or complete registration at the venue, in case you have not done yours.
%0a
%0a
Award interactive induction/workshop will hold in Abuja, Nigeria as follows:
%0a
%0a
Abuja (Physical and Virtual):
%0a
%0a
Date: Wednesday, 21st September, 2022.
%0a
%0a
Time: 11.00am prompt.
%0a
%0a
Venue: Silk Road Restaurant, Sinoki House,
%0a
%0a
5th Floor, Plot 770, Off Samuel Ademulegun Avenue, Opp. Federal Ministry of Transport, CBD, Abuja-FCT.
%0a
%0a
The Abuja events will be broadcasted live such that those not present physical can witness and participate virtually.
%0a
%0a
On the payment front, please, take note of the following payment details:
%0a
%0a
Induction fee is 188,000.00, due for payment now.
%0a
%0a
Annual Subscription is 30,000 payable before or on induction day at the venue.
%0a
%0a
The Annual Subscription is required, being a policy of CIMC membership at entry point. It is not mandatory but important and it does not prevent your certification or collection of certificate.
%0a
%0a
A total of N218,000 is payable in all.
%0a
%0a
Below is the payment method:
%0a
%0a
Bank: Zenith Bank Plc
%0a
%0a
Title: Management Connects and Support Consultants
%0a
%0a
Account Number: 1016644932
%0a
%0a
Many thanks and best regards.%0a
%0a
Michael Adewole Okara, (ChMC, FIMC, CMC, arpa)%0a
%0a
Board Representative.%0a
%0a
+2348035796502 | mcscglobal.org"""

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
    
    contacts =   {  '0806 266 6624': 'Mohammed Yakubu Katamba ', '+234 805 744 9498': ' John Owolabi', '07068778800': 'Dr George Manuwuike ', '+234 806 690 9344': 'Dr Mrs Ahuchaogu Franca Chika ', ' +234 803 677 6829 ': 'E. Chinedu Igwe ', '07030118101': 'Dr Ajengbe Ayokunle John', '0803 053 0106': 'Mayowa Bamidele', '0907 040 6798': 'Oladipupo Onaseso', '0705 356 5929': 'GILLIS TOMIDIEA IPALIBO ', '+23470253447115': 'Friday Odeh Idah', '08033945161': 'Charity Ayo Olaifa', '0803 835 8543': 'Abel Gloria Laruba ', '+2348033145174': 'Mr Dominic Okafor', '08035394130': 'Engr. Oluwalayi Ayodele Joseph', '+2348035976066': 'Arc CHIDI Clinton Okoli', '+234 703 029 6688': 'Zulaihat Ahmad-Dirisu', '0803 709 2402': 'DEME DEBRA PAMOSOO', '0708 221 1768': 'Maagbe-bul Christie Mbalumun ', '+2348072444244': 'MecCah Alfa-Wali ', '+234 708 708 3333': 'Ojimelukwe Okechukwu ', '07034708688': 'Raji T. Adewale', '+2347039554117': ' Job Ayodele Ekundayo', '08037010777': 'Rev. Jim Piomoki-Stevens', '8133943520': 'Barr. Timothy Olubor', '0805 611 1109': 'Idowu Solomon', '08038442908': 'Emmanuel Olawuyi ', '08034551482': 'George Chinonso - Obi', '8062611560': 'Oloruntoba Bamidele ', '08037505184': 'Chinedum Anowuru, FCIB, FNIM, FICMA, FCAI, LLB, MBA', '+2347046383713, +2347046216417': 'Sina Sofola, SAN', '+447443423890': 'Uchennia Akahalu ', '8111312517': 'Eluozo Collins ', '215-329-4154': 'Claudia Gale ', '8033344595': 'Oladejobi Godwin Adebola', '8023204138': 'Elvis Onuora FCA, FCTI', '8023152210, 8036206061': 'Oke Olabamiji', '8033597679': 'Mr. Adigun Oluwamayowa Oluwaseun', '08088879999': 'Akuns Habila John ', '08033276496': 'Ezeogo Emenike Anyaegbu Iguh', '07034274341': 'Mr Martins Okoro ', '08106852124': 'Sunny Akomeno Oroge', '08033170571': 'Okachukwu Gospel Herbert', '08187515414': 'Victoria Mfon Ekanem', 'check': 'Mrs. Constance N. Goddy-Nnadi', '+2348035785502': 'Shalom Asuquo', '+2348060421451, 07012745162, 09084534111': 'John Nwokeoma', '+2348061296216': 'Godwin Okoko ', '+234 810 327 2750': 'Mrs Lynda Ebere Anughere', '07032648558': 'Ezeodili James Morgan Ugochukwu', '8033377261': 'Prof. Basil O. Nwosu', '0806 596 9176': 'Agada Sunday Ojonimi', '8060740202': 'Dr. Alhaji Musa Liman', '8892150900': 'Dr Ibekwe Everistus', '08081521119': 'Chinyere Cecilia Bishop-Adigwe', '08159790903, 08131770688': 'Adamu S. Adakole FNIM', '8070481821': 'Bala Zango', '+234 807 453 1991, 08088888866, 07030000205': 'Sonnie Babatunde Ayere ', '8033778222': 'Frederick Bethel Saduwa ', '8035881242': 'Emmanuel Akissa', '08035028205': 'Akpe Oyinkarebai Michael\t\t', '07039094177': 'Chris Manuawuchukwu Agu\t\t', '0803 716 9795': 'West Pamela Inkoba\t', '+48572537567, +48669784338, +375299641852': 'Dr. James Onyinye Mbakpou\t', '08022226864': 'Onalu Uchenna . C\t\t', '8037003649': 'HASSAN SALIHU ANKA ', '\t7031384185, 08023012752': 'Adewale Davies Owoyemi\t', '8034746507': 'Barr Lohor Alexander\t\t', '8033483674': 'Essang Paddy\t', '08106411038, 08062638111': 'Olusola Gbadamosi\t\t', '7088607443 ': 'Prince Amaefula\t\t', '8080767155': 'Chukwudi Iwuozor\t\t', '8023608704': 'Patricia Eze', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke\t', '7035558287': 'Stephen Eche', '8131538812': 'SP Onyejegbu Basilia Cynthia\t', '8030824948': 'Ogunmefun Toyin\t', '8033341416': 'OLANIRAN ADERIBIGBE', '8033156117': 'Umar B. Bindir', '8173245448': 'Shirley Ehru Nehemiah', '09060002881': 'Dr. Augustine Brendan Inyang', ' 08033496381': 'Professor Uche Grace Emetarom ', '0803 703 9351': 'Ntuen Sylvia Tony', '08102547453': 'Olawumi Olugbenga Olawale', '8037879235': 'Dr ZUHAIR JIBIR ', '7036481502': 'Eni Okoi, Esq', '08033657142': 'Barr. Deborah Otanoegbe Aisedion', '8027862387': 'Austin Itsoya Momodu', '+234 (0)8028911399,+234(0)8068056242': 'Markus Njidda Uba ', '+221773339112': 'Bakhoum Clemence', '8032212135': 'Emumena, David Emuhowho', '7054069661': 'Daperi Amachree ', '8023361732': 'Prof. Kessington Obahiagbon', '08168755195, 08023580925': 'Ahmed Yakubu Kamaldeen', '(647) 203-0350': 'Prof. Adefemi Olokesusi (Ph.D)', '2348037008618': 'KALU, Peters PhD', '+233 200 429 430, +233 544 904 920': 'Kenneth Igiri ', '+2348033165162': 'Terseer Ugbor ', '8083889629': 'Dr. Effiong Okon Ekaeba', '2347034054962': 'Adeniyi Salaudeen', '+234 (9) 4615700, +2348023935869': 'Amin Abubakar Sadiq ', '+234(0)80 9099 8811': 'Adaobi Ekweanya ', '803 309 5945': 'Helen Tamunoibelema ', '07038402601, 08059453568': 'ALEXANDER IFEANYI OGOLO', '0802 324 5490': 'Debbie Akwara', '8062625402': 'Maikudi Ibrahim Abubakar', '7030834395': 'Engr. Mahraz Karaye', '7068490339': 'Titilayo Wumi Oluwafemi', '08035136609, 09098109072': 'Stephen Bamidele Ogodo',  '7038080616': 'Lovelyn Okoye', '+255627542057': 'Ernest Masasi', '2348033145174': 'Dominic Okafor ', '+447741368789 ': 'Salisu Uba ', '8034240632, 8072599298': 'Tpl Adeyemo Olajide Kamoru JP, fnitp, fimc', '08189624547, 2348064710849': 'Benson Ndaji ', '8039098931': 'JAMES SONDE ', '+2348037257819': 'OSUJI ALBERTO OBINNA', '8037126431': 'Akachukwu Moses Chukwudi', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO,', '+2347033200500': 'Uko Ekott, (FCIA, DCILRM, FIMC, CMC)', '+2348052362288, +2348159552222': 'Moses Mogbolu ', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8167353993': 'Tope Oluwadare ', ' +44 7512 093697, +44 7824 798888, +44 7043 050050': 'Ayodapo Oyebade ', '+254 722 599 621': 'Peter Okeyo Oraro', '8069766002': 'Ahmad Yahuza Getso', '+234146140167, 7359948, +2348023231273 ': 'Victoria Alonge ', '8064499724': 'Mr. S. Kola Adekoya', '7031042122': 'Oyegoke Adekunle Alani', '08173015230': ' Akinlamilo Elliot Olafisoye', '+2348037012676, +2349029461146 ': 'Oyinloye Oyedele P.', '+256 417 201 019, +256 771 003 594': 'Adekemi Ndieli ', '8033296209': 'Dr. Sylvester C. Offor FCA', '8033262326': 'Ezeogbuefi Gabriel .O', '8131634324': 'ISHOLA-COKER OLUWATOSIN', '8055128300': 'Abimbola Olulana', '08088804070': 'Dr. Fidelis Onyema Ugwushie', '09037808592, 08035665315': 'Engr. Benjamin Eboehi', '8036342106': 'KASSIM IDRIS', '+ 2348029055385': 'Nwaruh George ', '7032220542': 'PIUS IPUOLE ', '08032327228, 08030917088': 'Prof Samuel Ogunwale Ogundiran', '+2348034932689,+2347069551267': 'LAWSON BEESON ', '8035446978': 'Promise Nwafor A Anelechi ', '+2348032601105': 'Hon. Anselm C. Onuorah', '8024260942': 'Gidado Tahir ', '08036469928, 08098469928': 'Mohammed Saeed Suleiman ', '07062883006, 09097778162': ' Debby Oluyinka Daramola', '8036754537': 'Ogechukwu Eucharia Maduka', '+23412954690, +23412954691, +2349053333393': 'Adeyinka Adegbite, Esq', '906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara', '08056659371, 08098929477': 'Dr. Olotu, O. Ayopo', '8062862692': 'Victor Bisong', '7084415597': 'Ismaila Haliru Zarma', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '8035995868': 'Hawa BenHirki ', '+234 (1) 2713990 , +2348086633083': 'Kayode Ibrahim AKINTOLU', '+234 810 375 6894': 'Reginald Udenze Ihedike', '7060772784': 'Victor Obioma Uche', '8033865790': 'Prof. Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart ', '8036005365': 'Muhammad Ujudud Musa ', '+234 (0) 803 334 1079 ': 'Joseph Isere ', '+2348056038074, +234702540721': 'ONABEKUN ADEKUNLE ', ' +2347037905644 , 08071827748': 'Idornigie Ide Christopher ', ' +2348052448149': 'JOSEPH HUMPHREY KABE', '8033509752': 'Idumonza Isidahomhen ',  '+2348052913643, +23408033172828': 'Abimbola Omolabi PhD', '8070341328': ' Engr. Okurerie Ajiroghene Ogedegbe ', '08037093585, 09023924412, 07046852104': 'Nkem Joseph-Palmer ', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7020677189': 'Ndubuwa Ugwunna Victor', '9087259465': 'Engr Jane Ifeoma Kamanya', '08144513831, 0708160': 'Dr Muhammad Kabir Adam', '+2348064657799,+2348102875997': 'Dr Joseph Rankin', '8032479757': 'Aiyedun Olubunm Fcis Mtm', '0712187260, 0702916735': 'Dr Kasozi Nathan', '08069317779': 'Titi Yakubu ', '08033156025 , 08095000000 ': 'Engr Aishatu Aliyu Umar, FNSE', '08033107505': 'Mrs Juliet Ogedi David-west', '8065660093': 'Roselyn Eneji', '+234 803 4071 116': 'Paul Nnamah ', '8055076706': 'Olajide Ojo ', '0904530629': 'Abayomi Bello', '08039689404': 'WILSON OBIDAH, PhD', '8033496839': 'Dr. Charles Anosike FCMI MNIM GPM', '8033613144': 'Ujunwa Rosemary Felicia (Mrs)', '+2348033078252, +2348173078252, +2348055266838': 'Peter Imafidon Omokaro FIMC,CMC,FCIB', '+2348032007440': 'Erere Oyibo-Rhokaye ', '+2348033467900': 'Dr. Chukwunonso Izuchukwu Pharm.d Cmc Fimc', '8055928327': 'Rev. Sr. Paulette Ekejiuba Phd', '+2348037109285': 'Ndifreke Andrew-essien', '8128678873': 'Mr. Aniefiok E. Thomas', '+23279881111, +23276368359': 'Dipo Gbenro ', '+2347067941550': 'Bldr. Alvary A. Durkwa', '8030717044': 'Derek Omoleh ', '8055427409': 'Uchenna A. Okoroafor', '8032195105': 'Dr. Victor Evans', '8056488800': 'Akinbebije Damilola', '8058434421': "JATTO JONATHAN OSABUHEN'", '8035983539': 'Shitery Aaron Istifanus', '08066789611': 'Leonard Nzenwa ', '8062411073': 'Sunday Bala ', '8062611560, 8035691309': 'Olusegun Adepoju', '+2349036683244, +2348060895366': 'Busari Matthew', '07080858791': 'Uchenna Solomon Ohaeri ', '2349039231107': 'Joshua Samuel', '7011990709': 'Ogunbiyi-davies Biodun Abiola', '8051500690': ' Osinuga Rahman', '+23408032825342, 08188541950': 'Engr Olatunde Micheal IBRAHIM', '8034531431': 'Olajire Adebayo Aderemi', '8163686103': 'Dr. Ola Adigun-Daniels', '8069680993': 'Orkuma Emmanuel Anyoko-Shaba', '8037829881': 'Maharaz Saad', '8027291738': 'CHRISTWEALTH Kolawole Olusola', '08036197738': 'Aromeh Sunday Adole', '08037262350': 'George Idiaghe', '08061572906': 'Uwem Mkpong Archibong', '08033047278': 'Nasamu Ibrahim', '08034315211': 'Olatunde Sowunmi', '08067742773': 'Mr. Awusa Peter Ewa', '08034373712': "Ugwuoke Emeka Emmanuel':", '08033118894': ' Igenegbai Christiana Joy', '8035677488': 'Ekemezie Okechukwu '}
    message = """*Gentle Reminder: December Event (Physical and Virtual)*%0a%0a
Dear {},
%0a%0aTrust you are having a splendid day. We understand that you could not make it for the last event. It gives us great joy to inform you that our next event has been scheduled for the month of December to hold on the 13th in Lagos (Physical and Virtual). Please indicate your preference of participation on your revert. %0a
%0aOn the payment front, please, take note of the following payment details:%0a
%0aInduction fee is 188,000.00, due for payment now.%0a
%0aAnnual Subscription is 30,000 payable before or on induction day at the venue.%0a
%0aThe Annual Subscription is required, being a policy of CIMC membership at entry point. It is not mandatory but important and it does not prevent your certification or collection of certificate.%0a
%0aA total of N218,000 is payable in all.%0a

%0aBelow is the payment method:%0a
%0aBank: Zenith Bank Plc%0a
%0aTitle: Management Connects and Support Consultants%0a
%0aAccount Number: 1016644932%0a

%0aMeanwhile, you may proceed with registration if you have not done yours. Please proceed with registration online with the link below.%0a
%0aRegistration Package (Forms)%0a
%0aAlternatively, download our registration / application package (forms) with the link below. Please fill as appropriate: starting from degree level to professional level and work experience; attach your profile and revert to us ASAP so we can commence the registration process right away.We shall follow up this mail with your letter of invite so you can have the complete details.%0a
%0a[Download Forms] (https://drive.google.com/folderview?id=1-0ObrUpgebHOFIx9y_lspECURiPpWorw")%0a
%0aMany thanks and best regards.%0a


%0aMichael Adewole Okara</strong>, (ChMC, FIMC, CMC, arpa)%0a
%0aBoard Representative.%0a
%0a+2348035796502 | mcscglobal.org%0a
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

