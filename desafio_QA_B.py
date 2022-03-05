from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    #B - Verificar existência de campos obrigatórios num formulário:
    #    i. Aceder a https://demoqa.com/automation-practice-form
    #    ii. Preencher todos os campos excepto Last Name
    #    iii. Submeter o formulário carregando no Submit
    #    iv. Verificar que o campo Last Name fica identificado como sendo obrigatório
    
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://demoqa.com/automation-practice-form')
    page.set_viewport_size({"width": 1920, "height": 1080})
    if(page.wait_for_selector('#close-fixedban')): #If ads appear, close them
        page.click('#close-fixedban')

    page.fill('#firstName', 'Nome') #Name
    #page.fill('#lastName', 'Exemplo')

    page.fill('#userEmail', 'exemplo@exemplo.com') #Email

    page.click('#gender-radio-1', force=True) #Gender

    page.fill('#userNumber', '0123456789') #Mobile

    page.fill('#dateOfBirthInput', '2022-03-05') #Date of Birth
    page.keyboard.press('Enter')

    page.type('#subjectsInput', 'Maths') #Subjects
    page.keyboard.press('Enter')

    page.wait_for_selector('#hobbies-checkbox-1') #Hobbies
    page.check('#hobbies-checkbox-1',force=True)
    page.check('#hobbies-checkbox-2',force=True)
    page.check('#hobbies-checkbox-3',force=True)

    page.set_input_files('input#uploadPicture', 'pic.jpg') #Picture

    page.fill('#currentAddress', 'Morada Exemplo 2, 2352-428 Cidade') #Current Address

    page.click('#state') #State
    page.keyboard.press('Enter')

    page.click('#city') #City
    page.keyboard.press('Enter') 

    page.wait_for_selector('#submit')   
    page.click('#submit')

    last_name = page.locator('#lastName')
    expect(last_name).to_have_css("border-color", "rgb(220, 53, 69)") #If Last Name has this color after submitting, it means the field is identified as mandatory

    browser.close()