# Bienvenidos Digitallers 2025

## 10-07-2025- Clase 14

Librerias : Saber que librerias tengo instaladas
```cmd
pip list
```
Librerias que todos deben conocer :) : https://www.instagram.com/p/C_VyOHHRv0N/?img_index=1
* pygame
* tkinter

Diccionarios {}
* [] accede al un elemento de un diccionario por clave, lanza KeyError si la clave no existe. Tambien sirve para crear la clave en el diccionario
* dicc.get  es parecido al [] pero ei el elemento no esta devueve None o el valor por defecto (segundo parametro)
* dicc.tems() convierte el diccionario en una lista de tuplas [(clave, valor)]
* 

Excepciones Comunes en python
* TypeError (ej  "1" + 2)
* ValueError (ej int("hola"))
* IndexError
* KeyError (Clave No encontrada en un diccionario)
* AttributeError (El atributo no esta en un obeto o diccionario)
* NameError (VariableNoDefinida)
* ModuleNotFoundError

Algunos metodos utiles de python:
* min
* max
* len
* string.split
* random.randint
* lista.count

Type Hints
``` python
def dividir(num1: float, num2: float) -> float:
```

Compresion de listas
``` python
def lista_aleatoria(cantidad):
  #sintaxis de comprensión de listas
  return [random.randint(1,100) for _ in range(cantidad)]
```


## 08-07-2025- Clase 13

### Python.

**Salida Por Pantalla**
```python
print("Hola Digitallers")
```

**Variables**
```python
mensaje="Hola Digitallers"
print(mensaje)
```

**Tipos de Datos Basicos**
```python
>>> entero = 10
>>> decimal = 3.14
>>> texto = "Hola"
>>> es_verdad = True
>>> print(type(entero))
<class 'int'>
>>> print(type(decimal))
<class 'float'>
>>> print(type(texto))
<class 'str'>
>>> print(type(es_verdad))
<class 'bool'>
```
**Que paso aca?**
```python
>>> #Quiero que le pregunte dos numeros al usuario y los sume
>>> num1 = input("Ingrese un numero")
Ingrese un numero12
>>> num2 = input("Ingrese otro numero:")
Ingrese otro numero:34
>>> print(num1 + num2)
1234
```

**Deberia haber hecho...**
```
print(int(num1) + int(num2))
```

**Peeeeeeeeero peeeeeeero peeeeeero si trato de convertir en int una cadena que no tiene numeros da error**
```python
>>> print(int(texto))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Hola'
```

## 03-07-2025- Clase 12

### Chatbots

> https://botpress.com/

Vamos a programar nuestro chatbot con Colab...

> https://colab.research.google.com/drive/1gt6DY55GXNQ6aQcEko83gcfZYy525GIl?usp=sharing

ENUNCIADO
** Programa un chatbot donde el chatbot me muestre el comienzo de una historia y pregunte al usuario sobre como continuar. El chartbot tiene que tener 4 interacciones donde al final el usuario o muera o salga vencedor ** 
Bien AHI!!!

### Repasando los modelos chinos
* https://www.deepseek.com/es
* https://chat.qwen.ai/

## LA pagina de OpenAI para desarrolladores
> https://platform.openai.com/

## 01-07-2025- Clase 11

### Extensiones de IA Para Google Shets
> https://www.sheetgpt.ai/
Tambien lo programamos con appScripts\

### Machine Learning
* PPT Teorico : https://www.instagram.com/p/C1ntRrRswAu/?img_index=1
* Recurso Para aprender ML :https://www.kaggle.com/
* Extension ML para sheets : https://simplemlforsheets.com/

## 26-06-2025- Clase 10

### Adeleanto de Python

Claude saco la posibilidad de publicar los artefactos que estan copados y justo aparecio uno que es un mini tutorial de lo basico de pyton
> https://claude.ai/artifacts/inspiration/c9e8652f-1804-4903-a1d1-111c85a054e4
Se animan a hacerlo para la proxima clase?

### IA Generativa Profesional

#### IA Generativa para presentaciones

Para presentaciones tipo PowerPoint la mejor herramienta es :
> https://gamma.app/signup?r=cjucljp9heegmkv

#### IA Generativa para Videos Profesionales

