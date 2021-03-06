\newpage

# Clases de Complejidad

## Objetivo

El objetivo de esta sección del trabajo es analizar 4 problemas, sus posibles soluciones y su clasificación según clase de complejidad.

## Introducción Teórica

La clasificación de clases de complejidad de los problemas surge de la necesidad de comparar problemas para los cuales no se conoce una solución eficiente (polinomial), pero no se ha demostrado que no la tienen.

### Reducciones

Para comparar la dificultad de dos problemas X e Y tomamos como criterio la posibilidad de usar a uno para resolver al otro. Si se tiene un algoritmo que resuelve X, y en base a ese resultado podemos obtener una solución para el problema Y en tiempo polinómico, entonces decimos que:

- "Y es polinomialmente reducible a X" ($Y\leqslant_pX$)

- "X es tan difícil como Y", ya que resolver X asegura que podemos resolver Y, pero no se cumple la inversa. No nos referimos con dificultad al tiempo de ejecución.

Se dice por otro lado que dos problemas son _polinómicamente equivalentes_ ($Y \equiv_p X$) cuando cualquiera puede usarse para resolver al otro ($Y\leqslant_pX$ y $X\leqslant_pY$).

### Problemas de decisión

Identificamos a un problema de decisión por las siguientes componentes:

- Entrada: string $s \in S$ (siendo $S$ el espacio de strings posibles).
- Salida: _si_ o _no_ (string aceptada o rechazada).

Definimos entonces a un problema $X$ como el conjunto de strings que acepta.

Definimos a su vez a un algoritmo $A$ que resuelve a un problema $X$ como una función que toma inputs y devuelve si el problema acepta o no a esa string. Formalmente:

\begin{equation}
    A(s) = si \iff s \in X
\end{equation}

Nos son particularmente interesantes estos problemas porque la reducción de un problema de decisión $X$ a otro $Y$ consiste en transformar en tiempo polinómico la entrada de $X$ en una entrada de $Y$ de forma tal que la salida de $Y$ sea la esperada por $X$.

### Certificación

Llamamos _certificado_ a una cadena $t$ que aporta información sobre si una cadena de input $s$ será aceptada para un problema $X$. Por ejemplo, para un problema de decisión como "verificar si en un grafo hay ciclos", un posible certificado es un conjunto de vértices que supuestamente forman un ciclo. Un certificado, en este sentido, es algo similar a una solución propuesta.

Dado un problema $X$, una entrada $s$ y un certificado $t$, llamamos _certificador_ a una función B que toma certificados y evidencia con ellos que $s \in X$. Para el ejemplo anterior, un certificador tomaría el conjunto de vértices $t$ y la cadena $s$ (que serían los vértices del grafo) y verificaría que $t$ es efectivamente un ciclo en el grafo representado por $s$. Formalmente:

\begin{equation}
    B(s,t) = si \iff t \textrm{ demuestra que } s \in X
\end{equation}

Es importante observar que el certificador no analiza la cadena en sí, sino que evalúa el certificado. Por lo tanto, su función es en realidad comprobar soluciones propuestas al problema, lo cual no necesariamente resuelve el problema en sí mismo. Por este motivo, muchas veces es más sencilla y rápida la acción de un certificador que la de un algoritmo de resolución de un problema.

Llamamos _certificador eficiente_ a uno que certifica en tiempo polinómico.

### P y NP

Son de nuestro interés dos clases de complejidad:

- P: clase que contiene a todos los problemas para los cuales existen algoritmos que los resuelven en tiempo polinómico. Si X es un problema, A un algoritmo y p es una función polinómica:

\begin{equation}
    P = \{X / \exists A \in O(p(|s|)) \textrm{ que lo resuelve}\}
\end{equation}

- NP: clase que contiene a todos los problemas certificables en tiempo polinómico. Si X es un problema y B un certificador:

