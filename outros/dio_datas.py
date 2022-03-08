import datetime as dt

def usando_date():
    data_atual = dt.date.today()
    print(data_atual)
    print(data_atual.strftime("%d/%m/%Y"))
    print(data_atual.strftime("%A/%B/%Y"))

def usando_time():
    horario = dt.time(hour=15,minute=18,second=30)
    print(horario.strftime('%H:%M:%S'))

def usando_datetime():
    data_atual = dt.datetime.now()
    print(data_atual)
    print(data_atual.strftime("%d/%m/%y %H:%M:%S"))
    print(data_atual.strftime('%c'))
    print(data_atual.year)
    print(data_atual.weekday())
    dias = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(dias[data_atual.weekday()])
    data_criada = dt.datetime(2018,6,20,15,30,20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = "01/02/2019 12:20:22"
    data_convertida = dt.datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
    print(data_convertida)
    nova_data = data_convertida - dt.timedelta(days=365, hours=2, minutes=15)
    print(nova_data)
    hour = dt.timedelta(hours=15)
    soma = hour + dt.timedelta(hours=1)
    print(soma)


if __name__=='__main__':
    usando_date()
    usando_time()
    usando_datetime()
