# -*- coding: utf-8 -*-
import math
import sys

versao = sys.version_info[0]
if versao == 2:
    leitura = raw_input
elif versao == 3:
    leitura = input

done1 = 1
done2 = 1
sair = 1
mensagemfinal = " "
mensagemok = " "
jatemcodigo = False
primook = False

def inverso_multiplicativo(e, fn):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    fn_t = fn

    while e > 0:
        temp1 = fn_t / e
        temp2 = fn_t - temp1 * e
        fn_t = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if fn_t == 1:
        return d+fn

def checar_primo(num):
    if num == 2:
        return 2
    if num < 2 or num % 2 == 0:
        return 0
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return 0
    return num

def cont_ou_sair():
    print("1 - Continuar no programa")
    print("2 - Sair")
    sair = int(leitura("O que deseja fazer? "))
    if sair == 1:
        return 1
    elif sair == 2:
        return 2

while sair == 1:
    print("***************** RSA *****************")
    print("*                                     *")
    print("* 1 -> Definir conjunto de chaves RSA *")
    print("* 2 -> Criptografar uma mensagem      *")
    print("* 3 -> Descriptografar uma mensagem   *")
    print("*                                     *")
    print("***************************************")
    print("")
    menuP = int(leitura("O que deseja fazer? "))


    if menuP == 1:
        #seleciona os primos
        p, q = 0, 0
        while p == 0 or q == 0:
            p = checar_primo(int(leitura("Insira um valor primo P: ")))
            q = checar_primo(int(leitura("Insira um valor primo Q: ")))

        #determina n e f(n)
        n = p * q
        fn = (p - 1) * (q - 1)

        #recebe e
        print ("f(n) = {0}".format(fn))
        while primook == False:
            e = int(leitura("Insira um valor entre 1 {0} que seja primo em relacao a f(n): ".format(fn)))
            if fn % e == 0:
                print("O numero inserido nao eh valido!")
                primook = False
            else:
                primook = True

        #calcula inverso multiplicativo de e mod fn
        d = inverso_multiplicativo(e, fn)
        print("Inverso multiplicativo de {0} no modulo {1} = {2}".format(e, fn, d))
        print("")
        print("--------------------------------------------------------------\n")
        print("Chaves calculadas!")
        print("Publicas = (N = {0}; E = {1})".format(n, e))
        print("Privadas = (P = {0}; Q = {1}; D = {2})\n".format(p, q, d))
        print("--------------------------------------------------------------")
        print("")
        jatemcodigo = True
        sair = cont_ou_sair()
        if sair == 2: break


    ##CODIFICACAO
    if menuP == 2:
        if jatemcodigo == True:
            xxx = 0
        else:
            n = int(leitura("Insira o valor de N: "))
            e = int(leitura("Insira o valor de E: "))

        pre = leitura("Escreva a mensagem que deseja pre-codificar: ")
        precode = [ord(c) for c in pre]

        print("")
        print("A mensagem pre-codificada em ASCII eh:")
        print(precode)
        print("")

        blocosC = []
        for valor in range(0, len(precode)):
            indice = precode[valor]
            blococode = int(indice)
            blococoderes = (blococode ** e) % n
            blococodetemp = str(blococoderes)
            blocosC.append(int(blococodetemp))

        print("Mensagem codificada!")
        print(blocosC)
        print("--------------------")
        print("")
        codificou = True
        sair = cont_ou_sair()
        if sair == 2: break

    #DECODIFICACAO
    if menuP == 3:
        if jatemcodigo == True:
            xxx = 0
        else:
            p = int(leitura("Insira o valor de P: "))
            q = int(leitura("Insira o valor de Q: "))
            d = int(leitura("Insira o valor de D: "))
            n = p * q

        print("")
        print("Insira cada bloco da mensagem codificada. Digite 'fim' quando terminar.")
        print("")
        while done2 == 1:
            bloco_to_decode = leitura("Insira o bloco: ")
            if bloco_to_decode == "fim":
                done2 = 2
                break
            else:
                bloco_to_decode = int(bloco_to_decode)
                bloco_decoded = (bloco_to_decode ** d) % n
                letra = chr(bloco_decoded)
                mensagemok += letra
                done2 = 1

        print("")
        print("Mensagem decodificada!")
        print(mensagemok)
        print("----------------------")
        print("")

        sair = cont_ou_sair()
        if sair == 2: break
