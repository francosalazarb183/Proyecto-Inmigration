# Los datos del proyecto

Los datos tienen que ser nuevos: nada de lo que hemos usado en clase. Podéis coger uno de los conjuntos de abajo, de Kaggle o de Hugging Face, o traer los vuestros.

## Qué son datos tabulares

Para este proyecto los datos tienen que ser tabulares, es decir, una tabla, como un Excel o como los pisos y el Titanic:

- Cada fila es un caso: una venta, un partido, un vino, un coche.
- Cada columna es algo que sabemos de ese caso: el precio, la fecha, el país.
- Todas las filas tienen las mismas columnas.

Suelen venir en CSV, en Excel o en parquet, y se leen con pandas en una línea.

No son tabulares, y no sirven para este proyecto: textos sueltos (reseñas, artículos, conversaciones), imágenes, audios, vídeos, PDFs o un JSON con listas dentro de listas.

## Qué tienen que cumplir

Elijáis lo que elijáis, los datos tienen que cumplir esto:

1. Que sean tabulares y estén en una sola tabla.
2. Que sean nuevos. No valen los de clase: pisos, hoteles, Titanic, taxis, la carta del bar, Star Wars, el tiempo de Open-Meteo, ni los de las APIs del 14 de octubre (exoplanetas, libros, series y terremotos).
3. Que tengan más de 1.000 filas.
4. Que tengan al menos 6 columnas, con números y con texto, para poder comparar grupos.
5. Que entendáis qué es cada columna. Si no viene explicado, no los cojáis.
6. Que haya algo que limpiar: huecos, filas repetidas o valores raros. Si están perfectos, el EDA se queda corto.
7. Que se sepa de dónde salen y que se puedan usar: el enlace a la fuente y la licencia.
8. Que el CSV limpio que subáis a GitHub pese menos de 100 MB. Si los datos son más grandes, os quedáis con una parte (un país, unos años) en el cuaderno.
9. Que haya una pregunta detrás que os interese responder.

## Cómo se consiguen

**Kaggle.** Hace falta una cuenta, que es gratis. En la página del conjunto se pulsa Download, se descarga un zip, y el CSV de dentro va a la carpeta `datos/` del proyecto.

**Hugging Face.** No hace falta cuenta. Hay dos formas:

- Leerlos directamente desde el cuaderno, con su dirección, igual que hicimos con Open-Meteo. Es lo más cómodo, porque no hay que descargar nada:

```python
vinos = pd.read_parquet("https://huggingface.co/datasets/spawn99/wine-reviews/resolve/main/data/train-00000-of-00001.parquet")
```

- O descargarlos: en la página del conjunto, la pestaña "Files and versions", el archivo y el botón de descarga.

Los que acaban en `.csv` se leen con `pd.read_csv` y los que acaban en `.parquet`, con `pd.read_parquet`. Si `read_parquet` da error, hay que hacer `pip install pyarrow`.

## En Hugging Face (sin cuenta)

Todos están comprobados: se leen con la dirección que hay debajo.

**Reseñas de vinos.** 196.630 reseñas de una revista de vinos, con país, región, variedad, bodega, precio y puntos (de 80 a 100). Hay 32.877 filas repetidas, 15.808 vinos sin precio y muchas regiones vacías. 10.393 son de España. Pregunta: ¿los vinos caros tienen mejor nota? ¿Qué países y variedades tienen la mejor relación calidad-precio?
`https://huggingface.co/datasets/spawn99/wine-reviews/resolve/main/data/train-00000-of-00001.parquet`

**Coches de segunda mano en Europa.** 100.000 anuncios con marca, modelo, precio, kilómetros, año, potencia, combustible, cambio y país del vendedor. Al color le falta más de la mitad, y hay un precio de 10 millones de euros que habrá que mirar. La mayoría son de Alemania y unos 6.000 de España. Pregunta: ¿cuánto pierde un coche por cada año y cada kilómetro? ¿Qué marcas aguantan mejor el precio?
`https://huggingface.co/datasets/KTHESAT/european-used-cars-100k-sample/resolve/main/european_used_cars_100k.parquet`

**Canciones de Spotify.** 114.000 canciones de 114 géneros, con popularidad, duración, y medidas como lo bailable, la energía o el tempo. Viene casi limpio, así que lo interesante está en comparar géneros. Pregunta: ¿qué tienen en común las canciones más populares? ¿Qué géneros son más bailables?
`https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/resolve/main/dataset.csv`

**Clientes de una telefónica.** 7.043 clientes con su contrato, lo que pagan al mes, los servicios que tienen y si se dieron de baja (el 26,5 %). Parece que no le falta nada, pero el total facturado viene como texto y tiene 11 huecos disfrazados. Pregunta: ¿qué clientes se van? ¿Influye el tipo de contrato?
`https://huggingface.co/datasets/scikit-learn/churn-prediction/resolve/main/dataset.csv`

