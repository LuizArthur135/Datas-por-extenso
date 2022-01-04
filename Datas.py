def data():
    mes = {'01':'janeiro', '02':'fevereiro', '03':'março', '04':'abril', '05':'maio', '06':'junho', '07':'julio', '08':'agosto', '09':'setembro', '10':'outubro', '11':'novembro', '12':'dezembro'}
    dias = {'01':'um', '02':'dois', '03':'três', '04':'quatro', '05':'cinco', '06':'seis', '07':'sete', '08':'oito', '09':'nove', '10':'dez', '11':'onze', '12':'doze', '13':'treze', '14':'quartoze', '15':'quinze', '16':'dezesseis', '17':'dezesete', '18':'dezoito', '19':'desenove', '20':'vinte', '21':'vinte e um', '22':'vinte e dois', '23':'vinte e três', '24':'vinte e quatro', '25':'vinte e cinco', '26':'vinte e seis', '27':'vinte e sete', '28':'vinte e oito', '29':'vinte e nove', '30':'trinta', '31':'trinta e um'}
    data = str(input('Digite uma data: ')).split('/')
    valida_data(data)
    print(f'dia {dias[data[0]]} de {mes[data[1]]} de {data[2]}')

def valida_data(date):
	dia = int(date[0])
	mes = int(date[1])
	ano = int(date[2])
	if  dia > 31 or mes > 12 or ano<0:
		print("DATA INVALIDA!")
		data()


data()