\begin{equation}
    NP = \{X / \exists B \in O(p(|s|)) \textrm{ que lo certifica}\}
\end{equation}

Inmediatamente podemos observar que $P \subseteq NP$, ya que si un problema puede resolverse en tiempo polinómico, entonces para certificar soluciones propuestas puede usarse el mismo algoritmo polinómico de resolución, ignorando el certificado.

Adicionalmente, de la definición de reducciones podemos observar que:

- Si $Y \leqslant_p X$ y $X$ es resoluble en tiempo polinómico, entonces $Y$ también. $X \in P \Rightarrow Y \in P$.
- Vale la recíproca: $Y\leqslant_pX \land Y \notin P \Rightarrow X \notin P$.

### NP-Completo

Además, existe un subconjunto de NP que cumple con la característica de que cualquiera de sus problemas es más difícil que cualquier otro de NP. A esta subclase la denominamos NP-completo. Visto de otro modo, que un problema pertenezca a aquella clase asegura que si se tiene un algoritmo para resolverlo, entonces es posible utilizarlo para resolver una transformación polinómica de cualquier problema de NP.

Resumiendo, un problema $X$ perteneciente a esta clase cumple con dos características:

1. $X \in NP$
2. $\forall Y \in NP: Y \leqslant_p X$

Es importante que se cumplan ambas, ya que los problemas que cumplen la segunda condición son llamados NP-hard independientemente de si son o no NP.

Dos propiedades importantes que se desprenden de la definición son:

- Si $X$ es NP-Completo y $X \leqslant_p Y$ entonces $Y$ es NP-Completo también, por la transitividad de la reducción.
- Si dos problemas son NP-Completos, son polinómicamente equivalentes.

## Determinar la clase de complejidad de un problema.

Para muchas aplicaciones es de interés determinar si un problema pertenece a alguna de las tres clases anteriores. En cada caso, el método utilizado será:

- P: encontrar una solución polinomial.
- NP: encontrar un certificador polinomial.
- NP-completo: primero es necesario probar que es NP. Luego, reducir un problema NP-completo conocido al problema en cuestión.

A continuación se presentan algunos problemas conocidos que serán de utilidad.

### SAT y 3-SAT

El problema SAT (satisfacibilidad booleana) consiste en los siguientes elementos:

- Un conjunto $X = \{x_1, x_2, \ldots x_n\}$ de variables booleanas.
- $k$ condiciones $C_i$ a satisfacer, cada una con $l$ términos unidos por disyunciones ($\lor$).
- Cada término $t_i$ en una condición es una de las variables booleanas de $X$ o su negación.

El problema se trata de decidir si existe una asignación de las variables $\nu: X \to \{0,1\}$ (mapeo concreto de cada variable a 0 o 1) que satisfaga simultáneamente todas las condiciones. Es decir, $\nu$ tal que $\bigwedge_{i=1}^{k} C_i = 1$.

La importancia de este problema reside en que el Teorema de Cook-Levin demuestra que es NP-Completo de forma directa, sin depender de otros problemas. Con ese objetivo modela cualquier con una tabla la computación completa de cualquier máquina de Turing y expresa los valores de la tabla y sus relaciones con variables booleanas que son entradas de SAT [@CLW]. De este modo se reduce cualquier lenguaje aceptable por una Máquina de Turing a un problema SAT.

El 3-SAT es un caso particular de este, donde $|C_i| = 3 \quad \forall i$. Es demostrable que es polinómicamente equivalente a SAT, ya que el segundo puede expresarse en su forma normal conjuntiva o disyuntiva eficientemente [@Cormen2009. Teorema 34.10].

Mostrar que SAT y 3-SAT son NP, por otro lado es sencillo. Un certificado es una asignación propuesta. Para verificarlo, solo será necesario ver para cada condición que esa asignación la hace verdadera. La certificación, por lo tanto, es lineal en el tamaño de la entrada, que es la cantidad total de términos ($\sum_{i=1}^{k} |C_i|$).

