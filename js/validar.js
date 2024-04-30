// Validar Registro de sesion
function validarRegistro() {
	var nombre = document.forms["formRegistro"]["nombre"].value;
	var correo = document.forms["formRegistro"]["correo"].value;
	var contraseña = document.forms["formRegistro"]["contraseña"].value;
	var direccion = document.forms["formRegistro"]["direccion"].value;
  var ciudad = document.forms["formRegistro"]["ciudad"].value;
	var text;
	var formValido = true;
	
	
	if (nombre.length == 0){
        text = "Nombre no debe estar vacio";   
		formValido = false;
    }else{
        text = "";
    }
    document.getElementById("valida_nombre").innerHTML = text;

	if (correo.length == 0){
        text = "Correo no debe estar vacio";   
		formValido = false;
    }else{
        text = "";
    }
    document.getElementById("valida_email").innerHTML = text;

  if (contraseña.length < 8){
    text = "Contrasena debe tener largo 8";
    formValido = false;
    }else{
      text = "";
    }
    document.getElementById("valida_password").innerHTML = text;
	
  if (direccion.length==0){
    text="Direccion no debe estar vacio"
    formValido = false;
  }else{
    text=""
  }
  document.getElementById("valida_direccion").innerHTML= text;

  if (ciudad.length==0){
    text="Ciudad no debe estar vacio"
    formValido = false;
  }else{
    text=""
  }
  document.getElementById("valida_ciudad").innerHTML= text;

	
	
	
	if (!formValido) {
    event.preventDefault(); 
    
}else{
  alert('REGISTRO COMPLETADO');
}
}
// Validar Inicio de sesion
function validarInicio() {
  var contraseña = document.forms["formInicio"]["contraseña"].value;
  var correo = document.forms["formInicio"]["correo"].value;
  var text;
  formValido=true;

if (correo.length == 0){
    text = "Correo no debe estar vacio";   
  formValido = false;
}else{
    text = "";
}
document.getElementById("valida_mail").innerHTML = text;

if (contraseña.length < 8){
    text = "Contrasena debe tener largo 8";
    formValido = false;
    }else{
      text = "";
    }
    document.getElementById("valida_contra").innerHTML = text;
    if (!formValido) {
      event.preventDefault(); 
      
  }else{
    alert('Inicio COMPLETADO');
  }
}
