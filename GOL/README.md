#"GAME OF LIFE"
##AYUDA Y USO BÁSICO DE LA APLICACIÓN

##¿Qué es GAME OF LIFE?

**Game Of Life** es un juego de simulación que nos permite, a través de un patron inicial, visualizar el nacimiento y la muerte
de celdas a lo largo del tiempo en función de condiciones de contorno pre-establecidas internamente.


**NUESTRO PATRÓN INICIAL***
```
SPACESHIPS
![Alt Text](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#/media/File:Game_of_life_animated_glider.gif)
```
El juego se ejecuta a través de la terminal, y deberá incorporar la cantidad de filas y columnas que desea para su board. Los requerimientos mínimos para un apto funcionamiento incluyen una matriz de 10x10.

```
Al cargar los datos iniciales, comienza el juego :game_die: .
```

El patrón seteado por defecto se simula en consola, desde la terminal donde se ejecuta, representado por '1' cada celda viva, y por '0' cada celda muerta. 

Podrá conocer información constantemente, tal como: CELDAS VIVAS / CELDAS MUERTAS / GENERACIONES que van transcurriendo a lo largo de toda la evolución.

**¿CUANDO TERMINA?***
El patrón por defecto -SPACESHIPS- es un loop infinito que no cumple la condición para que el sistema frene por su cuenta, por lo tanto deberá a través de comando **CTRL+C** terminar manualmente.

Al finalizar, recibirá los resultados totales generados mientras las generaciones iban transcurriendo.

**¿SE PUEDE INICIALIZAR OTRO PATRÓN?**
Hasta el momento no está incorporado la funcionalidad de modificar el patrón predeterminado.
