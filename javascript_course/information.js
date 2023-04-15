//Para definir variables podemos hacerlo de 3 formas con las siguientes palabras claves o recervadas
//ej:
//-var
//-let
//-const  --> con const no podemos cambiarle el valor a la varible 
//despues de estos ponemos el nombre de nuestra variable para asi definirla correctamente 

//-------

//El console.log -> Nos permite imprimir en consola lo que le pasemos

//--------
//CONDICIONALES
//Para usar condicionales es mejor usar la palabra recervada de LET para crear variables 

let miNumero = 6
if (miNumero == 6){
    console.log("Si, Mi numero vale 6")
}else {
    console.log("No, pregunta invalida")
}

//cuando usamos el
//-Doble igual == --> esto lo toma como un es o comparacion.
//-Tres igual === --> esto nos hace una comparacion tanto del valor como el tipo de variable que tenemos

//Tambien tenemos otras comparaciones que serian 
//!= diferente 
//< menor a
//> mayor a
//<= menor e igual
//>=mayor e igual 
//&& and --> compara dos preguntas y se deben cumplir ambas 
//|| or --> compara dos preguntas o mas pero si una de las condiciones se cumpliria 

//-----------------

//BUCLES O CICLOS 
let contador = 0
while(contador < 5){
    console.log(contador)

    contador = contador + 1
}

for(let contador = 0; contador < 10; contador = contador + 1){
    console.log(contador);
}

//FUNCIONES
