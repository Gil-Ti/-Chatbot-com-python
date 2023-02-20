import speech_recognition as sr
import pyttsx3

# Define a linguagem do reconhecimento de voz
r = sr.Recognizer()

# Configura a síntese de voz
engine = pyttsx3.init()

def chatbot(text):
    if "olá" in text.lower():
        return "Olá, como posso ajudar?"
    elif "como você está" in text.lower():
        return "Estou bem, obrigado por perguntar. E você?"
    elif "qual é a sua idade" in text.lower():
        return "Eu sou um programa de computador, então não tenho idade."
    elif "você pode me contar uma piada" in text.lower():
        return "Por que o computador foi ao médico? Porque estava com vírus!"
    elif "Quem é o responsável pela retenção tributária?" in text.lower():
        return "O responsável pela retenção tributária é aquele que efetua o pagamento ao contribuinte. Por exemplo, a empresa contratante é responsável por reter e recolher os tributos quando realiza o pagamento a um prestador de serviço."
    elif "Como é feito o cálculo da retenção tributária?" in text.lower():
        return "O cálculo da retenção tributária é feito sobre o valor total da operação ou serviço contratado, utilizando-se a alíquota específica de cada tributo. Essa alíquota varia de acordo com a natureza da operação e a legislação tributária."
    elif "O que acontece se a retenção tributária não for feita corretamente?" in text.lower():
        return "Se a retenção tributária não for feita corretamente, o responsável pelo pagamento poderá ser autuado e ter que arcar com multas e juros de mora. Além disso, o contribuinte que não teve o tributo retido na fonte poderá ser cobrado pelo valor devido, acrescido de juros e correção monetária."
    else:
        return "Desculpe, não entendi o que você falou"

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Fale algo: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
        response = chatbot(text)
        print(response)
        engine.say(response)
        engine.runAndWait()
    except:
        print("Desculpe, não entendi o que você falou")
