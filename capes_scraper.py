import os
from random import randint
import time
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common import action_chains
import pickle
import nltk
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords
import string
import itertools


class Firefox:
    def __init__(self):

        os.system('clear')
        load_dotenv()

    @staticmethod
    def driver_crude(self):

        if os.path.exists('/home/note/.mozilla/firefox/4luuu34u.crude') == True:
            path_crude = '/home/note/.mozilla/firefox/4luuu34u.crude'
        elif os.path.exists('/home/studio/.mozilla/firefox/3ykqrr4i.crude') == True:
            path_crude = '/home/studio/.mozilla/firefox/3ykqrr4i.crude'
        else:
            pass

        _ = f'driver_safe{randint(1, 999)}'
        _ = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",
                              service_log_path="geckodriver.log",
                              firefox_profile=path_crude)

        _.maximize_window()

        return _

    @staticmethod
    def capes(_):
        _.get("https://catalogodeteses.capes.gov.br/catalogo-teses/#!/")
        start_time = time.time()
        date_Time_Obj = datetime.now()
        
        inp_user = 'representações sociais'
        texts = []
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, UnexpectedAlertPresentException, TimeoutException)
    
        try:
            sleep(2 + float(f'0.{randint(3, 7)}'))
            WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.form-control')))
            
        
        finally:
            sleep(3 + float(f'0.{randint(3, 7)}'))
            _.find_element(By.CSS_SELECTOR, '.form-control').click()
            _.find_element(By.CSS_SELECTOR, '.form-control').send_keys(inp_user)
            _.find_element(By.CSS_SELECTOR, 'button.btn').click()
            
                            
            css_selec_1 = [ 'bt-painel-filtragem.ng-isolate-scope > div:nth-child(3) > ul:nth-child(3) > li:nth-child(3) > label:nth-child(2) > input:nth-child(1)',
                            '.btn-refine'
                        ]

            css_selec_2 = [ 'bt-painel-filtragem.ng-isolate-scope > div:nth-child(7) > bt-modal-filtragem-extra:nth-child(1) > a:nth-child(1)',
                            'label.filtro-opcao:nth-child(5)',
                            'label.filtro-opcao:nth-child(6)',
                            'label.filtro-opcao:nth-child(9)',
                            '#modalFiltroGrandeÀreaConhecimento > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)',
                            '.btn-refine'
                        ]

            css_selec_3 = [ 'bt-painel-filtragem.ng-isolate-scope > div:nth-child(8) > bt-modal-filtragem-extra:nth-child(1) > a:nth-child(1)',
                            '#modalFiltroÁreaConhecimento > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > label:nth-child(9)',

                            '.btn-refine'
                        ]

            @staticmethod
            def config(css_sel):
                sleep(3 + float(f'0.{randint(3, 7)}'))
                WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css_sel)))
                element = _.find_element(By.CSS_SELECTOR, css_sel)
                _.execute_script("return arguments[0].scrollIntoView();", element)
                _.execute_script("arguments[0].click();", element)
                
                
            for css in css_selec_1:
                config(css)
            sleep(1 + float(f'0.{randint(3, 7)}'))

            for css in css_selec_2:
                config(css)
            sleep(1 + float(f'0.{randint(3, 7)}'))

            for css in css_selec_3:
                config(css)
            sleep(1 + float(f'0.{randint(3, 7)}'))

            @staticmethod
            def scraper():
                try:
                    sleep(3 + float(f'0.{randint(3, 7)}'))
                    WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.resultados > div:nth-child(1)')))
                
                finally:
                    for i in range(1, 21):
                        path = f'.resultados > div:nth-child({i}) > div:nth-child(2)'

                        try:
                            texts.append(WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.visibility_of_element_located((By.CSS_SELECTOR, path))).text)
                            print(WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.visibility_of_element_located((By.CSS_SELECTOR, path))).text)
            
                        except (ignored_exceptions):
                            pass
            
                        finally:
                            sleep(1 + float(f'0.{randint(3, 7)}'))
            scraper()

            @staticmethod
            def pagination():

                while(True):
                    try:
                        page_button_1 = f'li.pagination-next:nth-child(15) > a:nth-child(1)'
                        WebDriverWait(_, 100).until(ec.visibility_of_element_located((By.CSS_SELECTOR, page_button_1)))
                        _.find_element(By.CSS_SELECTOR, page_button_1).click()
                        sleep(1 + float(f'0.{randint(3, 7)}'))
                
                    except (ignored_exceptions):
                        page_button_2 = f'li.pagination-next:nth-child(14) > a:nth-child(1)'
                        WebDriverWait(_, 100).until(ec.visibility_of_element_located((By.CSS_SELECTOR, page_button_2)))
                        _.find_element(By.CSS_SELECTOR, page_button_2).click()
                        sleep(1 + float(f'0.{randint(3, 7)}'))
                
                    finally:
                        WebDriverWait(_, 100).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.resultados > div:nth-child(1)')))
                        scraper()             
            pagination()

        timer = f'{date_Time_Obj}, " Firefox funcionou durante  {time.time() - start_time}'
        print(timer)

        # return texts, number_list
        
        return texts


    @staticmethod
    def capes_02(_):

        # number_list

        start_time = time.time()
        date_Time_Obj = datetime.now()
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, UnexpectedAlertPresentException, TimeoutException, ElementNotInteractableException)
        resumes = []

        # number_list = [
                    # '11022206', '11294160', '11294343', '10969860', '11123022', '11035372'
                    # ]


        number_list = [
                    '11286483', '11190402', '10967615', '11190967', '11323267', '11313425', '11322983', '11322661', '10967611', '10967608', '10955944', '11294409', 
                    '10293646', '10499268', '11325638', '11324474', '11298008', '11331198', '11270021', '10967609', '11324235', '11022199', '11118460', '11190832', 
                    '10965300', '11293728', '11250639', '11293553', '11330878', '11043391', '11328891', '11043380', '11190591', '11286823', '10899086', '11079735', 
                    '11326822', '11336922', '11273899', '11323417', '11322112', '10967614', '11284388', '10906516', '11036663', '11340831', '11336944', '11273871', 
                    '11085297', '11323529', '11321930', '10967616', '10967607', '11269238', '11022207', '11022186', '11250939', '11294224', '11331861', '11273623', 
                    '11042723', '11042737', '10967628', '11022202', '11022200', '10857419', '11294301', '11297755', '11298100', '11016772', '11536429', '11337125', 
                    '11042724', '11324331', '11323353', '11323468', '10967606', '10967604', '10967613', '10967605', '11292731', '11022198', '10976738', '11499018', 
                    '11321499', '11322830', '11337037', '11336598', '10967612', '11298128', '11079705', '11043388', '11190799', '11294457', '11327082', '11331454', 
                    '11340348', '11270684', '10967610', '11022206', '11294160', '11294343', '10969860', '11123022', '11035372'
                    ]
    
        for number in number_list:
            link = f'https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/trabalhoConclusao/viewTrabalhoConclusao.jsf?popup=true&id_trabalho={number}'

            def scraper(link):
                _.get(link)

                path = f'#resumo'
        
                try:
                    sleep(3 + float(f'0.{randint(3, 7)}'))
                    WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.visibility_of_element_located((By.CSS_SELECTOR, path)))
                    element = _.find_element(By.CSS_SELECTOR, path)
                    _.execute_script("return arguments[0].scrollIntoView();", element)
                    _.execute_script("arguments[0].click();", element)
    
                except (ignored_exceptions):
                    pass
    
                finally:
    
                    try:
                        resumes.append([f'{link}' , (WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.visibility_of_element_located((By.CSS_SELECTOR, path))).text)])
                        print(WebDriverWait(_, 100, ignored_exceptions=ignored_exceptions).until(ec.visibility_of_element_located((By.CSS_SELECTOR, path))).text)
                
                    except (ignored_exceptions):
                        pass
                
                    finally:
                        sleep(1 + float(f'0.{randint(3, 7)}'))

            scraper(link)

        timer = f'{date_Time_Obj}, " Firefox funcionou durante  {time.time() - start_time}'
        print(timer)

        with open('resumes.txt', 'w') as f:
            for line in resumes:
                f.write(f"{line}\n")

        with open('resumes.pkl', 'wb') as f:
            pickle.dump(resumes, f)

        return resumes


