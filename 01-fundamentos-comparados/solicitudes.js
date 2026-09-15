console.log("=== Solicitudes pendientes ===");

const solicitudes = ["Compra de insumos de oficina", "Mantención de aire acondicionado", "Permiso administrativo", "Reposición de tóner"];

solicitudes.push("La quinta")

for (let i = 0; i < solicitudes.length; i++) {

console.log((i + 1) + " - " + solicitudes[i]);

}

console.log("Total de solicitudes: " + solicitudes.length);
// predigo:
console.log(solicitudes);
// real: 

// el primero
// predigo: 
console.log(solicitudes[0]);
// real: 

// el último
// predigo: 
console.log(solicitudes[solicitudes.length - 1]);
// real: 

solicitudes.push("Test");

