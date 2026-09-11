from Model import model_lead
import control

def add_leads():
    name = input("Nome:")
    email = input("E-mail:")
    status = input("Status do fluxo de vendas:")

  #validar status
  #
    print(model_lead(name,email,status))

    control.create_lead(model_lead(name,email,status))

def list_leads():
    leads = control.read_leads()
    print(leads)

def main():
  while True:
    print("\nmini crm de leads")
    print("[1] adicionar leads")
    print("[2] listar leads")
    print("[0] sair do programa")

    opt = input("escolha uma opção:")

    if opt == "1":
        add_leads()
    elif opt == "2":
        list_leads
    elif opt == "0":
        print("até mais...")
        break
    else:
        print("opção invalida")

if __name__ == "__main__":
    main()