Herramienta Sugerida para Videos de Avatars
> HeyGen : https://www.heygen.com/
Otra Herramienta para videos de Avatars
> https://www.hedra.com/  (Plan Gratuito Deshabilitado por Ahora)






### IA Generativa-Generacion de Video

Herramienta para generar videos narrativos par redes sociales. 
* Lo importante no es generar el video sino la narracion)
* En vez de Generar la imagen con IA la saca de una base de datos de imagenes sin derecho de autor
> InVideo : https://invideo.io/

PolloAI : Herramienta que recopila varios modelos generadores de Video  

> https://pollo.ai/invitation-landing?invite_code=dIOOD7

## 24-06-2025- Clase 9

### Truco para descargar Videos de youtube

Entra al video que querés descargar.
En la barra de direcciones, cambiá:
> https://www.youtube.com/watch?v=VIDEO_ID
por:
> https://ssyoutube.com/watch?v=VIDEO_ID
Te va a redirigir a un sitio como SaveFrom.net, donde podés elegir el formato y descargar el video.


### Herramientas Para estudiar

La Mejor herramienta para estudiar y agrupar material
> https://notebooklm.google.com/
Para Devs
> https://roadmap.sh/

### Herramientas para reuiones online

* https://tactiq.io/es
* https://www.read.ai/es (Lee emociones de los participantes)

### Generacion de Videos

#### Herramientas para Edicion de Videos

> https://www.capcut.com/es-es

#### Casos de Uso Generacion de Videos

- Prompt a Video
- Imagen a Video
- Efectos Predeterminados
- Transiciones

#### Herramientas Generacion de Videos

* RunwayML :  https://runwayml.com/
* KlingAI : https://klingai.com/global/
* Pika Labs : https://pika.art/
* PixVerse: https://app.pixverse.ai/
* Dream Machine : https://lumalabs.ai/dream-machine (PAGO)
* Invideo : https://invideo.io/ (PAGO)

## 18-06-2025- Clase 8

# LA PROXIMA CLASE VER HERRAMIENTAS PARA TRANSCRIBIR REUNIONES

### Enunciado Actividad proximas clases

> Esta clase y las siguientes vamos a crear un video musical por partes sobre una cancion tecno que muestre imagenes de paisajes paradisiacos

### IA Generativa : Imagenes

Modificar Imagen Existente. Vamos a utilizar la web  
> https://aistudio.google.com/
Esta pagina te permite probar los modelos de IA de google y ademas vamos a usar la para editar una imagen.

### IA Generativa : Generacion de Canciones

Sitios Que vimos
* Udio : https://www.udio.com/
* Suno : https://suno.com/
* Boomy : https://boomy.com/ (Un poquito mas avanzado para el que ya sabe musica)

Vamos a Editar el Video con CapCut (Vayan descargando)
> https://www.capcut.com/es-es

### Herramientas de  Speech

#### Text-to-Speech

> https://www.naturalreaders.com/
 
NaturalReaders no permite bajar audio en la version Gratuita. Para hacerlo vamos a ver un hack que es activando el Streo Mix (Utilizar la salida de audio como entrada)
* Boton Derecho en el parlante en la barra de tareas y despues elegir "Sound Settings"
* Abajo a donde dice "More Sound Settings"
* Se te abre una ventanita nueva
* Vas a Recording y habilitas el Streo Mix (Boton Derecho, Enable)

#### Speech-To-Text
> https://chromewebstore.google.com/detail/unlimited-summary-generat/eelolnalmpdjemddgmpnmobdhnglfpje

### Herramientas de IA

* ChatGPT con PDF : https://www.chatpdf.com/es
* TextCortex   https://textcortex.com/es
* TextCortex Extension : https://chromewebstore.google.com/detail/textcortex-personal-ai-as/hahkojdegblcccihngmgndhdfheheofe

---
# 17-06-2025- Clase 7

# ME FALTO VER COMO MODIFICAR UNA IMAGEN EXISTENTE
# ME FALTO VER COMO GENERAR IMAGENES DESDE EL GOOGLE COLAB

### Enunciado Actividad proximas clases

> Esta clase y las siguientes vamos a crear un video musical por partes sobre una cancion tecno que muestre imagenes de paisajes paradisiacos

