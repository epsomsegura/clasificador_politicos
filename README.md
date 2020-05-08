# Clasificador de polaridad para políticos en Twitter
## Problema
Durante las campañas de elección de candidatos a puestos políticos se encuentran grandes volúmenes de información relacionados con estas personas y los partidos a los que pertenecen dentro de las publicaciones en redes sociales. Al ser personas u organizaciones públicas que buscan ejercer un cargo en la administración de una entidad federativa, surgen opiniones positivas o negativas generadas por los ciudadanos de estas zonas.

Twitter es una de las redes sociales que presentan contenido relacionado con este tema, sin embargo, resulta complejo hacer un análisis manual de la polaridad de opiniones públicas de los ciudadanos con respecto a candidatos postulados a ejerer un puesto en la administración pública.

Durante las campañas políticas, resulta importante conocer el impacto que tiene un candidato con respecto a la aceptación o rechazo de los posibles votantes, sin embargo, la cantidad de información que se genera en Twitter complica la factibilidad de realizar un análisis manual de cada una de las opiniones de las personas que hacen comentarios relacionados con una persona pública.

Mediante el análisis de textos es posible generar resultados de la polaridad de los comentarios haciendo uso de herramientas de procesamiento de lenguaje natural, ya que la naturaleza de la información obtenida desde esta red social, principalmente de los tweets y respuestas a estos, usan un lenguaje natural, lo que complica usar métodos de detección de palabras ya que el contexto puede cambiar el sentido del mensaje.

## Descripción del Dataset
Haciendo uso de la API de desarrollo de Twitter es posible obtener información relacionada con un tema en específico, ya que solo es necesario incluir un conjunto de palabras clave para que la herramienta ofrecida por la red social retorne un archivo en formato .JSON de los tweets y respuestas a estos relacionados con las palabras a consultar.