### Independent Set (IS)

Un conjunto de vértices de un grafo $G = (V,E)$ es _independiente_ si no contiene ningún par de vértices adyascentes.

Mientras que encontrar un IS de tamaño pequeño es trivial (cualquier vértice es un IS de tamaño 1), encontrar instancias grandes es costoso. Por este motivo, el problema de decisión asociado consiste en decidir si hay un IS de tamaño al menos $k$ para un $k$ dado.

### Vertex Cover (VC)

Se dice que un conjunto de vértices _cubre_ al grafo cuando todas las aristas tienen al menos uno de sus extremos en el conjunto.

Al revés del problema anterior, encontrar un VC de tamaño grande es trivial, ya que por ejemplo el conjunto $V$ completo es un VC. Sin embargo, encontrar instancias pequeñas no es sencillo. Por lo tanto, el problema de decisión asociado consiste en decidir si existe un VC de tamaño a lo sumo $k$ para un $k$ dado.

### Relación entre los problemas

**Teorema**: VC $\equiv_p$ IS

**Demostración**: queremos probar que si $S$ es un IS en $G$, entonces $V-S$ es un VC en $G$.

1. $S$ es IS $\Rightarrow$ $V - S$ es VC:

    Como dijimos antes, $V$ es un VC. Si quitamos uno a uno elementos de $S$ a $V$, sabemos que en ningún caso se quitarán ambos extremos de una arista. Si así fuera, dos de los elementos quitados estarían unidos y $S$ no sería un IS.

2. $V - S$ es VC $\Rightarrow$ $S$ es IS:

    Por contradicción: Si $S$ no fuera un IS, entonces podríamos afirmar que existen dos vértices $v_1,v_2 \in S$ tal que $v_1$ y $v_2$ están conectados. Entonces, $V - S$ no contendrá la unión entre esos dos vértices y por lo tanto no será un VC, contradiciendo la hipótesis.

Entonces se ve que con resolver IS para tamaño $k$, se resuelve VC para tamaño $n-k$ y viceversa. Entonces, la única transformación requerida entre un problema y otro es la cuenta $n-k$, lo cual es $O(1)$, lo cual demuestra que son polinomialmente equivalentes.

**Teorema**: 3-SAT $\leqslant_p$ IS

**Demostración**: queremos probar que se puede modelar el problema de 3-SAT como un problema de conjuntos independientes. Creamos el siguiente modelo:

- Para cada una de las $k$ condiciones creamos tres vértices, uno por cada término. Tendremos entonces, $|V| = 3k$
- Para modelar las incompatibilidades entre los términos de distintas condiciones ($x_i$ en una y $~x_i$ en otra), unimos con aristas estos casos.
- Como es suficiente satisfacer un término de cada condición para que la asignación satisfaga a todas, entonces unimos los 3 vértices de cada condición entre sí, formando triángulos. Esto no significa que no es posible satisfacer más términos, solo que hacerlo complica las incompatibilidades y no es necesario para demostrar que existe una asignación satisfactoria.

De este modo, si encontramos un conjunto independiente de al menos $k$ vértices, nos aseguramos de que elegimos al menos $k$ términos, uno de cada condición, sin que haya incompatibilidades. Este conjunto da como resultado, justamente, una asignación satisfactoria.

**Corolario**: 3-SAT $\equiv_p$ SAT $\leqslant_p$ IS $\equiv_p$ VC

Por este motivo, tanto IS como VC son NP-completos y podemos tratar de reducir esos problemas a los que querramos demostrar que también lo son.

### Subset-Sum (SS) \label{s:ss}

Este es el problema que será utilizado en todos los problemas NP-Completos. El problema consiste en:

- Un conjunto de valores $W = \{w_1, \ldots w_n\} \in \mathbb{N}$.
- Un número $K$ que es nuestra suma objetivo.

