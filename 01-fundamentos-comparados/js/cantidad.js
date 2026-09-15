function validarCantidad(cantidad) {
  if (cantidad >= 0) {
    return "ok";
  }
  return "falta la cantidad";
}

//ok
console.log(validarCantidad(5));
//falta la cantidad
console.log(validarCantidad(undefined));
//ok
console.log(validarCantidad(0));
