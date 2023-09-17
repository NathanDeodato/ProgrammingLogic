programa {
  inclua biblioteca Matematica --> m

  funcao inicio() {
    // Código de conversão monetária baseado em 3 moeda diferentes
    
    escreva("- Programa de conversão monetária -")

    real moeda_br
    escreva("\nDigite o valor que deseja converter: R$")
    leia(moeda_br)

    real dolar = 4.87
    real euro = 5.19
    real yuan = 0.67

    escreva("\n- Seletor de moeda -")
    escreva("\n[1] dólar")
    escreva("\n[2] euro")
    escreva("\n[3] yuan")

    inteiro moeda_select
    escreva("\nSelecione: ")
    leia(moeda_select)

    real moeda_convertida

    se(moeda_select == 1) {
      real calc_1 = moeda_br / dolar
      
      escreva("\n- Real for Dolar -")
      escreva("\nconvertido: $", m.arredondar(calc_1, 2))
    }
    se(moeda_select == 2) {
      real calc_2 = moeda_br / euro

      escreva("\n- Real for Euro -")
      escreva("\nconvertido: $", calc_2)

    }
    se(moeda_select == 3) {
      real calc_3 = moeda_br / yuan

      escreva("\n- Real for Yuan -")
      escreva("\nconvertido: $", calc_3)
    }
    
  }
}
