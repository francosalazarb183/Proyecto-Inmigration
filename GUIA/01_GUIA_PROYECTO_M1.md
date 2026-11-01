# Proyecto del módulo 1: tu primera app de datos

Este proyecto junta todo lo que hemos hecho hasta ahora: coger unos datos, entenderlos con un EDA y enseñárselos a otra persona en una app de Streamlit. Esta vez los datos los elegís vosotros y todo el trabajo es vuestro.

Lo presentáis el **jueves 5 de noviembre**, como si se lo contarais a un cliente.

## Qué hay que hacer

1. Elegir unos datos y una pregunta.
2. Hacer el EDA en un cuaderno, con las 9 preguntas que ya conocéis, y guardar los datos limpios en un CSV.
3. Hacer una app de Streamlit que lea ese CSV, con la misma estructura que la de los pisos y la del Titanic.
4. Subirlo todo a GitHub, con un README que explique el proyecto.
5. Presentarlo en 8-10 minutos.

No lleva machine learning. Este módulo es de análisis y visualización, y lo que se mira es que entendáis los datos, los limpiéis con sentido y contéis bien lo que habéis encontrado.

## Los datos

Tienen que ser datos nuevos, que no hayamos usado en clase. Hay dos opciones:

- **Uno de los conjuntos de `03_DATOS.md`**, de Kaggle o de Hugging Face. Allí tenéis lo que trae cada uno, una pregunta para empezar y cómo descargarlo.
- **Unos datos vuestros**, de algo que conozcáis bien: hostelería, deporte, vuestra ciudad... Es lo que más luce, pero antes tengo que validarlos yo.

En los dos casos tienen que ser datos tabulares (una tabla, como un Excel) y cumplir los requisitos que están explicados en `03_DATOS.md`: más de 1.000 filas, columnas de números y de texto, algo que limpiar, que entendáis cada columna y que se sepa de dónde salen.

Rellenad `02_PROPUESTA.md` y enseñádmela antes de poneros con el EDA. Buscad también un plan B por si los datos principales no sirven.

## La plantilla

En `PLANTILLA_PROYECTO_M1.zip` tenéis la carpeta del proyecto ya preparada:

```
proyecto-m1/
├── README.md          la portada del proyecto, con los apartados que hay que rellenar
├── requirements.txt   las librerías, para crear el entorno y para publicar la app
├── .gitignore         para que el .venv no se suba a GitHub
├── eda.ipynb          el cuaderno del EDA, con las 9 preguntas
├── app.py             la app, con los 8 pasos en comentarios
├── datos/             aquí van vuestros datos y el CSV limpio
└── capturas/          las capturas de la app para el README
```

Descomprimidla, cambiadle el nombre a la carpeta por el de vuestro proyecto (por ejemplo `vinos-calidad-precio`) y abridla en VS Code. El entorno se crea igual que en clase, con "Python: Create Environment".

## El EDA

El cuaderno `eda.ipynb` tiene las 9 preguntas de siempre, con pasos cortos, igual que el del Titanic:

1. ¿Qué tengo?
2. ¿Qué me falta?
3. ¿Hay filas repetidas?
4. ¿Cómo son los números?
5. ¿Hay algo raro?
6. ¿Qué hay más?
7. ¿Cambia algo de un grupo a otro?
8. ¿Van juntas dos columnas?
9. ¿Qué he aprendido?

Al final se guardan los datos limpios en `datos/datos_limpios.csv`. Así la limpieza se hace una sola vez, en el cuaderno, y la app solo tiene que leer ese CSV.

Cada decisión que toméis con los datos (quitar una columna, rellenar huecos, quitar un valor raro) tiene que llevar debajo, en una frase, por qué. Y cada gráfico, lo que se ve en él.

## La app

`app.py` tiene en comentarios los 8 pasos de una app de datos, los mismos de los pisos y del Titanic:

1. La página y el título.
2. Cargar los datos limpios, con `@st.cache_data`.
3. Los filtros, en la barra de la izquierda.
4. Filtrar la tabla.
5. Si no queda nada, avisar y parar.
6. Las métricas.
7. Las pestañas: la tabla, los gráficos y, si tenéis coordenadas, el mapa.
8. Una pregunta para el usuario, como "¿Cuánto cobrarías por tu piso?".

Si os atascáis, buscad el mismo paso en vuestro `app_pisos.py` o en `teoria_streamlit.ipynb`.

## GitHub