El problema de decisión es _si_ cuando existe un subconjunto de $W$ tal que la suma de sus elementos es $K$

El libro Algorithm Design [@KT. Sección 8.8] demuestra que SAT se reduce a 3D-Matching, que a su vez se reduce a este problema.

### Subset-Sum-Zero (SSZ) \label{s:ssz}

A su vez, una variante que utilizaremos tiene un conjunto de valores $W = \{w_1, \ldots w_n\} \in \mathbb{Z}$ y su problema de decisión asociado es _si_ cuando existe un subconjunto que sume 0.

Primero mostramos que este problema es NP. Dado un certificado $t$ que consiste en un subconjunto propuesto 0, se asegura que ese conjunto sume efectivamente 0. Si es necesario asegurarse de que es un subconjunto de W, eso puede hacerse con fuerza bruta en tiempo cuadrático (aunque sería más eficiente usar un hash).

Para mostrar que es NP-Completo reducimos SS general a este problema.

La reducción consiste en generar una nueva entrada $W' = W \cup \{-K\}$. Como $W$ solo tenía números naturales, entonces la única forma de que el nuevo conjunto sume 0 es si había un conjunto que sumara $K$ en $W$ y tome el nuevo elemento agregado $-K$ en $W'$. De este modo, entonces, $W'$ será la entrada de SSZ, con un costo de reducción $O(1)$.

Entonces: SS $\leqslant_p$ SSZ y por lo tanto SSZ $\in$ NP-Completo.

## Problema de Ciclos Negativos (CN)
_Se tiene un grafo dirigido y pesado G, cuyas aristas tienen pesos que pueden ser negativos. Se pide devolver si el grafo tiene algún ciclo con peso negativo._

El algoritmo de Bellman-Ford de búsqueda de caminos mínimos en grafos tiene la característica de ser óptimo con aristas de pesos negativos (cuando Dijkstra no lo es) y la ventaja de detectar, al final de su ejecución, ciclos negativos.

Aquel consiste, en cada paso, en recorrer todas las aristas $(u,v) \in E$ viendo si la distancia actual al vértice $v$ es mejorable si se llega desde $u$. Esto puede verse en pseudocódigo como:

```python
for e in edges:
    if(distance[e.dst] > distance[e.src] + e.weight):
        distance[e.dst] = distance[e.src] + e.weight
        parent[e.dst] = e.src
```

**Si no hay ciclos negativos**, en cada uno de estos pasos el algoritmo deja en su valor óptimo la distancia a cada vértice a distancia sin peso más cercano. Es decir, en el primer paso, los vértices adyascentes al origen $s$ quedarán con su menor distancia. En el segundo, los adyascentes a esos (distancia sin peso 2 a $s$) quedarán minimizados. Si recordamos que un camino mínimo no puede tener más de $|V| - 1$ aristas (no puede recorrer más de una vez un vértice o no sería óptimo), sabemos que el algoritmo encontrará el mejor camino en a lo sumo $|V|-1$ pasos de los anteriores.

Por otro lado, **en caso de haber ciclos negativos**, estos son mejorables infinitamente (se los puede seguir recorriendo sin fin y seguir bajando su peso total). De este modo, si luego de $|V|-1$ iteraciones todavía hay una arista mejorable, podemos asegurar que el grafo tiene ciclos negativos, que era el objetivo de este problema.

Entonces, el problema CN se reduce a aplicar el algoritmo de Bellman-Ford y responder 1 si el algoritmo encontró ciclos negativos.

Esto no significa necesariamente que sea el algoritmo más eficiente para resolver este problema, pero a los fines de este trabajo es suficiente, dado que el algoritmo es claramente polinómico, con complejidad $O(|E||V|)$.

Concluimos entonces que CN $\in$ P.

## Problema de Ciclos Nulos (C0)

