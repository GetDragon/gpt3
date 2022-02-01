import json
import os
import openai

openai.api_key = "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"
texto = """ART. 215.—Cuando sobrevengan hechos distintos de los previstos en los artículos 212 y 213 que perturben o amenacen perturbar en forma grave e 
inminente el orden económico, social y ecológico del país, o que constituyan grave calamidad pública, podrá el Presidente, con la firma de todos los 
ministros, declarar el estado de emergencia por períodos hasta de treinta días en cada caso, que sumados no podrán exceder de noventa días en el año 
calendario.
Mediante tal declaración, que deberá ser motivada, podrá el Presidente, con la firma de todos los ministros, dictar decretos con fuerza 
de ley, destinados exclusivamente a conjurar la crisis y a impedir la extensión de sus efectos.
Estos decretos deberán referirse a materias que tengan 
relación directa y específica con el estado de emergencia, y podrán, en forma transitoria, establecer nuevos tributos o modificar los existentes. 
En estos últimos casos, las medidas dejarán de regir al término de la siguiente vigencia fiscal, salvo que el Congreso, durante el año siguiente, 
les otorgue carácter permanente.
El gobierno, en el decreto que declare el estado de emergencia, señalará el término dentro del cual va a hacer uso de 
las facultades extraordinarias a que se refiere este artículo, y convocará al Congreso, si este no se hallare reunido, para los diez días siguientes al 
vencimiento de dicho término.
El Congreso examinará hasta por un lapso de treinta días, prorrogable por acuerdo de las dos cámaras, el informe motivado 
que le presente el gobierno sobre las causas que determinaron el estado de emergencia y las medidas adoptadas, y se pronunciará expresamente sobre la 
conveniencia y oportunidad de las mismas.
El Congreso, durante el año siguiente a la declaratoria de la emergencia, podrá derogar, modificar o 
adicionar los decretos a que se refiere este artículo, en aquellas materias que ordinariamente son de iniciativa del gobierno. En relación con aquellas 
que son de iniciativa de sus miembros, el Congreso podrá ejercer dichas atribuciones en todo tiempo.
El Congreso, si no fuere convocado, se reunirá 
por derecho propio, en las condiciones y para los efectos previstos en este artículo.
El Presidente de la República y los ministros serán responsables 
cuando declaren el estado de emergencia sin haberse presentado alguna de las circunstancias previstas en el inciso primero, y lo serán también por 
cualquier abuso cometido en el ejercicio de las facultades que la Constitución otorga al gobierno durante la emergencia.

El gobierno no podrá desmejorar los derechos sociales de los trabajadores mediante los decretos contemplados en este artículo.
Tl;dr:"""
texto2 = """
La literatura
El Libro de los Ritos (en chino tradicional, 禮; pinyin, Lǐjì), un antiguo texto chino. Algunas definiciones de la literatura han llevado a incluir todos los trabajos escritos.
Hasta el siglo XVII, lo que actualmente denominamos «literatura» se designaba como poesía o elocuencia. Durante el Siglo de Oro español, por poesía se entendía cualquier invención literaria, perteneciente a cualquier género y no necesariamente en verso, entendiéndose por tal tres tipos fundamentales de "poesía / literatura": la lírica (propia del canto, en verso), la épica (propia de la narración, en verso largo o prosa) y la dramática (en diálogo).3​ A comienzos del siglo XVIII se comenzó a emplear la palabra «literatura» para referirse a un conjunto de actividades que utilizaban la escritura como medio de expresión. A mediados de la misma centuria, Lessing publica Briefe die neueste Literatur betreffend, donde se utiliza «literatura» para referirse a un conjunto de obras literarias. A finales del siglo XVIII, el significado del término literatura se especializa, restringiéndose a las obras literarias de reconocida calidad estética. Este concepto se puede encontrar en la obra de Marmontel, Eléments de littérature (1787), y en la obra de Madame de Staël, De la literatura considerada en relación con las instituciones sociales.
En Inglaterra, en el siglo XVIII, la palabra «literatura» no se refería solamente a los escritos de carácter creativo e imaginativo, sino abarcaba el conjunto de escritos producidos por las clases instruidas: cabían en ella desde la filosofía a los ensayos, pasando por las cartas y la poesía. Se trataba de una sociedad en la que la novela tenía mala reputación, y se cuestionaba si debía pertenecer a la literatura. Por eso Eagleton sugiere que los criterios para definir el corpus literario en la Inglaterra del siglo XVIII eran ideológicos, circunscritos a los valores y a los gustos de una clase instruida. No se admitían las baladas callejeras ni los romances, ni las obras dramáticas. En las últimas décadas del siglo XVIII apareció una nueva demarcación del discurso de la sociedad inglesa. Eagleton nos cuenta que surge la palabra «poesía» como un producto de la creatividad humana en oposición a la ideología utilitaria del inicio de la era industrial. Tal definición la encontramos en la obra A Defence of poetry (1821) de Shelley. En la Inglaterra del Romanticismo, el término «literato» era sinónimo de «visionario» o «creativo». Pero no dejaba de tener tintes ideológicos, como en el caso de Blake y Shelley, para quienes se transformó en ideario político, cuya misión era transformar la sociedad mediante los valores que encarnaban en el arte. En cuanto a los escritos en prosa, no tenían la fuerza o el arraigo de la poesía; la sociedad los consideraba como una producción vulgar carente de inspiración.
La literatura se define por su literariedad
Don Quijote y Sancho Panza, personajes de Don Quijote de la Mancha.
En busca de la definición de los conceptos «literatura» y «literario», surgió la disciplina de la teoría de la Literatura, que empieza por delimitar su objeto de estudio: la literatura. No hay una definición unívoca del término, ya que dependerá del crítico literario que la defina, como así también de la época y del contexto que la define. Sin embargo, los primeros estudiosos que se preocuparon por el estudio de esta disciplina son los llamados formalistas rusos.
A comienzos del siglo XX, el Formalismo ruso se interesa por el fenómeno literario, e indaga sobre los rasgos que definen y caracterizan dichos textos literarios, es decir, sobre la literaturidad de la obra. Roman Jakobson plantea que la literatura, entendida como mensaje literario, tiene particularidades de tal forma que la hacen diferente de otros discursos; ese interés especial por la forma es lo que Jakobson llama «función poética», por la que la atención del emisor recae sobre la forma del mensaje (o, lo que es lo mismo, hay una «voluntad de estilo» o de estilizar el lenguaje por parte del escritor). En efecto, hay determinadas producciones lingüísticas cuya función primordial es proporcionar placer literario, un deleite de naturaleza estética, producido por la belleza, en relación con el pensamiento aristotélico. El lenguaje combinaría en sus elementos más simples dos tipos de elementos: redundancias, recurrencias o repeticiones rítmicas formales y de contenido semántico, esto es, analogías, por un lado, y por el otro, desvíos de la norma, para alejarse del lenguaje común, causar extrañeza, renovar: la llamada anomalía; de ese modo se impresiona la imaginación y la memoria y se llama la atención sobre la forma del mensaje, su peculiar forma expresiva. De ambas tendencias, la rítmica o repetitiva es popularizante, y la segunda, por el contrario de sesgo aristocratizante.
El lenguaje literario sería uno estilizado y con una trascendencia particular, destinado a la perdurabilidad; muy diferente de las expresiones de la lengua de uso común, destinada a su consumo inmediato. La literatura, por otra parte, exige por tradición un respaldo sustentable: El Ingenioso Hidalgo Don Quijote de La Mancha no habría podido escribirse si no hubieran existido antes los libros de caballerías.
Wolfgang Kayser, a mediados del siglo XX, plantea cambiar el término «Literatura» por el de Belles Lettres, diferenciándolas del habla y de los textos extraliterarios, en el sentido de que los textos literario–poéticos son un conjunto estructurado de frases portadoras de un conjunto estructurado de significados, en el que los significados se refieren a realidades independientes del que habla, creándose así objetividad y unidad propias.
Tl;dr:"""
response = openai.Completion.create(engine="text-curie-001", prompt=texto, max_tokens=1100, temperature=0.11)
print(response['choices'][0]['text'])