La estructura de este archivo la genera la misma plataforma. A continuación, se presenta un ejemplo de dicha estructura retornada por la API:

    {
    "created_at": "Wed Nov 27 16:08:58 +0000 2019",
    "id": 1199721788164300800,
    "id_str": "1199721788164300801",
    "full_text": "López Obrador reculando. \nQue haría sin la mafia del poder? \n😁 https://t.co/ofBBW4ik84",
    "truncated": false,
    "display_text_range": [
        0,
        62
    ],
    "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
        {
            "url": "https://t.co/ofBBW4ik84",
            "expanded_url": "https://twitter.com/brozoxmiswebs/status/1199500607746433024",
            "display_url": "twitter.com/brozoxmiswebs/…",
            "indices": [
            63,
            86
            ]
        }
        ]
    },
    "metadata": {
        "iso_language_code": "es",
        "result_type": "recent"
    },
    "source": "<a href='http://twitter.com/download/android' rel='nofollow'>Twitter for Android</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
        "id": 1199690180585615400,
        "id_str": "1199690180585615360",
        "name": "Lucyadams",
        "screen_name": "Lucyada51246888",
        "location": "",
        "description": "Lú Za \nNo soy lo que escribo, soy lo que tú sientes al leerme. Cada imagen cada palabra cuenta una historia.",
        "url": null,
        "entities": {
        "description": {
            "urls": []
        }
        },
        "protected": false,
        "followers_count": 1,
        "friends_count": 6,
        "listed_count": 0,
        "created_at": "Wed Nov 27 14:03:58 +0000 2019",
        "favourites_count": 9,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": false,
        "verified": false,
        "statuses_count": 11,
        "lang": null,
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "F5F8FA",
        "profile_background_image_url": null,
        "profile_background_image_url_https": null,
        "profile_background_tile": false,
        "profile_image_url": "http://pbs.twimg.com/profile_images/1199712288485195780/TBI2Zixl_normal.jpg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1199712288485195780/TBI2Zixl_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1199690180585615360/1574866196",
        "profile_link_color": "1DA1F2",
        "profile_sidebar_border_color": "C0DEED",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "has_extended_profile": false,
        "default_profile": true,
        "default_profile_image": false,
        "following": false,
        "follow_request_sent": false,
        "notifications": false,
        "translator_type": "null"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": true,
    "quoted_status_id": 1199500607746433000,
    "quoted_status_id_str": "1199500607746433024",
    "quoted_status": {
        "created_at": "Wed Nov 27 01:30:05 +0000 2019",
        "id": 1199500607746433000,
        "id_str": "1199500607746433024",
        "full_text": "QUIENES FUERON SEÑALADOS POR AMLO  COMO INTEGRANTES DE LA MAFIA DEL PODER, HOY COMIENZAN A SER EMPRESARIOS MEXICANOS CON UNA VISIÓN SOCIAL (Hablando se entiende la gente).\nhttps://t.co/i191OIfQ3V",
        "truncated": false,
        "display_text_range": [
        0,
        195
        ],
        "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
            {
            "url": "https://t.co/i191OIfQ3V",
            "expanded_url": "http://ow.ly/1r1a50xlzeY",
            "display_url": "ow.ly/1r1a50xlzeY",
            "indices": [
                172,
                195
            ]
            }
        ]
        },
        "metadata": {
        "iso_language_code": "es",
        "result_type": "recent"
        },
        "source": "<a href='https://www.hootsuite.com' rel='nofollow'>Hootsuite Inc.</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "user": {
        "id": 107120856,
        "id_str": "107120856",
        "name": "brozo xmiswebs",
        "screen_name": "brozoxmiswebs",
        "location": "",
        "description": "El Mañanero Diario: un informativo recio, crudo, neto, arrimador y chacotero. Aquí se van a enterar de  lo q nos parezca digno de compartir; lo q no, no. Órale!",
        "url": "https://t.co/HKvKYr4Dex",
        "entities": {
            "url": {
            "urls": [
                {
                "url": "https://t.co/HKvKYr4Dex",
                "expanded_url": "http://www.elmananerodiario.com",
                "display_url": "elmananerodiario.com",
                "indices": [
                    0,
                    23
                ]
                }
            ]
            },
            "description": {
            "urls": []
            }
        },
        "protected": false,
        "followers_count": 6146738,
        "friends_count": 1231,
        "listed_count": 12640,
        "created_at": "Thu Jan 21 16:20:18 +0000 2010",
        "favourites_count": 47050,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": false,
        "verified": true,
        "statuses_count": 66326,
        "lang": null,
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "C0DEED",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_tile": false,
        "profile_image_url": "http://pbs.twimg.com/profile_images/863986088502640641/2_JuuNt-_normal.jpg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/863986088502640641/2_JuuNt-_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/107120856/1545228661",
        "profile_link_color": "0084B4",
        "profile_sidebar_border_color": "C0DEED",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "has_extended_profile": false,
        "default_profile": false,
        "default_profile_image": false,
        "following": false,
        "follow_request_sent": false,
        "notifications": false,
        "translator_type": "null"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 1280,
        "favorite_count": 2938,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "es"
    },
    "retweet_count": 0,
    "favorite_count": 0,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "lang": "es"
    }

También se hace uso de otro dataset categorizado por rangos de edad, género y texto de tweets aleatorios, los cuales apoyan al entrenamiento de predicción de polaridad de opiniones escritas por usuarios de Twitter. A continuación, se describen las propiedades utilizadas dentro del dataset en formato .JSON utilizadas:

1. Klass: Define una clase relacionada al rango de edad de los twitters a analizar
2. age_group: Define el rango de edad de los usuarios que escriben tweets
3. gender: Define el género de los usuarios que escriben tweets
4. language: Define el idioma utilizado de los usuarios que escriben tweets
5. text: Es un arreglo de texto de 1000 tweets escritos por los usuarios