Como ejemplo vimos algunas del canal del profe que hizo con sus alumnos
> https://www.youtube.com/@ElectricDreams-n9c
Si va todo bien y lo terminamos lo subimos al canal del profe

#### Prompt Engineering para generacion de imagenes
Tips:
* Prompt en ingles
* Utilizar ChatGPT para escribir mejores prompts

#### Modelos de Generacion de Imagenes

##### Modelos Propietarios
* Phoenix
* Ideogram GenAI

##### Modelos Open Source
* Flux

#### Herramientas Generacion de Imagenes
* LeonardoAI : https://leonardo.ai/ Herramienta para generar imagenes probando varios modelos. Te da 150 creditos que se renuevan diariamente
* Ideogram : https://ideogram.ai/. Ideal para generar imagenes con texto
* Microsoft Designer : https://designer.microsoft.com/
* ImageFX (De Google) (Solo Prompts en ingles) :https://labs.google/fx/tools/image-fx
> Tambien probamos Whisk que me deja animar imagenes y hacer videos : https://labs.google/fx/es/tools/whisk
* FreePic : https://www.freepik.es/ ( Gracias Rodrigo...se fue :( ) 


#### Casos de Uso
* **Texto a Imagenes** : A partir de un prompt generar una imagen (Lo hicimos con Leonardo.AI)

* **Imagen a Imagen** : Utilizar una imagen de referencia y cambiarla con el prompt (Lo hicimos con Leonardo.AI)

* **Imagenes con Texto** : Se puede hacer con el modelo Phenix 1.0 de Leonardo aunque es ideal para este caso de uso utlizar la herramienta IdeoGRAM

* **Generacion de Imagenes Hiper Realistas** : Donde termina la realidad y empieza la ia?
> Curiosidad Imagenes Rostros Hiper Realistas: https://thispersondoesnotexist.com/

* **Upscaler (mejorar calidad de una imagen)** : Probamos el Upscaler de la herramiente FreePic
* Generacion de imagenes para Dieño Grafico (Banners, Flyers) (Estilo Canva) :
* **Generacion de Imagenes con Modelos Open Source** : Utilizamos freepic que me dejo utilizar el modelo Flux Fast


---
## 12-06-2025- Clase 6

### Roles De IA

* Data Analyst
  > Usan herramientas como PowerBI https://www.plainconcepts.com/what-is-power-bi/
* Data Science
* Deep Learning
* Compter Vision
* Desarrollo de Chatbots
* Ai Tool Expert
* Ai Developer
* Cloud AI Engineering
* AI Research Scientist

### Herramientas de IA

 Arrancamos con una Seccion de la clase : Presentar herramientas/apps de IA
> Todas las clases, la primera parte de la clase van a traer alguna herramienta de Inteligencia Artificial
> https://www.grammarly.com/ (Gracias Jorge)

#### Catalogo de Herramientas de IA 
* https://theresanaiforthat.com/
* https://huggingface.co/spaces
*

### Uso de la API

Todos los LLM que vimos tienen dos formas de utilizarse
* La interfaz web
     *  https://chatgpt.com/
     *  https://groq.com/
     *  https://gemini.google.com/
* La API : Tienen una pagina del desarrador
    * https://platform.openai.com/)
    * https://console.groq.com/
  
> 👎Lo malo de openAI es que te cobra por usar sus modelos por API

Pasos para usar la api de Groq
1. Sacar una api key de groq en https://console.groq.com/keys (puede requerir loguearse)
2. Crear un google colab con tres celdas de codigo
3. Instalar la libreria de groq en la primer celda
   
```python
!pip install groq
```
  
4. Cargar la api key a una variable en la segunda celda
```python
    mi_api_key = input("Igrese su Api Key")
```
6. Invocar la llamada a groq en la tercer celda
```python
    from groq import Groq
    
    client = Groq(
        api_key=mi_api_key,
    )
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Quien descubrio america? Contestar el nombre sin acotar nada mas.",
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    
    print(chat_completion.choices[0].message.content)
```
7. ..
8. ddd

---
## 10-06-2025- Clase 5

### Programacion en Python

Vamos a programar en python desde https://colab.google/
> El datacenter que nos presta google : https://colab.google/static/images/home/data-center.jpg

