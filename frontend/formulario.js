document
 .getElementById("submitButtonRegister")
 .addEventListener("click", (e) => {
  e.preventDefault(); // Evita que el formulario se envíe de forma predeterminada
  sendData(); // Llama a la función para enviar los datos
 });

function sendData() {
 Validacion = CamposObligatorios(document.getElementsByClassName("myForm"));
 if (Validacion == true) {
  let formulario = document.getElementById("myForm");
  var user = new FormData(); // Obtiene los datos del formulario
  user.append("id_card", document.getElementById("id_card_register").value);
  user.append("name_user", document.getElementById("name_user_register").value);
  user.append(
   "hash_password",
   document.getElementById("hash_password_register").value
  );

  var userCompletos = Object.fromEntries(user.entries());

  listaUser = {};
  listaUser.userCompletos = JSON.stringify(userCompletos);

  fetch("http://127.0.0.1:8000/users/", {
   method: "POST",
   body: listaUser.userCompletos,
   headers: { "Content-Type": "application/json" },
  })
   .then(function (response) {
    if (response.ok) {
     document.getElementById("user").innerHTML =
      "¡Usuario!, Se creo el usuario satisfactoriamente";
    } else {
     document.getElementById("user").innerHTML = "Error en la solicitud:";
    }
   })
   .catch(function (error) {
    document.getElementById("user").innerHTML = "Error en la solicitud:";
   });

  var account = new FormData(); // Obtiene los datos del formulario
  account.append("id_user", document.getElementById("id_card_register").value);
  account.append(
   "name_surname",
   document.getElementById("name_surname_register").value
  );
  account.append("balance", document.getElementById("balance_register").value);

  var accountCompletos = Object.fromEntries(account.entries());

  listaAccount = {};
  listaAccount.accountCompletos = JSON.stringify(accountCompletos);

  fetch("http://127.0.0.1:8000/accounts/", {
   method: "POST",
   body: listaAccount.accountCompletos,
   headers: { "Content-Type": "application/json" },
  })
   .then(function (response) {
    if (response.ok) {
     document.getElementById("cuenta").innerHTML =
      "¡Cuenta!, Se creo la cuenta";
    } else {
     document.getElementById("cuenta").innerHTML = "Error en la solicitud:";
    }
   })
   .catch(function (error) {
    document.getElementById("cuenta").innerHTML = "Error en la solicitud:";
   });
  formulario.reset();
 }
}

document
 .getElementById("submitButtonTransaction")
 .addEventListener("click", (e) => {
  e.preventDefault(); // Evita que el formulario se envíe de forma predeterminada
  console.log("ingresamos aca");
  sendTransaction();
 });

function sendTransaction() {
 Validacion = CamposObligatorios(
  document.getElementsByClassName("formTransaccion")
 );
 if (Validacion == true) {
  var transaccion = new FormData();
  transaccion.append(
   "id_account",
   document.getElementById("num_cuenta_transaction").value
  );
  transaccion.append(
   "id_type_transactions",
   document.getElementById("select_tipoTransaccion").value
  );

  transaccion.append("amount", document.getElementById("monto").value);
  var trasactionCompletos = Object.fromEntries(transaccion.entries());

  update(trasactionCompletos);
  listaTransaction = {};
  listaTransaction.trasactionCompletos = JSON.stringify(trasactionCompletos);

  //console.log(trasactionCompletos);
  fetch("http://127.0.0.1:8000/transactions/", {
   method: "POST",
   body: listaTransaction.trasactionCompletos,
   headers: { "Content-Type": "application/json" },
  })
   .then(function (response) {
    if (response.ok) {
     true;
    } else {
     document.getElementById("transaccionmsj").innerHTML =
      "Error en la solicitud:";
    }
   })
   .catch(function (error) {
    document.getElementById("transaccionmsj").innerHTML =
     "Error en la solicitud:";
   });
 }
}

function update(datos) {
 listaTransaction = {};
 listaTransaction.datos = JSON.stringify(datos);
 fetch("http://127.0.0.1:8000/accounts/", {
  method: "PUT",
  body: listaTransaction.datos,
  headers: { "Content-Type": "application/json" },
 })
  .then(function (response) {
   if (response.ok) {
    document.getElementById("transaccionmsj").innerHTML =
     "¡Transaccion!, Se realizo la transacción satisfactoriamente";
   } else {
    document.getElementById("transaccionmsj").innerHTML =
     "Saldos insuficientes";
   }
  })
  .catch(function (error) {
   document.getElementById("transaccionmsj").innerHTML =
    "Error en la solicitud:";
  });
 document.getElementById("formTransaccion").reset();
}

function CamposObligatorios(forms) {
 Validacion = false;
 var validation = Array.prototype.filter.call(forms, function (form) {
  if (form.checkValidity() === false) {
   event.preventDefault();
   event.stopPropagation();
  } else {
   Validacion = true;
  }
  form.classList.add("was-validated");
 });
 return Validacion;
}

$(document).ready(function () {
 hide_div();
 hideButtoms();

 // :Funcion que oculta botones
 function hideButtoms() {
  $("#jqxLoaderinicio").hide();
  $("#btn-cslt-adjuntarSap").hide();
 }
 // :funcion que oculta las vistas
 function hide_div() {
  document.getElementById("div-consultar-cuenta").style.display = "none";
  document.getElementById("div-transaccion").style.display = "none";
  // document.getElementById("div-buttons").style.display = "none";
  // document.getElementById("form-editar").style.display = "none";
 }
 $("#consultar_saldo").on("click", function () {
  document.getElementById("div-consultar-cuenta").style.display = "";
  document.getElementById("div-transaccion").style.display = "none";
  consulData();
 });

 $("#transaccion").on("click", function () {
  document.getElementById("div-consultar-cuenta").style.display = "None";
  document.getElementById("div-transaccion").style.display = "";
  document.getElementById("fila").remove();
 });

 function consulData() {
  console.log(document.getElementById("name_user_register").value);
  var xhr = new XMLHttpRequest();
  xhr.open(
   "GET",
   "http://127.0.0.1:8000/accounts/" +
    document.getElementById("name_user_register").value,
   true
  );
  xhr.onreadystatechange = function () {
   if (xhr.readyState === XMLHttpRequest.DONE) {
    if (xhr.status === 200) {
     var data = JSON.parse(xhr.responseText);
     // Aquí puedes hacer algo con los datos recibidos
     table(data);
    } else {
     console.error("Error en la solicitud:", xhr.status);
    }
   }
  };
  xhr.send();
 }

 function table(data) {
  const table = document.getElementById("accountUsuario");

  table.innerHTML +=
   "<tr id='fila'><td>" +
   data.id_account +
   "</td><td>" +
   data.id_user +
   "</td><td>" +
   data.name_surname +
   "</td><td>" +
   data.balance +
   "</td></tr>";
 }
});
