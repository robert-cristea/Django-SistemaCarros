
//        <!-- Adding parts & rows -->

            function deleteRow(id)
            {
            document.getElementById(id).remove()
            }

            function childrenRow() {

            var table = document.getElementById("childTable1");
            // GET TOTAL NUMBER OF ROWS
            var x =table.rows.length;
            var id = "tbl"+x;
            var row = table.insertRow(x);
            row.id=id;
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            var cell4 = row.insertCell(3);
            var cell5 = row.insertCell(4);
            var cell6 = row.insertCell(5);
            cell1.outerHTML = ' <td><input type="text" name="parts_code" class="form-control input-new-customer-code newcode" autofocus/></td>';
            cell2.innerHTML = ' <input type="text" name="parts_description" class="form-control input-new-customer-description" />';
            cell3.innerHTML = ' <input type="text" name="parts_quantity" class="form-control input-new-customer-quantity" />';
            cell4.innerHTML = ' <input type="text" name="parts_unit_price" class="form-control input-new-customer-unit-price" />';
            cell5.innerHTML = ' <input type="text" name="parts_total_price" class="form-control input-new-customer-total" />';
            cell6.innerHTML = '  <input type="button" class="btn btn-block btn-default" id="addrow" onclick="deleteRow(\''+id+'\')" value="Delete" /> ';
            }
            document.getElementsByClassName("newcode").onfocus = function() {setFocusInput()};
            function setFocusInput(){
                document.getElementsByClassName("newcode").focus();
            }



//        <!-- Adding labors & rows -->

            function deleteRow2(id)
            {
            document.getElementById(id).remove()
            }

            function childrenRow2() {

            var table2 = document.getElementById("childTable2");
            // GET TOTAL NUMBER OF ROWS
            var x2 =table2.rows.length;
            var id2 = "tbl2"+x2;
            var row2 = table2.insertRow(x2);
            row2.id=id2;
            var cell12 = row2.insertCell(0);
            var cell22 = row2.insertCell(1);
            var cell32 = row2.insertCell(2);
            var cell42 = row2.insertCell(3);
            var cell52 = row2.insertCell(4);
            var cell62 = row2.insertCell(5);
            var cell72 = row2.insertCell(6);
            var cell82 = row2.insertCell(7);
            var cell92 = row2.insertCell(8);
            cell12.outerHTML = ' <td><input type="text" name="parts_code" class="form-control input-new-customer-sm newcode2" autofocus /></td>';
            cell22.innerHTML = ' <input type="text" name="parts_description" class="form-control input-labor-description" />';
            cell32.innerHTML = ' <select class="form-select"><option>Select</option><option>Operator 1</option><option>Operator 2</option><option>Operator 3</option><option>Operator 4</option><option>Operator 5</option></select>';
            cell42.innerHTML = ' <input type="text" name="parts_unit_price" class="form-control input-labor-hourly-rate" />';
            cell52.innerHTML = ' <input type="text" name="parts_unit_price" class="form-control input-labor-hours" />';
            cell62.innerHTML = ' <input type="text" name="parts_unit_price" class="form-control input-labor-minutes" />';
            cell72.innerHTML = ' <input type="text" name="parts_unit_price" class="form-control input-labor-rate" />';
            cell82.innerHTML = ' <div class="form-check"><input type="checkbox" class="form-check-input" id="formrow-customCheck"><label class="form-check-label" for="formrow-customCheck"></label></div>';
            cell92.innerHTML = '  <input type="button" class="btn btn-block btn-default" id="addrow2" onclick="deleteRow2(\''+id2+'\')" value="Delete" /> ';
            }
            document.getElementsByClassName("newcode2").onfocus = function() {setFocusInput()};
            function setFocusInput(){
                document.getElementsByClassName("newcode2").focus();
            }



//         <!-- Adding payments rows -->

            function deleteRow3(id)
            {
            document.getElementById(id).remove()
            }

            function childrenRow3() {

            var table3 = document.getElementById("childTable3");
            // GET TOTAL NUMBER OF ROWS
            var x3 =table3.rows.length;
            var id3 = "tbl3"+x3;
            var row3 = table3.insertRow(x3);
            row3.id=id3;
            var cell31 = row3.insertCell(0);
            var cell32 = row3.insertCell(1);
            var cell33 = row3.insertCell(2);
            cell31.outerHTML = ' <td><select class="form-select" autofocus><option>Select</option><option>Cash</option><option>Credit card</option><option>Debit card</option></select></td>';
            cell32.innerHTML = ' <input type="text" name="payments_amount" class="form-control" />';
            cell33.innerHTML = ' <input type="button" class="btn btn-block btn-default" id="addrow3" onclick="deleteRow3(\''+id3+'\')" value="Delete" /> ';
            }



