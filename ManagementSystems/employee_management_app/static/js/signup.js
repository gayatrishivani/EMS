
function validation(){
    if(document.getElementById("username").value &&
    document.getElementById("exampleInputPassword1").value && 
    document.getElementById("emailid").value && document.getElementById("exampleInputPassword2").value){
        document.getElementById("button").disabled = false;
    }else{
        document.getElementById("button").disabled = true;
    }
}