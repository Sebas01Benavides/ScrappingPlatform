function cargarDatos() {
    fetch("/datos")
        .then(function (response) {
            return response.json();
        })
        .then(function (payload) {
            const tbody = document.getElementById("tabla-body");
            const mensaje = document.getElementById("mensaje");

            tbody.innerHTML = "";
            mensaje.textContent = "";

            if (payload.status === "success" && payload.data.length > 0) {
                for (let i = 0; i < payload.data.length; i++) {
                    const item = payload.data[i];
                    const fila = document.createElement("tr");

                    fila.innerHTML =
                        "<td>" + (item.id ?? "") + "</td>" +
                        "<td>" + (item.nombre ?? "") + "</td>" +
                        "<td>" + (item.precio ?? "") + "</td>" +
                        "<td>" + (item.hash_datos ?? "") + "</td>" +
                        "<td>" + (item.fuente ?? "") + "</td>" +
                        "<td>" + (item.fecha_extraccion ?? "") + "</td>";

                    tbody.appendChild(fila);
                }
            } else {
                mensaje.textContent = "No hay datos para mostrar.";
            }
        })
        .catch(function (error) {
            const mensaje = document.getElementById("mensaje");
            mensaje.textContent = "Error cargando datos.";
            console.error("Error:", error);
        });
}