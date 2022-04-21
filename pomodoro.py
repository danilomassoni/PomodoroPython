import time
from plyer import notification
import playsound


count = 0
minutos = int(input("Quantos minutos cada pomodoro? "))
descanso = int(input("Quantos minutos cada descanso? "))
tempo_pomo = minutos * 60
tempo_descanso = descanso * 60

contar = int(input("Quantos pomodoros gostaria de fazer hoje: "))
notification.notify(
    title = "Começando!",
    message = "Vamos fazer "+ str(contar) + " pomodoros de " + str(minutos) + " minutos.",
    timeout = 10,
)
print("Vamos começar os trabalhos!!")



while (True):
    time.sleep(tempo_pomo)
    count += 1
    notification.notify(
        title = "Vamos lá!",
        message = "Pausa de " + str(descanso) + " min! Você já completou " + str(count) + " pomodoros",
        timeout = 10,
    )
    time.sleep(tempo_descanso)
    notification.notify(
        title = "Pausa do descanso!",
        message = "Vamos fazer outro pomodoro...",
        timeout = 10,
    )
    if count == contar:
        print("Vamos finalizar!")
        notification.notify(
            title = "PARABÉNS!",
            message = "Você completou " + str(count) + " pomodoros!",
            timeout = 10,
        )
        break
    else:
        print("Continue!")