Ya tenéis cuenta de GitHub y GitHub Desktop instalado, así que solo hay que crear el repositorio del proyecto:

1. Abrid GitHub Desktop y comprobad que estáis con vuestra cuenta (en Mac, GitHub Desktop > Settings > Accounts; en Windows, File > Options > Accounts).
2. File > Add Local Repository y elegid la carpeta del proyecto. Os dirá que no es un repositorio: pulsad "create a repository" y después "Create Repository".
3. Arriba, "Publish repository". Quitad la marca de "Keep this code private" para que se pueda ver, y pulsad "Publish Repository".

A partir de ahí, cada vez que terminéis algo: abrís GitHub Desktop, escribís abajo a la izquierda qué habéis hecho, pulsáis "Commit to main" y después "Push origin".

Quiero ver el proyecto avanzar poco a poco, no un único commit el último día. Algo así:

- Plantilla del proyecto y datos originales
- EDA: qué tengo, qué me falta y duplicados
- EDA: números, valores raros y grupos
- EDA terminado y datos limpios
- App: datos, filtros y métricas
- App: pestañas, gráficos y pregunta final
- README con los hallazgos y capturas

## Publicar la app

Si os da tiempo, la app se puede publicar gratis en Streamlit Community Cloud, y así cualquiera la abre con un enlace:

1. Entrad en share.streamlit.io con vuestra cuenta de GitHub.
2. Create app, elegid vuestro repositorio, la rama main y el archivo app.py.
3. Deploy. Tarda un par de minutos la primera vez.

Para que funcione, el CSV limpio tiene que estar subido a GitHub en `datos/` y el `requirements.txt` tiene que estar en la carpeta principal, como en la plantilla.

## El README

Es lo primero que ve quien entra en vuestro repositorio. La plantilla ya tiene los apartados:

- El título y una frase de qué es y para quién.
- La pregunta que responde.
- Los datos: de dónde salen (con el enlace), cuántas filas y columnas tienen y qué es cada fila.
- Qué habéis limpiado y por qué.
- Tres hallazgos, cada uno con un número.
- La app: una captura y cómo se usa. El enlace, si la habéis publicado.
- Cómo se ejecuta en otro ordenador.

## La presentación

Entre 8 y 10 minutos, como si se lo contarais a un cliente que os ha encargado el análisis. Al cliente no le importa el código, le importa qué habéis encontrado y para qué le sirve.

Un orden que funciona, con lo que más o menos le toca a cada parte:

1. El problema: qué pregunta respondéis y a quién le interesa (1 minuto).
2. Los datos: de dónde salen, cuántos son y qué habéis tenido que arreglar, contado sin código (1-2 minutos).
3. Tres hallazgos, con su número y lo que significan (3 minutos).
4. La app funcionando, en directo (2-3 minutos).
5. Para qué sirve y qué haríais después (1 minuto).

No enseñéis el cuaderno ni el código. Si una frase no la entendería alguien que no sabe Python, cambiadla.

## Lo mínimo y lo que lo hace mejor

Para poder presentar hace falta, como mínimo:

- El cuaderno del EDA con las 9 preguntas respondidas.
- Una app que funcione, con la tabla, dos filtros, tres métricas y dos gráficos.
- El repositorio en GitHub con el README.

Y lo que hace que el proyecto sea mejor, si os da tiempo:

- Una pregunta para el usuario en la app, o un mapa.
- La app publicada en Streamlit Community Cloud.
- Datos propios, buscados por vosotros.
- Commits poco a poco durante el proyecto.
- Un hallazgo que no se vea a simple vista, como la trampa de Cherburgo en el Titanic.

## El feedback

Después de la presentación, cada uno recibe feedback de lo que está bien y de lo que puede mejorar, en tres partes:

- **Contenido:** la pregunta, la limpieza con sus porqués, el EDA y los hallazgos.
- **Diseño:** la app (que funcione, que se entienda y que deje explorar los datos) y el repositorio con su README.
- **Exposición:** la presentación, que sea clara, que la demo funcione y que se ajuste a los 8-10 minutos.

## Fechas

| Día | Qué |
|---|---|
| Lunes 26 de octubre | Elegir los datos, rellenar la propuesta y empezar el EDA |
| Miércoles 28 | Terminar el EDA y guardar los datos limpios. Crear el repositorio en GitHub |
| Jueves 29 | La app |
| Miércoles 4 de noviembre | Terminar la app, el README y publicarla. Ensayar la presentación |
| **Jueves 5 de noviembre** | **Presentaciones** |
