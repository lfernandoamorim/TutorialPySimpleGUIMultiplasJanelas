#Exemplo para criação de multiplas janelas
import PySimpleGUI as sg


#Criar as janelas e estilos
def janela_login():
    sg.theme("Reddit")
    meulayout = [
        [sg.Text("Nome")],
        [sg.Input()],
        [sg.Button("Continuar")]
    ]
    return sg.Window("Login",layout=meulayout,finalize=True)

def janelaPedido():
    sg.theme("Reddit")
    meulayout = [
        [sg.Text("Fazer Pedido")],
        [sg.Checkbox("Pizza Pepperoni",key="pizza1"),sg.Checkbox("Pizza de Frabgo",key="pizza2") ],
        [sg.Button("Voltar"), sg.Button("Fazer Pedido")]
    ]
    return sg.Window("Montar Pedido",layout=meulayout,finalize=True)

#para criar apenas a primeira e não aparecer a segunda janela (None)
janela1, janela2 = janela_login(),None

#loop para ler os eventos que ocorrem em nossa janela
while True:
    window,event,values = sg.read_all_windows()
    #quando a janela for fechada
    if (window == janela1 or window == janela2) and event == sg.WIN_CLOSED:
        break
    #quando for para a próxima janela
    if window == janela1 and event == "Continuar":
        janela2 = janelaPedido()
        janela1.hide()
    #Quando clicar em Voltar    
    if window == janela2 and event == "Voltar":
        janela2.hide()
        janela1.un_hide()
    #Quando clicar em Fazer PEdido
    if window == janela2 and event == "Fazer Pedido":
        if values["pizza1"] == True and values["pizza2"] == True:
            sg.popup("Foram solicitadas as pizzas de Perperoni e Frango")
        elif values["pizza1"] == True:
            sg.popup("Foram solicitadas as pizzas de Perperoni")
        elif values["pizza2"] == True:
            sg.popup("Foram solicitadas as pizzas de Frango")
        else:
            sg.popup("Escolha uma Pizza!!!")
