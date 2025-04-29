function show(){
    document.getElementById("extra").style.display = "block"
    document.getElementById("paragraph").style.display = "block"
}
function more(){
    if(document.getElementById("pThree").style.display === "block"){
        document.getElementById("pThree").style.display = "none"
        document.getElementById("btn").innerHTML ="Show More"
    }else{
        document.getElementById("pThree").style.display = "block"
        document.getElementById("btn").innerHTML ="Show Less"
    }
}