_Se tiene un grafo dirigido y pesado G, cuyas aristas tienen pesos que pueden ser negativos. Se pide devolver si el grafo tiene algún ciclo con peso exactamente igual a cero._

Se puede demostrar que el problema de búsqueda de ciclos negativos es NP-Completo.

Primero demostraremos que es NP, o sea, que es certificable en tiempo polinomial. Dado un certificado que consiste en un ejemplo de ciclo simplemente tenemos que calcular la suma de sus pesos y ver si es cero, y además verificar que es un ciclo. Esto puede hacerse en tiempo lineal con el siguiente pseudocódigo:

```python
# Nuestro certificado fue guardado en una lista c de aristas
suma += 0
for i, edge in enumerate(c):
    suma += c[i].weight
    if edge.src != c[i-1].dst:
        return 0
return 1 if suma == 0 else 0
```

Luego reducimos un problema NP-Completo conocido, que es el SSZ (sección \ref{s:ssz}) a C0.

La reducción puede verse en la figura \ref{fig:reduccionP2} y tiene los siguientes pasos:

1. Crear un grafo de $2n$ vértices. Por cada elemento $w_i$ creamos un vértice $u_i$ y uno $v_i$.
2. Unimos cada $v_i$ con su respectivo $u_i$ mediante una arista de peso $w_i$.
3. Luego unimos cada $u_i$ con todos los $v_j$ (incluyendo el propio), mediante aristas de peso 0.

\begin{figure}
    \centering
    \includegraphics[width=0.75\columnwidth]{images/P2.png}
    \caption{Reducción Propuesta para un conjunto de 3 elementos.}
    \label{fig:reduccionP2}
\end{figure}

Esta reducción se efectúa en un tiempo cuadrático en la cantidad de elementos, ya que consiste en conectar a cada los vértices $u$ con todos los vértices $v$.

Entonces, lo que ocurre es lo siguiente:

- Como lo que debe encontrar C0 es un ciclo, entonces seguro que ese ciclo incluye al menos a ambos vértices de un elemento. Nunca se elegirá "medio vértice", ya que si así ocurriera, sería un camino abierto.
- Sabemos que **si el ciclo pasa por un elemento, se suma su valor**, ya que necesariamente debe pasar de $v_i$ a $u_i$ (si un camino llega a $v_i$ su única salida es hacia $u_i$).
- Como toda arista que no es la propia de cada elemento es nula, entonces un ciclo que tome varios elementos tendrá como peso total la suma de los elementos.
- Si un ciclo suma 0, entonces la suma de los elementos por los que pasa es 0.

En conclusión, si encontramos un ciclo de peso total 0, entonces habremos encontrado un subconjunto de elementos que suman 0 entre sí, lo cual es la solución al problema planteado.

Por lo tanto, SSZ $\leqslant_p$ C0 y entonces C0 $\in$ NP-Completo.

## Problema de decisión de Scheduling con tiempos de ejecución distintos (P3)

_Se tiene un conjunto de $n$ tareas, cada una con un tiempo de ejecución $t_i \in R_{+}$, una fecha límite de finalización $d_i \in R_+$ y una ganancia $v_i \in R_+$ que será otorgada si se finaliza antes que su tiempo límite. Se pide devolver si existe alguna planificación que obtenga una ganancia total, mayor o igual a $k \in R_+$ sabiendo que no se pueden ejecutar dos tareas a la vez._

Vamos a demostrar que este problema es NP-Completo. Para ello, primero debemos demostrar que el problema es NP, pudiendo verificar una solución al problema en tiempo polinomial.

Supongamos que tenemos una planificación de la forma $y = s[1 \ldots n]$ tal que para cada tarea $i$, denominamos a $s[i]$ como el tiempo en el que inicia dicha tarea.
Para verificar que esta solución corresponde al problema, tenemos que ver que las tareas no se solapen y que la ganancia total obtenida (es decir, la suma de las ganancias de las tareas que terminaron antes de su deadline) sea al menos $k$.

