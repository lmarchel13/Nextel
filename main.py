import json, time, os, pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testes import MyTest

def googleSearch(browser,text):
    output = list()
    searchBar = browser.find_element_by_name('q')
    if searchBar:
        searchBar.clear()
        searchBar.send_keys(text)
        searchBar.send_keys(Keys.RETURN)

    results = browser.find_element_by_id('res')
    if results:
        for item in results.find_elements_by_class_name('g'):
            title = item.find_element_by_tag_name('h3').text.strip()
            if title != '' and len(output) != 3:
                print(title)
                output.append(title)

    myTest = MyTest(output,'')
    myTest.checkLength()
    return output

def createJson(data,output_filename):
    print('\n[ Inserindo os resultados no arquivo "'+output_filename+'" ]')
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False)

    myTest = MyTest([],output_filename)
    if myTest.isFileCreated():
        print('[ Arquivo "'+output_filename+'" criado com sucesso! ]')

if __name__ == '__main__':
    try:
        start = time.time()
        print('[ Lendo arquivo com os dados para pesquisa ]\n')
        with open('data.json') as f:
            data = json.load(f)
    except Exception as e:
        print('[Erro] '+str(e))

    print('[ Dados obtidos com sucesso ]')
    print('[ Iniciando pesquisa com os dados obtidos ]')
    try:
        url = "http://www.google.com.br"

        browser = webdriver.Chrome()
        browser.get(url)
        WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME, 'q')))

        output = {}
        for value in data['google-me']:
            print('\n[ Resultados da pesquisa para "'+str(value)+'" ]')

            output[value] = googleSearch(browser,value)


        browser.quit()
        print('[ Pesquisa realizado com sucesso ]')
        print('[ Resultado da pesquisa no formato JSON ]')
        print(json.dumps(output, indent=2))

        createJson(output,'output.json')

        print('[ Tempo Total de de Execução ] '+str( round( time.time() - start,2))+'s  ')
        print('\n[ Encerrando programa ...] ')
    except Exception as e:
        print('[Erro] ' + str(e))