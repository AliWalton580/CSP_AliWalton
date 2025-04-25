let images =["https://theartofeducation.edu/wp-content/uploads/2020/07/Pic-1.jpg"
]

count = 0
function change(){
    document.getElementById("img").src = images[count]
    if(count === 1){
        count = 0
    }else{
        count += 1
    }
}

function highlight(){
    document.getElementById("btn").style.backgroundColor = "orange"
    document.getElementById("btn").style.color = "white"
}

function normal(){
    document.getElementById("btn").style.backgroundColor = "gray"
    document.getElementById("btn").style.color = "black"
}

function show(){
    document.getElementById("hidden").style.display = "block"
}
function more(){
    if(document.getElementById("extra").style.display !="flex"){
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML ="Show Less"
    }else{
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML ="Show More"
    }
}