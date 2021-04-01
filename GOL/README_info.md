# "GAME OF LIFE"
## DECISIONES DE DISEÑO Y ARQUITECTURA

###### PRIMEROS CONCEPTOS :book:

Como primera instancia se analizó el funcionamiento interno, se trataban de posiciones referenciadas una por cada celda, donde en su totalidad formaban parte de una matriz. Dicha matriz necesitaría analizada posición por posición para cumplir con las condiciones de entorno y la lógica de supervivencia que el sistema requería.

**PRIMERAS DECISIONES**

Se optó usar Python como lenguaje de programación para poder incorporar librerias que permitan una agil manipulación de vectores y matrices. Especificamente NUMPY, librería cabecera de la lógica de la arquitectura desarrollada.

######¡A COCINAR!**

Como primer paso de la maquetación, se implemento una clase llamada Board, dado que todo funcionaba internamente dentro de un mismo tablero referenciando a la matriz. En dicha clase serán almacenados todos los metodos que abarcan el funcionamiento del sistema y los atributos basicos de tablero principal y tablero auxiliar.

**METODOS**

El primer metodo create_board() genera a través de Numpy una matriz inicialidada en valores 0 (np.zeros()), sobre dichos valores se setean las coordenadas que me permiten manifestar mi patrón inicial predeterminado (planeador). La matriz creada recibe por parametros la cantidad de filas y columnas que se ingresen por consola.

*MATRIZ CREADA*

![Alt Text](https://wikimedia.org/api/rest_v1/media/math/render/svg/6222e9f1577287b35d8c10bdb1a8018dcb46a934)

La clase continua con dos metodos que para funcionar reciben cada posición de la matriz ([x][y]) a traves de un for. Estos estan relacionados entre sí, comencemos por el segundo: **count_neighbours()**

Este metodo nos permite analizar cuantos vecinos posee respectivamente. También, es la responsable de ilimitar los bordes, generando una simulación de una matriz infinita.
La lógica que se implementó para llevar a cabo dicha caracteristica funciona a través de 2 pares de coordenadas X-X2 e Y-Y2 que reciben como valor -1 o 10 respectivamente.

¿Que nos permitió?
Al llegar a los valores límites de filas o columnas, utilizando correctamente las coordenadas en las ecuaciones podiamos redireccionar a la posición limitrofe pasante del borde.

La ejecución de este metodo nos devuelve la cantidad de vecinos considerando los 8 posibles movimientos que cada posición posee. Como el objeto el cual se itera para analizar cada posición pertenece a la misma clase, no fue necesario que le pasemos por parametro la matriz a analizar, simplemente cada coordenada.

Este resultado es utilizado en el metodo: **check_neighbours()**.
check_neighbours es un método creado para analizar el estado actual y redefinir en caso de ser necesario el resultado de cada celda a través de '1' - vivo y '0' - muerto:

Analiza con el uso de condicionales el resultado que obtuvo en count_neighbours y la compara con la lógica que debería de cumplir: en caso de estar viva; con más de tres vecinos muere por sobrepoblación y con menos de 2 vecinos muere por despoblación. Si posee 2 o 3 vecinos, se mantiene viva. En caso de estar muerta, analiza si posee 3 vecinos y nace una nueva generación.

El siguiente método corresponde a **count_status()** que nos permite llevar el recuento de la cantidad de celdas vivas y muertas a través de la iteración de toda la matriz: donde encuentre un '1', almacena un acumulador de celdas vivas y donde encuentre un '0' almacena un acumulador de celdas muertas.

El método **check_status()** fue implementado para, en caso de futuras versiones, incorporar patrones que no sean infinitos, permitirle al sistema finalizar por sí solo una vez que detecte todos valores '0' (celdas muertas) en el tablero. En el patrón actual no posee funcionamiento ya que es un loop que nunca finalizaría a causa de ese motivo.

Y por ultimo tenemos el método **main()** que fue el selecto para llevar a cabo el funcionamiento del sistema. Comienza con la recopilación de valores iniciales de filas y columnas, la construcción de ambas matrices (principal y auxiliar), la impresión en pantalla de la matriz inicial para conocer cual es el modelo sobre el cual se está iterando y luego un bucle While para estar en constante iteración. Dentro del mismo se analizan los metodos nombrados, mostrando como resultado los valores acumulados para cada iteración:
```
print("Generation {}:\n{}\nCells dead: {}\nCells alive: {}".format(i, self.boardAux, status[0], status[1]))
```
Con un tiempo de intervalo de 1 segundo entre cada una de ellas.

Todo el loop del While funciona dentro de un try, donde se manipulo el intercepto KeyboardInterrupt para dar un mensaje amigable que nos permita conocer que el funcionamiento terminó con el siguiente resultado:
```
print("\n- Evolutions done with keyboard - \n Results:\n {} generations\n {} cells alive\n {} cells dead
  \n----------------".format(i, status[1], status[0]))
```

**De esta manera finaliza nuestro README.INFO sobre decisiones de diseño y arquitectura del soft**.

## ¡Gracias!
