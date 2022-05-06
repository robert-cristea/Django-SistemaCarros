

function totales(){

    var descuento=document.getElementById('id_descuento').value;
    var total=document.getElementById('id_total').value;
    totales=(descuento * total) / 100;
    document.getElementById("id_total").value = totales;

}




function updateEmptyFormIDs(element,totalForms){
    //get current form input name
    var thisInput=element
    //console.log("thisInput en updateEmptyFormIDs:",{thisInput})
    //get current form input name
    var currentName=element.attr('name')
    //console.log("currentName en updateEmptyFormIDs:",{currentName})
    //replace "prefix" with actual number
    var newName=currentName.replace(/__prefix__/g,totalForms)
    //console.log("newName en updateEmptyFormIDs:",{newName})

    //update input w/new name
    thisInput.attr('name',newName)
    thisInput.attr('id',"id__"+newName)

    var newFormRow=element.closest(".part-form");

    var newRowId="row_id_"+newName
    newFormRow.attr("id",newRowId)
    //console.log('newRowId:',{newRowId})
    //console.log('newFormRow:',{newFormRow})

    newFormRow.addClass("new-parent-row")
    var parentDiv=element.parent();
    parentDiv.attr("id","parent_id_"+newName)
//    console.log('parentDiv:',{parentDiv})

    var inputLabel=parentDiv.find("label")
    inputLabel.attr("for","id_"+newName)
//    console.log('inputLabel:',{inputLabel})
    return newFormRow

}



function addForm(){
//$('.add-new-form').click(function(e){
    //e.preventDefault()
    var formId="id_form-TOTAL_FORMS"
    //copy empty form
    var emptyRow=$("#empty-row").clone();

    //remove id from new form
    emptyRow.attr("id",null);

    //get starting form count for formset
    var totalForms=Number($('#'+formId).val());

   //create new form row from empty from row
    var newFormRow;
    //no entendi
    emptyRow.find("input,select,textarea").each(function(){
        newFormRow=updateEmptyFormIDs($(this),totalForms)
    })

    //insert new form at the end of the last form
    $(".part-form:last").after(newFormRow)

    //update total form count
    $('#'+formId).val(totalForms+1);

}
//    });

function deleteForm(e) {
    // var value = Number.parseInt($("#id_form-TOTAL_FORMS").val()) - 1;
    // $("#id_form-TOTAL_FORMS").val(value);
    console.log(e.previousSibling);
    e.previousSibling.checked = true;
    e.parentNode.parentNode.style.display='none';
}

function multiplicar(){

    //obteniendo el numero
    var formId="id_form-TOTAL_FORMS"
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1
    console.log("totalForms en multiplicar",{totalForms})

    //para el id_0
//    let quantity0='id_form-0-quantity';
//    let unit_price0='id_form-0-unit_price';
//    let total_price0='id_form-0-total_price';

//    quantity0 = parseInt($('#'+quantity0).val());
//    console.log({quantity0});
//    unit_price0 = parseInt($('#'+unit_price0).val());
//    console.log({unit_price0});
    //let multiplicarTotal_Price0=quantity0*unit_price0;

    //$('#'+total_price0).val(quantity0*unit_price0);
    //console.log({total_price0});

    //para el id dinamico
    let quantity='id__form-'+totalForms+'-quantity';
    let unit_price='id__form-'+totalForms+'-unit_price';
    let total_price='id__form-'+totalForms+'-total_price';

    quantity = Number($('#'+quantity).val());
    console.log("el elemento quantity:",{quantity});
    unit_price = Number($('#'+unit_price).val());

    console.log("el elemento unit_price:",{unit_price});

    let multiplicarTotal_Price=quantity*unit_price;
    console.log({multiplicarTotal_Price});
    $('#'+total_price).val(multiplicarTotal_Price);

    //total_price = parseInt($('#'+total_price).val());
    //multiplicarTotal_Price=quantity*unit_price;

    console.log({multiplicarTotal_Price});

    return total_price;
}




//EL DESCUENTO DEL PORCENTAJE DINAMICO ESTÁ BIEN, SÓLO REVISAR EL 0
//
function descuentoParte(total_price){
   //obteniendo el numero de total_forms
    var formId="id_form-TOTAL_FORMS"
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1


    //porcentaje dinamico

    let descuentoPartes='id__form-'+totalForms+'-descuento_parte';
    console.log('dinamico funcion descuentoParte: ',{descuentoPartes});
    descuentoPartes = Number($('#'+descuentoPartes).val());
    console.log({descuentoPartes});
    console.log('dinamico funcion descuentoParte total_price: ',{total_price});
    totalPrice=Number($('#'+total_price).val());
    $('#'+total_price).val((totalPrice*descuentoPartes)/100);


    return total_price;

}




