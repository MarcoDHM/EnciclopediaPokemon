function comprueba(lista, nombre) {
    if (nombre.toLowerCase().startsWith('a')) {
        return "Sí, permiso activo";
    } else {
        return "No tiene permiso activo";
    }
}

let usuarios = ["Ana", "Juan", "María", "Pedro", "Alberto", "Luisa", "Andrés", "Laura", "Carlos", "Adriana"];

console.log("Listado de usuarios:");
for (let usuario of usuarios) {
    console.log(usuario);
}

let nombreIngresado = prompt("Ingrese su nombre: ");
let resultado = comprueba(usuarios, nombreIngresado);
console.log(resultado);
