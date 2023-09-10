// Script for navigation bar
const  bar = document.getElementById('bar')
const nav = document.getElementById('navbar')
const close= document.getElementById('close')
if (bar){
    bar.addEventListener('click',() =>{
        nav.classList.add('active');    
    })}
if (close){
    close.addEventListener('click',() =>{
        nav.classList.remove('active');    
    })
}

// $('.plus-cart').click(function(){
//     var id = $(this).attr("pid").toString();
//     var eml = this.parentNode.children[1];
//     console.log(eml)
//     $.ajax({
//         type:"GET",
//         url:"/pluscart",
//         data:{
//             prod_id :id
//         },
//         success:function(data){
//             console.log("data= ",data);
//             eml.innerText  = data.quantity
//             document.getElementById("amount").innerText =data.amount
//             document.getElementById("totalamount").innerText =data.totalamount
//         }
//     })
// })  

window.addEventListener("scroll",function(){
    var header= document.querySelector("body");
    header.classList.toggle("sticky",window.scrollY > 0);
})
//
