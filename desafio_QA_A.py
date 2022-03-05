from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    #A - Preencher formulário simples e submeter:
    #    i. Aceder a https://demoqa.com/text-box
    #    ii. Preencher o formulário
    #    iii. Submeter carregando no botão Submit
    
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://demoqa.com/text-box')
    page.set_viewport_size({"width": 1920, "height": 1080})
    if(page.wait_for_selector('#close-fixedban')): #If ads appear, close them
        page.click('#close-fixedban')

    page.fill('#userName', 'Nome Exemplo') #Full Name

    page.fill('#userEmail', 'exemplo@exemplo.com') #Email

    page.fill('#currentAddress', 'Morada Exemplo, 4342-942 Cidade') #Current Address

    page.fill('#permanentAddress', 'Morada Exemplo 2, 2352-428 Cidade') #Permanent Address

    page.click('#submit')

    browser.close()