// Ótima pergunta! O motivo de usarmos `sDiagSec += matriz[i][2 - i]` 
//no cálculo da diagonal secundária é para acessar os elementos certos 
//dentro da matriz **3×3**. Vamos analisar isso em detalhes.  

// ---

// ## 📌 Como funciona `matriz[i][2 - i]`?

// ### 🔹 Índices da Matriz 3×3  
// Lembre-se de que os **índices** da matriz começam em `0` e vão até `2`:  

// ```
// [0][0]   [0][1]   [0][2]  
// [1][0]   [1][1]   [1][2]  
// [2][0]   [2][1]   [2][2]  
// ```

// A **diagonal secundária** é composta pelos elementos:  

// ```
// -   -   3  → [0][2]  
// -   5   -  → [1][1]  
// 7   -   -  → [2][0]  
// ```

// Ou seja, os índices são:  
// - **`matriz[0][2]`** → primeiro elemento da diagonal secundária  
// - **`matriz[1][1]`** → segundo elemento da diagonal secundária  
// - **`matriz[2][0]`** → terceiro elemento da diagonal secundária  

// ### 🔹 Como a fórmula `matriz[i][2 - i]` resolve isso?
// Vamos ver o que acontece em cada iteração do loop:

// | Valor de `i` | Cálculo de `2 - i` | Índice acessado |
// |--------------|--------------------|-----------------|
// | `i = 0` | `2 - 0 = 2` | `matriz[0][2]` → 3 |
// | `i = 1` | `2 - 1 = 1` | `matriz[1][1]` → 5 |
// | `i = 2` | `2 - 2 = 0` | `matriz[2][0]` → 7 |

// Como vemos, a fórmula `matriz[i][2 - i]` percorre exatamente os elementos da diagonal secundária! 🚀  

// ---

// ### 🎯 Resumo:
// - **Diagonal principal** usa `matriz[i][i]` porque os índices são iguais.  
// - **Diagonal secundária** usa `matriz[i][2 - i]` porque precisamos pegar `(0,2)`, `(1,1)`, `(2,0)`.  
// - O número **2** é porque estamos trabalhando com uma matriz **3×3** (os índices vão de `0` a `2`).  

// Se fosse uma **matriz 4×4** 
// a fórmula seria `matriz[i][3 - i]`, e assim por diante!  

// Espero que tenha ficado claro! Qualquer dúvida, manda aí! 😃🔥