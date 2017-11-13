from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
import pymysql

conn = pymysql.connect(host='localhost', user='glasalvia', passwd='dolina1986', db='sitio_fotografia', charset='utf8mb4')
conn.autocommit(True)
cur = conn.cursor(pymysql.cursors.DictCursor)

@csrf_exempt
def api_leo(request):

	if request.method == 'GET':

		categoria = request.GET.get('categoria', False)
		categoria = str(categoria)

		cur.execute("SELECT src, srct,title, description from leo_api where Album = '"+categoria+"'")
		query = cur.fetchall()
		query = json.dumps(query)

		resultado = '{'+'"items":'+query+'}'
		resultado = json.loads(resultado)

		return JsonResponse(resultado, safe=False)

	if request.method == 'POST':

		categoria = request.POST.get("categoria", False)
		categoria = str(categoria)

		cur.execute("SELECT src, srct,title, description from leo_api where Album = '"+categoria+"'")
		query = cur.fetchall()
		query = json.dumps(query)
		
		resultado = '{'+'"items":'+query+'}'
		resultado = json.loads(resultado)

		return JsonResponse(resultado, safe=False)