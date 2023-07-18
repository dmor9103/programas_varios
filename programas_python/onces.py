# Un padre le da dinero a su hijo que cree suficiente para una gaseosa y un pastel, si sobra el suficiente dinero, este podra alcanzar para comprar otro pastel
# variables usadas:
# gas = gaseosa
# pas = pastel
# gas_pas = gaseosa mas pastel
# din_com = dinero para las comida
# din_sob = dinero sobrante
# s_n = si y no
# sn = si y no
def sobro(sn):
    print("Te pudiste comprar una gaseosa y un pastel y " + sn + " compraste otro pastel")
gas = int(1000)
pas = int(450)
gas_pas = gas + pas
din_com = int(input("Digite cuanto dinero para las onces le dio el padre al hijo: "))
while(din_com < gas_pas):
    print("dinero insuciciente!")
    din_com = int(input("Digite cuanto dinero para las onces le dio el padre al hijo: "))
    if din_com == gas_pas:
        break
din_sob = din_com - gas_pas
if din_sob >= pas:
    s_n = input("""
    desea comprar otro pastel
    - SI - NO -
    """)
    s_n.lower()
    if s_n == "si":
        sobro("si")
    elif s_n == "no":
        sobro("no")
elif din_sob < pas:
    print("No te sobro el suficiente dinero, adios")