# f5 = Firefox() 
# fcr5 = f5.driver_crude(f5)
# texts = f5.capes(fcr5)
# resumes = f5.capes_02(fcr5)


with open('resumes.pkl', 'rb') as f:
    resumes = pickle.load(f)

def stopwords_cleaner(words):
    s = set(string.punctuation)
    stopwords = nltk.corpus.stopwords.words('portuguese')
    filtered_word = [word for word in words if (word.lower() not in stopwords) and (word.lower() not in s)]
    return filtered_word

def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word).lower())
    return phrase

compare = []
#base = ['representações', 'sociais', 'ensino', 'poluição', 'fundamental', 'indústria', 'energia', 'lixo']
#base = ['novo', 'ensino', 'medio']

for i in (base):
    compare.append(stopwords_cleaner(Stemming(Tokenize(i))))

compare_clean = []
for i in range(len(compare)):
    compare_clean.append(compare[i][0])


def list_elem(name , subset):
    quasi = []
    for i in range(len(resumes)):
        for elem in subset:
            if elem in subset and \
                elem in stopwords_cleaner(Stemming(Tokenize(resumes[i][1]))):
                    quasi.append([resumes[i][0], resumes[i][1]])

    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(quasi, f)


def subsets(compare_clean):
    names = []
    for L in range(len(compare_clean) + 1):
        for subset in itertools.combinations(compare_clean, L):
            name = f"{('_'.join(map(str, subset)))}"
            list_elem(name, subset)
            print(name, subset)

            if len(name) != 0:
                names.append(name)
    return names

names = subsets(compare_clean)

for name in names:

    with open(f'{name}.pkl', 'rb') as f:
        alfa = pickle.load(f)
    
        print(f'O conjunto {name} possui {len(name)} items \n\n')
    
        for i in range(len(alfa)):
            for o in range(len(name.split('_'))):
                term = (name.split('_'))
                if alfa[i][1].count(f'{term[o]}') != 0:
                    print(f"O resumo de índice {i} apresenta {alfa[i][1].count(f'{term[o]}')} ocorrências do termo {f'{term[o]}'}")
            print('\n')
    print('\n\n')


# name = 'represent_ensin_fundament'
# 
# with open(f'{name}.pkl', 'rb') as f:
    # alfa = pickle.load(f)
# 
    # print(f'O conjunto {name} possui {len(name)} items \n\n')
# 
    # print(alfa)

