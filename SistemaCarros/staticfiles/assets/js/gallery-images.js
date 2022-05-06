/*fotos carros*/

let fileInput=document.getElementById("file-input");
let imageContainer=document.getElementById("images");
let numOfFiles=document.getElementById("num-of-files");

function preview(){
    imageContainer.innerHTML="";
    console.log({imageContainer});
    numOfFiles.textContent=`${fileInput.files.length}
    Files Selected`;

    for(i of fileInput.files){
        let reader=new FileReader();
        console.log({reader});
        let figure=document.createElement("figure");
        console.log({figure});
        let figCap=document.createElement("figcaption");
        console.log({figCap});
        figCap.innerText=i.name;
        figure.appendChild(figCap);
        reader.onload=()=>{
         let img=document.createElement("img");
         img.setAttribute("src",reader.result);
         figure.insertBefore(img,figCap);
        }
        imageContainer.appendChild(figure);
        reader.readAsDataURL(i);
    }
}




/*warranty*/

let fileInputz=document.getElementById("file-inputz");
let imageContainerz=document.getElementById("imagez");
let numOfFilez=document.getElementById("num-of-filez");

function previewz(){
    console.log("todo ok con previewz");
    imageContainerz.innerHTML="";
    numOfFilez.textContent=`${fileInputz.files.length}
    Files Selected`;

    for(i of fileInputz.files){
        let reader=new FileReader();
        let figure=document.createElement("figure");
        let figCap=document.createElement("figcaption");
        figCap.innerText=i.name;
        figure.appendChild(figCap);
        reader.onload=()=>{
         let img=document.createElement("img");
         img.setAttribute("src",reader.result);
         figure.insertBefore(img,figCap);
        }
        imageContainerz.appendChild(figure);
        reader.readAsDataURL(i);
    }
}