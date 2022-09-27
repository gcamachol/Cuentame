--Comandos usados para extraer la información con Scrapy:
Archivo principal: extractdata\extractdata\spiders\economic_indicators.py

py -m pip install virtualenv
py -m virtualenv venv
venv\Scripts\activate
py -m pip install -r requeriments.txt
scrapy version
scrapy startproject extractdata
cd extractdata
pip install pyopenssl==22.0.0

--Revisar correcta conexión a datos
scrapy shell "https://www.dane.gov.co/index.php/indicadores-economicos"
response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h2/strong/text()').getall()
response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h1/text()').getall()

-Ejecutar spider
scrapy crawl e_indicators



--Script almacenar datos base de datos
Archivo principal: extractdata\savedata.py

--DDL Tabla
CREATE TABLE "Cuentame".indicadores_economicos (
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    indicador varchar(16) NULL,
    valor varchar(16) NULL,
    fecha date NULL
);


--Creación API acceso al contenido de base de datos 
Se crea funcion dentro del motor de DB para poder consultar el contenido

CREATE OR REPLACE FUNCTION Cuentame.get_indicators(p_busqueda)
 RETURNS TABLE(indicador character varying, valor character varying, fecha date)
 LANGUAGE plpgsql
AS $function$
declare
p_busqueda varchar;

begin
	
 return query
		select * 
		  from "Cuentame".indicadores_economicos
         where indicador like '%p_busqueda%';
	
	   
end; 
$function$
;

