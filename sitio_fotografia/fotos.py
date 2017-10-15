import pymysql

conn = pymysql.connect(host='localhost', user='glasalvia', passwd='dolina1986', db='sitio_fotografia', charset='utf8mb4')
conn.autocommit(True)
cur = conn.cursor()

cur.execute("SELECT * from Catalogo where Album = 'Books'")
catalogo = cur.fetchall()

for foto in catalogo:
	titulo = str(foto[0])
	descripcion = str(foto[1])
	album = str(foto[2])
	fecha = str(foto[3])
	archivo = str(foto[4])
	modelo = str(foto[5])
	lente = str(foto[6])
	apertura = str(foto[7])
	velocidad = str(foto[8])
	iso = str(foto[9])

	bloque = """
			<div class="item">
				<div class="item__content">
					<img src="""+archivo+""" alt="img01" />
					<h3 class="item__title">"""+titulo+"""<span class="item__date">"""+fecha+"""</span></h3>
					<div class="item__details">
						<ul>
							<li><i class="icon icon-camera"></i><span>"""+modelo+"""</span></li>
							<li><i class="icon icon-focal_length"></i><span>"""+lente+"""</span></li>
							<li><i class="icon icon-aperture"></i><span>"""+apertura+"""</span></li>
							<li><i class="icon icon-exposure_time"></i><span>"""+velocidad+"""</span></li>
							<li><i class="icon icon-iso"></i><span>"""+iso+"""</span></li>
						</ul>
					</div>
				</div>
			</div>
			"""
	print(bloque)