El certificador propuesto es el siguiente:

\begin{lstlisting}[mathescape]
Para cada elemento $s[i]$ de nuestra solución propuesta
    Para cada elemento $s[j]$ restante ($i \neq j$)  
        Si $s[i] < s[j]$  
            $fin[i] = s[i] + t_i$  
            Si $fin[i] \leq s[j]$  
                Si $fin[i] <= d_i$  
                    $GananciaTotal += v_i$  
                Fin Si  
            Sino  
                return False  
            Fin Si  
        Fin Si  
    Fin Para  
Fin Para  
Si $GananciaTotal \le k$  
    return False  
return True  
\end{lstlisting}

En otras palabras, para cada comienzo de tarea, se debe verificar que dicha tarea, sumado a su tiempo de ejecución, no se solape con el comienzo de ninguna otra tarea que empieza después de la actual. Además, si esto se cumple, y el fin de la tarea ocurre antes de su deadline, se suma a la ganancia total obtenida. Luego resta a saber si la ganancia total obtenida supera al $k$ determinado para esa instancia del problema.
Este certificador corre en tiempo polinomial, es $O(n^2)$.

Demostrado esto, ahora realizamos una reducción de un problema conocido NP-Completo a nuestro problema, para formalizar la demostración de que P3 es NP-Completo. Para ello, utilizamos el Subset Sum Problem (sección \ref{s:ss}).

A partir de una instancia del Subset Sum Problem: SSPI = $(sspi[1 \ldots n], k)$ donde sspi es un set de números enteros positivos y $k$ un número positivo, puedo construirme una instancia de P3, siendo los tiempos de ejecución $t_{i} = sspi_i$, las ganancias $v_{i} = sspi_i$, mi límite $k$ equivalente en ambas instancias y mis deadlines $d_{i} = k \forall i$.
Esta transformación es $O(n)$.

Ahora bien, si yo consigo una planificación $P$ que resuelve mi problema $P3$, entonces, tengo un set $S$ de tareas que terminan de ejecutarse antes de su deadline, por ende, $\sum_{i \in S} sspi_{i} \leq k$ y cuya ganancia es al menos $k$, esto es $\sum_{i \in S} sspi_{i} \geq k$. Combinando ambas restricciones, obtenemos $\sum_{i \in S} sspi_{i} = k$, lo cual es una solución para el Subset Sum Problem.


## Problema de Scheduling con k fijo (P4)

_Se tiene un conjunto de n tareas, cada una con un tiempo de ejecución igual a 1, una fecha límite de finalización_ $d_i \in N$ _y una ganancia_ $v_i \in R$ _que será otorgada si se finaliza antes que su tiempo límite. Se pide devolver si existe alguna planificación que obtenga una ganancia total_ $k \in R$ _sabiendo que no se pueden ejecutar dos tareas a la vez._

El problema NP-completo conocido que resulta intuitivo aplicar es _SS_ (sección \ref{s:ss}), ya que el problema de decisión _P4_ es una elección de elementos de un conjunto para que sumen un valor específico.

Para reducir subset-sum a nuestro problema, podemos transformar la entrada del siguiente modo:

- Cada elemento $w_i$ será una tarea con:
	- Tiempo de ejecución igual a 1. Esto es obligatorio para la entrada de este problema.
	- Deadline n+1 (o infinito). Esto permite que todas las tareas sean elegidas.
- La ganancia deseada $K$ será el mismo número que la suma del SS original.

Esta transformación es lineal, ya que todo lo que hace es crear una tarea por elemento.

Esta entrada será la de P4, que decidirá si existe una planificación que tenga como ganancia total $K$, o sea que elegirá un subconjunto de $W$ que sume $K$, resolviendo el problema de _subset-sum_. Por lo tanto, sabemos que SS $\leqslant_p$ P4 y por lo tanto P4 $\in$ NP-Completo.
