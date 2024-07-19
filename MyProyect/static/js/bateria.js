window.onload = (event) => {
    getBaterias();
    $("#myrow").html(`<div class="col-lg-6 mb-2">
          <div class="card text-center h-100">
            <img src="{% static 'Img/BateriaPearl.jpg' %}" class="card-img-top CARTAS h-100" alt="...">
            <div class="card-body"> 
              <h5 class="card-title">Bateria Pearl Vision</h5>
              <p class="card-text">$1.500.000 CLP</p>
              <a href="carrito" class="btn btn-primary">Agregar al carrito</a>
              <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#pearl">Ficha Tecnica</a>
            </div>
          </div>
        </div>`);
  };

  function getBaterias(){
    fetch('http://localhost:8000/api/instrumentos/?format=json')
        .then(response => response.json())
            .then(data => {
                console.log(data)
                data.forEach(instrumento => {
                    console.log(instrumento);
                    if (instrumento.tipo_instrumento==2){
                    $("#myrow").html(`<div class="col-lg-6 mb-2">
                        <div class="card text-center h-100">
                          <img src="${instrumento.imagen}" class="card-img-top CARTAS h-100" alt="...">
                          <div class="card-body"> 
                            <h5 class="card-title">${instrumento.nombre}</h5>
                            <p class="card-text">${instrumento.precio}</p>
                            <a href="carrito" class="btn btn-primary">Agregar al carrito</a>
                            <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#pearl">Ficha Tecnica</a>
                          </div>
                        </div>
                      </div>`);
                    }
                
            });
  });
}