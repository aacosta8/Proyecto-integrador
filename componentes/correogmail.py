# Se establece conexion con el servidor pop de gmail
import poplib
from email.parser import Parser
m = poplib.POP3_SSL('pop.gmail.com',995)
m.user('estilistasdecorazon@gmail.com')
m.pass_('anaalexjuan')

numero = len(m.list()[1])
p = Parser()

for i in range (numero):
    outfile = open("correos.txt", 'a')
    #print "Mensaje numero"+str(i+1)
    outfile.write("Mensaje")
    outfile.write("\n")
    outfile.write("\n")
    # Se lee el mensaje
    response, headerLines, bytes = m.retr(i+1)
    mensaje='\n'.join(headerLines)
    email = p.parsestr(mensaje)
    tipo = email.get_content_type()
    if ("text/html" == tipo):
        # Si es texto plano, se escribe en pantalla
        outfile.write( email.get_payload(decode=True) )
        outfile.write("\n")
        outfile.write("\n")
        outfile.close()
                
m.quit()


infile = open('correos.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero

controlador = 1

for line in infile:

    if controlador == 1:
        controlador = 0
        print "------------"
    
    if line.startswith("<b>Nombre") :
        print line[15:-13]
        
    if line.startswith("<b>Email") :
        print line[14:-13]
        controlador = 1

    # Cerramos el fichero.
infile.close()