function taxes_free(total_price) {

    //obteniendo el numero
    var formId="id_form-TOTAL_FORMS"
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1
    //console.log("totalForms en taxes_free",{totalForms})

    let tax_free='id__form-'+totalForms+'-tax_free';

//si el check es true
     if (document.getElementById(tax_free).checked){
          //total_price=operacionPorcentaje;
          total_price = Number($('#'+total_price).val());
          let libre_impuestos = (total_price*4)/100;
          //console.log("taxes free en total_price", {total_price});

          //libre_impuestos
          total_price='id__form-'+totalForms+'-total_price';
          $('#'+total_price).val(libre_impuestos);
          total_price=libre_impuestos
          return total_price;

      }

    else{
      //console.log("total price en la funcion taxes free en el else",{total_price});
      document.getElementById('#'+total_price).value =total_price;

      //document.getElementById("id_total").value =total_price;
    }


}


//*******************************************EDITAR AQUI

function descuentoTotalFuncion(total_price){

    //obteniendo el numero
    var formId="id_form-TOTAL_FORMS"
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1
    total_price='id_form-'+totalForms+'-total_price';
    document.getElementById(total_price);
    let sumaTotales=0;
    let i=1;
          while ( i < totalForms+1){
            total_price='id__form-'+i+'-total_price';
            total_price=Number(document.getElementById(total_price).value);
            sumaTotales=sumaTotales+total_price;
            i++;
          }


    if (document.getElementById('id_descuento_0').checked){
          descuentoTotal=Number(document.getElementById('id_descuentoTotal').value);
          let totalOperacion=sumaTotales-descuentoTotal;
          let total=document.getElementById('id_total');
          total=totalOperacion;
          let to=totalOperacion.toFixed(2);
          document.getElementById("id_total").value=to;
     }


    else{
            descuentoTotal=Number(document.getElementById('id_descuentoTotal').value);
            operacionPorcentaje=(descuentoTotal*sumaTotales)/100;
            let op=operacionPorcentaje.toFixed(2);
            document.getElementById("id_total").value=op;
    }
}


//**********************************************LABORS


function updateEmptyFormID(element,totalForms){
    //get current form input name
    var thisInput=element
    console.log("mano obra updateEmptyFormIDs thisInput:",{thisInput})
    //get current form input name
    var currentName=element.attr('name')
    console.log("mano obra updateEmptyFormIDs currentName en :",{currentName})
    //replace "prefix" with actual number
    var newName=currentName.replace(/__prefix__/g,totalForms)
    console.log("mano obra updateEmptyFormIDs newName:",{newName})

    //update input w/new name
    thisInput.attr('name',newName)
    thisInput.attr('id',"id__"+newName)

    var newFormRow=element.closest(".form-rows");

    var newRowId="row_id_"+newName
    newFormRow.attr("id",newRowId)
    console.log('manoobra newRowId:',{newRowId})
    console.log('manoobra newFormRow:',{newFormRow})

    newFormRow.addClass("new-parent-row")
    var parentDiv=element.parent();
    parentDiv.attr("id","parent_id_"+newName)
//    console.log('parentDiv:',{parentDiv})

    var inputLabel=parentDiv.find("label")
    inputLabel.attr("for","id_"+newName)
//    console.log('inputLabel:',{inputLabel})

    return newFormRow

}



function addForms(){
//$('.add-new-form').click(function(e){
    //e.preventDefault()
    var formId="id_manoobra-TOTAL_FORMS"
    console.log("manoobra de formId:",{formId})
    //copy empty form
    var emptyRow=$("#empty-rows").clone();
    console.log("manoobra de emptyRow:",{emptyRow})

    //remove id from new form
    emptyRow.attr("id",null);

    //get starting form count for formset
    var totalForms=Number($('#'+formId).val());
    console.log("manoobra de totalForms:",{totalForms})

   //create new form row from empty from row
    var newFormRow;
    //no entendi
    emptyRow.find("input,select,textarea").each(function(){
        newFormRow=updateEmptyFormID($(this),totalForms)
    })

    //insert new form at the end of the last form
    $(".form-rows:last").after(newFormRow)

    //update total form count
    $('#'+formId).val(totalForms+1);

}


//**********************************************PAYMENT


