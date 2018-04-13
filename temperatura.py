
import httplib, urllib
import time
import subprocess

def upload(value):
	#ATENCAO! Sua"Chave de Escrita" vai aqui!
	params = urllib.urlencode({'field1': value,'key':'HO7KPN3GW8Q4PPHE'})
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	# Conecta no servidor HTTP do thingspeak.com
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
	    conn.request("POST", "/update", params, headers) # Tenta fazer uma requisicao
	    response = conn.getresponse() # Recebe e imprimi na tela a resposta
	    print response.status, response.reason
	    conn.close() # Fecha a conexao
	except (httplib.HTTPException) as error:
	    print "Error at httplib module: %s" % error
	except (IOError) as error:
	    print "Error at urllib module: %s" % error # Escreve no terminal caso ocorra falha
	except:
	    print "connection failed"
	print ""

if __name__ == "__main__":
	i = 0
	while True:
		temp = 20.2+i
		i+=0.01
		#temp = get_temp() # Faz a leitura da temperatura
		# Faz upload da leitura
		upload(temp)
		time.sleep(1) # Espera 16s
		# OBS: Para o thingspeak.com o tempo minimo entre
	    # uma amostra e a seguinte deve ser de 15 segundos
