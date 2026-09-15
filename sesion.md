Commit hecho: 71188a5 Arreglos y bucle for en JavaScript. Quedaron adentro los // predigo: vacíos y el push("Test"), pero eso se limpia en cualquier commit futuro, no es para volver atrás.

map y filter
Los dos hacen lo mismo que un for: recorren el arreglo completo. La diferencia es qué te devuelven.

map → un arreglo del mismo tamaño, con cada elemento transformado.
filter → un arreglo más chico, solo con los elementos que cumplen una condición.
map transforma. filter selecciona. Ninguno de los dos toca el arreglo original: ambos devuelven uno nuevo.

Primero con for, que ya sabes
Tengo precios y quiero los mismos precios con IVA (multiplicar por 1.19 — este era el 1.19 de la pregunta 3 del diagnóstico):


const precios = [1000, 2500, 700];
const conIva = [];

for (let i = 0; i < precios.length; i++) {
  conIva.push(precios[i] * 1.19);
}

console.log(conIva);   // [ 1190, 2975, 833 ]
Funciona perfecto. Declaro un arreglo vacío [], recorro, y voy empujando cada precio transformado.

Lo mismo con map:


const precios = [1000, 2500, 700];

const conIva = precios.map(function (precio) {
  return precio * 1.19;
});

console.log(conIva);   // [ 1190, 2975, 833 ]
Mismo resultado, sin contador, sin length, sin arreglo vacío, sin push.

Qué está pasando ahí adentro
Esto es lo nuevo: le estás pasando una función a map.


precios.map(function (precio) {
  return precio * 1.19;
});
map recorre el arreglo solo, y por cada elemento llama a tu función pasándole ese elemento. Tú no escribes el recorrido: escribes solo qué hacer con un elemento, y map se encarga de repetirlo.


precios.map(function (precio) {
//                     └──┬──┘
//              el nombre que TÚ le pones a "el elemento de esta vuelta"
  return precio * 1.19;
//└──┬─┘
//  obligatorio: lo que devuelvas es lo que va al arreglo nuevo
});
precio es un nombre que eliges tú. Podría llamarse p, x o valor. En cada vuelta vale un elemento distinto: primero 1000, después 2500, después 700.

El return es obligatorio. Si lo olvidas, map no recibe nada y te devuelve [undefined, undefined, undefined]. Es el error número uno con map, y es la misma idea de return que ya trabajaste en return.js.

La forma corta: la flecha
Vas a ver esto escrito casi siempre así:


const conIva = precios.map(precio => precio * 1.19);
Es exactamente lo mismo. Se llama arrow function. Tres atajos aplicados de una vez:


function (precio) { return precio * 1.19; }     // forma larga
         precio  =>        precio * 1.19        // forma corta
se borra la palabra function
aparece => (un = y un > pegados) entre el parámetro y el cuerpo
si el cuerpo es una sola expresión, se borran las llaves y el return queda implícito
Usa la que te resulte más legible. Para la prueba tienes que reconocer las dos.

filter
Misma estructura, pero tu función devuelve verdadero o falso en vez de un valor transformado:


const precios = [1000, 2500, 700, 4300];

const caros = precios.filter(function (precio) {
  return precio > 1000;
});

console.log(caros);   // [ 2500, 4300 ]
filter llama a tu función con cada precio. Si devuelves true, ese elemento entra al arreglo nuevo. Si devuelves false, se descarta.

precio	precio > 1000	¿entra?
1000	false	no
2500	true	sí
700	false	no
4300	true	sí
Fíjate que 1000 no entra: 1000 > 1000 es falso. Si quisieras incluirlo sería >=.

En forma corta:


const caros = precios.filter(precio => precio > 1000);
El mini sistema completo

// Control de compras

const montos = [15000, 80000, 4300, 120000, 50000];

const mayores = montos.filter(monto => monto >= 50000);
const conIva = mayores.map(monto => monto * 1.19);

console.log("=== COMPRAS QUE REQUIEREN VISTO BUENO ===");

for (let i = 0; i < mayores.length; i++) {
  console.log((i + 1) + " - Neto: " + mayores[i] + " | Con IVA: " + conIva[i]);
}

console.log("Total de compras revisadas: " + montos.length);
console.log("Requieren visto bueno: " + mayores.length);
Imprime:


=== COMPRAS QUE REQUIEREN VISTO BUENO ===
1 - Neto: 80000 | Con IVA: 95200
2 - Neto: 120000 | Con IVA: 142800
3 - Neto: 50000 | Con IVA: 59500
Total de compras revisadas: 5
Requieren visto bueno: 3
Nota el orden: primero filtro, después transformo. mayores tiene 3 elementos y conIva también 3, así que el mismo i sirve para los dos arreglos. Y montos sigue intacto con sus 5 elementos originales: por eso puedo informar ambas cifras al final.

Tu mini sistema
Archivo nuevo, 01-fundamentos-comparados/montos.js:

Un arreglo montos con 5 o 6 cantidades en pesos.
Con filter, saca las que superan los 100000 a un arreglo nuevo.
Con map, calcula el IVA de esas (multiplicar por 1.19) a otro arreglo.
Un título y un for que liste las filtradas con su monto neto y su monto con IVA.
Dos líneas al final: cuántas había en total y cuántas quedaron tras el filtro.
Usa la forma que prefieras, larga o de flecha. La estructura es la misma del ejemplo; cambian el nombre del arreglo y el número del filtro.

Avísame cuando esté.