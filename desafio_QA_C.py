from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    #C - Validar existência de registos numa listagem:
    #    i. Aceder a  https://demoqa.com/books
    #    ii. Pesquisar por livros cujo título contém javascript       
    #    iii. Validar que a listagem apresenta 4 registos
    
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://demoqa.com/books')
    page.set_viewport_size({"width": 1920, "height": 1080})
    if(page.wait_for_selector('#close-fixedban')): #If ads appear, close them
        page.click('#close-fixedban')

    page.type('#searchBox', 'Javascript') #Search 'javascript'
    locator = page.locator("//div[@class='rt-tr -even']|//div[@class='rt-tr -odd']") #Xpath to locate valid rows

    expect(locator).to_have_count(4) #Test if there are 4 'javascript' rows

    browser.close()