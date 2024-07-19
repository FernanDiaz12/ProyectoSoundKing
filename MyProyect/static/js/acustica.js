window.onload = (event) => {
    getAcustica();
    $("#myrow").html(`<div class="col-lg-6 mb-2">
          <div class="card text-center h-100">
            <img src="{% static 'Img/GuitarraTakamine.jpeg' %}" class="card-img-top CARTAS h-100" alt="...">
            <div class="card-body">
              <h5 class="card-title">Guitarra Takamine GJ72CE</h5>
              <p class="card-text">$500.000 CLP</p>
              <a href="#" class="btn btn-primary">Agregar al carrito</a>
              <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#takamine">Ficha Tecnica</a>
            </div>
          </div>
        </div>`);
  };

  function getAcustica(){
    fetch('http://localhost:8000/api/instrumentos/?format=json')
        .then(response => response.json())
            .then(data => {
                console.log(data)
                data.forEach(instrumento => {
                    console.log(instrumento);
                    if (instrumento.tipo_instrumento==3){
                    $("#myrow").html(`<div class="col-lg-6 mb-2">
                        <div class="card text-center h-100">
                          <img src="${instrumento.imagen}" class="card-img-top CARTAS h-100" alt="...">
                          <div class="card-body"> 
                            <h5 class="card-title">${instrumento.nombre}</h5>
                            <p class="card-text">$1.500.000 CLP</p>
                            <a href="#" class="btn btn-primary">Agregar al carrito</a>
                            <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#pearl">Ficha Tecnica</a>
                          </div>
                        </div>
                      </div>`);
                    }
                
            });
  });
}