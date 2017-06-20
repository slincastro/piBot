def blink():
        print "Ejecucion iniciada..."
        iteracion = 0
        while iteracion < 30: ## Segundos que durara la funcion
                GPIO.output(4, True) ## Enciendo el 17
                time.sleep(1) ## Esperamos 1 segundo
                GPIO.output(4, false) ## Enciendo el 27
                time.sleep(1) ## Esperamos 1 segundo
                iteracion = iteracion + 2 ## Sumo 2 porque he hecho dos parpadeos
        print "Ejecucion finalizada"
        GPIO.cleanup() ## Hago una limpieza de los GPIO
