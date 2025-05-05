let images =["https://images.squarespace-cdn.com/content/v1/5e7a324590664f18b1bfea0c/257b112e-7cb1-418a-9286-aa04e031dd30/snowbirdclifflodgeview.jpg" , "https://media-cdn.tripadvisor.com/media/photo-s/0b/a6/39/44/the-cliff-lodge-in-summer.jpg"
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
    if(document.getElementById("hidden").style.display === "block"){
        document.getElementById("hidden").style.display = "none"
        document.getElementById("btn").innerHTML ="Show More"
    }else{
        document.getElementById("hidden").style.display = "block"
        document.getElementById("btn").innerHTML ="Show Less"
    }
}