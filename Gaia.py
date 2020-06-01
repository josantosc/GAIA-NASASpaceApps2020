import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options   

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Gaia")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")
trainerer = ListTrainer(chatbot)

dir_path = os.getcwd()

driver = webdriver.Chrome(dir_path+'chromedriver')
driver.get('https://web.whatsapp.com/')
driver.implicitly_wait(18)

def pegaConversa(): 
    try:
        post = driver.find_element_by_class_name('_3zb-j')
        ultimo = len(post) -1
        texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        return texto
    except: 
        pass    

def enviaMensagem(mensagem):
    caixa_de_texto = driver.find_element_by_class_name('_2s1vp')
    valor = '*Gaya: * '+str(mensagem)
    for part in valor.split('\n'):
        caixa_de_texto.send_keys(part)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).perform()
    time.sleep(0.5)
    botao_enviar = driver.find_element_by_class_name('_35ew6')
    botao_enviar.click()

def treinar(mensagem):
    resposta = 'como respondo isso? me ensina, por favor...? utilize ;"'+str(mensagem)+'"'
    enviaMensagem(resposta)
    novo = []
    try:
        while True:
            ultima = pegaConversa()
            if ultima =="!":
                enviaMensagem("Voce desativou me aprendizado")
                break 
            elif ultima.replace(';','') != '' and ultima != mensagem and ultima[0] == ";" :
                auxiliar = ultima 
                print(mensagem.lower().strip())
                print(ultima.replace().lower().strip())
                novo.append(mensagem.lower().strip())
                novo.append(ultima.replace().lower().strip())
                trainerer.train(novo)
                enviaMensagem("Vlw por me ensinar <3")
                break
    except: 
        pass 
    try 

	except:
	print("Adeus humano")
