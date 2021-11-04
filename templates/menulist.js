import {menu} from "./menu.js"
const productsList = document.querySelector('#menulist');

listProduct()
function listProduct() {
    for (let i = 0; i < menu.length; i++) {

        let divProducts = document.createElement("div");
        divProducts.setAttribute('id', menu[i].menuId);
        divProducts.setAttribute('class', 'col-3')

        let imgfood = document.createElement('div');
        imgfood.setAttribute('class', 'gradien');
        imgfood.innerHTML += `<img src='${menu[i].productImg}' width="250px" style="marginBottom:20px;"><div class="overlayText"><p class="textImage">Add</p></div>`;


        let pProductName = document.createElement('h3');
        pProductName.innerHTML = `<h3 style="color:#8d4f48;">${menu[i].productName}</h3>`;

        let list = document.createElement('ul');
        list.setAttribute("class", "list-unstyled");
        list.innerHTML += `<li style="color:#b47775;">Price ${product[i].productPrice}</li>`

        // let addCart = document.querySelector('#Add');
        // addCart.addEventListener("click", () => {
        //     alert("Helloworld")
        // });


        divProducts.appendChild(imgfood);
        divProducts.appendChild(pProductName);
        divProducts.appendChild(list);
        productsList.appendChild(divProducts);

    }
}