let images =["https://smashingpencilsart.com/wp-content/uploads/2021/06/art-supplies-photo-min-2048x1314-1.jpg","https://www.auarts.ca/sites/default/files/styles/responsive_1280/public/2025-01/jan-30-homepage-banner-hero-size.jpg?itok=4CWhbZrM","https://newgenbaker.com/wp-content/uploads/2019/03/food-3048440_960_720.jpg"
]
function hello(){
    document.getElementById("title").innerHTML = "Hello World!"
}
count = 0
function change(){
    document.getElementById("img").src = images[count]
    if(count === 2){
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
    if(document.getElementById("extra").style.diaply !="flex"){
          document.getElementById("extra").style.display = "none"
    document.getElementById("shw").innerHTML ="Show Less"
    }else{
    document.getElementById("extra").style.display = "none"
    document.getElementById("shw").innerHTML ="Show More"
    }
}