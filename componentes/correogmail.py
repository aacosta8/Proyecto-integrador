# Se establece conexion con el servidor pop de gmail
import poplib
from email.parser import Parser
m = poplib.POP3_SSL('pop.gmail.com',995)
m.user('estilistasdecorazon@gmail.com')
m.pass_('anaalexjuan')

numero = len(m.list()[1])
p = Parser()


#------------Leer el correo-----------------
for i in range (numero):
    outfile = open("../archivos/correos.txt", 'a')
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


#------------Contador de mensajes-----------------
men = 0

infilemen = open('../archivos/correos.txt', 'r')

for linem in infilemen:
    if linem.startswith("<b>Nombre") :
        men = men +1

infilemen.close()



#------------Creando archivo json-----------------

infile = open('../archivos/correos.txt', 'r')
outfile =open('../archivos/correos.json', 'w')
# Mostramos por pantalla lo que leemos desde el fichero

controlador = 0

outfile.write('{ \"interesados\":[\n')

for line in infile:


    if controlador == 1  and men != 0:
        controlador = 0
        outfile.write(',\n')
    
    if line.startswith("<b>Nombre") :
        outfile.write('\t{"Nombre": ')
        outfile.write('"')
        outfile.write(line[15:-13])
        outfile.write('", ')
        
    if line.startswith("<b>Email") :
        outfile.write('"correo": ')
        outfile.write('"')
        outfile.write(line[14:-13])
        outfile.write('"}')
        controlador = 1
        men = men - 1
        
    # Cerramos el fichero.

outfile.write('\n]}')

infile.close()
outfile.close()

# {"employees":[
#     {"firstName":"John", "lastName":"Doe"},
#     {"firstName":"Anna", "lastName":"Smith"},
#     {"firstName":"Peter", "lastName":"Jones"}
# ]}