function updateEmptyFormIDz(element,totalForms){
    //get current form input name
    var thisInput=element
    //get current form input name
    var currentName=element.attr('name')
//    console.log("pago updateEmptyFormIDs currentName en :",{currentName})
    //replace "prefix" with actual number
    var newName=currentName.replace(/__prefix__/g,totalForms)
//    console.log("pago updateEmptyFormIDs newName:",{newName})

    //update input w/new name
    thisInput.attr('name',newName)
    thisInput.attr('id',"id__"+newName)

    var newFormRow=element.closest(".form-rowz");

    var newRowId="row_id_"+newName
    newFormRow.attr("id",newRowId)
//    console.log('pago newRowId:',{newRowId})
//    console.log('pago newFormRow:',{newFormRow})

    newFormRow.addClass("new-parent-row")
    var parentDiv=element.parent();
    parentDiv.attr("id","parent_id_"+newName)
//    console.log('parentDiv:',{parentDiv})

    var inputLabel=parentDiv.find("label")
    inputLabel.attr("for","id_"+newName)
//    console.log('inputLabel:',{inputLabel})

    return newFormRow

}



function addFormz(){
//$('.add-new-form').click(function(e){
    //e.preventDefault()
    var formId="id_pagos-TOTAL_FORMS"
//    console.log("pagos de formId:",{formId})
    //copy empty form
    var emptyRow=$("#empty-rowz").clone();
//    console.log("pagos de emptyRow:",{emptyRow})

    //remove id from new form
    emptyRow.attr("id",null);

    //get starting form count for formset
    var totalForms=Number($('#'+formId).val());
//    console.log("pagos de totalForms:",{totalForms})

   //create new form row from empty from row
    var newFormRow;
    //no entendi
    emptyRow.find("input,select,textarea").each(function(){
        newFormRow=updateEmptyFormIDz($(this),totalForms)
    })

    //insert new form at the end of the last form
    $(".form-rowz:last").after(newFormRow)

    //update total form count
    $('#'+formId).val(totalForms+1);

}


function convMinHr(){
    console.log("todo ok convMinHr");

    var formId="id_manoobra-TOTAL_FORMS"
    console.log(" mano obra convMinHr",{formId})
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1
    console.log("convMinHr en totalForms",{totalForms})

    let minutos='id__manoobra-'+totalForms+'-minutos';
    console.log("convMinHr en minutos:",{minutos})
    minutosVal=Number(document.getElementById(minutos).value)
    console.log("convMinHr en minutos:",{minutosVal})
    let operacion=minutosVal/60;
    console.log("convMinHr en minutos:",{operacion})
    return operacion;

}

function convTarifa(operacion){
    console.log("todo ok en convTarifa")

    var formId="id_manoobra-TOTAL_FORMS"
    console.log(" mano obra convTarifa",{formId})
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1
    console.log("convTarifa en totalForms",{totalForms})

    let horas='id__manoobra-'+totalForms+'-horas';
    let tarifa='id__manoobra-'+totalForms+'-tarifa';
    let tarifaTotal='id__manoobra-'+totalForms+'-tarifa_total';

    console.log("convTarifa en horas:",{horas})
    console.log("convTarifa en tarifa:",{tarifa})
    console.log("convTarifa en tarifa_total:",{tarifaTotal})

    let horasVal=Number(document.getElementById(horas).value)
    console.log("convTarifa en horas:",{horasVal})

    let tarifaVal=Number(document.getElementById(tarifa).value)
    console.log("convTarifa en tarifa:",{tarifaVal})

    let tarifaTotalId=document.getElementById(tarifaTotal)
    console.log("convTarifa en tarifaTotal:",{tarifaTotalId})
    console.log("convTarifa en operacion:",{operacion})

    let tarifaTotalVal=Number(operacion+horasVal);
    console.log("convTarifa en tarifaTotalVal:",{tarifaTotalVal})
    tarifaTotalVal=Number(tarifaTotalVal*tarifaVal);
    console.log("convTarifa en tarifaTotalVal:",{tarifaTotalVal})
 //   console.log("convTarifa en tarifaTotalVal:",{tarifaTotalVal})


    document.getElementById(tarifaTotal).value=tarifaTotalVal;
//    console.log("convTarifa en tarifaTotalVal:",{tarifaTotalVal})

    return (tarifaTotalVal,tarifaTotal);

}




