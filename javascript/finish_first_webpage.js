let images =["https://theartofeducation.edu/wp-content/uploads/2020/07/Pic-1.jpg"
]

count = 0
function change(){
    document.getElementById("img").src = images[count]
    if(count === 2){
        count = 0
    }else{
        count += 1
    }
}
function show(){
    document.getElementById("extra").style.display = "block"
    document.getElementById("paragraph").style.display = "block"
}
function more(){
    if(document.getElementById("extra").style.display !="flex"){
        document.getElementById("paragraph").style.display = "none"
         document.getElementById("extra").style.display = "none"
        document.getElementById("paragraph").innerHTML ="Show Less"
    }else{
        document.getElementById("extra").style.display = "show"
        document.getElementById("paragraph").innerHTML ="Show More"
    }
}