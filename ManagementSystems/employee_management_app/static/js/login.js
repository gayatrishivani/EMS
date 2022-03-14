
function validation(){
    if(document.getElementById("exampleInputEmail1").value && document.getElementById("exampleInputPassword1").value){
        document.getElementById("button").disabled = false;
    }else{
        document.getElementById("button").disabled = true;
    }
}
