function show(){
    document.getElementById("extra").style.display = "block"
    document.getElementById("paragraph").style.display = "block"
}
function more(){
    if(document.getElementById("hidden").style.display === "block"){
        document.getElementById("hidden").style.display = "none"
        document.getElementById("btn").innerHTML ="Show More"
    }else{
        document.getElementById("hidden").style.display = "block"
        document.getElementById("btn").innerHTML ="Show Less"
    }
}