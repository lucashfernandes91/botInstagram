from selenium import webdriver
from time import sleep


user = 'SEU-LOGIN'
password = 'SUA-SENHA'
lista_hashtag = ['dog', 'goal'] # hashtags que quer seguir
seguidores_hashtag = 2  # Número de novos seguidores por hashtag

# Se estiver usando windowns colocar a pasta "geckodriver" na raiz "C:/". Ex.: C:\geckodriver
# ou 
# Informe o local do drive
# Ex.: webdriver = webdriver.Firefox(firefox_binary='/bin/firefox')
webdriver = webdriver.Firefox()
webdriver.get('https://www.instagram.com')
sleep(5)


username = webdriver.find_element_by_name('username').send_keys(user)
password = webdriver.find_element_by_name('password').send_keys(password)
button_login = webdriver.find_element_by_xpath("//button[@type='submit']").click()
sleep(5)


for hashtag in lista_hashtag:
    i = 0
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
    sleep(10)

    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    first_thumbnail.click()
    sleep(30)

    print('----- \n Hashtag em uso: {} \n'.format(hashtag))

    while i < seguidores_hashtag:

        perfil = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text

        if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Seguir':

            print('Novo perfil seguido: {}'.format(perfil))
            # Fallow
            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
            sleep(20)

            #  Line
            button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
            button_like.click()
            sleep(20)

            # Next image
            webdriver.find_element_by_link_text('Próximo').click()
            sleep(20)

        else:
            print('Não encontrou botão de Seguir no perfil: {}'.format(perfil))

        i += 1

print('Script finalizado')