**Juegos Olímpicos.** 271.116 participaciones de deportistas desde 1896, con edad, altura, peso, país, deporte y medalla. Faltan unas 60.000 alturas y pesos, hay 1.385 filas repetidas, y la medalla vacía significa que no ganó ninguna, igual que la licencia de los pisos. Pregunta: ¿cómo han cambiado los deportistas con los años? ¿Qué países ganan más en cada deporte?
`https://huggingface.co/datasets/jason1966/abdullahmeo_120-years-of-olympic-athletes-dataset/resolve/main/athlete_events.csv`

**Netflix.** 8.807 títulos con tipo (película o serie), país, año, clasificación, duración y género. Faltan 2.634 directores y 831 países. Es algo más difícil, porque la duración viene como texto ("90 min" o "2 Seasons") y hay que separarla. Pregunta: ¿qué países y géneros hay más en el catálogo? ¿Cómo ha cambiado con los años?
`https://huggingface.co/datasets/hugginglearners/netflix-shows/resolve/main/netflix_titles.csv`

**Felicidad en el mundo.** 1.367 filas, una por país y año de 2015 a 2023, con la nota de felicidad, el PIB por persona, la esperanza de vida, la libertad y la corrupción. Casi todo son números, así que va bien para relaciones entre columnas. Pregunta: ¿qué tienen los países más felices? ¿Cómo ha cambiado España?
`https://huggingface.co/datasets/AhanaBiswas/WorldHappinessDataset2015-2023/resolve/main/World%20Happiness%20Dataset%202015-2023.csv`

**Ofertas de trabajo de datos.** Cientos de miles de ofertas de trabajo de analista, científico e ingeniero de datos, con país, salario, si es en remoto y las herramientas que piden. Pesa 231 MB, así que leedlo con su dirección y quedaos con un país o unos meses. Pregunta: ¿qué herramientas piden más? ¿Cuánto se cobra según el puesto y el país?
`https://huggingface.co/datasets/lukebarousse/data_jobs/resolve/main/data_jobs.csv`

## En Kaggle (con cuenta)

**Ventas de videojuegos.** Unos 16.600 juegos con su plataforma, año, género, editora y ventas en millones por región. Hay años y editoras vacíos, y un juego que vendió muchísimo más que el resto. Pregunta: ¿qué géneros y plataformas venden más? ¿Se juega a lo mismo en Japón que en Europa?
https://www.kaggle.com/datasets/gregorut/videogamesales

**Ventas de una cadena de cafeterías.** Unas 149.000 ventas de tres cafeterías de Nueva York, con fecha, hora, local, producto, cantidad y precio. Pregunta: ¿cuáles son las horas punta? ¿Qué se vende más en cada local? Viene en Excel: se lee con `pd.read_excel`, y antes hay que hacer `pip install openpyxl` y añadir openpyxl al `requirements.txt`.
https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales

**Restaurantes de Zomato.** Unos 9.500 restaurantes con su tipo de cocina, lo que cuesta comer dos personas, la nota, los votos y las coordenadas, así que da para un mapa. Pregunta: ¿qué tipo de cocina tiene mejor nota? ¿Los más caros son los mejores? Ojo: el precio va en la moneda de cada país, así que solo se puede comparar dentro de un mismo país.
https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data

**Superstore.** Unas 10.000 ventas de una tienda de Estados Unidos, con fecha, región, categoría, ventas, descuento y beneficio. Pregunta: ¿dónde se gana y dónde se pierde dinero? ¿Tienen la culpa los descuentos? Si al leerlo sale un error de encoding, hay que añadir `encoding="latin-1"` al `read_csv`.
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

**Partidos de fútbol entre selecciones.** Más de 45.000 partidos desde 1872, con los equipos, los goles, el torneo y dónde se jugó. Pregunta: ¿cuánto ayuda jugar en casa? ¿Qué selecciones ganan más?
https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

## Vuestros propios datos

Lo que más luce es un proyecto de algo que conocéis bien. Si venís de la hostelería, por ejemplo, datos de turismo, de restaurantes o de vuestra ciudad. Sitios donde buscar:

- datos.gob.es, los datos abiertos de toda España.
- Los portales de datos abiertos de cada ayuntamiento, como datos.madrid.es.
- El INE (ine.es), con turismo, empleo, precios...
- Google Dataset Search (datasetsearch.research.google.com).
- Los propios buscadores de Kaggle y de Hugging Face.

Tienen que cumplir los mismos requisitos de arriba, y antes de lanzaros me los tenéis que enseñar para validarlos.
