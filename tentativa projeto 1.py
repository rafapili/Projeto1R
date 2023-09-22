def main():
    tema = "Suporte Técnico"
    print(f"Bem-vindo ao {tema}!")

    while True:
        print(f"\nOpções de Atendimento em {tema}:")
        opcoes = {
            '1': "Como instalar o software?",
            '2': "Como redefinir a senha?",
            '3': "Como entrar em contato conosco?",
            '4': "Horário de Atendimento",
            '5': "Sair"
        }

        for chave, descricao in opcoes.items():
            print(f"{chave} - {descricao}")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '1':
            print("Passo 1: Faça o download do software.")
            print("Passo 2: Execute o instalador.")
            print("Passo 3: Siga as instruções de instalação.")
            input("Pressione Enter para continuar...")
        elif escolha == '2':
            print("Passo 1: Acesse a página de redefinição de senha.")
            print("Passo 2: Insira seu e-mail.")
            print("Passo 3: Siga as instruções para criar uma nova senha.")
            input("Pressione Enter para continuar...")
        elif escolha == '3':
            print("Você pode entrar em contato conosco por e-mail ou telefone.")
            print("Nosso e-mail de suporte é support@exemplo.com")
            print("Nosso número de telefone é (123) 456-7890.")
            input("Pressione Enter para continuar...")
        elif escolha == '4':
            print("\nHorários de Atendimento:")
            print("1 - Segunda a sexta-feira, digite 1 para ver o horario")
            print("2 - Segunda a sexta-feira, digite 2 para ver o horario")
            print("3 - Terça a sábado, digite 3 para ver o horario")
            print("4 - Sábado e domingo, digite 4 para ver o horario")

            horario = input("Escolha uma opção (1/2/3/4): ")

            if horario == '1':
                print("Das 9h às 18h.")
            elif horario == '2':
                print("Das 10h às 17h.")
            elif horario == '3':
                print("Das 8h às 17h.")
            elif horario == '4':
                print("Das 12h às 20h.")
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
            input("Pressione Enter para continuar...")
        elif escolha == '5':
            print(f"Obrigado por utilizar nosso {tema}. Adeus!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