Un ejemplo de esta estructura de datos puede ser visto haciendo clic *[aquí](https://github.com/oscarch01/Clasificador-de-Polaridad-Para-Pol-ticos/blob/master/training_corpus.json)*.

## Entrenamiento
Para el proceso de entrenamiento se lleva a cabo la siguiente lista de tareas:
1. Mediante la API de Twitter se obtienen publicaciones relacionadas con un tema en específico, eso es posible haciendo uso de el paquete de **Tweepi**, mediante la función de **recover_tweets**, al cual se le envía como parámetro la frase o palabra a buscar dentro de los tweets. Cabe mencionar que es posible agregar como parámetro la cantidad de tweeters que se desea obtener. Posteriormente, mediante la función **format** de **Tweppi** se crea un objeto que almacena el nombre del usuario seguido del texto de su publicación o respuesta a otro tweet.
Para esta tarea **se omite la utilización de los retweets**.
2. Se crea un objeto a partir de la lectura de un corpus de entrenamiento, el cual es filtrado para mantener la información relacionada con el género, el rango de edad y el texto del tweet. Al ser un objeto en formato JSON, es posible iterar en el contenido de este, por lo que se decide hacer uso de los primeros 50 tweets para construir dicho objeto para entrenar un algoritmo de regresión logística.
3. Se valida la existencia de un espacio vectorial con el objetivo de disminuir el tiempo de ejecución del algoritmo. Si el espacio vectorial existe, se hace uso de la información almacenada en el, de lo contrario, se agrega la información resultante del filtrado de texto del corpus de entrenamiento, el cual es tokenizado para almacenar cada una de las palabras de cada oración dentro de un arreglo.
4. Se agrega al espacio vectorial el texto obtenido de los tweets desde la API. Este texto es tokenizado por palabras de cada oración dentro de un arreglo.
5. Para realizar la regresión logística, primero es necesario crear un vector de cada una de las palabras almacenadas en el espacio vectorial. Cada palabra tokenizada se convierte en una llave a la cual se le asigna el valor de 0, con el objetivo de contar cuantas veces aparece esta en el texto. El contenido del corpus se transforma en un dataframe mediante las funciones de la libreria **Pandas**.Posteriormente se hace el llenado del vector para su análisis futuro. Es necesario iterar cada texto almacenado en el corpus, para lo que se crea un arreglo mediante **NumPy**, el cual, si está vacío, se agrega por completo el vector generado anteriormente, de lo contrario, se apila un nuevo vector generado a partir de cada uno de los textos leidos en la iteración del corpus. Después, se hace uso de la propiedad de género, la cual es transformada a un objeto **NumPy**, para su posterior análisis.
6. Se preparan los parámetros para el entrenamiento. Para este caso, se hace uso del 70 por ciento de los datos obtenidos para el entrenamiento, el 30 por ciento para pruebas. Una vez obtenidos los resultados de la división de los datos, se lleva a cabo la evaluación mediante regresión logística.


## Evaluación
La evaluación de la regresión logística se lleva a cabo mediante la función de **LogisticRegression** de la libreria **SciKitLearn**, la cual hace uso de los datos de entrenamiento obtenidos en la división realizada anteriormente. Posteriormente se hace la evaluación del nivel de predicción mediante la regresión logística entrenada y los datos de prueba.

## Descripción de los resultados
De acuerdo a los resultados obtenidos mediante la predicción basada en regresión logistica y los datasets utilizados, se logra obtener un porcentaje de predicción del 71 por ciento. Posteriormente se hace una prueba con los datos obtenidos desde la API de Twitter, obteniendo resultados similares a los del dataset de entrenamiento.

El algoritmo es capaz de reconocer el género del usuario que escribe un tweet relacionado con un tema en específico, sin embargo, al no contar con un dataset clasificado para obtener la polaridad de un tweet resulta complejo obtener resultados relacionados con este tema. Se requiere etiquetar de manera manual el dataset definiendo una polaridad para cada tweet, también es posible solucionar este problema haciendo uso de palabras clave en el tweet, es posible hacer uso de un algoritmo complementario de similitud coseno que apoye a la identificación de palabras que den significado positivo o negativo por cada tweet.