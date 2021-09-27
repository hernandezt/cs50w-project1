/* Consulta */
document.addEventListener('DOMContentLoaded', rellenarcarrusel());
function rellenarcarrusel()
{
    let carrusel = new XMLHttpRequest();
    carrusel.open("GET", "/carruselconbestrating");
    carrusel.send();
    carrusel.onreadystatechange = function()
    {
        if (this.readyState == 4) 
        {
            let respuesta = this.response;
            respuesta = JSON.parse(respuesta);
            console.log(respuesta);
            let contenedor = document.getElementById("contenedor");
            for(var i = 0; i < respuesta.length; i++)
            {
                let carrusel_item = document.createElement("div");
                if (i == 0)
                {
                    carrusel_item.setAttribute("class", "carousel-item active");
                }
                else
                {
                    carrusel_item.setAttribute("class", "carousel-item");
                }
                
                let image = document.createElement("img");
                image.setAttribute("class", "d-block w-20");
                image.setAttribute("src", respuesta[i]["image"]);
                
                carrusel_item.appendChild(image);
                contenedor.appendChild(carrusel_item);                
            }
            
            return false;
        }
    }
}