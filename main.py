
main.py
    # El formulario
    @app.route('/form')
    def form():
        return render_template('form.html')
    
    #Resultados del formulario
    @app.route('/submit', methods=['POST'])
    def submit_form():
        # Declarar variables para la recogida de datos
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        date = request.form['date']
    
    
    
        # Puedes guardar tus datos o enviarlos por correo electrónico
        return render_template('form_result.html', 
                               # Coloque aquí las variables
                               name=name,
                               email=email,
                               address=address,
                               date=date,
                               )
