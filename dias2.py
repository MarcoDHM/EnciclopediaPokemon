// Definimos la lista de días de la semana
var dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"];

// Pedimos al usuario que ingrese un día de la semana
var diaIngresado = prompt("Por favor, ingresa un día de la semana:");

// Convertimos el día ingresado a minúsculas para evitar problemas de mayúsculas/minúsculas
diaIngresado = diaIngresado.toLowerCase();

// Verificamos si el día ingresado está en la lista
if (dias.includes(diaIngresado)) {
    console.log("¡Sí, está en la lista!");
} else {
    console.log("Lo siento, ese día no está en la lista.");
}
