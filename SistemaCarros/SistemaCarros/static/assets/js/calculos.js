


function totales(){

    var descuento=document.getElementById('id_descuento').value;
    var total=document.getElementById('id_total').value;
    totales=(descuento * total) / 100;
    document.getElementById("id_total").value = totales;

}


function updateEmptyFormIDs(element,totalForms){
    //get current form input name
    var thisInput=element
    //get current form input name
    var currentName=element.attr('name')
    //replace "prefix" with actual number
    var newName=currentName.replace(/__prefix__/g,totalForms)

    //update input w/new name
    thisInput.attr('name',newName)
    thisInput.attr('id',"id_"+newName)

    var newFormRow=element.closest(".part-form");

    var newRowId="row_id_"+newName
    newFormRow.attr("id",newRowId)

    newFormRow.addClass("new-parent-row")
    var parentDiv=element.parent();
    parentDiv.attr("id","parent_id_"+newName)

    var inputLabel=parentDiv.find("label")
    inputLabel.attr("for","id_"+newName)
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
    e.previousSibling.checked = true;
    e.parentNode.parentNode.style.display='none';
    descuentoTotalParteFuncion();
}


function calculate_total_price(quantity, price, discount, tax_free) {
    let total_price = quantity * price;
    console.log(discount);
    total_price = discount != 0 ? total_price * discount / 100: total_price;
    total_price = tax_free ? total_price*0.025 : total_price;
    return total_price;
}
function multiplicar(event){

    const formId = event.id.split("-")[1];
    let quantity=Number.parseFloat($("#" + 'id_form-'+formId+'-quantity').val());
    let unit_price=Number.parseFloat($("#" + 'id_form-'+formId+'-unit_price').val());
    let total_price="#" + 'id_form-'+formId+'-total_price';
    let descuentoPartes=Number.parseFloat($("#" + 'id_form-'+formId+'-descuento_parte').val());
    let tax_fee = $("#" + 'id_form-'+formId+'-tax_free').prop("checked")?true:false;

    const multiplicar_total_price = calculate_total_price(quantity, unit_price, descuentoPartes, tax_fee);
    $(total_price).val(multiplicar_total_price.toFixed(2));
    descuentoTotalParteFuncion();
}
function descuentoTotalParteFuncion(){

    const total_form_count = Number.parseInt($("#id_form-TOTAL_FORMS").val());

    let total_value = 0;
    for(let i = 0; i < total_form_count; i ++) {
        if($("#id_form-" + i + "-DELETE").prop('checked') == false && $("#id_form-" + i + "-comprado_cliente").prop('checked') == false) {
            total_value += Number.parseFloat($("#id_form-" + i + "-total_price").val());
        }
    }
    let total_discount = Number.parseFloat($("#id_descuentoTotal_parte").val());
    if(isNaN(total_discount)) {
        total_discount = 0;
        $("#id_descuentoTotal_parte").val(0);
    }
    if($("#id_descuento_parte_0").prop("checked"))  total_value -= total_discount;
    else if(total_discount!=0) total_value = total_value * total_discount / 100;


    $("#id_total_parte").val(total_value.toFixed(2));
    //$("#id_total_parte").val(total_value * discount_total / 100);

}
//**********************************************LABORS
function calculate_total_rate(rate, h, m, tax_free) {

    let total_price = rate * h + rate * m/ 60;
    total_price = tax_free ? total_price*0.025 : total_price;
    return total_price;
}
function convTarifa(evt){
    const formId = evt.id.split("-")[1];
    let horas=Number.parseFloat($("#" + 'id_form-'+formId+'-horas').val());
    let minute=Number.parseFloat($("#" + 'id_form-'+formId+'-minutos').val());
    let rate=Number.parseFloat($("#" + 'id_form-'+formId+'-tarifa').val());
    let tarifa_total="#" + 'id_form-'+formId+'-tarifa_total';
    let tax_fee = $("#" + 'id_form-'+formId+'-libre_impuestos').prop("checked")?true:false;
    const total_value =calculate_total_rate(rate, horas, minute, tax_fee);

    $(tarifa_total).val(total_value.toFixed(2));
    descuentoTotalManaobraFuncion()
}

function descuentoTotalManaobraFuncion() {
    const total_form_count = Number.parseInt($("#id_form-TOTAL_FORMS").val());
    let total_value = 0;
    for(let i = 0; i < total_form_count; i ++) {
        if($("#id_form-" + i + "-DELETE").prop('checked') == false) {
            total_value += Number.parseFloat($("#id_form-" + i + "-tarifa_total").val());
        }
    }
    let total_discount = Number.parseFloat($("#id_descuentoTotal_manaobra").val());
    if(isNaN(total_discount)) {
        total_discount = 0;
        $("#id_descuentoTotal_manaobra").val(0);
    }
    if($("#id_descuento_manaobra_0").prop("checked"))  total_value -= total_discount;
    else if(total_discount!=0) total_value = total_value * total_discount / 100;
    $("#id_total_manaobra").val(total_value.toFixed(2));
}
//ESTIMATE MODAL
function showCancelEstimateModal(evt) {
    $("#modal-estimate-id").html("Estimate No. #MN" + $(evt).data("id"));
    $("#modal-estimate-cancel").attr("data-id", $(evt).data("id"));
}

function cancelEstimate(evt) {
    const id = $(evt).data("id");
    window.location.href="/estimates/cancel/" + id;
}

function setTotalReports(id) {

    percentValue = Number.parseFloat($("#tech_percent_" + id).val());
    deductValue = Number.parseFloat($("#tech_deduct_" + id).val());
    adjustValue = Number.parseFloat($("#tech_adjust_" + id).val());
    if(isNaN(percentValue)) percentValue = 100;
    if(isNaN(deductValue)) deductValue = 0;
    if(isNaN(adjustValue)) adjustValue = 0;

    total = percentValue * Number.parseFloat($("#tech_payment_"+id).html()) / 100  - deductValue + adjustValue;
    $("#tech_total_" + id).html(total.toFixed(2));

}

function technicianReportDetail(index, estimate_id, tech_id) {
    console.log(index);
    percent = Number.parseFloat($("#tech_percent_" + index).html());
    total = Number.parseFloat($("#tech_total_" + index).html());
    if(isNaN(percent)) percent = 100;
    window.location.href="/reports/reports-technicians-view-payment/" + estimate_id + "/" + tech_id + "/" + percent + "/" + total;
}

