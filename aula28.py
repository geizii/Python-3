""" CONSTANTE = "variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) """

velocidade = 61 # Velocidade atual do carro
local_carro = 101 # local em que carro está na estrada

RADAR_1 = 60 # Velocidade média máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está 
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) and \
            velocidade > RADAR_1

if velocidade > RADAR_1:
    print('velocidade do carro passou do radar 1')

if vel_carro_pass_radar_1 and carro_multado:
    print('carro multado em radar 1')