**Funciones de Python**
* print : Se usa para mostrar algo por pantalla
* input : Se usa para pedirle informacion al usuario
* * int() : Funcion que Convierte un tipo de dato string en un integer

**Operadores en python**
* %  : Devuelve el resto de la division
* \> : Operador mayor que
* < : Operador menor que


***Estructuras de Control en python**
* for : Para ejecutar codigo una cantidad fija de veces
```python
for i in range(1, 11):
    print(i)
```
* if : Para ejecutar un codigo dada una condicion
```python
if numero % 2 == 0:
    print(f"El número {numero} es PAR")
else:
    print(f"El número {numero} es IMPAR")
```

### Prompt Engenieering : Patron Personalizacion de Salida

Salidas Posbiles Que podemos pedir
* CSV (Comma Separated Values)
* Mermaid (https://mermaid.live/)
   * Claude tiene artefactos con previsualizacion de Mermaid
* Salidas en un lenguaje de programacion

---
## 06-05-2025- Clase 4

#### Prompt Engeniering : Prompting Wars...
> https://forms.gle/KU9ojZtd5e4UGLgX8  
Resultado  
> https://chatgpt.com/share/68421bb3-7a2c-8005-819a-43a01def69b5  

#### System Prompts
Preguntandole a los LLM sobre su System Prompt me respondieron:
* ChatGPT : https://chatgpt.com/share/68421db9-bc90-8005-bf48-2821c8ea71ff
* Groq : https://grok.com/share/c2hhcmQtMg%3D%3D_233b02a4-295f-4d2f-bfaa-efda7e7de6e3

### Prompt Engineering : Tips

> Usar la IA para que mejore mis prompts como prompt engineering

#### Prompt Engineering : Contexto / Interaccion / Prompt Chainning

> Cuando escribo un prompt es importante darle al modelo de lenguaje toda la informacion que pueda llegar a ser relevante para lo que estamos pidiendo sin retringirse en la longitud del prompt

?Que informacion le doy?  Porque no dejamos que ChatGPT me haga preguntas : Patron Interaccion
* Ejemplo Sin Patron Interaccion : https://chatgpt.com/share/68422217-065c-8005-ae18-d7ab84e2c867
* Ejemplo con Petron Interaccion : https://chatgpt.com/share/6842222d-f6d0-8005-9587-4fc183a8b58f

Ejemplo *Prompt Chainning*: https://chatgpt.com/share/6842232a-f780-8005-9846-9a7d73c2ff13

#### Prompt Engenieering : Patron Personalizacion de Salida

Salidas Posbiles Que podemos pedir
* Tabla
* Json
* XML
* HTML (Viene con dos amigos que son CSS y el javascript)
    * Lo puedo imprimir y generar un PDF
* Markdown
     * Lo podemos utilizar para escribir una plantilla exacta de como queremos la respuesta para lograr que la IA sea un poco mas "deretministica"
 
Ejemplo de plantilla utilizada
```markdown
# [Nombre]
**[Creador]**
*[Fecha_Creacion]*
*[Pais de Origen con emoji de bandera]*

## [Lista de Temporadas]
1. [Nombre Temporada 1]
2. [Nombre Temporada 2]
..

## Synopsis
> [Sinopsis]
---
```

---
## Clase 3

### Prompt Engineering  

**Patron Persona**  

* Prompt Sin Patron : Explicame porque llueve.
* Prompt a un Experto : Actua como un experto en Meterologia y ciencias de la atmosfera con un alto conocimiento en qimica y fisica y dame una explicacion cientifica y detallada porque llueve
* Prompt a un experto alternativo : Actua como un shaman metafisico experto en el mundo de los espiritud y el multiverso y explicame porque llueve
* Prompt a una celebridad : Actua como si fueras el corredor de F1 Colapinto y explicame porque llueve


### Recapitulando lo pendiente de la clase anterior

Vamos a ver como ejecutar un  LLM localmente....  
* Instalamos el LMStugio de esta Web : https://lmstudio.ai/
* Otra Alternativa : https://ollama.com/

Repasamos Huggin Face y Jugamos con algunos Spaces :https://huggingface.co/

### Actualizaciones

> Ya se activaron los examenes en el Alumni. Vayan haciendo el del modulo 1.

### Mas Modelos de Lenguaje

* Arrancamos viendo Manus : https://manus.im/
* Vimos como probar otros modelols de lenguaje de google : https://aistudio.google.com/

## 2025-05-29-Clase 2

### Recomendacion
* Abrirse una cueta de GitHub
* Cuenta de GMAIL Alternativa

### TEmario de Clases

- Modelos de lenguaje Propietarios y los Modelos Open Source

* Modelos de Lenguaje Propietarios
     * Claude (La competencia mas directa de chatGPT) : https://claude.ai/new
          * Anthropic
          * Buenisimo para generar paginas WEB
          * Tiene ARTEFACTOS
          * Desventaja : Conversaciones mas corta que ChatGPT
       
* Modelos Opern Source
     * DeepSeek (Modelo de razonamiento)
     * Familia LLama
     * Groq (https://groq.com/#)  
            * Es una pagina que hostea modelos de inteligencia artificial open source  
            * Se caracteriza por su rapida velocidad de respuesta al contar con un harware especializado llamado LPU (Language Processing Unit)  
      * Mistral (mistral.ai)
             * Modelo Frances. Nunca va aser el primero. Kuak.
             * Bueno para programar en python
       * Qwnen
             * Desarrollado por la empresa Alibaba

### Preguntas

* Que modelo de lenguaje es mejor que otro?
> Una pagina que nos puede aproximar a la respuesta es : https://lmarena.ai/

 * De donde me descargo o consulto los modelos Open Source?
> https://huggingface.co/


### Actividades Propuesta 

* Propuesta : Probar los distintos modelos de lenguaje que vamos a ver en clase y sacar conclusiones
* Buscar otros LLM que no hayamos visto en clase
* Probar modelos Open Source de HugginFaces en la seccion "Spaces"


## 2025-05-27-Clase 1

### RECOMENDACIONES 
* Si tienen una sola cuenta de gmail CREARSE una cuenta de gmail para el curso. Vamos a probar herramientas y la gran mayoria piden login con GMAIL. Despues las herramientas mandan mails. Para que no molesten eso mails... cuenta Nueva de gmail...
* Ir Resolviendo los examenes del alumni masomenos a la par. No dejar todo al final. Consultar en clase lo que no se da y no entiende

### Que vamos a ver en el curso Digitallers Inteligencia Artificial 

* Herramientas e IA
* Modelos de Inteligencia artificial
* Trabajar con distintas herramientas de IA del mercado para ver las cosas que se pueden hacer IA.
* Prompt Engineering
* Generar Diagramas
* Generar Imagenes, Generar Canciones, Generar Videos...
* Generar Presentaciones
* Generar Investigaciones
* Machine Learning
* Programar en Python
* Va a aprender los fundamentos para poder desarrollar nosotros las herramientas que vimos en la primera parte

### Links
* Repo del Profe : https://github.com/estebancalabria/Intro-Ia/
* Juego creado por Rodigo Valenzuela con ia : https://bird-psi-six.vercel.app/   
* Conferencia China de Robots: https://www.youtube.com/watch?v=giyl27gKvS4  
     
### Modelos de Lenguaje  

* Modelo de lenguajes propietarios (No son Open Source)  m
    * Chat GPT (https://chatgpt.com/) : Bueno para generacion de texto creativo
         * Desarrollado por OpenAI 
     * Grok (https://grok.com) : El que menos censura tiene. Puedo hacer imagenes de famosos  
         - Gemini (https://gemini.google.com/app) : 
              -  Integracion con herramientas de google  
              -  Conocimiento factico  
              -  Hicimos programitas re facheros y probamos el canvas  
              -  Nos planificamos unos viajes con google flighs y generamos eventos en google calendar  
               - Investigaciones con google research   
         - Mencionamos Manus :https://manus.im/  
   - Modelos de lenguajes Open Source  
         - Deep Seek (aka El modelo Chino) : https://www.deepseek.com/en  
               - Destaca en tareas de razonamiento con su modo DeepThink (R1) (Chain of Thoughts)  
               - No le preguntes sobre el regimen de china ni nada de eso que se enoja  
     
### Definciones 
* Modelo Multimodal : Procesa tanto texto como imagenes  
