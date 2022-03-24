//extrae el id y el name en el formulario

function updateEmptyFormIDs(element,totalForms){
   var thisInput=element
   var currentName=element.attr('name')

   //ESTO ES LO QUE REEMPLAZA PREFIX CON totalForms
   var newName=currentName.replace(/__prefix__/g,totalForms)

   //esto es lo que reemplaza name con el numero totalForms
   thisInput.attr('name',newName)

   //esto es lo que reemplaza id con el numero totalForms
   thisInput.attr('id',"id_"+newName)


   var newFormRow=element.closest(".form-row");
   var newRowId="row_id_"+newName
   newFormRow.attr("id",newRowId)

   newFormRow.addClass("new-parent-row")


   var parentDiv=element.parent();
   parentDiv.attr("id","parent_id_"+newName)

   var inputLabel=parentDiv.find("label")
   inputLabel.attr("for","id_"+newName)


   return newFormRow

   }

//das click al boton y te agrega más filas

$( "#add_more" ).click(function(e) {
  var formId="id_form-TOTAL_FORMS"
  var emptyRow=$("#empty-row").clone();
  emptyRow.attr("id",null)
  var totalForms=parseInt($('#'+formId).val());
  var newFormRow;
  //checar si poner varios inputs
  emptyRow.find("input, checkbox").each(function(){
        newFormRow=updateEmptyFormIDs($(this),totalForms)
  })
  //$("#additems").val("true");
  //chacar esto si es id o class
  $(".form-row:last").after(newFormRow)
  $('#'+formId).val(totalForms+1);
});



