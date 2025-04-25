let images =["https://smashingpencilsart.com/wp-content/uploads/2021/06/art-supplies-photo-min-2048x1314-1.jpg","https://theartofeducation.edu/wp-content/uploads/2020/07/Pic-1.jpg"
]

let count = 0
function change(){
    if(count < images.length){
        document.getElementById("img").src = images[count]
        count += 1
    }else{
        count = 0
        document.getElementById("img").src = images[count]
    }
}
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