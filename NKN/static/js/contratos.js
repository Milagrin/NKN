//Funcionalidad

$(function () {
    var operation = "C"; //"C"=Crear
    var selected_index = -1; // Indice de el elemento seleccionado en la lista
    var tblContratos = localStorage.getItem("tblContratos"); //Retornar los datos almacenados
    tblContratos = JSON.parse(tblContratos); //Convertir String a Object
    if (tblContratos === null) // Si no hay datos, inicializar un array vacio
        tblContratos = [];
  
    function Create() {
      //Obtener los valores de la forma HTML y transformalos en String.
      var contrato = JSON.stringify({
        Rut: $("#txtRutP").val(),
        Name: $("#txtNombreP").val(),
        DateI: $("#dtFechaI").val(),
        DateF: $("#dtFechaT").val(),
        Tipo: $("#txtTipoC").val()
      }); 
      //Añadir el objeto a la tabla
      tblContratos.push(contrato);
      //Almacenar los datos en el Local Storage
      localStorage.setItem("tblContratos", JSON.stringify(tblContratos));
      alert("Los datos han sido almacenados correctamente"); //Mensaje de alerta
      return true;
    }
  
    function Edit() {
      // Editar el item seleccionado en la tabla
      tblContratos[selected_index] = JSON.stringify({
        Rut: $("#txtRutP").val(),
        Name: $("#txtNombreP").val(),
        DateI: $("#dtFechaI").val(),
        DateF: $("#dtFechaT").val(),
        Tipo: $("#txtTipoC").val()
      });
      //Almacenar los datos en el Local Storage
      localStorage.setItem("tblContratos", JSON.stringify(tblContratos)); 
      alert("Los datos han sido editados correctamente"); //Mensaje de alerta
      return true;
    }
  
    function Delete() {
      //Eliminar el elemento seleccionado en la tabla
      tblContratos.splice(selected_index, 1); 
      //Actualizar los datos del Local Storage
      localStorage.setItem("tblContratos", JSON.stringify(tblContratos)); 
      alert("Contrato Eliminado correctamente"); //Mensaje de alerta
    }
  
    function List() {
        $("#tbList").html("");
        $("#tbList").html(
            "<thead>"+
            "<tr>"+
            "<th>Rut</th>"+
            "<th>Nombre</th>"+
            "<th>Fecha Inicio</th>"+
            "<th>Fecha Termino</th>"+
            "<th>Tipo Contrato</th>"+
            "</tr>"+
            "</thead>"+
            "<tbody>"+
            "</tbody>"
              ); //Agregar la tabla a la estructura HTML
      for (var i in tblContratos) {
          var con = JSON.parse(tblContratos[i]);
          $("#tbList tbody").append("<tr>"+
            "<td>" + con.Rut + "</td>"+
            "<td>" + con.Name + "</td>"+
            "<td>" + con.DateI + "</td>"+
            "<td>" + con.DateF + "</td>"+
            "<td>" + con.Tipo + "</td>"+
            "<td><img src='/img/edit.png' alt='Edit" + i + "' class='btnEdit'/>&nbsp &nbsp<img src='/img/delete.png' alt='Delete" + i + "' class='btnDelete'/></td>" +
            "</tr>"
        );
      } //Recorrer y agregar los items a la tabla HTML
    }
  
    $("#frmContrato").bind("submit", function () {
      if (operation === "C")
          return Create();
      else
          return Edit();
    }); //Función para decidir si se encuentra añadiendo o editando un item
    
    List();
  
    $(".btnEdit").bind("click", function () {
      operation = "E"; //"E" = Editar
      //Obtener el identificador del item a ser editado
      selected_index = parseInt($(this).attr("alt").replace("Edit", ""));
      // Convertir de JSON al formato adecuando para editarlos datos
      var con = JSON.parse(tblContratos[selected_index]); 
       $("#txtRutP").val(con.Rut);
        $("#txtNombreP").val(con.Name);
        $("#dtFechaI").val(con.DateI);
        $("#dtFechaT").val(con.DateF);
        $("#txtTipoC").val(con.Tipo);
        $("txtRutP").attr("readonly", "readonly");
        $("txtNombreP").focus();
    });
  
    $(".btnDelete").bind("click", function () {
      //Obtener el identificador del item a ser eliminado
      selected_index = parseInt($(this).attr("alt").replace("Delete", "")); 
      Delete(); //Eliminar el item
      List(); //Volver a listar los items en la tabla
    });
  });
  