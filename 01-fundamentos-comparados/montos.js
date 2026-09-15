const montos = [30000, 20000, 10001, 400, 500];

const mayores = montos.filter(monto => monto > 10000);

const conIva = mayores.map(monto => monto * 1.19);

console.log("Montos netos y montos con iva numerado ");
for (let i = 0; i < mayores.length; i++) {

    console.log((i + 1) + ". Monto neto: " + mayores[i] + " - Monto con IVA: " + conIva[i]);

}

let total = 0;
for (let i = 0; i < conIva.length; i++) {
    total += conIva[i];
}

console.log(`Total de montos con IVA: ${total}`);
console.log(`Total de montos netos: ${mayores.reduce((acc, monto) => acc + monto, 0)}`);
console.log("Total de compras revisadas: " + montos.length);
console.log("Requieren visto bueno: " + mayores.length);