function taxes_freez(tarifaTotalVal,tarifaTotal) {

    //obteniendo el numero
    var formId="id_manoobra-TOTAL_FORMS"
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1


    let libre_impuestoz='id__manoobra-'+totalForms+'-libre_impuestos';
    console.log("taxes_freez, libre impuestos:",{libre_impuestoz});
    tarifa_total='id__manoobra-'+totalForms+'-tarifa_total';
    console.log("taxes_freez, tarifa total:",{tarifa_total});

    let checkBox = document.getElementById(libre_impuestoz);
    console.log("taxes_freez, checkBox:",{checkBox});
    tarifaTotal = Number($('#'+tarifa_total).val());
    console.log("taxes_freez, tarifaTotal:",{tarifaTotal});



      if (checkBox.checked == true){
              console.log("en el if checked true:");
              tarifaTotal = Number($('#'+tarifa_total).val());
              console.log("taxes_freez, tarifaTotal:",{tarifaTotal});
              let libre_impuestoz = (tarifaTotal*4)/100;
              console.log("taxes_freez, libre_impuestoz:",{libre_impuestoz});
              //console.log("taxes free en total_price", {total_price});

              //libre_impuestos

              tarifa_total='id__manoobra-'+totalForms+'-tarifa_total';
              console.log("taxes_freez, tarifa_total:",{tarifa_total});
              $('#'+tarifa_total).val(libre_impuestoz);

              console.log("if taxes_freez, tarifa_total:",{tarifa_total});
              console.log("if taxes_freez, libre_impuestoz:",{libre_impuestoz});
              console.log("if taxes_freez, tarifaTotal:",{tarifaTotal});

              return tarifaTotal;

      }
      document.getElementById(libre_impuestoz).disabled = true;
//      else {
//         console.log("en el else");
//         tarifa_total='id__manoobra-'+totalForms+'-tarifa_total';
//         //tarifaTotal=Number(document.getElementById(tarifa_total).value);
//         tarifaTotal = Number($('#'+tarifa_total).val());
//         console.log("taxes_freez, tarifa_total:",{tarifa_total});
//         console.log("taxes_freez, tarifaTotal:",{tarifaTotal});
//         document.getElementById(libre_impuestoz).disabled = true;
//      }
}




function Discountz(tarifaTotal){

    //obteniendo el numero
    var formId="id_manoobra-TOTAL_FORMS"
    let totalForms=Number($('#'+formId).val());
    totalForms=totalForms-1
    console.log("Discountz en totalForms",{totalForms})
    tarifa_total='id__manoobra-'+totalForms+'-tarifa_total';
    console.log("Discountz, tarifa total:",{tarifa_total});
    document.getElementById(tarifa_total);
    //total_price = parseInt($('#'+total_price).val());
    console.log("Discountz en tarifa_total",{tarifa_total})
    let sumaTotales=0;
    let i=0;
    console.log("en el if de Discountz, totalForms:",{totalForms});
          while ( i < totalForms+1){
            tarifa_total='id__manoobra-'+i+'-tarifa_total';
            console.log("en el if de Discountz, totalForms:",{i});
            console.log("en el if de Discountz, tarifa_total:",{tarifa_total});
            tarifa_total=Number(document.getElementById(tarifa_total).value);
            //mal
            console.log("en el if de Discountz, tarifa_total:",{tarifa_total});
            console.log("todo ok");
            sumaTotales=sumaTotales+tarifa_total;
            console.log("en el if de Discountz, sumaTotales:",{sumaTotales});
            i++;
            console.log("en el if de Discountz, i:",{i});
          }


    if (document.getElementById('id_descuento_0').checked){
          console.log("hola if");
          descuentoTotal=Number(document.getElementById('id_numeroDescuento').value);
          console.log("en el if de Discountz en descuentoTotal:",{descuentoTotal});
          let totalOperacion=Number(sumaTotales-descuentoTotal);
          console.log("en el if de Discountz en totalOperacion:",{totalOperacion});
          let total=document.getElementById("totals");
          console.log("en el if de Discountz en total:",{total});
          total=totalOperacion;
          console.log("en el if de Discountz en total:",{total});
          let to=Number(totalOperacion.toFixed(2));
          console.log("en el if de Discountz en to:",{to});
          document.getElementById("totals").value=to;

//        document.getElementById("id_total").value=total;
          console.log("en el if de descuentoTotalFuncion en total:",{to});

          return to;
     }


    else{
            console.log("hola else");
            descuentoTotal=Number(document.getElementById('id_numeroDescuento').value);
            console.log("en el else de descuentoTotalFuncion en descuentoTotal:",{descuentoTotal});
            operacionPorcentaje=Number((descuentoTotal*sumaTotales)/100);
            let op=Number(operacionPorcentaje.toFixed(2));
            //ok
            console.log("en el if de descuentoTotalFuncion en total:",{op});
            document.getElementById("totals").value=Number(op);
    }
 }