import random
import time

# --- 1. BASE DE DATOS: LIBRO DEL I CHING (1-45) ---
LIBRO_ICHING = {
    1: {
        "nombre": "CH'IEN / EL CREADOR",
        "trigrama_sup": "ch’ien, lo creador, el cielo",
        "trigrama_inf": "ch’ien, lo creador, el cielo",
        "exposicion": (
            "El hexagrama se compone de seis líneas llenas. Corresponden a la potencia original yang que es "
            "luminosa, fuerte, espiritual, activa. Es uniformemente fuerte de naturaleza y corresponde a una "
            "síntesis del poder y la energía. Su imagen es el cielo. Designa la acción creadora de la divinidad "
            "en el universo, y en el mundo de los hombres, la acción de los santos sabios y del soberano que "
            "desarrolla su naturaleza superior. Corresponde al 4° mes (mayo-junio)."
        ),
        "juicio": (
            "Lo creativo, favorecido por la perseverancia, produce un éxito sublime.\n\n"
            "NOTAS DEL JUICIO:\n"
            "1) Éxito: poder de realizar.\n"
            "2) Sublimidad: excelencia y origen.\n"
            "3) Favorecer: aventajar y crear lo justo.\n"
            "4) Perseverancia: sabiduría que reconoce las leyes fijas."
        ),
        "imagen": (
            "El movimiento del cielo es poderoso. Así el hombre noble se transforma en fuerte e incansable. "
            "La repetición del signo Ch'ien significa que un día es seguido por otro, engendrando la idea de tiempo "
            "y de una duración potente que está más allá de él. El sabio descarta conscientemente todo elemento "
            "vulgar para llegar a ser infatigable."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: 'Dragón escondido. No actuar'.\n"
                "Simboliza la energía que en invierno se sumerge en la tierra. La fuerza creadora está aún oculta. "
                "Representa a un gran hombre cuyos méritos aún no son reconocidos; debe esperar con paciencia "
                "pacífica y fuerte sin dejarse desalentar."
            ),
            2: (
                "Nueve en el segundo lugar significa: 'El dragón aparece en el campo. Es ventajoso ver al gran hombre'.\n"
                "Los efectos de la fuerza luminosa comienzan a manifestarse. El gran hombre aparece en el campo de "
                "acción entre sus iguales. Lo distingue la seriedad de sus propósitos y su influencia organizada."
            ),
            3: (
                "Nueve en el tercer lugar significa: 'A lo largo de todo el día el hombre noble se mantiene creativamente activo. "
                "Cuando la noche cae su mente continúa ocupada. Peligro. Sin reproches'.\n"
                "Su reputación comienza a extenderse. Existe el peligro de dejarse arrastrar por la ambición y "
                "destruir la pureza interior, pero si posee la prudencia suficiente, permanecerá sin reproches."
            ),
            4: (
                "Nueve en el cuarto lugar significa: 'Vuelo hesitante sobre los abismos. Sin reproches'.\n"
                "Momento del pasaje al acto. El hombre se encuentra ante un dilema: tomar parte importante en el "
                "mundo o retraerse y cultivar la personalidad en la quietud. Si es consecuente con su naturaleza "
                "íntima, encontrará la vía conveniente."
            ),
            5: (
                "Nueve en el quinto lugar significa: 'Un dragón vuela en el cielo. Es ventajoso ver al gran hombre'.\n"
                "El gran hombre ha alcanzado la esfera de las naturalezas celestes. Su influencia se hace visible "
                "en el mundo. 'Las cosas que tienen afinidad entre ellas en su esencia íntima se buscan mutuamente'."
            ),
            6: (
                "Nueve en la cúspide significa: 'El dragón arrogante deberá arrepentirse'.\n"
                "Cuando un hombre alcanza cumbres tan altas que no se relaciona con el resto de la humanidad, queda "
                "aislado, lo que lleva al fracaso. Previene contra aspiraciones que exceden la propia capacidad."
            )
        },
        "especial": (
            "Cuando todas las líneas son nueve significa: 'Aparece un vuelo de dragones sin cabezas. Fastuoso'.\n"
            "Todo el hexagrama está en movimiento y cambia al hexagrama K'un (Lo Receptivo). Significa que la "
            "mansedumbre unida a la fuerza en las decisiones trae buena fortuna."
        ),
        "lineas": {1: "Dragón escondido.", 2: "Dragón en el campo.", 3: "Activo todo el día.", 4: "Vuelo hesitante.", 5: "Dragón en el cielo.", 6: "Dragón arrogante."}
    },
    2: {
        "nombre": "K'UN / LO RECEPTIVO",
        "trigrama_sup": "K'un Lo receptivo, Tierra.",
        "trigrama_inf": "K'un Lo receptivo, Tierra.",
        "exposicion": (
            "Este hexagrama está constituido exclusivamente por líneas quebradas, que representan la oscuridad, "
            "la docilidad, el poder receptivo primario del yin. El atributo del hexagrama es la docilidad, "
            "imagen de la tierra. Es el complemento perfecto de Lo Creativo, no el opuesto; no hay combate sino "
            "complementación. Representa la naturaleza en contraste con el espíritu, la tierra en contraste con "
            "el cielo, el espacio frente al tiempo, lo femenino-maternal frente a lo masculino-paternal. "
            "Lo Receptivo tiene que ser activado y conducido por lo Creativo; entonces ahí produce buenos resultados. "
            "Pero cuando abandona su posición y trata de marchar al lado y en igualdad con lo creativo, entonces "
            "lo receptivo deviene peligroso. Corresponde al 10° mes (noviembre-diciembre)."
        ),
        "juicio": (
            "“Lo receptivo produce un éxito sublime, favorecido por la perseverancia de una yegua. "
            "Si el hombre noble emprende algo y trata de guiar, errará el camino. Pero si dócilmente se deja "
            "guiar, entonces seguirá una buena dirección. Es favorable encontrar amigos en el oeste y en el sur, "
            "y alejarse de los amigos del este y del norte. La tranquila perseverancia trae buena fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "1) Éxito: poder de realizar.\n"
            "2) Sublimidad: excelencia.\n"
            "3) Poder favorecer: aventajar.\n"
            "4) Perseverancia: definida como la de una yegua, que combina la fuerza del caballo con la docilidad de la vaca."
        ),
        "imagen": (
            "“La condición de la tierra es el abandono receptivo. El hombre noble de vasta naturaleza sostiene "
            "al mundo exterior”.\n\n"
            "Así como en el primer hexagrama el redoblamiento del trigrama significa duración temporal, en el segundo "
            "significa la extensión del espacio y la firmeza con la que la tierra lleva todo lo que vive y se mueve "
            "sobre ella. El hombre noble transforma su carácter en vasto, sólido y resistente para ser capaz de "
            "llevar y soportar los hombres y las cosas."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Cuando se camina sobre la escarcha, el hielo sólido no está lejos”.\n"
                "La fuerza oscura significa la muerte. En el otoño, cuando llegan las primeras heladas, la fuerza "
                "de la oscuridad y del frío comienza solamente a desplegarse. En la vida es posible prevenir la "
                "decadencia estando atento a esos signos y afrontándolos en el momento debido."
            ),
            2: (
                "Seis en el segundo lugar significa: “Directo, cuadrado, grande. Sin designio, sin embargo, todo "
                "lo permanente es favorecido”.\n"
                "El símbolo del cielo es un círculo, el de la tierra el cuadrado. La naturaleza genera sin error "
                "los entes que debe realizar, esa es su rectitud. El hombre alcanza la suprema sabiduría cuando "
                "todas sus acciones corresponden a la esencia creadora de la naturaleza."
            ),
            3: (
                "Seis en el tercer lugar significa: “Líneas ocultas. Uno es capaz de permanecer perseverante. "
                "Si por azar uno está al servicio de un rey, no ocuparse de nuevas tareas, sino acabar las que "
                "están empezadas”.\n"
                "Si un hombre es capaz de disimular sus habilidades, le permitirá madurar en paz. No busca ser "
                "honrado por las cosas que hace, sino que espera liberar las fuerzas activas que operan en lo "
                "receptivo."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Un talego amarrado. Ni loas ni reproches”.\n"
                "El principio oscuro se abre cuando se mueve y se cierra cuando reposa. Aquí se encuentra indicada "
                "una actitud de extrema reticencia. Es conveniente permanecer en reserva, sea en la soledad como "
                "en la agitación del mundo, puesto que allí también nos podemos ocultar."
            ),
            5: (
                "Seis en el quinto lugar significa: “Una orla amarilla en el traje acarrea la mayor buena fortuna”.\n"
                "Amarillo es el color de la tierra, del justo medio y de la justicia. La orla amarilla simboliza un "
                "adorno poco notorio, la reserva aristocrática. Cuando alguien ha sido llamado a trabajar en una "
                "posición prominente pero no independiente, el éxito depende sobre todo de la discreción."
            ),
            6: (
                "Seis en la cúspide significa: “Los dragones luchan en el espacio. Su sangre es negra y amarilla”.\n"
                "En el lugar superior, la línea oscura da lugar a la línea luminosa. Si ella intenta mantener una "
                "posición que no le es propia, podrá acarrear sobre sí la ira del más fuerte. Cuando corre sangre "
                "negra y amarilla es el síntoma de que algo anormal acontece y los dos poderes resultan heridos."
            )
        },
        "especial": (
            "Cuando todas las líneas son seis significa: “La perseverancia constante de lo durable es ventajosa”.\n"
                "En esta situación el hexagrama receptivo se transforma en el símbolo de lo creativo. Gana poder "
                "a través de la duración ateniéndose firmemente a lo justo. Solo una persistencia durable de lo perfecto."
        ),
        "lineas": {1: "Pisar escarcha.", 2: "Directo, cuadrado.", 3: "Líneas ocultas.", 4: "Talego amarrado.", 5: "Orla amarilla.", 6: "Dragones luchan."}
    },
    3: {
        "nombre": "CHUNG / LAS DIFICULTADES INICIALES",
        "trigrama_sup": "K´an El abismo, Agua.",
        "trigrama_inf": "Chen El movimiento, Trueno.",
        "exposicion": (
            "El nombre del hexagrama en realidad se refiere a una brizna de pasto empujando contra un obstáculo "
            "para salir de la tierra, de aquí el significado de 'la dificultad inicial'. El hexagrama indica la "
            "manera en que el cielo y la tierra producen los seres humanos. Es su primer encuentro, acompañado "
            "de dificultad. El trigrama inferior, lo que despierta, se dirige hacia arriba (trueno). El signo "
            "superior es K'an, lo insondable, el agua, lo peligroso. La situación describe una profusión densa "
            "y caótica. Pero el caos se aclara: el movimiento hacia arriba mientras lo insondable se sumerge "
            "tiene como imagen el peligro que se disipa. Las tensiones se descargan en la tormenta."
        ),
        "juicio": (
            "“Las dificultades iniciales llevan a un éxito sublime mediante la perseverancia. Nada debe ser "
            "emprendido. Es ventajoso buscar auxiliares”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Los tiempos de crecimiento están rodeados de dificultades, semejante a un nacimiento. Existe una "
            "perspectiva de gran éxito si se persevera, pero el resultado puede ser todavía incierto y sombrío. "
            "Todo gesto prematuro puede acarrear el fracaso. Es importante no permanecer solo y pasivo; hay que "
            "buscar auxiliares con los que se podrá enfrentar el caos y avanzar hacia el triunfo."
        ),
        "imagen": (
            "“Nubes y trueno: la imagen de la dificultad inicial. El hombre noble pone orden a la confusión”.\n\n"
            "Eso significa que el orden ya está presente en la dificultad inicial, tal como se desenreda la seda "
            "del capullo que hizo el gusano para ordenarla en madejas. A los impedimentos hay que saberlos "
            "contornear y a los problemas analizarlos y resolverlos. Hay que ser capaz al mismo tiempo de unir "
            "y separar."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Vacilación y obstáculos. Es conveniente permanecer perseverante. "
                "Es conveniente buscar ayuda”.\n"
                "Si una persona se encuentra en una disyuntiva al iniciar una empresa, no debe forzar el avance "
                "sino ser prudente y hacer una pausa. No se debe dejar desconcertar, sino mantener constantemente "
                "su meta presente. Es importante buscar el concurso de los asistentes correctos, desechando la "
                "arrogancia y el orgullo."
            ),
            2: (
                "Seis en el segundo lugar significa: “Las dificultades se acumulan. El caballo y el carro son "
                "desenganchados. No es un ladrón; sino que demandará cuando llegue el momento. La doncella es casta. "
                "No quiere comprometerse. Diez años –y entonces ella se compromete”.\n"
                "Cuando aparece alguien con auxilio, primero se le mira con desconfianza. Gradualmente se comprende "
                "que no trae malas intenciones. Esto no se acepta porque todavía no es el momento apropiado. "
                "Diez años es todo un ciclo para que retornen las condiciones normales y pueda unirse el esfuerzo."
            ),
            3: (
                "Seis en el tercer lugar significa: “Quien quiera cazar al venado sin el guardabosque sólo pierde su "
                "camino en el bosque. El hombre noble entiende los signos del tiempo y prefiere abstenerse. "
                "Seguir adelante lleva a la humillación”.\n"
                "Cuando se quiere cazar sin un guía en un bosque desconocido uno se pierde. Los esfuerzos prematuros "
                "sin una guía necesaria terminan en el fracaso y la deshonra. El hombre noble prefiere renunciar "
                "a un logro que provocar el fracaso y la humillación."
            ),
            4: (
                "Seis en el cuarto lugar significa: “El caballo y el carro se desenganchan. Procurar la unión. "
                "Ir trae buena fortuna de cualquier manera que se actúe”.\n"
                "Estamos en una situación en que nuestro deber es actuar pero faltan las fuerzas. Sin embargo se "
                "presenta una ocasión de establecer contacto. Hay que coger las conexiones que se ofrecen. Uno no "
                "debe refrenar sus pasos debido a un falso orgullo. Aceptar ayuda en una situación difícil no es "
                "una desgracia."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Dificultades para bendecir. Un poco de perseverancia trae "
                "buena fortuna. Demasiada perseverancia acarrea mala suerte”.\n"
                "Uno está en una posición en la cual se encuentran dificultades para poder expresar sus buenas "
                "intenciones. Uno debe ser cauteloso e ir paso a paso. No debe tratar de forzar la consumación "
                "de una gran empresa. Es solamente en calma y a precio de un trabajo sincero que se puede actuar "
                "progresivamente."
            ),
            6: (
                "Seis en la cúspide significa: “El caballo y el carro se desenganchan. Corren lágrimas de sangre”.\n"
                "Para algunos las dificultades iniciales son excesivas. Permanecen prisioneros de ellas sin poder "
                "liberarse. Se paralizan y nunca encuentran su camino. Renuncian a la lucha y abandonan. Tal "
                "resignación es la más triste de todas las cosas. No se debe persistir en esa actitud."
            )
        },
        "lineas": {1: "Vacilación y obstáculos.", 2: "Dificultades acumuladas.", 3: "Cazar sin guía.", 4: "Procurar la unión.", 5: "Dificultades para bendecir.", 6: "Lágrimas de sangre."}
    },
    4: {
        "nombre": "MÊNG / LA NECEDAD JUVENIL (la Ingenuidad)",
        "trigrama_sup": "Ken, La Inmovilidad, la Montaña.",
        "trigrama_inf": "K'an El abismo, Agua.",
        "exposicion": (
            "La idea de juventud y de locura está sugerida por la figura del trigrama superior, Ken (una montaña), "
            "y la del inferior, K’an (el agua). La fuente que surge del pie de la montaña es el símbolo de la "
            "juventud sin experiencia. El atributo del signo superior es la inmovilidad; la del inferior es el "
            "peligro. Detenerse sorprendido ante un peligroso abismo es un símbolo de la candidez juvenil. Pero "
            "el agua es algo que naturalmente fluye; al llenar los lugares profundos que obstaculizan su camino, "
            "el éxito es obtenido."
        ),
        "juicio": (
            "“La locura juvenil triunfa. No soy yo quien busca al joven inexperto sino que es él quien debe buscar "
            "mi ayuda. En el primer oráculo, yo informo. Si él pregunta dos o tres veces, importuna. Si importuna, "
            "no le daré información. La perseverancia es ventajosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "En la juventud, la inexperiencia no es un peligro siempre que se encuentre un maestro experimentado "
            "y se mantenga una actitud respetuosa frente a él. El maestro debe esperar ser llamado en lugar "
            "de ofrecerse; sólo así la instrucción llega en el tiempo y modo correctos. Si se plantean preguntas "
            "poco inteligentes o que demuestren desconfianza, el maestro debe ignorarlas en silencio."
        ),
        "imagen": (
            "“Un manantial al pie de la montaña: imagen de la juventud. El hombre noble cultiva su carácter por "
            "la escrupulosidad en todo lo que hace”.\n\n"
            "El carácter no se desarrolla esquivando los obstáculos, sino sabiéndolos vencer. La seriedad que no "
            "descuida nada es como el agua que llena todos los vacíos progresivamente y sin pausa, siguiendo así "
            "su marcha adelante."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Para hacer triunfar lo insensato es necesario imponer una disciplina. "
                "Hay que eliminar todas las trabas. Seguir en ese camino acarrea humillación”.\n"
                "La juventud en su inexperiencia se encuentra inclinada a tomar todo con despreocupación. Un cierto "
                "control a través de la disciplina es bueno, pero no debe degenerar en tiranía."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Soportar a los insensatos con dulzura trae buena fortuna. "
                "Saber como tratar a una mujer trae buena fortuna. El hijo es capaz de hacerse cargo de la familia”.\n"
                "Se muestra aquí a un hombre con fuerza superior interior, capaz de tolerar con dulzura los defectos "
                "de la inexperiencia humana. Esta combinación de cualidades lo capacita para tomar responsabilidades."
            ),
            3: (
                "Seis en el tercer lugar significa: “No debes tomar a una doncella cuando ella ha visto a un hombre "
                "de bronce y ha perdido el dominio de ella misma. No pongas obstáculos para que él tome posesión "
                "de ella. Nada que sea ventajoso”.\n"
                "Un hombre débil que trata de imitar a un individuo poderoso pierde su individualidad. Una aproximación "
                "tan servil no debe ser estimulada; resulta mala tanto para el joven como para el maestro."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Complicarse ingenuamente trae humillación”.\n"
                "Para los jóvenes ingenuos, lanzarse en imaginaciones vacías es peligroso. Si persisten en proyectos "
                "irrealizables, la humillación los persigue. A menudo el maestro no tiene otro recurso que dejarlos "
                "entregados a su suerte para que la experiencia les enseñe."
            ),
            5: (
                "Seis en el quinto lugar significa: “La candidez pueril trae buena fortuna”.\n"
                "Una persona ingenua que sigue las instrucciones de manera infantil y sin pretensiones está en la "
                "senda correcta. El hombre libre de arrogancia que se subordina a la autoridad del maestro será "
                "favorecido."
            ),
            6: (
                "Nueve en la cima significa: “No se deben cometer excesos de poder cuando se castigan las "
                "transgresiones de un insensato. Lo único benéfico es prevenir los excesos de poder y evitar las "
                "transgresiones”.\n"
                "El castigo no es un fin en sí mismo sino un medio para restablecer el orden. La intervención debe "
                "ser preventiva y tender a la mantención de la seguridad y la paz."
            )
        },
        "lineas": {1: "Disciplina necesaria.", 2: "Soportar con dulzura.", 3: "No imitar servilmente.", 4: "Complicarse ingenuamente.", 5: "Candidez pueril.", 6: "Evitar excesos de poder."}
    },
    5: {
        "nombre": "HSÜ / LA ESPERA (NUTRICIÓN)",
        "trigrama_sup": "K´an El abismo, Agua.",
        "trigrama_inf": "Ch'ien Lo Creativo, Cielo.",
        "exposicion": (
            "Todos los seres necesitan ser nutridos. Pero el alimento llega a su tiempo y hay que saber esperarlo. "
            "Este hexagrama muestra las nubes en el cielo, dando lluvia y refrescando todo lo que crece y proveyendo "
            "a la humanidad comida y bebida. La lluvia llega por sí misma, no podemos hacerla venir a la fuerza sino "
            "que tenemos que esperarla. La idea de 'espera' está además sugerida por las propiedades de cada uno "
            "de los trigramas: en el interior la fuerza (Ch'ien) y adelante el peligro (K'an). La fuerza frente al "
            "peligro no consiste en arremeter contra él incontroladamente sino en esperar el momento propicio."
        ),
        "juicio": (
            "“La Espera. Si eres sincero, tendrás brillo y éxito. La perseverancia trae buena fortuna. "
            "Es ventajoso atravesar la gran corriente”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La espera no consiste en una esperanza vacía. Hay una certeza interior de alcanzar la meta. "
            "Alguien se enfrenta a un peligro que debe ser superado. La debilidad y la impaciencia no ayudan. "
            "Sólo un hombre fuerte puede superar al destino, puesto que puede mantenerse firme hasta el fin gracias "
            "a su seguridad interior. Esta fuerza se revela como una sinceridad inflexible."
        ),
        "imagen": (
            "“Las nubes suben en el cielo: la imagen de la espera. El hombre noble come y bebe. Se alegra con un "
            "buen banquete y reconforta su mente”.\n\n"
            "Las nubes en el cielo indican una próxima lluvia. Lo único que se puede hacer es esperar que la lluvia "
            "caiga. No podemos forzar el futuro interfiriendo en las cosas antes que llegue su tiempo. Podemos, sí, "
            "fortificar el cuerpo comiendo y bebiendo e igualmente reconfortar la mente."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Esperando en la Pradera. Enseña a aguardar con paciencia. "
                "Es ventajoso permanecer en lo duradero. Sin reproches”.\n"
                "El peligro todavía no se presenta. Las condiciones todavía son simples. Uno debe tratar de "
                "llevar su vida normalmente por todo el tiempo posible. Sólo así se puede evitar un prematuro "
                "desgaste de energías."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Esperando en la arena. Hay algunas habladurías. "
                "El final trae buena fortuna”.\n"
                "El peligro se acerca gradualmente. La arena está cerca de los bancos del río. Comienzan a "
                "manifestarse los inconvenientes. En tales circunstancias nace fácilmente un malestar general. "
                "Si el que permanezca en calma y resignado puede lograr que para él las cosas finalmente marchen bien."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Esperar en el lodo, provoca la llegada del enemigo”.\n"
                "El cieno, que ya está impregnado del agua del río, no es un lugar favorable para esperar. "
                "El que se encuentra en una posición tan desfavorable atrae naturalmente a los enemigos que "
                "tratarán de explotar la situación. La precaución y una seria prudencia es todo lo que se puede hacer."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Esperar en la sangre. Salir del agujero”.\n"
                "La situación es extraordinariamente peligrosa. Es de suma gravedad, una cuestión de vida o muerte. "
                "Estamos atrapados en un agujero del cual debemos salir rápidamente. Sólo podemos resistir y dejar "
                "que el destino siga su curso. Esta calma resistente es la sola manera de salir de ese agujero."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Esperar comiendo y bebiendo. La perseverancia trae buena fortuna”.\n"
                "Incluso en medio del peligro se presentan momentos de paz cuando las cosas marchan "
                "relativamente bien. Debemos saber aprovechar cada momento teniendo siempre en vista la meta; "
                "la perseverancia es indispensable para lograr la victoria. Aquí se encuentra la clave del hexagrama."
            ),
            6: (
                "Seis en la cúspide significa: “Se cae en el pozo. Llegan tres huéspedes inesperados. Honrémoslos, "
                "y finalmente habrá buena fortuna”.\n"
                "La espera se termina, el peligro ya no puede ser evitado. Se cae en un pozo. Pero precisamente "
                "en este estado de desamparo sobreviene un cambio imprevisto. Hay una intervención extraña. "
                "Si uno mira con respeto este nuevo cambio, se escapa finalmente del peligro."
            )
        },
        "lineas": {
            1: "Esperando en la Pradera.",
            2: "Esperando en la arena.",
            3: "Esperar en el lodo.",
            4: "Esperar en la sangre.",
            5: "Comer y beber.",
            6: "Tres huéspedes inesperados."
        }
    },
    6: {
        "nombre": "SUNG / EL CONFLICTO",
        "trigrama_sup": "Ch'ien Lo Creativo, Cielo.",
        "trigrama_inf": "K'an El Abismo, Agua.",
        "exposicion": (
            "El trigrama superior -cielo- tiene un movimiento hacia arriba; el trigrama inferior -agua- "
            "descendente conforme a su naturaleza. Los movimientos de los dos trigramas van en sentido opuesto, "
            "de allí la idea de conflicto. El atributo del creador es la fuerza, mientras que el atributo del "
            "abismo es lo insondable, el peligro, la perfidia. Cuando la astucia se enfrenta a la violencia hay "
            "conflicto. Un carácter de este tipo es seguramente pendenciero."
        ),
        "juicio": (
            "“Conflicto. Eres sincero y encuentras obstáculos. Un alto prudente en la mitad del camino trae "
            "fortuna. Llevar a término el asunto trae infortunio. Hay que ver al gran hombre. No es prudente "
            "atravesar el gran océano”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El conflicto se desarrolla cuando uno está convencido de estar en lo cierto y corre a la oposición. "
            "Cuando uno está implicado en un conflicto, el único medio de salvación reside en la circunspección "
            "y en la fuerza interior. Llevar un conflicto a un desenlace penoso tiene malos efectos aunque "
            "estemos en la razón, porque la enemistad se perpetúa. Es importante ver al gran hombre que con "
            "imparcialidad y autoridad puede terminar el conflicto amigablemente."
        ),
        "imagen": (
            "“El cielo y el agua van por caminos opuestos: la imagen del Conflicto. Esto es lo que el hombre "
            "noble considera siempre cuidadosamente el comienzo de todos los asuntos que trata”.\n\n"
            "La imagen alude a las causas del conflicto que están latentes en las dos tendencias opuestas de los "
            "trigramas. Si los derechos y los deberes están claramente definidos, o si en un grupo las tendencias "
            "espirituales se armonizan, la causa profunda del conflicto desaparece por adelantado."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Si alguien no quiere proseguir un asunto habrá un poco de "
                "habladurías. Al fin, llega la fortuna”.\n"
                "Cuando un conflicto se encuentra en estado incipiente, lo mejor es evitarlo. Especialmente "
                "cuando el adversario es más fuerte no es prudente empujar el conflicto a una decisión. "
                "Puede haber una ligera disputa pero al fin todo irá bien."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Uno no puede comprometerse en un conflicto; uno vuelve "
                "al hogar, se va. La gente de su pueblo, trescientas familias, permanecen libres de culpa”.\n"
                "En la lucha con un enemigo más fuerte, la retirada no es una deshonra. Retirarse a tiempo es "
                "una manera de prevenir peores consecuencias. Una actitud sabia y conciliadora beneficiará a "
                "toda la comunidad."
            ),
            3: (
                "Seis en el tercer lugar significa: “Nutrirse a sí mismo en las antiguas virtudes induce a la "
                "Perseverancia. Peligro. Al final viene la buena fortuna. Si por azar está al servicio de un "
                "rey, no hay que buscar trabajos”.\n"
                "Se trata de una advertencia para no llamar al peligro que comporta la tendencia a la expansión. "
                "Sólo lo que ha sido honestamente adquirido resulta una posesión permanente. Es suficiente con "
                "cumplir con el trabajo asignado y dejar el honor a los otros."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Uno no puede comprometerse en el conflicto. Uno vuelve "
                "y se somete al destino, cambiando su propia actitud, y encuentra la paz en la perseverancia. Fortuna”.\n"
                "Se refiere a alguien cuya propia actitud es al comienzo falta de mesura. No está contento con "
                "su situación y quisiera mejorarla a través del conflicto. Pero no debe dejarse llevar a la lucha "
                "porque ella no justificará el conflicto frente a su conciencia. Esto trae buena fortuna."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Lidiar frente a él trae una gran fortuna”.\n"
                "El oráculo representa aquí al árbitro de un conflicto. Es alguien poderoso y justo que tiene el "
                "poder suficiente de conferir la fuerza al derecho. Se le puede confiar un asunto litigioso. "
                "Si alguien está en lo justo, encontrará allí la mejor fortuna."
            ),
            6: (
                "Nueve en la cima significa: “Si por casualidad un ceñidor de cuero le es regalado, al fin de "
                "la mañana le será arrebatado tres veces”.\n"
                "Aquí tenemos a alguien que condujo un conflicto a un final amargo y triunfó. Ganó una "
                "condecoración, pero no la felicidad. Es atacado una y otra vez y el resultado es un "
                "conflicto sin fin."
            )
        },
        "lineas": {
            1: "No proseguir el asunto.",
            2: "Retirada a tiempo.",
            3: "Nutrirse en antiguas virtudes.",
            4: "Volver y someterse al destino.",
            5: "Lidiar ante el árbitro justo.",
            6: "El ceñidor arrebatado."
        }
    },
    7: {
        "nombre": "SHIH / EL EJÉRCITO",
        "trigrama_sup": "K'un Lo Receptivo, Tierra.",
        "trigrama_inf": "K´an El Abismo, Agua.",
        "exposicion": (
            "El hexagrama está compuesto del trigrama K'an (el agua) y K'un (la tierra). "
            "Simboliza el agua que se acumula en el interior de la tierra, de la misma forma que la fuerza militar "
            "se sustenta en la masa del pueblo. Los atributos son el peligro al interior y al exterior "
            "la obediencia. La línea que controla el hexagrama es el nueve fuerte en el segundo lugar, "
            "que representa al hábil general que mantiene al ejército bajo su poder."
        ),
        "juicio": (
            "“El ejército necesita de la perseverancia y de un hombre fuerte. Fortuna sin reproches”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Un ejército es una masa que necesita organización. Sin una estricta disciplina nada puede lograrse, "
            "pero esta no debe sustentarse en la fuerza, sino en un hombre fuerte que gane los corazones del pueblo. "
            "La guerra es siempre peligrosa y debe usarse como una droga tóxica, sólo como último recurso. "
            "Solo con una causa justa y una meta clara explicada por un líder experimentado se alcanza la victoria."
        ),
        "imagen": (
            "“En el medio de la tierra está el agua: la imagen del Ejército. El hombre noble acrecienta su influjo "
            "por la generosidad hacia el Pueblo”.\n\n"
            "El agua es una presencia invisible sobre la tierra, igual que el poder militar en las masas. "
            "Solo un pueblo económicamente fuerte puede alcanzar el poder militar. Este poder debe cultivarse "
            "mejorando las condiciones de la gente con un gobierno humanitario."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Un ejército debe moverse en buen orden. Cuando el orden no es bueno, "
                "la mala fortuna acecha”.\n"
                "Al comienzo de una empresa militar el orden es imperativo. Debe existir una causa justa, "
                "obediencia y coordinación. Si no, el resultado inevitable es el fracaso."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Al centro del ejército. Buena fortuna. Sin reproches. "
                "El rey otorga una triple condecoración”.\n"
                "El líder debe estar al centro, en contacto con las masas que dirige. Necesita también "
                "el reconocimiento del gobernante. Las condecoraciones recibidas honran a todo el ejército a "
                "través de su persona."
            ),
            3: (
                "Seis en el tercer lugar significa: “Acaso el ejército transporte cadáveres en un carro. Mala fortuna”.\n"
                "Evoca el daño que resulta cuando otro se inmiscuye en el comando en lugar del jefe designado. "
                "Si el verdadero líder se eclipsa y el mando es ocupado por personas que interfieren o mucha gente "
                "asume el liderazgo, acarreará la desgracia."
            ),
            4: (
                "Seis en el cuarto lugar significa: “El ejército retrocede. Sin reproches”.\n"
                "Enfrentado a un enemigo superior, una retirada es el único procedimiento correcto para salvar "
                "al ejército del desastre. No es falta de coraje, sino prudencia ante una lucha sin esperanzas."
            ),
            5: (
                "Seis en el quinto lugar significa: “Hay caza en el campo. Es necesario que alguien los capture. "
                "Sin reproches. Que el más viejo conduzca el ejército y que los más jóvenes transporten los cadáveres. "
                "Aquí la perseverancia acarrea mala fortuna”.\n"
                "Se refiere a una invasión enemiga donde el combate se justifica. Pero la guerra debe ser dirigida "
                "por un líder experimentado (el más viejo). Si los jóvenes pelean solo por sí mismos o el mando degenera "
                "en confusión salvaje, llevará al infortunio."
            ),
            6: (
                "Seis en la cúspide significa: “El gran príncipe triunfa en el mando, funda estados, otorga feudos. "
                "No debe emplearse a la gente inferior”.\n"
                "La guerra terminó victoriosamente. El rey reparte premios. Es vital que la gente inferior no "
                "llegue al poder. Si ayudaron, se les debe pagar con dinero, pero no con tierras ni privilegios, "
                "porque abusarían del poder."
            )
        },
        "lineas": {
            1: "Moverse en buen orden.",
            2: "Al centro del ejército.",
            3: "Transporte de cadáveres.",
            4: "El ejército retrocede.",
            5: "El más viejo conduce.",
            6: "No emplear a gente inferior."
        }
    },
    8: {
        "nombre": "PI / LA SOLIDARIDAD (la Unión)",
        "trigrama_sup": "K'an El Abismo, Agua.",
        "trigrama_inf": "K'un Lo Receptivo, Tierra.",
        "exposicion": (
            "Las aguas en la superficie de la tierra reúnen sus cursos cada vez que pueden hacerlo, como por "
            "ejemplo en el mar, donde todos los ríos se reúnen. Hay allí el símbolo que traduce la solidaridad "
            "y su ley. La misma idea es evocada por el hecho de que todas las líneas son débiles hasta la 5ª, "
            "la del gobernante del hexagrama. Los débiles se reúnen para ayudarse mutuamente porque ellos están "
            "sometidos bajo la influencia de la voluntad firme en el lugar de la autoridad."
        ),
        "juicio": (
            "“La solidaridad trae buena fortuna. Pregunta otra vez al oráculo para saber si tienes la sublimidad, "
            "la constancia y la perseverancia. Entonces no hay reproches. Los inseguros se aproximan poco a poco. "
            "Quien viene demasiado tarde encuentra el infortunio”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Se trata de asociarse con otros con el fin de complementarse. Tal unión requiere un centro alrededor "
            "del cual uno se agrupa. Convertirse en un centro para la unión de los hombres es un asunto grave y "
            "de gran responsabilidad. Quien quiera reunir a los otros sin tener la aptitud y la vocación, causa "
            "más confusión que si no hubiera ninguna reunión. Los que lleguen demasiado tarde sufrirán por ello; "
            "se trata de una unión que debe realizarse en el tiempo oportuno."
        ),
        "imagen": (
            "“En la tierra está el agua: la imagen de la solidaridad. Los reyes de la antigüedad dividían los "
            "estados en feudos y cultivaban relaciones amistosas con los señores feudales”.\n\n"
            "El agua llena los espacios vacíos de la tierra y se adhiere fuertemente a ella. La organización "
            "social debe igualmente observar la unión gracias a una comunidad de intereses que hace que los "
            "diferentes individuos se sientan miembros de un todo. El poder central debe vigilar que cada miembro "
            "encuentre su verdadero interés en la unión."
        ),
        "lineas_detalle": {
            1: (
                "Seis al comienzo significa: “Sostenlo en la verdad y la lealtad: aquí no hay reproches. "
                "La verdad es como una escudilla de arcilla llena. Al final, la buena fortuna viene del exterior”.\n"
                "Cuando se trata de entablar relaciones la sinceridad es fundamental. Esta actitud, simbolizada "
                "por la escudilla de arcilla llena, muestra el importante valor del contenido contra la forma vacía. "
                "Esta firmeza es tan grande que puede atraer la fortuna de cualquier parte."
            ),
            2: (
                "Seis en el segundo lugar significa: “Sostenerlo interiormente. La perseverancia trae la fortuna”.\n"
                "Si alguien responde a los altos requerimientos que lo llaman a la acción, sus relaciones con los "
                "demás deben permanecer en el ámbito personal y así no se extraviará. El hombre noble conserva "
                "su dignidad y no se envilece."
            ),
            3: (
                "Seis en el tercer lugar significa: “Estás ligado con gente inconveniente”.\n"
                "A menudo nos mezclamos con gente que no corresponde a nuestra esfera. En ese caso hay que precaverse "
                "de no dejarse arrastrar a una falsa intimidad que nazca sólo del hábito. Mantener trato social "
                "sin intimidad es la única actitud correcta."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Tú también debes ligarte abiertamente a él. La perseverancia "
                "trae fortuna”.\n"
                "Aquí las relaciones con alguien que es el centro de interés ya están sólidamente establecidas. "
                "Además, aquí se puede y se debe mostrar abiertamente la dependencia. Solamente es necesario "
                "permanecer firme y no dejarse inducir al error por nada."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Manifestación de solidaridad. En las cacerías reales, "
                "el rey emplea batidores para acorralar la caza solo por tres lados y deja libre a la que huye "
                "por el frente. Los ciudadanos no necesitan advertencia. Fortuna”.\n"
                "Representa a un gobernante que atrae al pueblo. El que viene hacia él es recibido, y al que no "
                "viene se lo deja ir. No ruega ni halaga a nadie sino que deja la libertad de elección. "
                "Establece una libre subordinación. Si alguien cultiva en sí mismo la pureza necesaria, "
                "las personas que le están destinadas se acercan por ellas mismas."
            ),
            6: (
                "Seis en la cúspide significa: “No encuentra cabeza para la solidaridad. Infortunio”.\n"
                "La cabeza es el comienzo. Si el comienzo no es justo, no hay esperanzas de llegar a un final "
                "correcto. Si se pierde el momento apropiado para la unión y se vacila ante la perspectiva de "
                "una entrega de sí mismo verdadera, se lamentará el error cuando sea demasiado tarde."
            )
        },
        "lineas": {
            1: "Sinceridad como escudilla llena.",
            2: "Sostenerlo interiormente.",
            3: "Gente inconveniente.",
            4: "Ligarse abiertamente.",
            5: "La cacería por tres lados.",
            6: "Sin cabeza para la unión."
        }
    },
    9: {
        "nombre": "HSIAO CH'U / EL PODER DOMINANTE DE LO PEQUEÑO",
        "trigrama_sup": "Sun Lo Suave, Viento.",
        "trigrama_inf": "Ch'ien Lo Creativo, Cielo.",
        "exposicion": (
            "Este hexagrama representa la fuerza de lo pequeño: el poder de lo sombrío en cuanto algo que restringe, "
            "domestica y frena. La imagen es la del viento que sopla alto en el cielo. Retiene el creciente hálito "
            "creador, mueve las nubes, las hace más densas pero no lo suficiente para que se transformen en lluvia. "
            "Representa una constelación donde un elemento fuerte es por un cierto tiempo refrenado por un elemento "
            "débil. Sólo a través de la suavidad y de la gentileza puede tal situación ser acompañada por el éxito."
        ),
        "juicio": (
            "“El influyente poder domesticador de lo pequeño tiene éxito. Nubes densas, pero nada de lluvia "
            "para nuestra región del oeste”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La situación se compara con la China en los tiempos del rey Wen. La hora de una acción en gran escala "
            "todavía no ha llegado. Se pueden comenzar los trabajos de aproximación y empezar a tomar medidas "
            "preventivas. Solo se podrá actuar utilizando modestos medios de persuasión amistosa y sugestiones "
            "llenas de bondad. Necesitamos tener una firme determinación interior y adaptar nuestra acción "
            "exterior a una conducta suave."
        ),
        "imagen": (
            "“El viento ejerce su empuje alto en el cielo. La imagen del poder domesticador de lo pequeño. "
            "El hombre noble refina el aspecto visible de su naturaleza”.\n\n"
            "El viento puede empujar las nubes pero, no siendo más que aire, no puede producir efectos grandes "
            "y duraderos. En la época donde no es posible ejercer una acción poderosa, a uno no le queda más "
            "que refinar la expresión de su naturaleza efectuando cosas pequeñas y cumpliendo solo con detalles."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Vuelta al camino. ¿Cómo podríamos ser reprochados por esto? "
                "Buena fortuna”.\n"
                "Está en la naturaleza del hombre fuerte arremeter. Pero de esta manera se encuentran obstáculos. "
                "Entonces vuelve al camino normal, correspondiente a su situación, donde es libre de avanzar "
                "o retroceder. No pretender obtener algo por la fuerza es algo bueno e inteligente."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Él consiente en ser enviado de retorno. Buena fortuna”.\n"
                "Uno quiere arremeter, pero se da cuenta por el ejemplo de otras personas de la misma naturaleza "
                "que el camino está bloqueado. En este caso, un hombre razonable no se expondrá personalmente "
                "al rechazo, sino que se replegará con los demás. Esto trae buena fortuna."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Los rayos se desprenden de las ruedas del carro. "
                "Marido y mujer ponen los ojos en blanco”.\n"
                "Hay un intento de avanzar por la fuerza porque el obstáculo no parece todavía considerable. "
                "Pero este avance forzado está condenado al fracaso. El ser más fuerte no podrá utilizar su poder "
                "para ejercer una autoridad correcta a su alrededor. Experimenta un rechazo cuando esperaba una "
                "victoria fácil; esto compromete su dignidad."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Si eres sincero, la sangre y el temor se van. Sin reproches”.\n"
                "Si alguien se encuentra en la posición difícil de consejero de un hombre poderoso, debe restringirse. "
                "A sus lados hay un peligro tan inminente que acecha la posibilidad de un derramamiento de sangre. "
                "Sin embargo, el poder de la verdad desinteresada causa tal efecto que los esfuerzos consiguen "
                "felizmente obtener el éxito."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Si eres sincero y leal, eres rico en tus cercanías”.\n"
                "La lealtad crea lazos firmes. Esta manera mutua de completarse conduce a la verdadera riqueza que "
                "se manifiesta como algo que no se guarda para sí mismo con egoísmo, sino que se comparte con el "
                "prójimo. Placer compartido es doble placer."
            ),
            6: (
                "Nueve en la cima significa: “La lluvia llega, viene el reposo. Esto se debe al efecto duradero "
                "del carácter. La mujer se pone en peligro por la perseverancia. La luna está casi llena. "
                "Si el hombre noble insiste, llega el infortunio”.\n"
                "El éxito se ha obtenido. El empuje del viento ha hecho llover. Pero un tal éxito exige mucha "
                "prudencia; abandonarse a la ilusión de que será perdurable sería peligroso. El elemento débil "
                "que ganó la victoria no debe obstinarse ni sobreestimarse. Avanzar más todavía, antes que llegue "
                "la época apropiada, puede traer mala fortuna."
            )
        },
        "lineas": {
            1: "Vuelta al camino normal.",
            2: "Enviado de retorno.",
            3: "Los rayos se desprenden de las ruedas.",
            4: "La sangre y el temor se van.",
            5: "Sincero y leal, rico en cercanías.",
            6: "La lluvia llega, viene el reposo."
        }
    },
    10: {
        "nombre": "LÜ / LA MARCHA (La manera de conducirse)",
        "trigrama_sup": "Ch'ien Lo Creativo, Cielo.",
        "trigrama_inf": "Tui. La Alegría, Lago.",
        "exposicion": (
            "El nombre del hexagrama significa la manera correcta de conducirse. El trigrama superior, el cielo, "
            "simboliza el padre y el inferior, el lago, la hija más joven. Así está indicada la distinción entre "
            "lo superior y lo inferior y la manera en que ella aporta la tranquilidad cuando la conducta en la "
            "sociedad es correcta. Significa literalmente trillar, caminar sobre algo. Lo pequeño y feliz se apoya "
            "sobre lo grande y fuerte. Cuando lo débil se interpone a lo fuerte no es peligroso si ello ocurre con "
            "serenidad y sin arrogancia."
        ),
        "juicio": (
            "“Caminando sobre la cola de un tigre. Este no muerde al hombre. Éxito”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La situación es realmente difícil. El más fuerte y el más débil están estrechamente ligados. El débil "
            "molesta, pero el fuerte lo acepta y no lo hiere porque su conducta es alegre e inofensiva. "
            "Se trata de alguien tratando con gente inconsiderada e inaccesible. En tal caso se puede alcanzar la "
            "meta si uno observa buenos modales. Las buenas maneras y la conducta agradable conducen al éxito "
            "incluso cuando se trata con gente intratable."
        ),
        "imagen": (
            "“El cielo arriba, el lago abajo. La imagen de la marcha. El hombre noble discrimina entre lo superior "
            "y lo inferior y esto fortifica los pensamientos del pueblo”.\n\n"
            "El cielo y el lago muestran una diferencia de altura inherente a su propia naturaleza que no suscita "
            "envidia. Entre los hombres también se requieren estas diferencias. Es importante que las diferencias "
            "existentes no sean arbitrarias ni injustas; si corresponden a diferencias reales y auténticos valores "
            "personales, la gente las aceptará y el orden reinará."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Conducta simple. Progreso sin reproches”.\n"
                "Se presenta una situación donde todavía no estamos obligados a ningún intercambio social. "
                "Podemos seguir nuestras predilecciones sin pedir nada a nadie. Un hombre virtuoso prefiere "
                "conducirse con simplicidad y se contenta con los frutos de su trabajo."
            ),
            2: (
                "Nueve en el segundo lugar significa: “La senda despejada hace el camino fácil. La perseverancia "
                "de un hombre oscuro trae buena fortuna”.\n"
                "Se indica la situación de un sabio solitario que permanece apartado del torbellino de la vida. "
                "Confía en sí mismo y pasa por la vida inmutable, por un camino plano. Mientras esté contento "
                "y no trate de modificar el destino, permanecerá libre de complicaciones."
            ),
            3: (
                "Seis en el tercer lugar significa: “Un hombre tuerto puede ver; un cojo puede caminar. Tira de la "
                "cola a un tigre. El tigre muerde al hombre. Mala fortuna. Un acto heroico en defensa del gran príncipe”.\n"
                "Un tuerto ve, pero no tiene visión clara. Un cojo camina, pero no progresa bastante. Si alguien "
                "se considera fuerte a sí mismo a pesar de sus defectos y se expone al peligro, llama al desastre. "
                "Esta manera temeraria solo se justifica en el caso de un guerrero que defiende a su príncipe."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Tira la cola a un tigre. Precaución, circunspección llevan "
                "finalmente a la buena fortuna”.\n"
                "Se trata de una empresa peligrosa. La fuerza interior existe, pero debe estar acompañada por una "
                "actitud exterior de precaución vacilante en lo aparente. Se asegura el éxito final, que consiste "
                "en alcanzar la meta venciendo el peligro cuando se avanza con precaución."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Conducta resuelta. Perseverancia con conciencia del peligro”.\n"
                "Este trazo gobernante representa a alguien que tiene la necesidad de llevar una conducta resuelta. "
                "Pero al mismo tiempo es consciente del peligro que entraña su resolución. Esta conciencia del "
                "peligro hace posible el éxito."
            ),
            6: (
                "Nueve en la cima significa: “Observa tu conducta y considera los signos favorables. Cuando todo "
                "se cumple, llega la mejor fortuna”.\n"
                "La obra se ha terminado. Para saber si la consecuencia será afortunada deben observarse nuestras "
                "acciones anteriores; si tuvieron buenos efectos, la buena fortuna está asegurada. Solo por el "
                "resultado de sus actos el hombre puede discernir lo que puede esperar."
            )
        },
        "lineas": {
            1: "Conducta simple y simplicidad.",
            2: "El camino del sabio solitario.",
            3: "El tuerto y el cojo (temeridad).",
            4: "Precaución ante el tigre.",
            5: "Resolución con conciencia del peligro.",
            6: "Observar los efectos de los actos."
        }
    },
    11: {
        "nombre": "T'AI / LA PAZ",
        "trigrama_sup": "K'un Lo Receptivo, Tierra.",
        "trigrama_inf": "Ch'ien Lo Creativo, Cielo.",
        "exposicion": (
            "Lo receptivo (K'un), cuyo movimiento está dirigido hacia abajo, está arriba; lo creativo (Ch'ien), "
            "cuyo movimiento tiende hacia arriba, está abajo. Las influencias de ambos trigramas están en armonía, "
            "de manera que todas las cosas brotan y prosperan. Este hexagrama está asociado al primer mes "
            "(febrero-marzo), cuando las potentes energías de la naturaleza preparan la nueva primavera."
        ),
        "juicio": (
            "“Paz. Lo pequeño se va y viene lo grande. Buena fortuna. Éxito”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Indica una era donde el cielo está bajo la tierra, uniendo sus virtudes en una armonía íntima. "
            "En el mundo de los hombres es una época de concordia social: los grandes se rebajan hacia los humildes, "
            "mientras los pequeños nutren sentimientos amistosos hacia los grandes. Al interior se encuentra "
            "el elemento luminoso (2ª línea gobernante) y el oscuro al exterior. Cuando los buenos tienen "
            "las riendas del poder, los malos pasan bajo su influencia y se mejoran."
        ),
        "imagen": (
            "“Cielo y tierra unidos; la imagen de la paz. El gobernante divide y completa el curso del cielo y de la tierra; "
            "proporciona y regula los dones del cielo y de la tierra y así ayuda al pueblo”.\n\n"
            "Se trata de una época de prosperidad general que debe ser regulada por un gobernante apropiado para "
            "aprovecharla lo más posible. El tiempo se divide en estaciones y el espacio en puntos cardinales "
            "por obra humana para acrecentar el rendimiento natural."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Cuando se tira del pasto, la tierra también sale. Cada uno de acuerdo "
                "a su naturaleza. Emprender trae buena fortuna”.\n"
                "En tiempos de prosperidad, todo hombre valioso atrae hacia él a personas que comparten sus sentimientos. "
                "Al igual que al arrancar una rama de pasto vienen con ella las raíces mezcladas, el propósito de un hombre "
                "valioso debe ser emprender la obra para la cual está capacitado."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Soportar con tolerancia a los groseros, atravesar resueltamente el río, "
                "no descuidar lo que está distante y no tener en cuenta sus acompañantes. Así se consigue marchar por el medio”.\n"
                "Es necesario un carácter hábil para tratar con toda la gente. Debemos estar dispuestos a emprender tareas "
                "peligrosas y prestar atención a lo alejado, evitando facciones y camarillas para encontrar el justo medio."
            ),
            3: (
                "Nueve en el tercer lugar significa: “No hay llanura que no sea seguida de una cuesta, ni de ida que no sea "
                "seguida de un retorno. Sin reproches para quien permanezca constante en el peligro. No te desconsueles frente "
                "a esa verdad, aprovecha de la felicidad que todavía posees”.\n"
                "Todo lo terreno está sometido al cambio; la prosperidad es seguida por la decadencia. Esta convicción "
                "permite no ilusionarse en las épocas favorables. Mientras el hombre noble sea interiormente superior al destino, "
                "la fortuna no lo abandonará."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Se rebaja agitando las alas sin jactarse de su riqueza, en comunidad "
                "con su vecino, cándido y sincero”.\n"
                "Cuando existe confianza mutua, los superiores devienen simples y se comunican con los inferiores sin jactancia. "
                "Este contacto es espontáneo y basado en una convicción profunda."
            ),
            5: (
                "Seis en el quinto lugar significa: “El soberano Yi da su hija en matrimonio. Esto es beneficioso y aporta "
                "fortuna suprema”.\n"
                "El soberano Yi (T'ang) decretó que las princesas, aunque superiores por rango, debían obedecer a sus esposos. "
                "Hay aquí una alusión a la unión con modestia de lo alto con lo bajo, lo cual trae la máxima fortuna."
            ),
            6: (
                "Seis en la cima significa: “La muralla se cayó en el foso. No usar las armas ahora. Proclama tus órdenes "
                "en tu propia ciudad. La perseverancia trae humillación”.\n"
                "El cambio anunciado en el trazo 3 ha comenzado; la fatalidad se abate. Debemos someternos al destino "
                "y no oponer resistencia violenta. El único recurso es mantenerse en el círculo más estrecho; tratar de eludir "
                "el daño por medios habituales llevará al colapso y la humillación."
            )
        },
        "lineas": {
            1: "Emprender en compañía.",
            2: "El justo medio y tolerancia.",
            3: "La ley del cambio eterno.",
            4: "Unión sincera sin jactancia.",
            5: "Unión con modestia.",
            6: "Someterse al destino."
        }
    },
    12: {
        "nombre": "P'I / LA ESTAGNACIÓN (La inmovilidad)",
        "trigrama_sup": "Ch'ien Lo Creativo, Cielo.",
        "trigrama_inf": "K'un Lo Receptivo, Tierra.",
        "exposicion": (
            "Este hexagrama es el opuesto del anterior. El cielo, en lo alto, se retira cada vez más y la tierra "
            "se hunde sin cesar. Las fuerzas creadoras no tienen relaciones mutuas. Es el tiempo de la estagnación "
            "y de la decadencia. El hexagrama está ligado al 7º mes (agosto-septiembre), periodo en el cual el año "
            "ha pasado su punto culminante y se marchita con la llegada del otoño."
        ),
        "juicio": (
            "“La estagnación. La mala gente no favorece la perseverancia del hombre noble. Lo grande se va y viene "
            "lo pequeño”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Cielo y tierra ya no se comunican y todas las cosas se paralizan. La confusión y el desorden prevalecen. "
            "La oscuridad está adentro y la luz afuera; en el interior reina la debilidad y en el exterior la dureza. "
            "Adentro está lo vulgar y afuera la nobleza. Si el hombre noble ya no tiene posibilidad de actuar, debe "
            "permanecer fiel a sus principios y retirarse discretamente."
        ),
        "imagen": (
            "“Cielo y tierra no están unidos. La imagen de la estagnación. El hombre noble se retira en su fuero "
            "interior para escapar de las dificultades. No permite que se lo gratifique con sobornos”.\n\n"
            "Cuando reina la influencia de los hombres inferiores, la actividad fructífera se hace imposible. "
            "El hombre noble no se deja seducir por proposiciones brillantes que lo invitan a participar en la vida pública. "
            "Debe ocultar sus méritos y retirarse en secreto."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Cuando se tira del pasto, la tierra sale con él. Cada uno de acuerdo "
                "a su naturaleza. La perseverancia trae buena fortuna y éxito”.\n"
                "A diferencia del hexagrama 11, aquí el hombre insta a los otros a retirarse con él de la vida pública. "
                "Solo el retiro oportuno puede librarnos de la humillación. El éxito es saber salvaguardar nuestra "
                "personalidad y poner al abrigo nuestros valores."
            ),
            2: (
                "Seis en el segundo lugar significa: “Ellos toleran y soportan; esto significa buena fortuna para "
                "la gente inferior. La estagnación sirve al gran hombre para obtener el éxito”.\n"
                "Los inferiores están dispuestos a halagar de manera servil. Pero el gran hombre soporta tranquilamente "
                "las consecuencias de la estagnación. No debe mezclarse con la gente vulgar porque ese no es su lugar. "
                "Aceptando sufrir personalmente, asegura el éxito de sus principios."
            ),
            3: (
                "Seis en el tercer lugar significa: “Ellos sienten vergüenza”.\n"
                "La gente inferior, cuando llega al poder ilegítimamente, no se siente igual frente a las responsabilidades. "
                "Comienza a sentirse humillada, lo cual marca un cambio ventajoso."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Aquel que actúa al mando de lo más elevado permanece sin reproches. "
                "Aquellos que se le impongan toman parte de la herida”.\n"
                "El tiempo de la estagnación está a punto de terminar. Quien está en los puestos de comando permanece "
                "sin reproches. Solo el hombre con las condiciones necesarias para la época puede asumir la tarea."
            ),
            5: (
                "Nueve en el quinto lugar significa: “La estagnación va yéndose. Buena fortuna para el gran hombre. "
                "¿Y si él fracasa? En el camino puede enredarse en una mata de moras”.\n"
                "El hombre apto para resolver el desorden ha llegado. El éxito se asegura solo con grandes precauciones. "
                "Confucio dice: “El peligro reside allí donde se siente seguro”. No debe olvidarse del peligro cuando "
                "está seguro para afirmar sin cesar la estabilidad del Imperio."
            ),
            6: (
                "Nueve en la cima significa: “La estagnación termina. Ponerse de pie, buena fortuna”.\n"
                "La estagnación no dura para siempre, pero requiere la intervención de alguien capaz de ponerle término. "
                "La paz, si se libra a sí misma, se transforma en estagnación; esta última requiere esfuerzos múltiples "
                "para volver a la prosperidad. Se pone de relieve la actitud creativa del hombre que puede poner "
                "el mundo en orden."
            )
        },
        "lineas": {
            1: "Retiro oportuno con otros.",
            2: "Soportar sin mezclarse con lo vulgar.",
            3: "Vergüenza en los inferiores.",
            4: "Actuar bajo el mando elevado.",
            5: "Vigilancia constante ante el riesgo.",
            6: "Intervención para terminar el desorden."
        }
    },
    13: {
        "nombre": "T'UNG JÊN / LA COMUNIDAD CON LOS HOMBRES (La alianza)",
        "trigrama_sup": "Ch'ien Lo Creativo, Cielo.",
        "trigrama_inf": "Li. Lo Oscilante, Fuego.",
        "exposicion": (
            "La imagen del trigrama superior Ch'ien es el cielo y la del trigrama inferior Li es el fuego. "
            "La naturaleza del fuego es elevarse flameante hacia el cielo. Así está evocada la idea de la "
            "comunidad. El segundo trazo débil, por su posición central reúne entorno de él las cinco líneas "
            "fuertes. Este hexagrama es el opuesto al Nº 7, el ejército. Aquí, la claridad interior caracteriza "
            "la unidad pacífica entre los hombres, que necesita, para ser mantenida, de un único trazo débil "
            "entre múltiples trazos fuertes. No hay en el hexagrama ningún otro signo de debilidad, sino una "
            "unión pacífica entre personas fuertes."
        ),
        "juicio": (
            "“La comunidad con los hombres en pleno día. Éxito. Es ventajoso atravesar la gran corriente. "
            "La perseverancia del hombre es ventajosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La verdadera comunidad debe basarse en intereses universales, no en objetivos egoístas. "
            "Cuando reina la concordia, pueden ser llevadas a cabo con éxito las empresas difíciles como "
            "atravesar la gran corriente. Se requiere un líder iluminado con convicciones definidas y "
            "entusiastas. El trigrama inferior tiene el sentido de claridad y el superior el sentido de "
            "la fuerza creadora."
        ),
        "imagen": (
            "“El cielo junto con el fuego: la imagen de la comunidad con los hombres. Así el hombre noble "
            "organiza la división en grupos y establece las distinciones entre las cosas”.\n\n"
            "El cielo y el fuego se mueven en la misma dirección y sin embargo son distintos. La comunidad "
            "humana no debe ser una pura mezcla espontánea —sino ella sería un caos— sino que requiere una "
            "organización dentro de la diversidad."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Comunidad de los hombres en la puerta. Sin reproches”.\n"
                "La comunidad debe comenzar delante de la puerta; allí todos son iguales y próximos entre sí. "
                "Los fundamentos deben ser accesibles por igual a todos los participantes. Los acuerdos "
                "secretos traen mala fortuna."
            ),
            2: (
                "Seis en el segundo lugar significa: “Comunidad de los hombres en el clan. Humillación”.\n"
                "El peligro reside en la formación de facciones separadas (clanes cerrados) en que predominan "
                "los intereses personales. Estos fraccionamientos motivan a los excluidos a aliarse con otros "
                "grupos y al final todos se condenan a la humillación."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Esconde armas en la entrada. Trepa sobre la alta montaña "
                "del frente. Durante tres años él no se levanta”.\n"
                "La comunidad se transformó en desconfianza. Se desconfía del otro y se preparan emboscadas. "
                "Cada uno tiene sus propias intenciones y reservas. Mientras más se mantenga esta situación, "
                "la verdadera comunidad se alejará más y más."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Trepa sobre la muralla. No puede acometer. Buena fortuna”.\n"
                "Se aproxima la reconciliación después de la discordia. Aunque todavía hay murallas que separan, "
                "usando el buen sentido uno considera que luchar no es razonable y allí reside la buena fortuna."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Al comienzo los hombres reunidos en comunidad lloran y "
                "se lamentan pero después ríen. Al cabo de grandes conflictos, ellos logran reencontrarse”.\n"
                "Ciertas personas pueden estar separadas exteriormente pero sus corazones están unidos. Si se "
                "mantienen fieles a sí mismos podrán superar los obstáculos. Confucio dice que cuando dos "
                "personas se comprenden en la intimidad del corazón, sus palabras son dulces y fuertes como "
                "el perfume de orquídea."
            ),
            6: (
                "Nueve en la cima significa: “Comunidad con los hombres en el desdeño. Sin reproches”.\n"
                "Aquí falta el cálido lazo afectivo. Uno está fuera de la comunidad pero hace alianza con ellos. "
                "La comunidad aquí no comprende a todos sino solo a aquellos que se reúnen en el exterior. "
                "Uno se une a la empresa, pero excluyendo las aspiraciones especiales."
            )
        },
        "lineas": {
            1: "Comunidad en la puerta (igualdad).",
            2: "Comunidad en el clan (facciones).",
            3: "Desconfianza y armas escondidas.",
            4: "Reconciliación y buen sentido.",
            5: "Unión de corazones tras el conflicto.",
            6: "Alianza externa sin lazo afectivo."
        }
    },
    14: {
        "nombre": "TA YU / LA POSESIÓN DE LO GRANDE (El gran haber)",
        "trigrama_sup": "Li Lo Oscilante, Llama",
        "trigrama_inf": "Ch'ien Lo Creativo, Cielo.",
        "exposicion": (
            "La llama en el cielo ilumina todo y todas las cosas se manifiestan bajo su luz. La 5ª línea débil "
            "está en el lugar de honor y todas las líneas fuertes están en armonía con ella. Aquél que, "
            "ocupando un alto puesto es humilde y moderado, ve todas las cosas venir hacia él. (El sentido "
            "de este hexagrama coincide con las palabras de Jesús: “Bienaventurados los mansos porque ellos "
            "heredarán la Tierra”.)"
        ),
        "juicio": (
            "“Posesión en gran medida. Éxito sublime”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Los dos trigramas indican que la fuerza y la claridad se unen. El gran haber es determinado por "
            "el destino y corresponde a la época. La virtud de una modestia excepcional contribuye al poder "
            "de mantener juntas las líneas fuertes. Fuerza al interior, claridad y cultura al exterior; el poder "
            "se exterioriza con fineza y dominio de sí mismo. A diferencia del Nº 8, aquí el jefe benévolo "
            "tiene cerca de él hombres robustos y hábiles."
        ),
        "imagen": (
            "“Fuego alto en el cielo. La imagen de la posesión de lo grande. Así el hombre noble reprime el mal "
            "y favorece el bien y obedece de esa manera a la benevolente voluntad del cielo”.\n\n"
            "El sol iluminando todas las cosas terrestres es la imagen de la posesión de lo grande. "
            "Esta posesión debe ser administrada apropiadamente: el hombre debe reprimir el mal y promover el bien "
            "para estar conforme a la voluntad divina."
        ),
        "lineas_detalle": {
            1: (
                "Nueve al comienzo significa: “No relacionarse con lo dañino. No hay reproches por ello. "
                "Si uno permanece consciente de las dificultades permanecerá sin reproches”.\n"
                "La gran posesión se encuentra en sus comienzos. Solo mientras se esté consciente de las "
                "dificultades puede mantenerse libre de arrogancia y prodigalidad."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Hay un gran carro a cargar. Podemos emprender algo. "
                "Sin reproches”.\n"
                "La gran posesión consiste sobre todo en su movilidad y disponibilidad. Con la imagen del gran carro "
                "se interpreta que tendremos auxiliares eficaces a la altura de la tarea para llevar a cabo "
                "empresas importantes."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Un príncipe lo ofrece al Hijo del Cielo. Un hombre pequeño "
                "no puede hacerlo”.\n"
                "Un hombre generoso no considera sus bienes como propiedad exclusivamente personal, sino que los pone "
                "a disposición de la colectividad. El hombre pequeño es incapaz de esto porque pretende conservarlo "
                "con gran sacrificio."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Hace diferencia entre él y el prójimo. Sin reproches”.\n"
                "Caracteriza la situación entre vecinos ricos y poderosos. Es conveniente no mirar a los lados para evitar "
                "la envidia y la competencia; no depender de su riqueza para permanecer libre de errores."
            ),
            5: (
                "Seis en el quinto lugar significa: “Aquél cuya verdad sea accesible y sin embargo, digna, "
                "tiene buena fortuna”.\n"
                "Se concilia con la gente por una sinceridad sin afectación. Pero en los tiempos de gran posesión, "
                "la simple benevolencia no es suficiente; la insolencia debe contenerse con dignidad para asegurar "
                "la fortuna."
            ),
            6: (
                "Nueve en la cima significa: “Está bendecido por el cielo. Fortuna. Todo es ventajoso”.\n"
                "En la abundancia, se permanece modesto y se venera al sabio retirado. Confucio dijo: “Bendecir "
                "significa ayudar. El cielo ayuda al ser abandonado (que no opone resistencia a los designios divinos) "
                "y los hombres ayudan al ser sincero”."
            )
        },
        "lineas": {
            1: "Conciencia de la dificultad para evitar la arrogancia.",
            2: "Movilidad y auxiliares eficaces (el gran carro).",
            3: "Generosidad y desapego de la propiedad privada.",
            4: "Evitar la envidia y la competencia con los poderosos.",
            5: "Sinceridad unida a la dignidad para evitar la insolencia.",
            6: "Modestia en el apogeo bajo la bendición del cielo."
        }
    },
    15: {
        "nombre": "CH'IEN / LA HUMILDAD (La modestia)",
        "trigrama_sup": "K'un Lo Receptivo, Tierra",
        "trigrama_inf": "Ken, La Inmovilidad, la Montaña.",
        "exposicion": (
            "Este hexagrama está compuesto de Ken, “lo inmóvil, la montaña” y de K'un “lo receptivo, la tierra”. "
            "La montaña es el hijo más joven del Creador, representación del cielo sobre la tierra. Dispensa en sus "
            "pies las bendiciones del cielo. Eso indica la modestia y sus efectos en los hombres fuertes y nobles. "
            "Muestra cómo la humildad que los rodea puede iluminarlos y a la vez elevar a los más modestos. La propiedad "
            "de la tierra es la bajura, pero aquí está elevada sobre la montaña, lo que muestra el efecto de la "
            "humildad en los hombres simples: ellos se elevan por este hecho."
        ),
        "juicio": (
            "“La modestia trae el éxito. El hombre noble lleva a buen fin sus asuntos”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La ley del cielo vacía lo que está lleno y colma lo que es humilde. Cuando el sol está en lo más alto, "
            "debe declinar; la luna mengua cuando está llena. Esta ley celeste actúa igualmente en los destinos humanos. "
            "La ley de la tierra es fluir hacia lo humilde. Los destinos siguen leyes fijas: prosperan los modestos y "
            "declinan los poderosos. El hombre puede escapar a su destino modificando su conducta; si llega a una "
            "alta posición y permanece modesto, brilla con la luz de la sabiduría."
        ),
        "imagen": (
            "“Sobre la tierra, una montaña: La imagen de la modestia. El hombre noble reduce sus deseos cuando "
            "son excesivos y los aumenta cuando son muy pequeños. Pesa las cosas y las equilibra”.\n\n"
            "La riqueza escondida en una montaña no es visible porque está oculta en las profundidades. "
            "Así, la altura y la profundidad se completan y el resultado es el suelo plano. El hombre noble, "
            "cuando establece el orden en el mundo, iguala los extremos que pueden ser causa de descontento "
            "social y crea condiciones justas y equitativas."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “El hombre noble, modesto en su humildad, puede cruzar la gran "
                "corriente. Buena fortuna”.\n"
                "Una empresa peligrosa puede dificultarse por un exceso de precauciones. La tarea se facilita "
                "si se lo hace de manera simple y rápida. La actitud sin pretensiones permite llevar a cabo "
                "las empresas más difíciles porque donde no hay pretensiones tampoco hay resistencias."
            ),
            2: (
                "Seis en el segundo lugar significa: “Humildad manifiesta. La perseverancia trae buena fortuna. "
                "La boca habla de la abundancia del corazón”.\n"
                "Si alguien es interiormente tan modesto que su disposición se manifiesta en su conducta exterior, "
                "eso le causa buena fortuna. De esa actitud nace la posibilidad de ejercer una influencia "
                "perdurable que nadie podrá impedir."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Un hombre noble y humilde en su mérito lleva las cosas "
                "a su conclusión. Fortuna”.\n"
                "El centro del signo indica lo que se mantiene en secreto. Si uno se deja deslumbrar por la gloria, "
                "las críticas no tardan en nacer. Si por el contrario se permanece modesto a pesar de sus méritos, "
                "uno se hace apreciar y se conseguirán los apoyos indispensables para la obra."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Nada que no sea ventajoso puede detener la modestia en "
                "movimiento”.\n"
                "Incluso la modestia a veces puede ser excesiva. Aquí ella está en marcha pues hay un colaborador "
                "meritorio y un gobernante benévolo que soportan una gran responsabilidad. La humildad aquí se "
                "manifiesta en la eficacia con la cual se realiza el trabajo, sin menospreciar el mérito."
            ),
            5: (
                "Seis en el quinto lugar significa: “No hacer alarde de la riqueza delante del vecino. Favorece "
                "atacar con fuerza. Nada que no sea ventajoso”.\n"
                "La modestia no debe confundirse con la bondad débil. En ciertas circunstancias se debe saber "
                "actuar con energía. Las medidas a tomar deben ser puramente objetivas sin herir la susceptibilidad "
                "de las otras personas. La humildad también debe manifestarse en la severidad."
            ),
            6: (
                "Seis en la cima significa: “La humildad que se exterioriza. Es favorable poner en marcha los "
                "ejércitos para castigar a la propia ciudad y al propio país”.\n"
                "Quien sea consecuente con su humildad debe estar atento a que ella se manifieste actuando "
                "enérgicamente en ese dominio. No se cumplirá una obra importante si no se tiene el coraje "
                "de poner en marcha los ejércitos contra sí mismo para corregir las faltas."
            )
        },
        "lineas": {
            1: "Cruzar la gran corriente con simplicidad y sin pretensiones.",
            2: "Influencia perdurable a través de la modestia manifiesta.",
            3: "Conclusión de la obra gracias al mérito mantenido en secreto.",
            4: "Modestia expresada a través de la eficacia y responsabilidad.",
            5: "Uso de la energía y severidad objetiva sin alarde de poder.",
            6: "Autocorrección y firmeza para imponer el orden interno."
        }
    },
    16: {
        "nombre": "YÜ / EL ENTUSIASMO",
        "trigrama_sup": "Chen, Lo que despierta, Trueno",
        "trigrama_inf": "K'un. Lo Receptivo, Tierra",
        "exposicion": (
            "El trazo fuerte en el cuarto lugar, el puesto de los altos funcionarios, encuentra en todos los "
            "otros trazos, que son débiles, la cortesía y la obediencia. El trigrama superior, Chen, tiene "
            "la propiedad del movimiento; el inferior, K’un, la obediencia y la devoción. El hexagrama "
            "muestra el comienzo de un movimiento que se enfrenta con una actitud de devoción y despierta "
            "actos de inspiración y entusiasmo. Representa una ley importante: el movimiento debe "
            "efectuarse siguiendo la línea de la menor resistencia."
        ),
        "juicio": (
            "“El entusiasmo. Es favorable enrolar auxiliares y poner en marcha los ejércitos”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El tiempo del entusiasmo llega con la presencia de un hombre notable en simpatía con el alma del "
            "pueblo. Para despertar el entusiasmo es necesario acordar las órdenes que uno imparte con la "
            "naturaleza de los gobernados. Solo son ejecutadas las leyes que se enraízan en el sentimiento "
            "popular. El entusiasmo permite enrolar auxiliares para efectuar el trabajo sin temer a oposiciones "
            "secretas y uniformizar movimientos de masas para obtener la victoria."
        ),
        "imagen": (
            "“El trueno sale resonando de la tierra: la imagen de entusiasmo. Así, los antiguos reyes hacían "
            "música en honor de los méritos, y los presentaban con magnificencia ante el Dios supremo, "
            "invitando a sus antepasados”.\n\n"
            "El entusiasmo del corazón se expresa espontáneamente en el sonido, la danza y el movimiento. "
            "La música fue considerada algo sagrado para purificar los sentimientos de la gente y establecer un "
            "vínculo con el mundo invisible. Vinculando el propio pasado con la divinidad en momentos de "
            "entusiasmo religioso, se establecía la unión entre Dios y la humanidad."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “El entusiasmo que se expresa, trae desgracia”.\n"
                "Alguien en posición subordinada que se jacta con entusiasmo por sus relaciones distinguidas. "
                "Esta arrogancia atrae fatalmente el desastre. El entusiasmo no debe ser un sentimiento "
                "egoísta, sino uno general que nos comunique con los otros."
            ),
            2: (
                "Seis en el segundo lugar significa: “Sólido como una roca. No es un día entero. La "
                "perseverancia trae buena fortuna”.\n"
                "Alude a quien no se deja engañar por ilusiones y reconoce con claridad los primeros signos de la "
                "época. Sabe retirarse en el momento oportuno ante el primer indicio de desacuerdo. "
                "Confucio dice: “Conocer los gérmenes es algo divino”. El hombre noble conoce lo oculto "
                "y lo visible, lo débil y lo fuerte."
            ),
            3: (
                "Seis en el tercer lugar significa: “Un entusiasmo que mira hacia arriba trae remordimiento. "
                "Las dudas crean remordimiento”.\n"
                "Aquí hay una mirada entusiasta hacia arriba que carece de autonomía. Si se duda demasiado "
                "se crea el remordimiento. Hay que discernir el momento más oportuno para actuar y "
                "hacerlo; es la única manera justa de proceder."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La fuente del entusiasmo. El logró grandes cosas. "
                "No dudes. Reúnes amigos en tu alrededor como un pasador sujeta los cabellos”.\n"
                "Alguien capaz de despertar entusiasmo por su seguridad y libertad de pensamiento. "
                "Suscita confianza y gana a los hombres para una colaboración entusiasta. Une a la "
                "gente por el apoyo que le brinda, como un pasador une los cabellos."
            ),
            5: (
                "Seis en el quinto lugar significa: “Permanentemente enfermo, todavía no llega a morir”.\n"
                "El entusiasmo aquí está obstruido por una presión constante que no permite actuar con libertad. "
                "Sin embargo, esta presión tiene la ventaja de prevenir que uno sea consumido por un entusiasmo "
                "vacío. Sirve para mantenerse vivo."
            ),
            6: (
                "Seis en la cima significa: “Entusiasmo enceguecido. Pero si se cambia después de que se haya "
                "alcanzado el fin, entonces no habrá reproches”.\n"
                "Dejarse enceguecer por el entusiasmo es malo, pero si después de consumarse esta torpeza todavía "
                "se puede cambiar, no habrá reproches. Recuperarse de un falso entusiasmo es posible y "
                "muy favorable."
            )
        },
        "lineas": {
            1: "Arrogancia y entusiasmo egoísta que atraen el desastre.",
            2: "Claridad para reconocer los gérmenes de los hechos y actuar a tiempo.",
            3: "Duda y dependencia de otros que generan remordimiento.",
            4: "Líder que inspira confianza y reúne colaboradores.",
            5: "Entusiasmo obstruido por presión constante que evita el vacío.",
            6: "Posibilidad de corregir un entusiasmo enceguecido tras el error."
        }
    },
    17: {
        "nombre": "SUI / LA SUCESIÓN (Lo Siguiente, el Séquito)",
        "trigrama_sup": "Tui, Lo Alegre, el Lago",
        "trigrama_inf": "Chen, Lo que Despierta, Trueno.",
        "exposicion": (
            "Arriba está lo feliz cuyo carácter es la alegría; abajo está lo que despierta, cuyo carácter "
            "es el movimiento. La alegría unida al movimiento llama a seguirla. Lo alegre es la hija menor, "
            "lo que despierta es el hijo mayor. Un hombre de cierta edad se inclina ante la joven y le muestra "
            "su consideración y respeto. De esta manera él es tan conmovedor que ella lo sigue."
        ),
        "juicio": (
            "“La sucesión logra un éxito sublime. La perseverancia es ventajosa. Sin reproches”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Para hacerse un séquito uno debe primero saberse adaptar. Es solamente sirviendo que uno llega "
            "a mandar, obteniendo el consentimiento satisfactorio de los que siguen. No debemos forzar a los "
            "otros, sino que ellos deben venir espontáneamente. La idea de crearse un séquito adaptándose a las "
            "exigencias de la hora es grande e importante; por eso el juicio es tan favorable."
        ),
        "imagen": (
            "“El lago está en el medio del trueno: imagen la sucesión. Así, al anochecer el sabio entra para "
            "recrearse y reposar”.\n\n"
            "En el otoño la electricidad vuelve a la tierra para descansar. No es el trueno en movimiento, "
            "sino en su reposo invernal. El séquito se muestra aquí como una adaptación a las exigencias del tiempo. "
            "Una situación solo puede hacerse buena si uno se sabe adaptar y si uno no se desgasta en una "
            "resistencia desplazada."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Las normas cambian. La Perseverancia trae buena fortuna. Salir "
                "a la puerta produce obras”.\n"
                "Existen situaciones excepcionales donde la actitud del guía se modifica. Aquél que quiere "
                "dirigir debe permanecer accesible y dejarse influenciar por las opiniones de sus subordinados. "
                "Al estar dispuesto a escuchar a los demás, se debe salir a la puerta y tratar con toda clase "
                "de personas para llevar la obra a bien fin."
            ),
            2: (
                "Seis en el segundo lugar significa: “Si alguien se adhiere a un niño, pierde al hombre fuerte”.\n"
                "En las relaciones estrechas, el individuo debe elegir cuidadosamente. Si se envilece con los "
                "indignos, se pierde la unión con los hombres de gran valor espiritual, los únicos cuya "
                "influencia es provechosa para hacer lo bueno."
            ),
            3: (
                "Seis en el tercer lugar significa: “Si uno se aferra a un hombre fuerte, se pierde el niño. "
                "Siguiendo se encuentra lo que se busca. Es ventajoso permanecer perseverante”.\n"
                "Cuando se establece la conexión correcta con la gente importante, eso provoca una cierta pérdida "
                "de seres inferiores y superficiales. Uno se siente satisfecho interiormente porque tiene lo "
                "que es necesario para el desarrollo personal, siempre que permanezca firme."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Siguiendo se obtiene el éxito. La perseverancia trae "
                "desgracia. Recorrer el camino con la verdad aporta claridad. ¿Cómo se podría reprochar?”\n"
                "Sucede a menudo que uno obtiene seguidores siendo condescendiente con los inferiores por "
                "beneficio personal. Si uno se acostumbra a la adulación, eso trae infortunio. Solo siendo "
                "sincero y libre de egoísmo se tiene la claridad necesaria para distinguir a la gente."
            ),
            5: (
                "Nueve en el quinto lugar significa: “La verdad en el bien. ¡Fortuna!”\n"
                "Cada hombre debe tener algo para seguir que le sirva como una estrella guía. Los que persiguen "
                "con convicción la belleza y la bondad podrán sentirse fortalecidos por estas palabras."
            ),
            6: (
                "Seis en la cima significa: “Se encuentra una firme lealtad y todavía se sobrepasan los límites. "
                "El rey lo presenta a la Montaña del Oeste”.\n"
                "Se alude a un sabio que ha dejado las agitaciones del mundo, pero encuentra a un seguidor que lo "
                "comprende y no lo deja retirarse. Así, regresa al mundo y ayuda al otro, creando una conexión "
                "eterna. Compartía entonces el destino de la dinastía gobernante."
            )
        },
        "lineas": {
            1: "Adaptación y apertura a las opiniones de los subordinados.",
            2: "Elección cuidadosa de compañías para no perder el valor espiritual.",
            3: "Vínculo con lo superior que implica abandonar lo inferior.",
            4: "Evitar la adulación y el éxito basado en motivos egoístas.",
            5: "Seguir con convicción un ideal de belleza y bondad.",
            6: "Lealtad suprema que une al sabio con el mundo por el bien común."
        }
    },
    18: {
        "nombre": "KU / EL TRABAJO SOBRE LO CORRUPTO (La Reparación)",
        "trigrama_sup": "Ken, La Inmovilidad, la Montaña.",
        "trigrama_inf": "Sun, La docilidad, Viento",
        "exposicion": (
            "El carácter chino Ku representa un plato en cuyo contenido crecen los gusanos. Es la "
            "representación de lo que se ha corrompido debido a que la dócil indiferencia del trigrama inferior "
            "se unió estrechamente a la rígida inercia del superior, degenerando en estancación. "
            "Puesto que existe un estado de cosas que deja que desear, la situación contiene al mismo tiempo "
            "lo necesario para terminarla. El hexagrama significa el trabajo sobre lo corrupto como una tarea."
        ),
        "juicio": (
            "“Trabajar en lo que está corrompido tiene un sublime éxito. Es conveniente atravesar la gran "
            "corriente. Antes del punto de partida, tres días. Después del punto de partida, tres días”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Lo que se corrompe por culpa de los hombres puede repararse con el trabajo de los hombres; no es un "
            "destino inexorable. El éxito requiere una justa reflexión previa para conocer las causas "
            "antes de remediarla (antes de la partida) y vigilancia posterior para evitar recaídas (después de la "
            "partida). La resolución y energía deben sustituir a la indiferencia e inercia."
        ),
        "imagen": (
            "“El viento sopla al pie la montaña: imagen de la Corrupción. El hombre noble agita a la gente y "
            "fortalece su espíritu”.\n\n"
            "Cuando el viento forma remolinos al pie de la montaña arruina los cultivos, reclamando una mejoría. "
            "Para desterrar la corrupción social hay que regenerar la nobleza. Primero se debe remover "
            "el estancamiento conmoviendo la opinión pública y luego fortalecer y tranquilizar el ánimo popular "
            "como la montaña nutre a las plantas."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Reparar lo que fue corrompido por el padre. Si es un hijo, no hay "
                "reproches sobre el padre muerto. Peligro. Al final buena fortuna”.\n"
                "La rígida adhesión a lo realizado ha traído corrupción, pero aún no está profundamente arraigada. "
                "Se puede remediar si uno es consciente del peligro inherente a las reformas; solo así se lleva a "
                "buen término."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Reparar lo que fue corrompido por la madre. Uno no debe "
                "ser demasiado perseverante”.\n"
                "Se refiere a errores provocados por la debilidad. Es necesario tener delicadeza y "
                "ciertas consideraciones al proceder a la reparación, evitando ser demasiado severo para no herir "
                "con brusquedad."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Reparar lo que fue corrompido por el padre. Habrá un "
                "pequeño remordimiento pero ningún reproche considerable”.\n"
                "Describe a quien procede con energía un poco excesiva corrigiendo errores del pasado. "
                "Provocará ciertas molestias, pero un exceso de energía es preferible a muy poca. "
                "Permanecerá libre de culpas graves."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Tolerando lo que fue destruido por el padre. Continuando "
                "se ve humillado”.\n"
                "Muestra a alguien que por debilidad no se opone a la corrupción del pasado y la deja seguir su "
                "curso en el presente. Si continúa así, el resultado inevitable será la humillación."
            ),
            5: (
                "Seis en el quinto lugar significa: “Reparando lo que fue destruido por el padre se encuentra "
                "con el elogio”.\n"
                "El individuo se confronta con corrupción originada en negligencias pasadas. Aunque no "
                "posee la fuerza para una renovación total, encuentra ayudantes hábiles para lograr una reforma "
                "profunda digna de elogios."
            ),
            6: (
                "Nueve en la cima significa: “No sirve a reyes ni príncipes, déjenlo buscar metas más altas”.\n"
                "Hay personas con tal evolución interior que tienen derecho a no inmiscuirse en asuntos políticos. "
                "Esto no significa inactividad o crítica pura; se justifica solo si trabajan sobre sí mismos "
                "apuntando a metas superiores, creando valores humanos para el futuro."
            )
        },
        "lineas": {
            1: "Reparar con cuidado y conciencia la corrupción inicial heredada.",
            2: "Corregir errores nacidos de la debilidad con delicadeza.",
            3: "Energía decidida para enmendar el pasado, asumiendo pequeñas molestias.",
            4: "La debilidad y tolerancia ante lo corrupto conducen a la humillación.",
            5: "Reforma profunda lograda con el apoyo de ayudantes hábiles.",
            6: "Retiro del mundo para crear valores superiores mediante el trabajo interno."
        }
    },
    19: {
        "nombre": "LIN / LA APROXIMACIÓN",
        "trigrama_sup": "K'un Lo Receptivo, Tierra",
        "trigrama_inf": "Tui Lo Gozoso, Lago",
        "exposicion": (
            "La palabra china Lin posee significaciones como “crecer” y “aproximación”. Lo que crece son los "
            "dos trazos fuertes que empujan desde abajo, expandiendo la fuerza luminosa. Esto indica la "
            "aproximación de lo que es fuerte y superior respecto a lo que es débil e inferior, con un sentido de "
            "condescendencia de un hombre superior hacia el pueblo. El hexagrama se atribuye al 12º mes "
            "(enero-febrero), cuando la fuerza luminosa asciende tras el solsticio de invierno."
        ),
        "juicio": (
            "“La aproximación tiene un éxito sublime. La perseverancia es ventajosa. Cuando llega el octavo mes "
            "habrá desgracia”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Indica una época de progreso llena de alegre esperanza; la primavera se acerca y el éxito está asegurado. "
            "Sin embargo, la primavera no durará siempre. Al octavo mes las cosas se invertirán y las líneas fuertes "
            "retrocederán. Es vital recordar esto a tiempo para prevenir el mal o dominar el peligro antes "
            "de que se insinúe."
        ),
        "imagen": (
            "“Sobre el lago está la tierra, la imagen de la aproximación. El hombre noble es inagotable en su deseo "
            "de enseñar y sin límites para sostener y proteger el pueblo”.\n\n"
            "La tierra limita al lago por arriba, representando la condescendencia del superior hacia los que están en el fondo. "
            "Como el lago es inacabable en profundidad, el sabio tiene disposición inagotable para enseñar; como la tierra es "
            "vastísima, el sabio sustenta y cuida a todo el mundo sin excluir a nadie."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Aproximación en común. La perseverancia trae la fortuna”.\n"
                "El bien comienza a predominar y encuentra buena recepción en los puestos influyentes, incentivando a los hombres "
                "de valor a unirse a la marcha adelante. Se debe estar atento a no perderse en la corriente de la época "
                "y mantener la buena dirección con perseverancia."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Aproximación en común. Buena fortuna. Todo es favorable”.\n"
                "Uno es incitado por lo superior a aproximarse debido a una fuerza y lógica interna sin reparos. "
                "Aunque todo ascenso es seguido por un descenso, no hay que dejarse desviar por ese destino universal; "
                "se debe marchar por el camino de la vida rápido, con valentía y osadía."
            ),
            3: (
                "Seis en el tercer lugar significa: “Aproximación adecuada. Nada que sea favorable. Si alguien es inducido "
                "a lamentarse por ello, queda libre de culpa”.\n"
                "Al adquirir poder se corre el riesgo de relajarse y caer en la negligencia por comodidad. Esto es dañino, "
                "pero si se siente pena por esa actitud y se reconoce la responsabilidad que acarrea el poder, entonces uno "
                "se libera de las culpas."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Aproximación perfecta. Sin reproches”.\n"
                "Muestra la actitud del superior hacia los inferiores. Se describe la aproximación sin prejuicios de una persona "
                "de alto rango hacia un hombre hábil al que introduce en su propio círculo. Esta apertura es muy favorable "
                "y libre de errores."
            ),
            5: (
                "Seis en el quinto lugar significa: “Sabia aproximación. Es lo correcto para un gran príncipe. Buena fortuna”.\n"
                "Un gobernante debe tener la sabiduría de atraer hacia sí gente hábil y experta. Su sabiduría consiste "
                "en seleccionar a las personas correctas y dejar que trabajen sin interferir en sus tareas, observando la "
                "situación para encontrar a los expertos necesarios."
            ),
            6: (
                "Seis en la cima significa: “Aproximación generosa. Buena fortuna. Sin reproches”.\n"
                "Un sabio que se había retirado decide retornar al mundo para aproximarse a los demás hombres. "
                "Esto representa una inmensa fortuna para quienes reciben su enseñanza y ayuda. Esta acción magnánima "
                "de rebajarse no da lugar a ningún reproche."
            )
        },
        "lineas": {
            1: "Unión a la marcha del progreso con perseverancia y valores.",
            2: "Avanzar con valentía sin temer al destino cíclico de ascenso y descenso.",
            3: "Evitar la negligencia del poder mediante la autocrítica y responsabilidad.",
            4: "Aproximación sin prejuicios hacia personas hábiles de rangos inferiores.",
            5: "Sabiduría para delegar y permitir que los expertos trabajen sin interferencia.",
            6: "Retorno generoso del sabio al mundo para ayudar a la humanidad."
        }
    },
    20: {
        "nombre": "KUAN / LA CONTEMPLACIÓN (La visión)",
        "trigrama_sup": "Sun La Docilidad, Viento",
        "trigrama_inf": "K'un Lo Receptivo, Tierra",
        "exposicion": (
            "El nombre chino de este hexagrama tiene un doble sentido: contemplar y ser visto (servir de ejemplo). "
            "Se representa como una torre que ofrece una amplia visión del entorno y es visible desde lejos. "
            "Muestra a un gobernante que contempla la ley del cielo y las costumbres del pueblo, dando un alto ejemplo "
            "a las masas a través de un gobierno acertado. Está ligado al octavo mes, cuando la fuerza "
            "oscura está en ascensión."
        ),
        "juicio": (
            "“Contemplación. Se hicieron las abluciones, pero aún no las ofrendas. Llenos de confianza dirigen hacia "
            "él la mirada”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El ritual sagrado del sacrificio comenzaba con una ablución; el intervalo antes de la ofrenda era el momento "
            "de supremo recogimiento interior. La contemplación sincera de este momento transforma a los "
            "testigos. Los hombres dotados de fe intensa ven las leyes divinas y las manifiestan en su "
            "personalidad, ejerciendo un poderoso poder espiritual sobre los demás."
        ),
        "imagen": (
            "“El viento sopla sobre la tierra: la imagen de la contemplación. Así los reyes antiguos visitaban las "
            "regiones del mundo, contemplaban la gente e impartían la enseñanza”.\n\n"
            "Como el viento llega a todos lados y la hierba se pliega ante él, los reyes de la antigüedad procuraban "
            "una vista general de su pueblo para modificar hábitos inadecuados. El hombre superior tiene "
            "una visión que no puede ser engañada y ejerce influencia por su simple presencia."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Contemplación de un niño. Para un hombre vulgar, no hay reproches. "
                "Para un hombre noble, hay humillación”.\n"
                "Muestra una contemplación sin inteligencia y de lejos. Para las masas esto no es grave "
                "porque no comprenden las acciones de los sabios, pero para un hombre superior es vergonzoso. "
                "No debe contentarse con una visión superficial, sino considerar las influencias en su contexto."
            ),
            2: (
                "Seis en el segundo lugar significa: “Contemplar a través de la rendija de la puerta. Es ventajoso "
                "para la perseverancia de una mujer”.\n"
                "Se tiene una visión limitada y subjetiva, relacionándolo todo con uno mismo sin comprender los "
                "motivos ajenos. Esto puede ser adecuado para quien se ocupa de asuntos domésticos "
                "internos, pero para alguien que debe actuar en la vida pública, esta limitación egoísta es mala."
            ),
            3: (
                "Seis en el tercer lugar significa: “Contemplando mi vida elijo entre el progreso y el retroceso”.\n"
                "Es un lugar de transición donde la mirada se orienta hacia uno mismo para encontrar dirección. "
                "Representa la victoria sobre el egoísmo al buscar objetividad. El examen no es solo sobre "
                "el pensamiento, sino sobre los actos producidos, pues solo las acciones determinan el progreso."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Contemplando la luz del reino, es ventajoso actuar como un "
                "huésped del rey”.\n"
                "Describe a quien comprende el secreto para hacer prosperar un reino. Debe ocupar una "
                "posición de autoridad pero actuar con la independencia de un huésped, siendo respetado por su "
                "propio valor y no utilizado como un simple instrumento."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Contemplando mi vida. El hombre noble no tiene reproches”.\n"
                "Alguien en un puesto de autoridad debe estar preparado para examinarse a sí mismo. El examen "
                "correcto consiste en mirar los resultados y la influencia que se ejerce sobre otros. Si "
                "los resultados son buenos, podrá estar libre de reproches."
            ),
            6: (
                "Nueve en la cima significa: “Contemplando su vida. El hombre noble no tiene reproches”.\n"
                "En el lugar más elevado, se excluye lo personal. Muestra a un sabio que, libre de sí mismo "
                "y de la agitación del mundo, contempla la ley de la vida. Reconoce que el bien supremo "
                "consiste en saber cómo permanecer libre de reproches ante lo universal."
            )
        },
        "lineas": {
            1: "Contemplación superficial; aceptable para la masa, humillante para el noble.",
            2: "Visión limitada y subjetiva; adecuada solo para el ámbito privado.",
            3: "Autoreflexión basada en los actos para decidir el rumbo a seguir.",
            4: "Comprensión de los asuntos públicos y actuación con independencia y respeto.",
            5: "Autoexamen de un líder a través del efecto de sus acciones en los demás.",
            6: "Sabiduría superior que contempla las leyes de la vida con desapego total."
        }
    },
    21: {
        "nombre": "SHIH HO / MORDIENDO A TRAVÉS",
        "trigrama_sup": "Li Lo Oscilante, Fuego",
        "trigrama_inf": "Chen Lo Excitante, Trueno.",
        "exposicion": (
            "El hexagrama representa una boca abierta con algo que la obstruye entre los dientes (en el cuarto lugar). "
            "Para unir los labios debe morderse enérgicamente el obstáculo. Se compone del trigrama Chen (Trueno) "
            "y Li (Fuego/Rayo), indicando la manera vigorosa en que la naturaleza se separa de lo que la molesta. "
            "Simboliza procesos y castigos que triunfan sobre crímenes y calumnias que enturbian la armonía social; "
            "a diferencia del hexagrama N° 6, aquí se trata de un proceso criminal."
        ),
        "juicio": (
            "“Morder a través tiene éxito. Es favorable dejar que se ejerza la justicia”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Cuando un obstáculo como un calumniador o traidor impide la unidad, hay que morder enérgicamente para "
            "evitar un perjuicio duradero. El hexagrama une la claridad (Li) con la excitación (Chen) para "
            "realizar la medida justa del castigo. Es importante que quien toma la decisión sea blando de "
            "naturaleza (5° línea) pero, gracias a su posición, ejerza una acción que inspire respeto."
        ),
        "imagen": (
            "“Truenos y rayos. La imagen de morder a través. Así los viejos reyes establecían leyes firmes y con "
            "penalidades bien definidas”.\n\n"
            "La claridad (rayo) permite distinguir las faltas leves de las graves, mientras que la firmeza (trueno) "
            "asegura la justa aplicación de las penas para mantener el respeto. Los castigos cobran "
            "importancia colectiva cuando no están claramente determinados o se aplican con negligencia; para "
            "consolidar las leyes, los castigos deben ser claros, fijos y rápidos."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Su pie está asegurado en el cepo. Sus dedos desaparecen. Sin "
                "reproches”.\n"
                "Se impone una sentencia leve a alguien que infringe la ley por primera vez. Se impide que el "
                "culpable siga pecando, siendo solo una advertencia para detenerse a tiempo en el camino del mal."
            ),
            2: (
                "Seis en el segundo lugar significa: “Muerde en la carne tierna, hasta que su nariz desaparece. "
                "Sin reproches”.\n"
                "Es fácil discriminar entre lo correcto y lo errado. Sin embargo, bajo el efecto de la irritación, "
                "la cólera puede ser excesiva. La desaparición de la nariz indica una indignación que nubla "
                "la sensibilidad, pero no hay gran daño pues la pena es simplemente justa."
            ),
            3: (
                "Seis en el tercer lugar significa: “Muerde una carne seca y rancia y se topa con algo venenoso. "
                "Leve humillación. Sin reproches”.\n"
                "El castigo es ejecutado por alguien sin el poder o autoridad suficiente, por lo que los condenados "
                "no se someten. Se encuentran dificultades y riesgos de atraer rencores (veneno) al "
                "ocuparse de este asunto averiado, resultando en una situación un poco humillante pero necesaria."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Muerde carne seca y cartilaginosa. Recibe flechas de metal. "
                "Es ventajoso reflexionar sobre las dificultades y perseverar. Fortuna”.\n"
                "Existen grandes obstáculos y oponentes poderosos. La tarea es ardua y requiere ser duro como el "
                "metal y directo como una flecha. Al reconocer las dificultades y perseverar, la tarea "
                "delicada es finalmente llevada a cabo con éxito."
            ),
            5: (
                "Seis en el quinto lugar significa: “Muerde carne seca y magra. Recibe oro amarillo. Reconocer el "
                "peligro constantemente. Sin reproches”.\n"
                "Se debe decidir sobre un asunto difícil pero claro. El ejecutor debe poseer una tendencia a la "
                "serenidad e imparcialidad (oro amarillo). Solo permaneciendo consciente de los peligros "
                "derivados de la responsabilidad asumida se evitan cometer errores."
            ),
            6: (
                "Nueve en la cúspide significa: “Su cuello está atrapado por una canga de madera de tal manera "
                "que sus orejas desaparecen. Desgracia”.\n"
                "Se trata de alguien incorregible. El castigo es pesado (la canga) porque el sujeto permanece sordo "
                "a las advertencias y consejos. Su obstinación conduce inevitablemente al infortunio debido a "
                "que las faltas se han amontonado hasta ser inocultables."
            )
        },
        "lineas": {
            1: "Castigo leve inicial que sirve como advertencia necesaria.",
            2: "Aplicación de justicia en un caso claro, aunque con indignación excesiva.",
            3: "Dificultad para imponer autoridad ante la falta de poder real.",
            4: "Superación de obstáculos poderosos mediante firmeza y perseverancia.",
            5: "Decisión difícil tomada con imparcialidad y conciencia del peligro.",
            6: "Infortunio por obstinación y sordera ante advertencias previas."
        }
    },
    22: {
        "nombre": "PI / LA GRACIA",
        "trigrama_sup": "Ken, La Inmovilidad, la Montaña.",
        "trigrama_inf": "Li Lo Oscilante, Fuego.",
        "exposicion": (
            "El hexagrama muestra el fuego que nace de las secretas profundidades de la tierra y arde "
            "iluminando la montaña y lo alto del cielo, revistiéndola de belleza. La gracia, la belleza "
            "de la forma es necesaria para que toda unión sea armoniosa y amable y no caótica y desordenada. "
            "Representa la belleza en reposo: claridad adentro y quietud afuera."
        ),
        "juicio": (
            "“La gracia tiene éxito. En asuntos pequeños es favorable emprender algo”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La gracia trae éxito, pero no es lo esencial; es un ornamento que debe usarse con parsimonia. "
            "En la vida humana, la belleza de la forma aparece cuando los caracteres fuertes como montañas "
            "se hacen agradables por una clara belleza. Sin embargo, la contemplación de la belleza por sí sola "
            "no pone la voluntad en reposo; es un momento de exaltación pasajera, no una vía de liberación."
        ),
        "imagen": (
            "“Fuego al pie de la montaña. La imagen de la gracia. Así el hombre noble progresa cuando aclara "
            "los asuntos corrientes pero no es de esta manera que logrará decidir las cuestiones importantes”.\n\n"
            "La luz del fuego ilumina la montaña haciéndola agradable, pero su luz no brilla lejos. De la misma "
            "forma, las formas hermosas bastan para iluminar cuestiones inmediatas, pero los asuntos de "
            "gran importancia requieren mayor seriedad y no pueden decidirse solo por la apariencia."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Da gracia a sus pies, deja el carro y camina”.\n"
                "En un puesto subordinado, uno debe encargarse por sí mismo del esfuerzo de avanzar. "
                "Un hombre resuelto desprecia las facilidades obtenidas de manera dudosa; es más digno "
                "avanzar por esfuerzo propio que viajar en carro sin tener el derecho."
            ),
            2: (
                "Seis en el segundo lugar significa: “Presta gracia a su barba”.\n"
                "La barba no es independiente, se mueve con el mentón. La forma debe ser resultado del "
                "contenido. Cuidar la forma (la barba) sin considerar el contenido interior del cual proviene "
                "es un signo de vanidad superficial."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Elegante y húmedo. La perseverancia constante trae buena fortuna”.\n"
                "Un momento de la vida lleno de encanto y gloria. Es una advertencia para no hundirse en "
                "el bienestar blando; la buena fortuna depende de ser constante en la perseverancia a pesar "
                "del estado relajado."
            ),
            4: (
                "Seis en el cuarto lugar significa: “¿Gracia o simplicidad? Un caballo blanco viene como si tuviera alas. "
                "No es un ladrón, quiere llegar en el momento justo”.\n"
                "Duda entre la apariencia exterior y la simplicidad. La respuesta es la simplicidad (el color blanco). "
                "Aunque se renuncie a comodidades, se encuentra la paz en una relación sincera. El caballo alado "
                "simboliza pensamientos que trascienden límites."
            ),
            5: (
                "Seis en el quinto lugar significa: “Gracia en las colinas y los jardines. El capullo de seda es pequeño y modesto. "
                "Humillación, pero finalmente, buena fortuna”.\n"
                "Se busca a alguien en la soledad de las alturas, lejos del lujo y la pompa. Aunque los presentes "
                "que se ofrecen sean modestos y causen vergüenza, lo que cuenta son los verdaderos sentimientos. "
                "Al final, todo va bien."
            ),
            6: (
                "Nueve en la cúspide significa: “Gracia simple. Sin error”.\n"
                "En el grado más elevado, la forma ya no disimula el contenido, sino que lo deja exponerse "
                "en todo su valor. La gracia suprema consiste en dar a los materiales una forma simple y práctica, "
                "sin ornamentos exteriores innecesarios."
            )
        },
        "lineas": {
            1: "Preferencia por el esfuerzo propio y digno sobre facilidades dudosas.",
            2: "La forma debe ser reflejo del contenido, no un adorno superficial.",
            3: "Peligro de estancarse en el bienestar; necesidad de perseverar.",
            4: "Elección de la simplicidad y la sinceridad sobre la apariencia.",
            5: "La modestia y los sentimientos sinceros valen más que la ostentación.",
            6: "El punto máximo de la gracia es la simplicidad absoluta."
        }
    },
    23: {
        "nombre": "PO / LA DISPERSIÓN (El Desgaste)",
        "trigrama_sup": "Tchen El despertador, El trueno",
        "trigrama_inf": "K'un Lo Receptivo, Tierra.",
        "exposicion": (
            "Representa una época donde las líneas oscuras (Yin) suben para causar la caída de la última "
            "línea firme y luminosa. El hombre vulgar mina progresivamente al noble de forma imperceptible. "
            "Es la imagen de una casa cuyo techo se fisura, amenazando con el colapso total. La fuerza "
            "Yin está a punto de derrocar completamente a la fuerza Yang."
        ),
        "juicio": (
            "“La dispersión. No es conveniente emprender algo ni de ir a ninguna parte”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Época donde lo débil avanza para superar a lo noble. No es cobardía, sino sabiduría saberse "
            "adaptar y abstenerse de la acción. El trigrama superior (Montaña) indica tranquilidad e "
            "inmovilidad, mientras el inferior (Tierra) indica docilidad. Hay que conformarse con el "
            "mal tiempo y permanecer quieto."
        ),
        "imagen": (
            "“La montaña descansa en la tierra. La imagen de la dispersión. Los superiores pueden asegurar "
            "su posición sólo mediante generosas concesiones con los que están abajo”.\n\n"
            "Si la montaña es escarpada y sin base amplia, se derrumba. Los que están arriba deben mostrar "
            "grandeza de alma y generosidad, como la tierra que sostiene a todos los seres. Solo así "
            "mantendrán su posición segura y tranquila."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “La pata de la cama se destroza. Los que perseveran serán "
                "destruidos. Desgracia”.\n"
                "Gente inferior avanza en secreto para minar el orden. Los que permanecen leales son "
                "destruidos por la intriga. La situación es desastrosa; no hay nada mejor que esperar."
            ),
            2: (
                "Seis en el segundo lugar significa: “La orilla de la cama se destroza. Los que perseveran "
                "serán destruidos. Desgracia”.\n"
                "El poder de la vulgaridad avanza y el peligro se acerca a la propia persona. Se está "
                "impotente y aislado. Es necesario tomar extremas precauciones y adaptarse a las "
                "exigencias del momento para evitar el desastre."
            ),
            3: (
                "Seis en el tercer lugar significa: “Se separa de ellos. Sin reproches”.\n"
                "Uno se encuentra en medio de una mala circunstancia, pero subsiste una relación con un "
                "hombre superior. Por este medio se adquiere estabilidad interior para liberarse de la "
                "mala influencia de quienes lo rodean."
            ),
            4: (
                "Seis en el cuarto lugar significa: “La cama se destroza hasta la piel. Desgracia”.\n"
                "El infortunio alcanza aquí el mismo cuerpo. La desgracia ha alcanzado el máximo punto "
                "y ya no se deja esquivar. No hay advertencias adicionales porque el golpe es directo."
            ),
            5: (
                "Seis en el quinto lugar significa: “Un banco de peces. El favor llega a través de las "
                "damas de la corte. Todo es favorable”.\n"
                "La naturaleza oscura se somete a la dirección del principio fuerte y luminoso en la "
                "cúspide. Se conduce al conjunto hacia lo correcto, como una princesa a sus damas. "
                "Al someterse libremente a lo superior, se recibe lo que se merece."
            ),
            6: (
                "Nueve en la cúspide significa: “Hay una gran fruto que todavía no ha sido comido. El hombre "
                "noble recibe un carruaje. La casa del hombre inferior se hace pedazos”.\n"
                "Fin de la dispersión. El mal se destruye a sí mismo al agotar su maldad. El hombre noble "
                "recupera su capacidad de actuar y es apoyado por la opinión general (el carro). La "
                "semilla del bien vuelve a caer en la tierra para un nuevo comienzo."
            )
        },
        "lineas": {
            1: "Destrucción clandestina desde la base; conviene esperar.",
            2: "El peligro acecha de cerca; evitar la inflexibilidad.",
            3: "Vínculo con lo superior que permite liberarse del entorno negativo.",
            4: "Infortunio inevitable que llega al punto máximo.",
            5: "Sometimiento voluntario a la guía correcta; éxito.",
            6: "El mal se agota y el bien retorna con fuerza renovada."
        }
    },
    24: {
        "nombre": "FU / EL RETORNO (El Cambio de Tiempo)",
        "trigrama_sup": "K'un Lo Receptivo, Tierra",
        "trigrama_inf": "Chen Lo que Despierta, Trueno.",
        "exposicion": (
            "Indica el momento en que, tras haber sido desalojadas todas las líneas luminosas, una de ellas "
            "retorna por abajo. El tiempo de la oscuridad pasó; ahora viene la victoria de la luz. Se asocia "
            "al solsticio de invierno y al 11° mes. Es un movimiento natural, espontáneo y circular, donde "
            "lo viejo es depuesto a favor de lo nuevo sin producir daño."
        ),
        "juicio": (
            "“Retorno. Éxito. Saliendo y volviendo sin error. Los amigos vienen sin reproches. El camino "
            "va y viene. Al séptimo día regresa. Es ventajoso tener donde ir”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Tras la decadencia comienza el regreso. No es algo impuesto, sino un acto natural que nace del "
            "abandono de sí mismo (K'un). Todo viene espontáneamente cuando ha llegado el tiempo; no debe "
            "precipitarse nada artificialmente. El siete es el número de la joven luz que nace cuando la "
            "oscuridad llega a su punto máximo."
        ),
        "imagen": (
            "“Trueno sobre la tierra. La imagen del punto de retorno. Así, los reyes de la antigüedad "
            "cerraban los pasajes en el tiempo del solsticio. Mercaderes y extranjeros no circulaban y "
            "el gobernante no viajaba por las provincias”.\n\n"
            "La potencia vital (el trueno) está todavía bajo tierra y debe fortificarse con el reposo. "
            "Es un tiempo para no malgastar la energía con usos prematuros. El retorno a la salud o a la "
            "comprensión debe tratarse con delicadeza y comodidad en sus comienzos para que conduzca a la prosperidad."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Retorno de corta distancia. No hay necesidad de remordimientos. "
                "Gran buena fortuna”.\n"
                "Pequeñas desviaciones deben corregirse a tiempo antes de ir demasiado lejos. Al dejar de lado "
                "el error de inmediato, no habrá causa para arrepentirse y todo irá bien. Es el desarrollo del carácter."
            ),
            2: (
                "Seis en el segundo lugar significa: “Retorno tranquilo. Buena fortuna”.\n"
                "El regreso requiere resolución y dominio de sí mismo. Es más fácil cuando se cuenta con buena "
                "compañía y uno puede plegarse a hombres de bien para arreglarse con ellos."
            ),
            3: (
                "Seis en el tercer lugar significa: “Regreso reiterado. Peligro. Sin arrepentimiento”.\n"
                "Existen personas con inestabilidad interior que necesitan invertir constantemente la dirección "
                "de su voluntad. Aunque hay peligro por los deseos incontrolados, la tendencia prolongada a "
                "corregir los defectos no está excluida."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Caminando errante en medio de los otros, se retorna solo”.\n"
                "Uno se encuentra rodeado de personas vulgares, pero está ligado interiormente a un amigo fuerte "
                "y bueno. La resolución de dirigirse hacia lo bueno, aunque signifique soledad externa, llevará "
                "en sí misma su recompensa."
            ),
            5: (
                "Seis en el quinto lugar significa: “Retorno magnánimo. Sin remordimientos”.\n"
                "Cuando llega el tiempo de volver, no hay que usar excusas triviales. Hay que examinarse "
                "prolijamente y, si se erró, confesar la falta con una resolución noble. Seguir este camino "
                "limpia el pasado."
            ),
            6: (
                "Seis en la cúspide significa: “Retorno fallado. Infortunio. La desgracia viene de afuera y "
                "de adentro. Por diez años no será posible atacar de nuevo”.\n"
                "Equivocarse en el momento de regresar conduce al infortunio por una actitud incorrecta hacia "
                "el mundo. La ciega obstinación pierde al sujeto; la consecuencia es el infortunio interior "
                "que luego se manifiesta afuera."
            )
        },
        "lineas": {
            1: "Corrección rápida de errores; gran fortuna.",
            2: "Regreso facilitado por la buena compañía y el dominio propio.",
            3: "Hábito de corregir defectos a pesar de la inestabilidad.",
            4: "Decisión de volver a lo correcto a pesar del entorno vulgar.",
            5: "Autoevaluación honesta y nobleza al reconocer errores.",
            6: "Obstinación que impide el retorno y causa desgracia prolongada."
        }
    },
    25: {
        "nombre": "WU WANG / LA INOCENCIA (Lo Inesperado)",
        "trigrama_sup": "Ch'ien Lo Creativo, Cielo.",
        "trigrama_inf": "Chen Lo que Despierta, Trueno.",
        "exposicion": (
            "Arriba está Ch'ien, lo creativo; abajo Chen, el movimiento. El trigrama inferior está bajo "
            "la influencia de la línea fuerte recibida del cielo. Cuando el movimiento sigue las leyes "
            "del cielo, el hombre es inocente y sin falsedad. Su espíritu es natural y veraz. Si intenta "
            "seguir otro designio, pierde su veracidad. El hexagrama comprende además la noción de lo "
            "imprevisto, de lo inesperado."
        ),
        "juicio": (
            "“Inocencia. Éxito supremo. La perseverancia es ventajosa. Si alguien no es lo que debe ser, "
            "tiene mala fortuna y eso no le ayudará a emprender ninguna cosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El hombre recibe del cielo una naturaleza intrínsecamente buena para guiar sus movimientos. "
            "Al adherirse a este principio, alcanza una inocencia pura que, sin detenerse en pensamientos "
            "de recompensa o interés, hace lo que es justo con seguridad instintiva. La actividad "
            "instintiva irracional produce solamente desgracias."
        ),
        "imagen": (
            "“Bajo el cielo vibra el trueno. Todas las cosas llegan al estado natural de inocencia como "
            "los reyes antiguos, ricos en virtudes y en armonía con sus tiempos, cuidaban y nutrían a "
            "todos los seres”.\n\n"
            "En primavera, cuando el trueno suena, todas las cosas germinan y crecen. Los buenos soberanos "
            "actúan desplegando la riqueza interior de su naturaleza, proporcionando el cuidado requerido "
            "por la vida y la civilización en el tiempo justo para progresar."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Cambio inocente trae buena fortuna”.\n"
                "Los primeros impulsos originales del corazón (las corazonadas) son siempre buenos y se "
                "pueden seguir con confianza, estando seguros de alcanzar la meta con buena fortuna."
            ),
            2: (
                "Seis en el segundo lugar significa: “Si cuando se labra un campo no se piensa en la cosecha "
                "y cuando se lo desbroza no se lo hace pensando en el uso que se hará del campo, entonces "
                "es ventajoso emprender algo”.\n"
                "Todo trabajo debe ser realizado por él mismo, según lo requieran el tiempo y el lugar, "
                "sin miras sobre el resultado. Entonces fructifica y es coronado por el éxito."
            ),
            3: (
                "Seis en el tercer lugar significa: “Desgracia inmerecida. La vaca amarrada da ganancia al "
                "vagabundo y pérdidas al aldeano”.\n"
                "A veces espera una desgracia inmerecida causada por otros. Lo que es ganancia para uno es "
                "pérdida para el propietario. Incluso en asuntos inocentes, uno debe conformarse con las "
                "exigencias del momento para evitar el infortunio."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “El que puede ser perseverante permanece sin culpa”.\n"
                "No podemos abandonar lo que realmente nos pertenece, incluso si se lo rechaza. No debe "
                "haber inquietud; solo hay que cuidarse de permanecer siempre fiel a su propia naturaleza "
                "y no escuchar a los demás."
            ),
            5: (
                "Nueve en el quinto lugar significa: “En una enfermedad inmerecida no hay necesidad de medicina”.\n"
                "Un mal inesperado puede llegar accidentalmente del exterior sin causa en la naturaleza del "
                "hombre. En ese caso no se debe recurrir a medios exteriores, sino dejar que la naturaleza "
                "siga su curso para que las cosas se arreglen por sí mismas."
            ),
            6: (
                "Nueve en la cima significa: “Una acción inocente trae desgracia. Nada es favorable”.\n"
                "Cuando la época no es propicia para el progreso, es importante esperar tranquilamente "
                "sin intenciones ulteriores. Si se actúa de manera irracional para ir contra el destino, "
                "no se obtendrá el éxito."
            )
        },
        "lineas": {
            1: "Seguir las corazonadas originales del corazón trae éxito.",
            2: "Actuar en el presente sin codiciar el resultado final.",
            3: "Aceptar las pérdidas por azar o acciones ajenas inesperadas.",
            4: "Permanecer fiel a la propia naturaleza por encima de opiniones externas.",
            5: "Dejar que los problemas externos se resuelvan por curso natural.",
            6: "No forzar el progreso cuando la época no es propicia."
        }
    },
    26: {
        "nombre": "TA CHU / EL PODER DOMINANTE DE LO GRANDE",
        "trigrama_sup": "Ken, La Inmovilidad, la Montaña.",
        "trigrama_inf": "Ch'ien, Lo Creativo, Cielo.",
        "exposicion": (
            "El creador está aprisionado por la inmovilidad. Esto da un gran poder, mucho más potente "
            "que el del N° 9. El signo encierra un triple significado: el cielo en medio de la montaña "
            "da la idea de 'tener firme' en el sentido de 'mantener juntos'; la inmovilización de Ch'ien "
            "da la idea de 'retener'; y finalmente, la idea de 'cultivar' o 'nutrir', que vale "
            "especialmente para el regente del hexagrama, el trazo superior que representa el sabio."
        ),
        "juicio": (
            "“El poder dominante de lo grande. La perseverancia es ventajosa. No comer en casa trae "
            "buena fortuna. Es ventajoso atravesar la gran corriente”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Para atesorar los poderes creativos se requiere un hombre fuerte y de claro entendimiento. "
            "Solo a través de la renovación diaria del carácter se pueden aumentar los poderes. En tiempos "
            "donde se usa el poder acumulado, todo depende de la fuerza de la personalidad. Es ventajoso "
            "ganarse el pan en una ocupación pública ocupando un cargo oficial; tal hombre triunfará "
            "aunque efectúe empresas difíciles como cruzar la gran corriente."
        ),
        "imagen": (
            "“Cielo en el medio de la montaña. La imagen del poder influyente de lo grande. El hombre "
            "noble se informa sobre con muchos refranes antiguos y experiencias pasadas, para fortalecer "
            "con ellos su carácter”.\n\n"
            "En las palabras y sentencias del pasado yace el tesoro escondido que podemos usar para "
            "fortalecer nuestro carácter. Estudiar el pasado no consiste en limitarse a conocer la historia, "
            "sino en hacer de la historia una realidad actual utilizando sus datos."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Hay peligro en ciernes. Es conveniente alejarse”.\n"
                "Se desea avanzar vigorosamente pero las circunstancias se oponen. Si se quiere avanzar "
                "a pesar de todo, se atraerá la desgracia. Es mejor resignarse, reponer sus energías y "
                "esperar que las fuerzas acumuladas ofrezcan una salida."
            ),
            2: (
                "Nueve en la segunda línea significa: “Los ejes de las ruedas fueron sacados del carro”.\n"
                "El progreso está obstaculizado. Aquí la fuerza de obstrucción es predominante, por lo "
                "que no hay combate y uno se adapta. Al contentarse con esperar, se acumulan energías "
                "y se crea una tensión que permitirá ulteriormente un avance vigoroso."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Un buen caballo que sigue a otro. La conciencia "
                "del peligro y la perseverancia son convenientes. Debes ejercitarte todos los días guiando "
                "el carro y manejando las armas. Es conveniente tener un lugar adonde ir”.\n"
                "El camino está abierto y los obstáculos han desaparecido. Se avanza con una fuerte voluntad, "
                "pero todavía amenaza el peligro y se debe permanecer consciente de ello. Hay que adiestrarse "
                "avanzando y a la vez vigilar contra ataques inesperados."
            ),
            4: (
                "Seis en el cuarto lugar significa: “La tablilla sobre el testuz de un toro joven. Gran "
                "buena fortuna”.\n"
                "Se domina la naturaleza salvaje antes de que se manifieste (antes de que crezcan los cuernos). "
                "Poner la tablilla evita que el animal sea peligroso más tarde. Es una buena manera de "
                "oponerse a la fuerza primaria para obtener un éxito fácil y considerable."
            ),
            5: (
                "Seis en el quinto lugar significa: “Los colmillos de un jabalí castrado. Buena fortuna”.\n"
                "Aquí se domina indirectamente el avance impetuoso. Al alterar la naturaleza del jabalí, "
                "sus colmillos dejan de ser una amenaza. Las fuerzas salvajes no deben ser combatidas "
                "directamente, sino que sus raíces deben ser erradicadas."
            ),
            6: (
                "Nueve en la cima significa: “Se alcanza el camino del cielo. Éxito”.\n"
                "El tiempo de la obstrucción pasó. La energía reprimida se abre camino y obtiene un gran "
                "éxito. Es un sabio quien es honrado por el soberano y sus principios se imponen y "
                "ordenan el mundo."
            )
        },
        "lineas": {
            1: "Peligro al avanzar; es mejor detenerse y reponer energías.",
            2: "Adaptación ante la obstrucción; acumular tensión para el futuro.",
            3: "Camino abierto pero requiere vigilancia y práctica diaria.",
            4: "Control preventivo de las fuerzas salvajes; éxito fácil.",
            5: "Dominio indirecto erradicando la raíz del problema.",
            6: "Triunfo total y difusión de los principios en el mundo."
        }
    },
    27: {
        "nombre": "I / LAS COMISURAS DE LOS LABIOS (La administración de la alimentación)",
        "trigrama_sup": "Ken, La Inmovilidad, la Montaña.",
        "trigrama_inf": "Chen Lo que Despierta, Trueno.",
        "exposicion": (
            "El hexagrama representa una boca abierta. Las líneas fuertes en los extremos son los labios "
            "y el espacio entre ellas es la abertura de la boca. De la imagen de la boca se pasa a la idea "
            "de la nutrición misma. Las líneas inferiores representan la alimentación del cuerpo, mientras "
            "que las superiores representan la alimentación y la cultura del espíritu."
        ),
        "juicio": (
            "“Las comisuras de los labios. La perseverancia trae buena fortuna. Observar la administración "
            "de alimento y de lo que el hombre se procura para llenar su propia boca”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Para conocer a alguien, basta observar a qué partes de su naturaleza nutre. El hombre noble "
            "cultiva sus partes nobles y protege a la gente de valor para que estos cuiden al resto. "
            "No se debe causar perjuicio a lo importante en detrimento de lo secundario, ni a lo noble "
            "por amor a lo que es vil."
        ),
        "imagen": (
            "“Al pie de la montaña, trueno. La imagen de la administración de los alimentos. El hombre "
            "noble es cuidadoso con sus palabras y mesurado para comer y beber”.\n\n"
            "El trueno bajo la montaña indica el movimiento de la vida que debe ser administrado con "
            "templanza. El carácter se cultiva moderando lo que sale de la boca (palabras) y lo que "
            "entra en ella (comida y bebida), siguiendo un modelo de equilibrio."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Dejas irse tu tortuga mágica, y me miras con las comisuras "
                "de tus labios caídas. Desgracia”.\n"
                "La tortuga mágica simboliza a alguien que podría vivir libre e independiente por sus "
                "propios medios. Sin embargo, renuncia a esa autonomía para mirar con envidia y descontento "
                "a otros. Esta envidia mezquina provoca burla y malos resultados."
            ),
            2: (
                "Seis en el segundo lugar significa: “Dirigirse a la cumbre por alimentación, desviándose "
                "del camino para buscar alimentos provenientes de la colina. Continuar haciéndolo trae desgracia”.\n"
                "Alguien que no puede mantenerse a sí mismo busca que otros lo hagan por él, eludiendo su "
                "obligación de ganarse la vida. Este comportamiento es indigno y aparta al ser de su verdadera "
                "naturaleza, llevando inevitablemente a la desgracia."
            ),
            3: (
                "Seis en el tercer lugar significa: “Apartándose del alimento. La perseverancia trae desgracia. "
                "No actúes así durante diez años. Nada es ventajoso”.\n"
                "Quien busca placeres que no nutren cae en un círculo vicioso de insatisfacción. La búsqueda "
                "ciega de los sentidos jamás conduce a la meta. Es un tiempo de esterilidad donde nada de "
                "lo que se emprenda resultará bien."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Volviéndose hacia la cumbre para obtener alimentos trae "
                "buena fortuna. Acechando, con ojos penetrantes como los de un tigre, con un deseo insaciable. "
                "No hay reproches”.\n"
                "Representa a alguien en posición elevada que se esfuerza por hacer brillar su luz y necesita "
                "ayuda para alcanzar fines superiores. Aunque su deseo es intenso como el de un tigre, su "
                "actitud es irreprochable porque busca el bien de la comunidad."
            ),
            5: (
                "Seis en el quinto lugar significa: “Desviarse del camino. Perseverar trae la buena fortuna. "
                "No se debe atravesar la gran corriente”.\n"
                "Uno debe ser consciente de sus propias deficiencias. Si faltan fuerzas, hay que pedir consejo "
                "a alguien elevado espiritualmente. Manteniendo esta disposición de humildad se obtiene "
                "fortuna, pero no se deben emprender grandes acciones por cuenta propia."
            ),
            6: (
                "Nueve en la cima significa: “La fuente de la nutrición. Tomar consciencia del peligro trae "
                "buena fortuna. Es ventajoso atravesar la gran corriente”.\n"
                "Describe a un sabio de cuya influencia emanan los sustentos para los demás. Su posición conlleva "
                "una gran responsabilidad. Si permanece consciente de este peso, podrá emprender con éxito "
                "obras grandes y difíciles, trayendo alegría general."
            )
        },
        "lineas": {
            1: "No envidies a otros; valora tu propia capacidad de ser independiente.",
            2: "Evita depender de los demás eludiendo tus propias responsabilidades.",
            3: "El placer vacío no nutre; salir del círculo vicioso de los sentidos.",
            4: "Ambición legítima cuando el fin es el bienestar de la comunidad.",
            5: "Reconocer las limitaciones propias y buscar guía espiritual.",
            6: "El sabio nutre a los demás; responsabilidad que permite grandes obras."
        }
    },
    28: {
        "nombre": "TA KUO / EL GRAN SOBREPESO (La preponderancia de lo grande)",
        "trigrama_sup": "Tui. Lo Gozoso, Lago",
        "trigrama_inf": "Sun. Lo Suave, Viento, Madera",
        "exposicion": (
            "El hexagrama representa una viga gruesa y pesada en el centro pero demasiado débil en los "
            "extremos. Esta estructura no es duradera y debe transformarse, de lo contrario el desastre "
            "amenaza. Hay cuatro trazos fuertes en el interior y dos débiles en el exterior, lo que genera "
            "un estado de carga excesiva para la fuerza que debe soportarla."
        ),
        "juicio": (
            "“El gran exceso de peso. La viga cumbrera se inclina por sí misma. Es ventajoso tener donde ir. Éxito”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Se trata de una situación excepcional que requiere medidas extraordinarias. Es necesario encontrar "
            "un camino de transición rápidamente. No se obtendrá nada con medidas forzadas o violentas; hay "
            "que proceder con suavidad, desatando los nudos y penetrando el sentido de la situación. Esto "
            "exige una real superioridad."
        ),
        "imagen": (
            "“El lago crece por encima de los árboles. La imagen del gran sobrepeso. El hombre noble no se "
            "inquieta cuando está solo ni se deja desanimar si debe renunciar al mundo”.\n\n"
            "Tiempos semejantes a una inundación. El árbol (Sun) resiste aun estando aislado, y la serenidad "
            "alegre (Tui) nunca se desalienta. Es la actitud de quien mantiene su integridad a pesar de "
            "las circunstancias externas extremas."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Colocar debajo juncos blancos. Sin reproches”.\n"
                "Ante una acción en tiempos excepcionales, se debe proceder con extrema precaución. Como poner "
                "una estera para impedir que algo pesado rompa el suelo. Esta prudencia exagerada asegura el "
                "éxito de una empresa extraordinaria."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Un sauce seco retoña en sus raíces. Un hombre viejo "
                "toma una esposa joven. Todo es ventajoso”.\n"
                "Representa una reanimación extraordinaria del proceso de crecimiento. En tiempos difíciles "
                "debemos unirnos incluso con personas de condiciones diferentes, pues en ellos reside la "
                "posibilidad de renovación."
            ),
            3: (
                "Nueve en el tercer lugar significa: “La viga cumbrera se rompe. Desgracia”.\n"
                "Una persona que en tiempos de gran tensión insiste en empujar y adelantarse a todo coste. "
                "No acepta advertencias y la carga termina por quebrar la estructura. Intentar forzar el "
                "avance en estos momentos solo acarrea la catástrofe."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La viga cumbrera está apuntalada. Buena fortuna. Si hay "
                "intenciones ocultas, es humillante”.\n"
                "Relaciones con gente de rango inferior permiten conseguir el control de la situación. Pero "
                "si se abusa de esas relaciones para el éxito personal en lugar del bienestar general, el "
                "resultado será la humillación."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Un álamo marchito produce flores. Una mujer vieja toma "
                "marido. Sin reproches. Sin alabanzas”.\n"
                "Un esfuerzo que agota las fuerzas sin renovarlas. Todo permanece estéril. Mantener solo "
                "relaciones con los superiores en tiempos de incertidumbre crea una situación que no es perdurable."
            ),
            6: (
                "Seis en la cima significa: “Se debe atravesar el agua. Pero el agua sobrepasa la cabeza. "
                "Desgracia. Sin reproches”.\n"
                "Lo extraordinario ha llegado al colmo. Se tiene el coraje de alcanzar la meta a todo precio, "
                "aunque se arriesgue la vida. Morir por hacer triunfar lo justo es irreprochable: hay cosas "
                "más importantes que la vida."
            )
        },
        "lineas": {
            1: "Extrema precaución inicial para asegurar el éxito.",
            2: "Renovación a través de uniones inusuales pero fértiles.",
            3: "Peligro de colapso por terquedad y exceso de presión.",
            4: "Apoyo externo para estabilizar la carga; evitar el egoísmo.",
            5: "Esfuerzo vistoso pero que no genera una renovación real.",
            6: "Sacrificio valiente por una causa noble; el infortunio no es falta."
        }
    },
    29: {
        "nombre": "K’AN / LO INSONDABLE (el abismo, el agua)",
        "trigrama_sup": "K'an, El Abismo, Agua",
        "trigrama_inf": "K'an, El Abismo, Agua",
        "exposicion": (
            "Se compone de la repetición del trigrama K’an, siendo uno de los hexagramas dobles. "
            "K’an significa la acción de hundirse bruscamente. La línea fuerte (yang) está encerrada "
            "entre dos débiles (yin), como el agua en un canal estrecho. Representa el corazón, el alma "
            "o la razón encerrada en el cuerpo; el principio de la luz incluido en lo tenebroso."
        ),
        "juicio": (
            "“Lo insondable repetido. Si eres sincero, conseguirás lo que quieres y obtendrás el éxito "
            "en lo que hagas”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "A través de la repetición del peligro, uno se acostumbra a él. El agua da el ejemplo: va "
            "y viene, llena todos los espacios y no retrocede ante ninguna caída, permaneciendo fiel "
            "a su naturaleza esencial. Si uno comprende el sentido de la situación y se adapta con "
            "sinceridad, encontrará la acción que lo lleve al éxito."
        ),
        "imagen": (
            "“Las aguas fluyen ininterrumpidamente y llegan a su meta: la imagen de lo insondable repetido. "
            "El hombre noble camina a través de la virtud y ejerce la función de la enseñanza”.\n\n"
            "El agua llega a su meta fluyendo sin interrupción y llenando cada cavidad antes de seguir. "
            "El hombre noble adopta una conducta sólida y constante; solo mediante la repetición y la "
            "consistencia lo bueno se convierte en una propiedad permanente del carácter."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Repetición de lo insondable. En lo insondable uno cae en un "
                "abismo. Desgracia”.\n"
                "Acostumbrarse al peligro de forma pasiva hace que el hombre lo integre como parte de sí "
                "mismo. Al familiarizarse con lo malo, se pierde el buen camino y el infortunio es la "
                "consecuencia natural."
            ),
            2: (
                "Nueve en el segundo lugar significa: “El abismo es peligroso. Uno debe esforzarse solamente "
                "para obtener pequeñas cosas”.\n"
                "En situaciones de peligro no hay que intentar librarse de inmediato sin medir consecuencias. "
                "Se debe mantener la calma y conformarse con logros mínimos al principio, tal como un chorro "
                "de agua necesita tiempo para abrirse camino hacia el espacio libre."
            ),
            3: (
                "Seis en el tercer lugar significa: “Adelante o atrás, abismo sobre abismo. En un peligro "
                "como éste, hacer una pausa y esperar, de otra manera caerás en un hoyo en el abismo. No "
                "te conduzcas así”.\n"
                "Cualquier movimiento, adelante o atrás, es peligroso. No debemos dejarnos arrastrar a la "
                "acción por desesperación, ya que solo lograríamos hundirnos más. Es imperativo detenerse "
                "y esperar hasta que se insinúe una salida."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Un jarra de vino, una escudilla de arroz. Simples "
                "vasijas de barro tendidas a través de la ventana. Por cierto que no hay reproche en ello”.\n"
                "En tiempos de crisis, las formas exteriores se simplifican al extremo. Lo que importa es "
                "la disposición interior sincera. Para aclarar una situación difícil, se debe proceder con "
                "simplicidad a partir de lo que es perfectamente claro y evidente."
            ),
            5: (
                "Nueve en el quinto lugar significa: “El abismo no está lleno hasta desbordar sino que solo "
                "está lleno hasta la orilla. Sin reproches”.\n"
                "El peligro surge de querer ir demasiado alto. Se debe buscar la línea de menor resistencia "
                "para alcanzar la meta. En esta etapa no se deben acometer grandes tareas, basta con lo necesario "
                "para alejar el peligro."
            ),
            6: (
                "Seis en la cúspide significa: “Limitado con cuerdas y cables, encerrado en entre los muros "
                "de una prisión erizada de púas. Por tres años no se logra encontrar el camino. Desgracia”.\n"
                "Representa a alguien que ha perdido el buen camino en momentos de peligro extremo y permanece "
                "aferrado a sus errores. Se encuentra bloqueado y sin perspectiva de salida, como un criminal "
                "en una prisión de la que no puede escapar."
            )
        },
        "lineas": {
            1: "Peligro de normalizar lo malo y perder el rumbo.",
            2: "En el peligro, avanza con pasos pequeños y calma.",
            3: "No fuerces el movimiento; la pausa es necesaria para no caer más hondo.",
            4: "La sinceridad y la simplicidad son más valiosas que las formas complicadas.",
            5: "Busca el camino de menor resistencia; no intentes desbordar tus límites.",
            6: "Extravío total y falta de libertad por persistir en el error."
        }
    },
    30: {
        "nombre": "LI / LO ADHERENTE (Lo oscilante, el fuego)",
        "trigrama_sup": "Li, Lo Oscilante, Fuego",
        "trigrama_inf": "Li, Lo Oscilante, Fuego",
        "exposicion": (
            "Es un hexagrama doble. El trigrama Li significa 'sujetarse a algo', 'estar condicionado', "
            "'reposar sobre algo' y 'claridad'. Representa a la hija del medio. El fuego no tiene forma "
            "definida, pero oscila para intentar quemar el objeto que alumbra. Mientras que Kan (el agua) "
            "significa el alma encerrada, Li significa el esplendor de la naturaleza."
        ),
        "juicio": (
            "“Lo que adhiere. La perseverancia es ventajosa. Ella trae el éxito. Cuidar la vaca trae "
            "buena fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Todo lo brillante necesita algo que perdure para no ser consumido enteramente. El hombre "
            "obtiene el éxito cuando reconoce sus limitaciones y se coloca en dependencia con las fuerzas "
            "benefactoras del universo. La vaca simboliza la extrema docilidad; cultivando esa actitud, "
            "el hombre encuentra su lugar en el mundo."
        ),
        "imagen": (
            "“Lo que brilla se eleva dos veces: la imagen del fuego. El gran hombre ilumina las cuatro "
            "regiones del mundo perpetuando esta claridad”.\n\n"
            "Representa el movimiento repetido del sol y la función de la luz con respecto al tiempo. "
            "El hombre noble continúa el trabajo de la naturaleza extendiendo la claridad de su ser "
            "para que penetre profundamente en la naturaleza humana."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Las huellas se entrecruzan. Si alguien lo intenta seriamente "
                "no habrá error”.\n"
                "Al comienzo de la actividad, la prisa prevalece y las impresiones se entrecruzan. Es vital "
                "preservar la compostura y no dejarse llevar por la agitación. Mantenerse serio y compuesto "
                "al inicio es la simiente necesaria para lo que vendrá después."
            ),
            2: (
                "Seis en el segundo lugar significa: “Luz dorada. Suprema fortuna”.\n"
                "Representa el mediodía, cuando el sol brilla con luz dorada. El dorado es el color de la "
                "medida y el entendimiento, el símbolo de la cultura y el arte en su suprema armonía y equilibrio."
            ),
            3: (
                "Nueve en el tercer lugar significa: “En la luz del sol poniente el hombre puede sentir "
                "palpitar su marmita y cantar y escuchar suavemente cómo se aproxima la vejez. Desgracia”.\n"
                "La vida es transitoria. Capturado por obligaciones o por la melancolía de la vejez, el hombre "
                "pierde su libertad. El hombre noble debe cultivar su interior y aprovechar cada momento, "
                "entendiendo que la muerte llegará tarde o temprano, asegurando así su destino."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Viene de repente. Arde, muere, es rechazado”.\n"
                "La claridad de la inteligencia puede consumir la vida si no tiene raíces. Es la imagen de un "
                "meteoro o un fuego de paja: alguien inquieto y excitable que destaca rápido pero no deja "
                "efectos duraderos. Es malo malgastarse y consumirse de forma tan abrupta."
            ),
            5: (
                "Seis en el quinto lugar significa: “Torrentes de lágrimas, suspiros y lamentos. Buena fortuna”.\n"
                "Es la culminación de la vida. Ante la vanidad de las cosas, uno puede abandonar la esperanza "
                "y el temor para conservar la claridad interior. Se trata de una verdadera conversión personal "
                "que cambia la aflicción en fortuna duradera."
            ),
            6: (
                "Nueve en la cima significa: “El rey lo emplea para vigilar y castigar. Es mejor matar a los "
                "dirigentes y capturar a los subordinados. Sin reproches”.\n"
                "El castigo debe crear disciplina, no solo penalizar. Es mejor eliminar la raíz del mal (los jefes) "
                "y perdonar a los seguidores. Para perfeccionarse, uno debe eliminar sus malos hábitos "
                "principales y ser tolerante con las faltas inofensivas."
            )
        },
        "lineas": {
            1: "Preserva la compostura ante la agitación del comienzo.",
            2: "Equilibrio y entendimiento supremo; el momento de mayor claridad.",
            3: "Acepta la transitoriedad de la vida sin caer en la melancolía.",
            4: "Evita el brillo fugaz y destructivo como el de un meteoro.",
            5: "La tristeza por la vanidad del mundo lleva a una conversión real.",
            6: "Disciplina justa: elimina el mal de raíz pero sé tolerante con lo menor."
        }
    },
    31: {
        "nombre": "HSIEN / LA INFLUENCIA (El galanteo)",
        "trigrama_sup": "Tui, Lo Gozoso, Lago",
        "trigrama_inf": "Ken, La Inmovilidad, la Montaña.",
        "exposicion": (
            "El nombre significa 'universal', 'general' e influir o estimular. El trigrama inferior Ken (la montaña) "
            "es fuerte y sensibiliza al superior Tui (el lago), que es débil, mediante una acción persistente. "
            "Representa la mutua y universal atracción entre los sexos. Así como la primera parte del libro "
            "comienza con el cielo y la tierra, la segunda comienza con el cortejo y el matrimonio como "
            "fundamentos de la vida social."
        ),
        "juicio": (
            "“Influencia. Éxito. La perseverancia es ventajosa. Tomar una doncella como esposa trae buena fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Todo triunfo se funda en fuerzas de atracción mutua. El éxito proviene de una tranquilidad interior "
            "acompañada de alegría exterior, manteniendo la satisfacción dentro de límites justos. Al reconocer "
            "las propias limitaciones y depender de fuerzas universales armoniosas, se logra el éxito. La docilidad "
            "y la dependencia voluntaria permiten encontrar el lugar de uno en el mundo."
        ),
        "imagen": (
            "“Sobre la montaña hay un lago: la imagen de la influencia. Por su disposición a recibir el sabio "
            "hace que los hombres se le acerquen”.\n\n"
            "Una montaña con un lago en su cima se estimula por su humedad. La imagen aconseja estar "
            "interiormente dispuesto y libre, permaneciendo receptivo a los buenos consejos. Quien pretende "
            "saberlo todo deja rápidamente de ser aconsejado."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “La influencia se manifiesta a sí misma en el dedo grande del pie”.\n"
                "El movimiento apenas se inicia. La intención está presente pero no es evidente para los demás "
                "ni tiene efectos visibles todavía. No conlleva en sí misma ni bien ni mal para el mundo exterior."
            ),
            2: (
                "Seis en el segundo lugar significa: “La influencia se manifiesta en las pantorrillas. Desgracia. "
                "Demorarse trae buena fortuna”.\n"
                "Un movimiento que no es autónomo y sigue a otros suele traer infortunio. Es mejor esperar "
                "tranquilamente hasta que una influencia efectiva guíe hacia la acción real."
            ),
            3: (
                "Nueve en el tercer lugar significa: “La influencia se muestra en los muslos. Detiene al que sigue. "
                "Continuar es humillante”.\n"
                "Actuar por impulsos del corazón o caprichos de otros es humillante. No se debe correr "
                "precipitadamente tras aquellos sobre quienes se desea influir; a veces es necesario retirarse "
                "y no renunciar a la libertad de reprimir los impulsos."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La perseverancia trae buena fortuna. Los remordimientos "
                "desaparecen. Si un hombre tiene su mente agitada y sus pensamientos van de un lado a otro, "
                "sólo lo seguirán los amigos hacia los cuales dirige pensamientos conscientes”.\n"
                "Se alcanza el dominio del corazón. La influencia debe ser buena y constante para evitar la "
                "versatilidad de sentimientos. Una influencia deliberada para manipular solo provoca agitación "
                "emocional limitada."
            ),
            5: (
                "Nueve en el quinto lugar significa: “La influencia se manifiesta en la nuca. Sin remordimientos”.\n"
                "La nuca es la parte más rígida; aquí la influencia no lleva a la confusión pero tampoco penetra "
                "profundamente. Si uno no puede ser influenciado en su profundidad consciente, tampoco podrá "
                "influir significativamente en el mundo exterior."
            ),
            6: (
                "Seis en la cima significa: “La influencia se manifiesta en las mandíbulas, las mejillas y la lengua”.\n"
                "Es la manera más superficial de influir: mediante meras palabras sin apoyo en algo real. Esta "
                "excitación vocal permanece insignificante y no agrega nada concerniente al bien o al mal."
            )
        },
        "lineas": {
            1: "Intención naciente sin efectos visibles todavía.",
            2: "Evita movimientos impulsivos; espera una influencia efectiva.",
            3: "No cedas a caprichos ni actúes por impulsos precipitados.",
            4: "La perseverancia y el dominio del corazón atraen amigos afines.",
            5: "Falta de profundidad en la influencia recibida y ejercida.",
            6: "Influencia superficial basada solo en palabras vacías."
        }
    },
    32: {
        "nombre": "HENG / LA DURACIÓN",
        "trigrama_sup": "Chen, Lo que Despierta, Trueno",
        "trigrama_inf": "Sun, Lo Suave, Viento.",
        "exposicion": (
            "Este hexagrama es lo inverso del precedente, 'la influencia'. Aquí la unión es un estado durable. "
            "Representa al hijo mayor (Chen, el Trueno) arriba y a la hija mayor (Sun, el Viento) abajo. "
            "Indica suavidad en el interior y movimiento en el exterior. Aplicado a lo social, representa "
            "el matrimonio como institución duradera donde el marido da dirección e impulso mientras la "
            "mujer permanece suave y obediente."
        ),
        "juicio": (
            "“Duración. Éxito. Sin reproches. La perseverancia es ventajosa. Conviene tener donde ir”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La duración no es un estado de descanso o detención, sino un movimiento que se cumple siguiendo "
            "leyes determinadas y se renueva constantemente. Es un movimiento organizado donde todo fin es "
            "seguido por un nuevo comienzo, como las órbitas de los cuerpos celestes o el desarrollo de las estaciones. "
            "Permite reconocer la naturaleza de todos los seres en el cielo y la tierra."
        ),
        "imagen": (
            "“Trueno y viento: La imagen de la duración. El hombre noble permanece firme y no cambia de dirección”.\n\n"
            "Aunque el trueno fluctúa y el viento sopla, las leyes que gobiernan su aparición son durables. "
            "La independencia del hombre noble no se basa en la rigidez, sino en una conducta sin desvíos "
            "determinada por la ley interna de su ser, transformándose con los cambios del tiempo."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Buscar la duración prematuramente trae desgracia persistente. "
                "Nada que sea provechoso”.\n"
                "Lo que dura se crea gradualmente con trabajo largo y reflexión asidua. Quien exige demasiado "
                "en un primer intento actúa de manera precipitada y no obtendrá nada."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Los remordimientos desaparecen”.\n"
                "Aunque la situación sea anormal y el hombre fuerce su carácter más allá de sus posibilidades, "
                "en la época de la duración puede controlar su energía interior para no desgastarse en exceso. "
                "Así desaparecen los motivos de arrepentimiento."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Quien no da duración a su carácter se encuentra con la desgracia. "
                "Humillación persistente”.\n"
                "Inconsistencia provocada por esperanzas o temores externos. El hombre se olvida de su propia "
                "consistencia interna, lo que lleva invariablemente a experiencias desastrosas y humillaciones "
                "que nacen de su propia naturaleza."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “No hay caza en el campo”.\n"
                "Para dar en el blanco hay que efectuar las acciones convenientes. Si no se busca de la manera "
                "correcta, persistir por mucho tiempo no será suficiente para encontrar lo que se busca."
            ),
            5: (
                "Seis en el quinto lugar significa: “Dar duración al propio carácter a través de la perseverancia. "
                "Esto es buena fortuna para la mujer e infortunio para el hombre”.\n"
                "La persistencia conforma a la mujer, pero el hombre debe ser flexible y adaptable según el deber "
                "del momento. Para él, acordar constantemente su conducta a una norma fija sin adaptarse a las "
                "circunstancias sería un error."
            ),
            6: (
                "Seis en la cima significa: “La impaciencia como condición duradera trae mala fortuna”.\n"
                "La perpetua impaciencia impide toda profundidad moral y se convierte en un peligro, "
                "especialmente para quienes están en posición de autoridad."
            )
        },
        "lineas": {
            1: "No fuerces resultados; la duración requiere tiempo y trabajo asiduo.",
            2: "Controla tu energía interior para evitar el desgaste innecesario.",
            3: "La falta de consistencia interna lleva a la humillación.",
            4: "La persistencia es inútil si no se busca de la manera correcta.",
            5: "El hombre debe ser flexible y adaptable; la mujer debe conservar la tradición.",
            6: "La impaciencia impide el desarrollo moral y genera peligro."
        }
    },
    33: {
        "nombre": "TUN / EL RETIRO (El repliegue)",
        "trigrama_sup": "Ch'ien, Lo Creativo, Cielo",
        "trigrama_inf": "Ken, La Inmovilidad, la Montaña.",
        "exposicion": (
            "El poder de la oscuridad está en ascenso y la luz se retira para ponerse en seguridad. "
            "Retirarse aquí no es una debilidad, sino una ley natural y la manera correcta de actuar "
            "para no desgastar las fuerzas. Evoca la idea de no resistir al mal para no quedar atrapado "
            "en su dinámica destructiva."
        ),
        "juicio": (
            "“Retirada. Éxito. En lo pequeño, la perseverancia es ventajosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La retirada es el camino al éxito cuando las fuerzas hostiles avanzan favorecidas por la época. "
            "No debe confundirse con una huida desesperada; es una retirada activa donde se mantiene la "
            "fuerza y la posición, dificultando el avance del adversario y preparando ya la contra-ofensiva."
        ),
        "imagen": (
            "“Montaña bajo el cielo: la imagen de la retirada. El hombre noble mantiene al hombre inferior "
            "a distancia, sin cólera pero con reserva”.\n\n"
            "El cielo se retira hacia lo alto permaneciendo inalcanzable para la montaña. El hombre noble "
            "se recoge en sí mismo, superando al hombre vulgar. No lo odia, pues el odio lo ligaría a él; "
            "con dignidad y reserva, obliga al inferior a quedarse inmóvil."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “En la cola durante la retirada. Es peligroso. No debe "
                "desearse emprender nada”.\n"
                "Al estar en la 'cola' de la retirada, se está en contacto directo con los perseguidores. "
                "En esta posición vulnerable, lo más prudente es detenerse y no intentar ninguna empresa, "
                "buscando solo la oportunidad de escapar del peligro."
            ),
            2: (
                "Seis en el segundo lugar significa: “Lo retiene firmemente con un cuero de buey amarillo. "
                "Nadie puede hacerle soltar la presa”.\n"
                "Representa a un hombre vulgar que se aferra con fuerza a los hombres superiores mientras "
                "estos se retiran. Como lo que pretende es justo y conforme al deber (amarillo), logra "
                "alcanzar su cometido de no ser abandonado."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Una retirada interrumpida es molesta y peligrosa. "
                "Retener a la gente tales que sirvientes y criados trae buena fortuna”.\n"
                "Si el momento de retirarse llega y uno es retenido, se pierde la libertad de acción. "
                "La solución es tomar al servicio a quienes impiden el retiro para mantener la iniciativa "
                "y no quedar indefenso bajo su poder, aunque no sea una situación placentera."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La retirada voluntaria trae buena fortuna al hombre "
                "noble y ruina al hombre vulgar”.\n"
                "El hombre noble acepta la separación de forma amistosa y se adapta sin violencia a sus "
                "convicciones. El hombre vulgar, al perder la guía del noble por quien se siente atraído, "
                "sufre el deterioro y la ruina."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Retirada amistosa. La perseverancia trae buena fortuna”.\n"
                "Es el momento oportuno para retirarse de forma resuelta y amistosa, sin dar lugar a "
                "explicaciones desagradables. Se requiere firmeza absoluta en la resolución para no "
                "extraviarse con argumentos irrelevantes."
            ),
            6: (
                "Nueve en la cima significa: “Retirada alegre. Todo es favorable”.\n"
                "La situación es clara y el desprendimiento interior es total. Se goza de la libertad "
                "de partir con una alegre tranquilidad en el alma. Al elegir sin titubeos el camino "
                "más conveniente, todo resulta favorable."
            )
        },
        "lineas": {
            1: "Peligro por estar en contacto directo con el perseguidor; no emprendas nada.",
            2: "Firmeza en la voluntad de seguir al superior; el éxito es para el que se aferra.",
            3: "Situación molesta por ser retenido; busca soluciones prácticas aunque sean incómodas.",
            4: "El noble se retira con dignidad; el vulgar se arruina sin su guía.",
            5: "Retirada firme y amistosa en el momento justo; evita discusiones innecesarias.",
            6: "Libertad y tranquilidad total en el retiro; el camino más favorable."
        }
    },
    34: {
        "nombre": "TA CHUANG / EL PODER DE LO GRANDE",
        "trigrama_sup": "Chen, Lo que Despierta, Trueno",
        "trigrama_inf": "Ch'ien Lo Creativo, Cielo",
        "exposicion": (
            "Cuatro líneas luminosas entran por abajo y se aprestan a proseguir su ascensión. "
            "El trigrama superior es Chen (el trueno) y el inferior es Ch'ien (el cielo). "
            "Lo creativo es fuerte y lo que despierta incita al movimiento; la unión de fuerza "
            "y movimiento da el sentido de 'poder de lo grande'. Este hexagrama está asignado "
            "al 2° mes (abril-mayo)."
        ),
        "juicio": (
            "“El Poder de lo grande. La perseverancia es ventajosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Se refiere a una época donde el valor interior sube con fuerza y llega al poder. "
            "Existe el riesgo de confiar demasiado en la propia fuerza sin preguntarse dónde "
            "está el bien. Para que el poder no degenere en pura violencia, debe permanecer "
            "unido a los principios del derecho y la justicia."
        ),
        "imagen": (
            "“Trueno está arriba, en el cielo. La imagen del poder de lo grande. El hombre "
            "noble no marcha por caminos que no están conformes con el orden”.\n\n"
            "El trueno en el cielo produce gran poder en armonía con el movimiento celestial. "
            "La verdadera grandeza reside en la conformidad con lo que es justo; por ello, "
            "en tiempos de gran poder, el hombre noble evita lo que no está en armonía con el orden."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Poder en los Pies. Continuar trae desgracia. "
                "Eso es ciertamente verdadero”.\n"
                "Los pies están en la posición más baja listos para avanzar. Al ocupar un lugar inferior, "
                "el gran poder tiende a provocar un movimiento hacia adelante por la fuerza; si se "
                "continúa así, seguramente llevará al infortunio."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Perseverancia trae buena fortuna”.\n"
                "Las puertas al éxito comienzan a entreabrirse y se avanza rápidamente. Es un punto "
                "donde es fácil caer en la presunción exagerada. El equilibrio interior sin el uso "
                "exclusivo del poder es lo que trae la buena fortuna."
            ),
            3: (
                "Nueve en el tercer lugar significa: “El hombre vulgar actúa usando la fuerza, el "
                "hombre noble no actúa así. Continuar es peligroso. Un chivo arremete contra "
                "un cerco y sus cuernos quedan atrapados”.\n"
                "Jactarse del poder lleva a complicaciones. El hombre noble permanece consciente "
                "del peligro de avanzar sin precaución y sabe renunciar a tiempo a desplegar "
                "abiertamente su fuerza, a diferencia del hombre vulgar que se deja embriagar por el triunfo."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Perseverancia trae buena fortuna. Los "
                "remordimientos disminuyen. El cerco se abre sin complicaciones. El poder radica "
                "en el eje de un gran carro”.\n"
                "Trabajando con calma, las resistencias ceden y el éxito se alcanza. No es necesario "
                "que la fuerza se manifieste exteriormente; mientras menos se exterioriza, más "
                "potentes son sus efectos, como el eje que mueve el carro."
            ),
            5: (
                "Seis en el quinto lugar significa: “Pierde el chivo fácilmente. Sin remordimientos”.\n"
                "En esta situación todo se hace fácil y no hay más resistencias. Se puede entonces "
                "abandonar la naturaleza belicosa (semejante a la del chivo) y no habrá de qué arrepentirse."
            ),
            6: (
                "Seis en la cima significa: “Un chivo embiste un cerco. No puede avanzar ni "
                "retroceder. Nada es ventajoso. Pero si se reconoce la dificultad, eso trae la "
                "buena fortuna”.\n"
                "Si nos aventuramos demasiado lejos podemos estancarnos. La obstinación acarrea "
                "dificultades insuperables. Si se analiza la situación, uno se apacigua y decide "
                "no continuar, todo se corregirá en el momento oportuno."
            )
        },
        "lineas": {
            1: "No fuerces el avance desde una posición inferior; traerá infortunio.",
            2: "El éxito requiere equilibrio interior, no solo el uso de la fuerza.",
            3: "No te jactes de tu poder ni actúes por impulso como el hombre vulgar.",
            4: "La fuerza interior y calmada vence resistencias sin necesidad de exhibirse.",
            5: "Abandona la actitud belicosa; la situación se ha vuelto favorable.",
            6: "Si te estancas por obstinación, detente y analiza para corregir el rumbo."
        }
    },
    35: {
        "nombre": "CHIN / EL PROGRESO",
        "trigrama_sup": "Li, Lo Oscilante, Fuego",
        "trigrama_inf": "K'un, Lo Receptivo, Tierra.",
        "exposicion": (
            "Representa el sol naciendo sobre la tierra. Es el símbolo de la rapidez, del progreso "
            "rápido y fácil que al mismo tiempo significa claridad y expansión creciente y amplia."
        ),
        "juicio": (
            "“Progreso. El Príncipe Poderoso es honrado con numerosos de caballos. En un solo día "
            "es recibido tres veces en audiencia”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Se describe un progreso basado en un caudillo que posee claridad interior para no abusar "
            "de su influencia. Los demás lo siguen de buena voluntad. Un soberano libre de celos lo atrae "
            "a su corte; un gobernante esclarecido y un servidor obediente son las condiciones de un "
            "gran progreso."
        ),
        "imagen": (
            "“El sol nace sobre la tierra. La imagen del Progreso. El hombre noble hace brillar por "
            "sí mismo sus propias disposiciones luminosas”.\n\n"
            "La luz del sol se desprende de las sombras y brilla con pureza. La verdadera naturaleza humana "
            "es buena en su origen, pero debe ser purificada del elemento terrestre para brillar con su "
            "claridad primitiva."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Progresando, pero volviendo atrás. La perseverancia trae buena fortuna. "
                "Si alguien no encuentra confianza debe permanecer en calma. Sin error”.\n"
                "En inicios inciertos, es común dudar o sufrir rechazo. Lo simple es continuar haciendo lo correcto; "
                "permanecer en calma y sin temor evita la ansiedad y el error."
            ),
            2: (
                "Seis en el segundo lugar significa: “Progresando pero con tristeza. La perseverancia trae buena fortuna. "
                "Se obtiene gran felicidad de un antepasado”.\n"
                "El progreso se detiene por falta de unión con quien ocupa el poder. Si se persevera con dulzura, "
                "se recibirá una felicidad merecida basada en principios firmes y no en motivos egoístas."
            ),
            3: (
                "Seis en el tercer lugar significa: “Todos están de acuerdo. El remordimiento desaparece”.\n"
                "Avanzar en compañía de otros cuyo acuerdo nos alienta. No hay motivo de remordimiento, "
                "pues no se necesita una autonomía total para triunfar contra el destino."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Progresa como una ardilla. La perseverancia trae peligro”.\n"
                "Hombres fuertes que ocupan lugares que no merecen para amasar bienes. Esta conducta es tenebrosa. "
                "Obstinarse en actuar así bajo la luz del progreso trae necesariamente peligro."
            ),
            5: (
                "Seis en el quinto lugar significa: “Los remordimientos desaparecen. No tomar a pecho ni la ganancia "
                "ni la pérdida. Las empresas traen buena fortuna. Todo sirve al progreso”.\n"
                "Alguien influyente que permanece gentil y reservado. No debe reprocharse el no haber aprovechado "
                "todas las ventajas; lo importante es asegurar obras ricas en bendiciones."
            ),
            6: (
                "Nueve en la cima significa: “Progresar arremetiendo (a cornadas) está permitido sólo con el propósito "
                "de castigar su propio dominio. Estar consciente del peligro trae buena fortuna. Sin reproches. "
                "La perseverancia trae humillación”.\n"
                "La agresividad solo se permite para enmendar errores propios. Usar esta energía contra extraños "
                "o sin estrecha relación lleva a la humillación."
            )
        },
        "lineas": {
            1: "Si no hay confianza inicial, mantén la calma y sigue haciendo lo correcto.",
            2: "Supera la tristeza con perseverancia y dulzura; la felicidad llegará.",
            3: "El consenso general permite avanzar sin remordimientos.",
            4: "Evita maniobras tenebrosas o acumular bienes indebidamente; hay peligro.",
            5: "No te obsesiones con ganancias o pérdidas; la gentileza trae éxito.",
            6: "Usa la energía agresiva solo para corregir fallas propias, no ajenas."
        }
    },
    36: {
        "nombre": "MING I / OSCURECIENDO LA LUZ",
        "trigrama_sup": "K'un, Lo Receptivo, Tierra.",
        "trigrama_inf": "Li, Lo Oscilante, Fuego.",
        "exposicion": (
            "El sol se ha hundido bajo la tierra y se ha oscurecido. El nombre significa literalmente "
            "'hiriendo a la luz'. Un hombre de naturaleza oscura está en posición de autoridad y trae "
            "perjuicio al hombre sabio y capaz. Es la situación inversa al progreso (35)."
        ),
        "juicio": (
            "“Oscureciendo la luz. En la adversidad conviene ser perseverante”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "No debemos dejarnos agobiar por circunstancias desfavorables ni doblegar nuestra resolución. "
            "Es posible superar la adversidad manteniendo la luz interior pero siendo flexible y adaptable "
            "al exterior. A veces hay que esconder la luz para hacer prevalecer la voluntad sin que se "
            "distinga desde afuera."
        ),
        "imagen": (
            "“La luz se ha sumergido en la tierra. La imagen de oscureciendo la luz. El hombre noble para "
            "vivir con la multitud vela su luz pero sigue brillando”.\n\n"
            "En tiempos de oscuridad, la cautela y la reserva son esenciales. No hay que despertar enemistad "
            "por conductas desconsideradas ni tratar de saberlo todo. Hay que dejar pasar las cosas como "
            "si hubiéramos sido engañados, manteniendo la integridad en silencio."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: «Oscureciendo la luz durante el vuelo. Abate sus alas. "
                "El hombre noble no come durante tres días en sus viajes, pero tiene un lugar donde ir. "
                "El huésped tiene ocasión de chismorrear acerca de él».\n"
                "El hombre resuelve superar obstáculos pero topa con un destino hostil. Se retrae y evade "
                "el enfrentamiento. Debe sufrir privaciones y, aunque tenga metas precisas, la gente hablará "
                "mal de él por no entenderlo."
            ),
            2: (
                "Seis en el segundo lugar significa: “El oscurecimiento de la luz le hace daño en el muslo "
                "izquierdo. Da ayuda con la fuerza de un caballo. Buena fortuna”.\n"
                "El hombre es herido por el Señor de la Oscuridad, pero la herida no es fatal. El rescate "
                "es posible si el herido no piensa en sí mismo, sino en salvar a los demás. La buena fortuna "
                "viene de actuar conforme al deber."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Oscureciendo la luz durante la caza en el sur. El gran "
                "caudillo es capturado. No debe esperarse perseverancia demasiado pronto”.\n"
                "Parece que la suerte trabaja a favor del hombre leal y logra capturar al caudillo del desorden. "
                "Sin embargo, no hay que apresurarse en eliminar todos los abusos de golpe; sería prematuro "
                "porque estos tienen raíces largas."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Penetra por el lado izquierdo del vientre. Se llega al "
                "verdadero corazón del oscurecimiento de la luz y se deja la puerta y la corte”.\n"
                "Se descubren los pensamientos más secretos de quien comanda la oscuridad. Al comprender que "
                "no hay esperanza de progreso, se está en condiciones de abandonar la escena del desastre "
                "antes de que estalle."
            ),
            5: (
                "Seis en el quinto lugar significa: “Oscureciendo la luz como en lo del príncipe Chi. "
                "La perseverancia fructifica”.\n"
                "Como el príncipe Chi, que fingió locura para mantener sus convicciones ante un tirano. Es un "
                "ejemplo de invencible perseverancia interior y prudencia extrema para no abandonar el puesto "
                "en tiempos de oscuridad."
            ),
            6: (
                "Seis en la cima significa: “No luz, sino oscuridad. Primero trepa hacia el cielo y luego "
                "cae en las profundidades de la tierra”.\n"
                "La oscuridad llega a su cúspide y hiere todo lo luminoso. Pero al final, el poder oscuro "
                "perece en su propia sombra justo cuando cree superar lo bueno, consumiendo la energía "
                "a la que debía su existencia."
            )
        },
        "lineas": {
            1: "Acepta las privaciones y las críticas mientras evades un destino hostil.",
            2: "A pesar de las heridas, enfócate en ayudar a otros; el rescate es posible.",
            3: "Logras una victoria sobre el desorden, pero no te apresures en los cambios.",
            4: "Al conocer la verdadera naturaleza del mal, retírate antes del desastre.",
            5: "Mantén tus convicciones en secreto mediante la prudencia y la disimulación.",
            6: "La oscuridad extrema termina consumiéndose a sí misma tras alcanzar su cima."
        }
    },
    37: {
        "nombre": "CHIA JEN / LA FAMILIA (El parentesco)",
        "trigrama_sup": "Sun Lo Suave, Viento",
        "trigrama_inf": "Li Lo Oscilante, Fuego",
        "exposicion": (
            "Representa las leyes que rigen dentro de la familia. La línea más alta representa al padre "
            "y la más baja al hijo. El quinto lugar es el esposo y el segundo la esposa. Las otras dos "
            "corresponden a un hermano y su mujer. La familia está regida por leyes que se aplican "
            "también al clan, al pueblo y al universo. Su influencia se representa por el viento que "
            "atiza el fuego."
        ),
        "juicio": (
            "“La familia. La perseverancia de la mujer es ventajosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El lazo que mantiene la unidad familiar es la fidelidad y la perseverancia de la mujer. "
            "Cuando cada miembro (padre, hijo, esposo, esposa) ocupa el lugar que le corresponde según "
            "las leyes de la naturaleza, reina el orden. La familia es la célula inicial de la sociedad, "
            "donde se sustentan los deberes morales y las relaciones humanas en general."
        ),
        "imagen": (
            "“El viento viene con fuerza del fuego. La imagen de la familia. El hombre noble da "
            "sustancia a sus palabras y duración a su manera de vivir”.\n\n"
            "El calor se transforma en fuerza (viento que sale del fuego). Para influir en otros, "
            "las palabras deben basarse en algo real y la conducta debe ser consecuente. "
            "Si las palabras y actitudes no concuerdan, no tendrán ninguna influencia ni efecto."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Neta distinción en el interior de la familia. Los "
                "remordimientos desaparecen”.\n"
                "Cada miembro debe conocer su lugar desde el principio. Los niños deben acostumbrarse "
                "a reglas precisas antes de contraer malas habitudes. Establecer el orden a tiempo "
                "evita reproches futuros."
            ),
            2: (
                "Seis en el segundo lugar significa: “Ella no debe seguir sus caprichos. Debe "
                "ocuparse de los alimentos en el interior. La perseverancia trae buena fortuna”.\n"
                "El lugar de la mujer está en el centro de la casa, cumpliendo con sus deberes inmediatos "
                "sin tratar de obtener nada por la fuerza. Su perseverancia trae buena fortuna a todo el hogar."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Cuando los ánimos se caldean en la familia la "
                "severidad excesiva acarrea remordimientos. La buena fortuna se aleja. Cuando mujer y "
                "niño retozan y ríen, al final conduce a la humillación”.\n"
                "Debe haber un justo medio. Aunque la severidad excesiva es preferible a la debilidad "
                "que conduce a la humillación, lo ideal es mantener la disciplina sin perder la "
                "libertad de movimiento de los individuos."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Ella es el tesoro de la casa. Inmensa fortuna”.\n"
                "Del bienestar de la dueña de casa depende la prosperidad de la familia. Cuando los gastos "
                "y los ingresos se equilibran mediante una intendencia correcta, se alcanza la gran fortuna."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Como un rey se acerca a su familia. Sin temor. "
                "Buena fortuna”.\n"
                "Representa a un hombre paternal dotado de riqueza interior. No hay que temerle porque "
                "el amor rige sus relaciones. Su naturaleza ejerce espontáneamente la influencia justa."
            ),
            6: (
                "Nueve en la cima significa: “Su trabajo inspira respeto. Al final llega la buena fortuna”.\n"
                "El orden familiar depende del carácter del dueño de casa. Si su influencia se impone "
                "por la fuerza de su verdad interior, todo marcha bien. Se deben asumir las "
                "responsabilidades espontáneamente."
            )
        },
        "lineas": {
            1: "Establece reglas claras desde el principio para evitar desorden futuro.",
            2: "Cúmple con tus deberes inmediatos con perseverancia y sin caprichos.",
            3: "Busca el equilibrio entre severidad e indulgencia; evita la debilidad extrema.",
            4: "La correcta administración y el bienestar interno traen prosperidad.",
            5: "El amor y la riqueza interior ejercen la mejor influencia en el entorno.",
            6: "Cultiva tu personalidad y verdad interior para inspirar respeto y orden."
        }
    },
    38: {
        "nombre": "K'UEI / LA OPOSICIÓN",
        "trigrama_sup": "Li Lo Oscilante, Llama",
        "trigrama_inf": "Tui Lo Gozoso, Lago",
        "exposicion": (
            "El hexagrama se compone del trigrama superior Li (fuego), que flamea hacia lo alto, "
            "y del inferior Tui (lago), cuya humedad se infiltra hacia lo bajo. Son dos movimientos "
            "en contraste directo. Representa a dos hijas que viven en la misma casa pero cuyos "
            "deseos divergen hacia distintos hombres."
        ),
        "juicio": (
            "“Oposición. En asuntos pequeños, buena fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Cuando hay oposición, no se pueden realizar grandes empresas comunes debido a puntos "
            "de vista divergentes. No debe procederse bruscamente; es mejor limitarse a producir "
            "efectos graduales en asuntos pequeños. La oposición es necesaria para establecer "
            "el orden mediante la diferencia por especies y categorías."
        ),
        "imagen": (
            "“Arriba, el fuego, abajo, el lago: la imagen de la oposición. En medio de cualquier "
            "compañía el hombre noble mantiene su individualidad”.\n\n"
            "El fuego y el agua nunca se mezclan y conservan sus esencias propias al estar en contacto. "
            "El hombre culto nunca permitirá asemejarse a aquellos cuya naturaleza difiere de la suya, "
            "manteniendo siempre su propia individualidad en las relaciones comunes."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Los remordimientos desaparecen. Si pierdes tu caballo, "
                "no corras tras él; volverá por su propia voluntad. Cuando veas gente malvada, "
                "protégete contra los errores”.\n"
                "No se debe buscar la unidad por la fuerza. Si algo nos pertenece por naturaleza, "
                "volverá espontáneamente. Ante el mal, lo importante es evitar errores propios "
                "y soportarlo con paciencia hasta que se retire."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Uno encuentra a su señor en una calle estrecha. "
                "Sin reproches”.\n"
                "A veces los malentendidos impiden que personas afines se reúnan formalmente. "
                "Un encuentro informal y casual puede servir para restablecer la conexión siempre "
                "que subsista la afinidad esencial."
            ),
            3: (
                "Seis en el tercer lugar significa: “Se ve que el carro tira en contra, los bueyes "
                "se detienen, un hombre con el pelo y la nariz cortados. No hay un buen comienzo "
                "pero sí un buen final”.\n"
                "A veces parece que todo conspira en contra y sufrimos vejaciones. A pesar de la "
                "oposición y de los castigos humillantes, debemos mantenernos unidos a quienes "
                "conocemos sus valores para tener un buen final."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Aislado por la oposición, uno encuentra a "
                "alguien de con ideas semejantes con el cual uno puede relacionarse en confianza. "
                "Ningún reproche a pesar del peligro”.\n"
                "Si en medio del aislamiento causado por una oposición interior se encuentra a "
                "alguien con similitudes fundamentales, es posible superar todos los peligros "
                "del aislamiento y lograr lo propuesto."
            ),
            5: (
                "Seis en el quinto lugar significa: “Los remordimientos desaparecen. El compañero "
                "encuentra su camino mordiendo a través de los velos. Si uno va hacia él ¿Cómo "
                "sería eso un error?”.\n"
                "Se reconoce a un compañero sincero a pesar de las diferencias externas. Él se "
                "abre paso rompiendo los velos que causan la separación; es un deber ir a su "
                "encuentro y trabajar con él."
            ),
            6: (
                "Nueve en la cima significa: “Aislado a través de la oposición, uno ve a su compañero "
                "como un cerdo cubierto de mugre, como un carro lleno de demonios. Primero se dispara "
                "el arco contra él. Después se deja el arco a un lado... llega la buena fortuna”.\n"
                "El aislamiento se debe a disposiciones interiores y malentendidos. Se adopta una "
                "actitud defensiva errónea hacia los amigos, pero al final la tensión se disuelve "
                "como la lluvia y la oposición se transforma en su contrario."
            )
        },
        "lineas": {
            1: "No fuerces la unión; lo que es afín volverá por sí mismo. Sé cauteloso ante el mal.",
            2: "Un encuentro informal puede solucionar malentendidos si hay afinidad esencial.",
            3: "Aunque enfrentes humillaciones y obstáculos, mantén tus valores para un buen final.",
            4: "En el aislamiento, la confianza en alguien con ideas afines ayuda a superar peligros.",
            5: "Ve al encuentro de quien demuestra su verdadera naturaleza rompiendo las barreras.",
            6: "Supera los prejuicios internos; al disolverse la tensión, la unión trae éxito."
        }
    },
    39: {
        "nombre": "CHIEN / EL OBSTÁCULO (La obstrucción)",
        "trigrama_sup": "K'an El Abismo, Agua",
        "trigrama_inf": "Ken La Inmovilidad, la Montaña.",
        "exposicion": (
            "El hexagrama pinta un abismo peligroso que se abre ante nosotros y muy cerca "
            "adelante nuestro una montaña que se levanta abrupta e inaccesible. Estamos "
            "rodeados por obstáculos. Pero la inmovilidad de la montaña sugiere la manera "
            "de liberarse: representar los obstáculos que aparecen en el tiempo pero que "
            "pueden y deben ser superados."
        ),
        "juicio": (
            "“Obstrucción. El suroeste es ventajoso. El noreste no es ventajoso. Es ventajoso "
            "ver al gran hombre. La perseverancia trae buena fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El suroeste es la región de la retirada, el noreste la del avance. Ante obstáculos "
            "insuperables directamente, es sabio hacer una pausa, hacer marcha atrás y esperar. "
            "Se requiere unir fuerzas con amigos y buscar el mando de alguien capaz de dirigir "
            "la situación. El propósito claro y decidido trae finalmente la buena fortuna."
        ),
        "imagen": (
            "“Agua sobre la montaña. La imagen de la obstrucción. El hombre noble dirige su "
            "atención a sí mismo y templa su carácter”.\n\n"
            "Las dificultades impulsan al hombre sobre sí mismo. Mientras el hombre inferior culpa "
            "a otros, el noble busca el error en sí mismo; mediante esta introspección, el "
            "obstáculo externo se transforma en un medio para el enriquecimiento interior."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Ir conduce al obstáculo, venir encuentra el elogio”.\n"
                "Ante un peligro, no se debe proseguir adelante ciegamente; eso solo complicaría "
                "las cosas. Lo correcto es retraerse un tiempo para reunir fuerzas esperando el "
                "momento apropiado para actuar."
            ),
            2: (
                "Seis en el segundo lugar significa: “El sirviente del rey se encuentra bloqueado "
                "por obstáculo tras obstáculo, pero no es culpa suya”.\n"
                "A veces el deber nos obliga a enfrentar peligros por una causa importante, impidiendo "
                "actuar según nuestro libre arbitrio. En tal caso, se puede estar en paz pues no "
                "es la propia falta la que coloca a uno en tales dificultades."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Ir conduce al obstáculo, es por eso que él vuelve”.\n"
                "Un jefe de grupo o padre de familia no debe arrojarse al peligro a la ligera, pues "
                "quienes confían en él no podrían continuar solos. Se bate en retirada hasta "
                "el momento propicio y regresa con los suyos que lo reciben con alegría."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Ir conduce a los obstáculos, venir conduce a la unión”.\n"
                "No se puede enfrentar el obstáculo sin la cooperación de gente fiable. Si se "
                "prosiguiera solo, se percibiría tarde que los apoyos eran insuficientes. Es mejor "
                "hacer una pausa y reunir a compañeros fieles sobre los cuales apoyarse."
            ),
            5: (
                "Nueve en el quinto lugar significa: “En medio de los más grandes obstáculos aparecen los amigos”.\n"
                "Aquí se ve al hombre indicado para remediar una situación crítica. Posee una efectiva "
                "vocación superior y fuerza de espíritu suficiente para atraer amigos que lo ayudarán "
                "a organizar el trabajo común para superar los obstáculos."
            ),
            6: (
                "Seis en la cima significa: “Ir conduce a los obstáculos, venir conduce a una gran fortuna. "
                "Es ventajoso ver al gran hombre”.\n"
                "Refiere a alguien que ha dejado el tumulto del mundo pero el deber lo llama de nuevo "
                "ante la adversidad. Por su experiencia y libertad interior es capaz de crear algo "
                "grande que traiga buena fortuna en compañía del cual se terminará el rescate."
            )
        },
        "lineas": {
            1: "No avances a ciegas ante el peligro; espera el tiempo apropiado.",
            2: "Si el deber te obliga a enfrentar obstáculos, mantén la paz interior.",
            3: "Retírate para proteger a quienes dependen de ti y espera el momento justo.",
            4: "No intentes superar el obstáculo solo; busca apoyo y compañeros fieles.",
            5: "La vocación superior atrae la ayuda necesaria en los momentos más críticos.",
            6: "Vuelve al mundo para ayudar; tu experiencia creará algo grande y favorable."
        }
    },
    40: {
        "nombre": "HSIEH / LA LIBERACIÓN",
        "trigrama_sup": "Chen Lo que Despierta, Trueno",
        "trigrama_inf": "K'an El Abismo, Agua.",
        "exposicion": (
            "El movimiento lleva fuera de la esfera del peligro. El obstáculo fue removido y las "
            "dificultades están en curso de solucionarse. Representa los diferentes "
            "estados de la evolución progresiva hacia una liberación total que apenas comienza."
        ),
        "juicio": (
            "“Liberación. El sudoeste es ventajoso. Cuando ya no hay más ningún lugar donde se deba ir, "
            "el retorno trae la buena fortuna. Si todavía queda algún lugar donde se deba ir, apresurarse "
            "trae buena fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Se refiere a una época en que las complicaciones comienzan a superarse. Debemos retornar "
            "al camino normal lo antes posible sin extralimitarnos en el triunfo. Si quedan asuntos "
            "pendientes, hay que resolverlos pronto para que la limpieza final ocurra sin retardo."
        ),
        "imagen": (
            "“Caen el trueno y la lluvia: la imagen de la liberación. El hombre noble perdona los errores "
            "y absuelve el pecado”.\n\n"
            "Tal como una tormenta purifica el aire, el hombre noble barre con los errores y pecados que "
            "provocan tensión. No se debe insistir en los defectos ajenos; las transgresiones "
            "involuntarias se pasan por alto y las intencionales se absuelven como el agua lava la suciedad."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Sin reproches”.\n"
                "Manteniéndose de acuerdo con la situación se necesitan pocas palabras. "
                "Los obstáculos se superaron y es momento de recuperar fuerzas en paz y tranquilidad."
            ),
            2: (
                "Nueve en la segunda línea significa: “Alguien mató tres zorros en el campo, y recibió "
                "una flecha dorada. La perseverancia trae buena fortuna”.\n"
                "Los obstáculos (zorros) deben ser apartados por medios rectos y apropiados. "
                "Al dedicarse con rectitud a la liberación, se encuentra sustento en la nobleza de los actos "
                "contra lo falso y vulgar."
            ),
            3: (
                "Seis en el tercer lugar significa: “Si un hombre viaja en carro y a pesar de eso lleva "
                "una carga en su espalda, incita a los ladrones a acercarse. La perseverancia lleva a la "
                "humillación”.\n"
                "Alguien que se libera de la miseria pero busca comodidad sin adaptarse interiormente atrae "
                "ataques. La insolencia ante superiores y la dureza con inferiores incitan a la "
                "gente a atacarlo."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Libérate de los lastres amarrados a tus pies. "
                "Entonces se acerca el compañero y puedes confiar en él”.\n"
                "El hombre noble debe liberarse de conexiones con personas vulgares que se le han hecho "
                "indispensables por rutina. Solo al estar libre de estas conexiones extrañas "
                "llegarán los amigos en quienes realmente podrá confiar."
            ),
            5: (
                "Seis en el quinto lugar significa: “Sólo el hombre noble puede liberarse a sí mismo. "
                "Eso trae buena fortuna. Así se muestra al hombre inferior que para él ese asunto es serio”.\n"
                "La liberación requiere resolución interna. El hombre noble no aleja a los inferiores "
                "con prohibiciones externas, sino desprendiéndose interiormente de ellos; al notar la seriedad "
                "del asunto, ellos confiarán o se separarán sin reproches."
            ),
            6: (
                "Seis en la cima significa: “El príncipe tira contra un halcón en el muro alto. Lo mata. "
                "Todo es ventajoso”.\n"
                "El halcón representa a un hombre vulgar endurecido en su maldad que obstruye la liberación. "
                "Debe ser removido enérgicamente utilizando los medios apropiados en el momento justo, después "
                "de haber puesto a punto todas las posibilidades."
            )
        },
        "lineas": {
            1: "Tras superar el obstáculo, descansa y recupera fuerzas en silencio.",
            2: "Elimina las influencias negativas mediante la rectitud y la nobleza.",
            3: "Adáptate interiormente a tu nueva situación para no atraer peligros o humillación.",
            4: "Suelte los vínculos con personas vulgares para permitir que lleguen amigos verdaderos.",
            5: "La liberación definitiva nace del desprendimiento interior, no de reglas externas.",
            6: "Actúa con energía para eliminar el último obstáculo que impide la libertad total."
        }
    },
    41: {
        "nombre": "SUN / LA MENGUA (La disminución)",
        "trigrama_sup": "Ken, La Inmovilidad, la Montaña.",
        "trigrama_inf": "Tui Lo Gozoso, Lago.",
        "exposicion": (
            "Este hexagrama es una modificación del Nº 11, Tai (La Paz). Muestra una disminución del "
            "trigrama inferior (Tui, El Lago) en provecho del superior (Ken, La Montaña). Es una "
            "disminución pura: si los cimientos son débiles y las murallas altas fuertes, la estructura "
            "pierde estabilidad. El tema central es cómo los cambios de fortuna pueden ocurrir "
            "sin perturbar el equilibrio general de la nación."
        ),
        "juicio": (
            "“La mengua combinada con la sinceridad acarrea la mayor fortuna sin reproches. Se puede "
            "perseverar en ello. Es ventajoso emprender algo. ¿Qué se puede hacer? Se pueden usar dos "
            "pequeñas escudillas para el sacrificio”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La disminución no siempre es mala; crecimiento y mengua vienen a su tiempo. Lo importante "
            "es no disimular la pobreza con pretensiones infundadas. La simplicidad es esencial para "
            "iniciar empresas importantes; incluso con medios escasos se puede expresar la sinceridad "
            "del corazón."
        ),
        "imagen": (
            "“Al pie de la montaña, el lago: la imagen de la mengua. El hombre noble controla su ira "
            "y restringe sus instintos”.\n\n"
            "El lago se evapora para enriquecer a la montaña con su humedad. Esto simboliza que la "
            "ira debe ser atenuada por la calma y los instintos domeñados por la restricción. Al "
            "disminuir las potencias inferiores del alma, los aspectos superiores se enriquecen."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Yéndonos rápido cuando nuestra tarea terminó no merece "
                "reproches, pero por lo menos se debe reflexionar sobre cuánto pueden menguar los demás”.\n"
                "Es generoso usar las energías propias al servicio de otros tras terminar las tareas urgentes. "
                "Sin embargo, quien ayuda debe considerar hasta qué punto el superior puede aceptar la ayuda "
                "sin ofenderse, actuando con sutileza de sentimientos."
            ),
            2: (
                "Nueve en el segundo lugar significa: “La perseverancia es ventajosa. Emprender algo trae "
                "desgracia. Sin disminuirse a sí mismo, se puede aumentar a los demás”.\n"
                "Ponerse al servicio de otros disminuyendo la propia dignidad no da un beneficio durable y "
                "es fuente de infortunio. Para dar un servicio de real valor es necesario no "
                "descuidarse a sí mismo."
            ),
            3: (
                "Seis en el tercer lugar significa: “Cuando tres personas viajan juntas, su número disminuye "
                "en uno. Cuando un hombre viaja solo, encuentra compañía”.\n"
                "Un lazo estrecho solo es posible entre dos; tres personas juntas despiertan celos. "
                "El individuo que está solo puede estar seguro de encontrar la compañía que lo complemente."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Cuando un hombre atenúa sus defectos, hace que los demás "
                "se apresuren en venir y reunírsele: sin reproches”.\n"
                "Los defectos propios a menudo impiden que la gente bien dispuesta se acerque. "
                "Si con humildad uno trata de corregirlos, los amigos se acercan más pronto y todos encuentran "
                "mutua alegría."
            ),
            5: (
                "Seis en el quinto lugar significa: “Alguien seguramente crece. Diez pares de tortugas no "
                "pueden oponérsele. Suprema fortuna”.\n"
                "Cuando la suerte destina a alguien a tener buena fortuna, esta llegará de todas maneras. "
                "Los oráculos otorgan signos favorables; no debe temer nada pues una voluntad superior "
                "ya ha decidido su destino."
            ),
            6: (
                "Nueve en la cima significa: “Cuando alguien crece sin menguar a los otros, no hay reproches. "
                "La perseverancia trae fortuna. Es ventajoso emprender algo. Se obtienen servidores, pero "
                "ya no se tiene un hogar separado”.\n"
                "Existen personas que dispensan bendiciones a todos sin detrimento de nadie. El éxito "
                "logrado no es una ganancia personal, sino un bien público accesible a todos a través del "
                "trabajo y la perseverancia."
            )
        },
        "lineas": {
            1: "Ayuda a otros tras cumplir tu deber, pero hazlo con tacto y discreción.",
            2: "Sirve a los demás sin sacrificar tu propia dignidad ni descuidarte.",
            3: "Busca conexiones individuales profundas; evita las complicaciones de los grupos de tres.",
            4: "Corrige tus propios defectos con humildad para atraer a gente valiosa.",
            5: "La fortuna decidida por el destino llegará sin que nada pueda oponérsele.",
            6: "El verdadero éxito es aquel que beneficia a la comunidad sin quitarle nada a nadie."
        }
    },
    42: {
        "nombre": "I CHI / EL INCREMENTO (el aumento)",
        "trigrama_sup": "Sun Lo Suave, Viento",
        "trigrama_inf": "Chen Lo que Despierta, Trueno.",
        "exposicion": (
            "Este hexagrama es considerado una modificación del Nº 12, Pi (La Estancación). La idea de "
            "incremento se expresa porque la línea luminosa superior se ha ubicado en el primer lugar "
            "inferior, transmitiendo su fuerza a todo el hexagrama. El sacrificio del ser superior "
            "para incrementar al inferior produce un aumento puro; gobernar bien es servir al pueblo."
        ),
        "juicio": (
            "“El incremento. Es ventajoso emprender algo. Es ventajoso cruzar la gran corriente”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El sacrificio de los superiores genera gratitud y alegría en el pueblo, haciendo que todas las "
            "empresas sean posibles. En tiempos de progreso, hay que hacer el mejor uso posible del "
            "tiempo, similar al matrimonio del cielo y la tierra cuando esta comparte el poder creativo. "
            "Este tiempo no es duradero, por lo que debe aprovecharse plenamente."
        ),
        "imagen": (
            "“Viento y truenos, la imagen del incremento. El hombre noble si ve lo bueno, lo imita; "
            "si hay defectos, se deshace de ellos”.\n\n"
            "El viento y el trueno se amplifican mutuamente. El hombre debe descubrir el camino para "
            "perfeccionarse imitando lo bueno que percibe en otros y deshaciéndose de lo malo en sí mismo. "
            "Este progreso ético es el incremento de personalidad más importante."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Es ventajoso realizar grandes hazañas. Suprema fortuna. "
                "Sin remordimientos”.\n"
                "Un gran impulso desde lo superior debe usarse para culminar algo grande para lo cual "
                "antes no se tenía energía. Al ser libre para la acción personal, se encuentra fortuna "
                "y se permanece libre de reproches."
            ),
            2: (
                "Seis en el segundo lugar significa: “Alguien verdaderamente crece; diez pares de tortugas "
                "no pueden oponérsele. La perseverancia constante trae buena fortuna. El rey lo presenta "
                "ante Dios. Fortuna”.\n"
                "El crecimiento real surge de la receptividad y el amor al bien. Si se está en armonía "
                "con las leyes del universo, ningún contratiempo puede impedirlo. Se debe actuar con "
                "fuerza interior y firmeza ante Dios y los hombres."
            ),
            3: (
                "Seis en el tercer lugar significa: “Uno se enriquece a través de acontecimientos "
                "infortunados. Sin reproche, si eres sincero, que camines por el medio y rindas cuentas al "
                "príncipe munido con un sello”.\n"
                "En tiempos de bendición, incluso los infortunios se vuelven ventajas. Actuar conforme "
                "a la verdad confiere una fuerza interior confirmada como por un sello oficial, permitiendo "
                "estar libre de error."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Si caminas en medio e informas al príncipe, te "
                "seguirán. Es ventajoso de ser empleado en el traslado de la capital”.\n"
                "Es el papel del intermediario desinteresado entre dirigentes y dirigidos. En épocas "
                "de auge, el beneficio debe retornar a la totalidad del pueblo. Esta influencia es "
                "vital en grandes empresas decisivas para el futuro."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Si en realidad tienes buen corazón, no preguntes. "
                "Suprema fortuna. Realmente la bondad será reconocida como tu virtud”.\n"
                "La verdadera bondad actúa por necesidad interior, sin preguntar por méritos o recompensas. "
                "Ese corazón bondadoso es recompensado con reconocimiento y su influencia se expande "
                "sin obstáculos."
            ),
            6: (
                "Nueve en la cima significa: “No lleva incremento a nadie. Alguien seguramente lo hiere. "
                "Su corazón no se mantiene constantemente firme. Desgracia”.\n"
                "Si los superiores no ayudan a los inferiores y descuidan su deber, pierden su influencia y se "
                "quedan solos, invitando al ataque. Una actitud brusca o un discurso agitado no "
                "encuentran eco y permiten que los enemigos se aproximen."
            )
        },
        "lineas": {
            1: "Aprovecha el impulso superior para realizar hazañas que antes parecían imposibles.",
            2: "El crecimiento armónico con las leyes naturales es imparable si hay perseverancia.",
            3: "Incluso la mala suerte se convierte en beneficio si actúas con sinceridad y rectitud.",
            4: "Como intermediario, asegura que los beneficios lleguen a todos de manera justa.",
            5: "Actúa desde el corazón sin buscar recompensa; tu virtud será reconocida por todos.",
            6: "No ayudar a los demás y ser inconsistente te aislará y te hará vulnerable al peligro."
        }
    },
    43: {
        "nombre": "KUAI / LA IRRUPCIÓN (Pasando a través)",
        "trigrama_sup": "Tui Lo Gozoso, Lago",
        "trigrama_inf": "Ch'ien Lo Creativo, Cielo.",
        "exposicion": (
            "Este hexagrama significa algo que irrumpe tras una larga acumulación de tensión, como "
            "una nube que hace llover para aliviar el ambiente. En lo humano, es la época donde la "
            "influencia de la gente vulgar disminuye y una acción resuelta produce el cambio esperado. "
            "Está asociado al tercer mes (abril-mayo)."
        ),
        "juicio": (
            "“Irrumpir. Uno debe resueltamente dar a conocer el asunto en la corte del rey. Debe ser "
            "anunciado correctamente y conforme a la verdad. Peligro. Es necesario avisar a su propia "
            "ciudad. No es oportuno recurrir a las armas. Es ventajoso emprender algo”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La lucha del bien contra el mal requiere reglas: 1. Unión de fuerzas y buena voluntad. "
            "2. No transigir con lo malo. 3. No usar la fuerza directa (odio contra odio), sino "
            "arreglar los propios asuntos. 4. La mejor forma de combatir el mal es el progreso "
            "enérgico del bien."
        ),
        "imagen": (
            "“El lago ha subido al cielo. La imagen de la irrupción. El hombre noble dispensa bienes "
            "por debajo de sí y se abstiene de reposar en su virtud”.\n\n"
            "Toda acumulación excesiva es seguida por una dispersión. El hombre noble evita el colapso "
            "distribuyendo sus riquezas y permaneciendo receptivo mediante un constante auto-análisis "
            "en lugar de volverse obstinado en su carácter."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Fuerza en los pies que avanzan. Si se va sin estar a la "
                "altura del asunto, se comete una falta”.\n"
                "Al comienzo, la resistencia es fuerte. Debemos mesurar nuestra fuerza y no aventurarnos "
                "más allá de lo posible. Lanzarse a ciegas es un error que puede traer resultados nefastos."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Un grito de alarma. Armas en la tarde y la noche. "
                "Nada que temer”.\n"
                "La resolución debe ir acompañada de precaución. Estar alerta aun sin peligro aparente "
                "permite estar preparado para cuando este llegue. Ser circunspecto asegura el éxito."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Ser poderoso en los pómulos trae desgracia. El hombre "
                "noble está firmemente resuelto. Camina solo y encuentra la lluvia. Es difamado y la gente "
                "murmura contra él. Sin reproches”.\n"
                "Se refiere a alguien en posición ambigua que mantiene relación con un hombre inferior "
                "para resolver la situación desde dentro. Será juzgado erróneamente por otros, pero "
                "superará el error por ser fiel a sí mismo."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “No hay piel en sus muslos, y caminar resulta difícil. "
                "Si un hombre quiere dejarse conducir como una oveja los remordimientos desaparecerán. "
                "Pero si se oyen sus palabras los demás no le creerán”.\n"
                "Alguien sufre por inquietud interior y obstinación. Si desistiera de su terquedad, todo "
                "iría bien, pero su condición lo vuelve incapaz de escuchar consejos."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Al tratar con la cizaña se requiere firme resolución. "
                "Caminar por el centro permanece libre de reproches”.\n"
                "La lucha contra lo inferior requiere una firme resolución constante. No se debe renunciar "
                "a la lucha ni desviarse del camino; solo así se evitarán las consecuencias negativas."
            ),
            6: (
                "Seis en la cima significa: “Sin llamado. Al final llega la desgracia”.\n"
                "Incluso cuando la victoria parece alcanzada, el mal puede reaparecer si quedan residuos. "
                "Descuidar el trabajo radical sobre el propio carácter permite que el mal encuentre un "
                "camino para retornar."
            )
        },
        "lineas": {
            1: "No te apresures al principio; mide tus fuerzas antes de avanzar contra la resistencia.",
            2: "Mantente alerta y preparado constantemente; la precaución es la base del éxito.",
            3: "Aunque seas malinterpretado por otros, mantén tu resolución interior sin desviarte.",
            4: "Abandona la obstinación y déjate guiar para superar los conflictos internos.",
            5: "Elimina las malas influencias con firmeza y sin desviarte del camino recto.",
            6: "No te confíes tras la victoria; elimina hasta el último residuo de negatividad."
        }
    },
    44: {
        "nombre": "KOU / VENIR AL ENCUENTRO",
        "trigrama_sup": "Ch'ien Lo Creativo, Cielo.",
        "trigrama_inf": "Sun Lo Suave, Viento.",
        "exposicion": (
            "Indica una situación en que el principio oscuro, tras haber sido eliminado, retorna furtiva e "
            "inesperadamente desde el interior y desde abajo. Es una situación desfavorable y "
            "peligrosa que debe comprenderse a tiempo para prevenir consecuencias. Está "
            "relacionado con el 5° mes (junio, julio) cuando el principio oscuro recomienza su ascensión."
        ),
        "juicio": (
            "“Viniendo a la cita. La muchacha es poderosa. Uno no debe casarse con esa muchacha”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El crecimiento de un elemento inferior se pinta como una muchacha atractiva que toma el comando. "
            "El hombre vulgar parece inofensivo y débil, ganando poder solo porque el hombre noble no lo mira "
            "como peligroso. Es indispensable que los elementos destinados a unirse lo hagan sin "
            "malas intenciones ocultas."
        ),
        "imagen": (
            "“Bajo el cielo está el viento: La imagen de la acción de venir al encuentro. Así actúa el "
            "príncipe cuando publica sus órdenes y las proclama por los cuatro puntos cardinales”.\n\n"
            "Representa una influencia que el soberano ejerce en todos lados. El cielo está lejos de las "
            "cosas de la tierra, pero las mueve con el viento; el soberano está alejado del pueblo, pero lo "
            "mueve con sus órdenes y decretos."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Debe ser detenido con un freno de bronce. La perseverancia trae "
                "buena fortuna. Si se lo deja seguir su curso, se experimentará desgracia. Incluso un "
                "cerdo recostado encuentra qué mordisquear a su alrededor”.\n"
                "Si un elemento inferior se introduce, debe ser detenido inmediata y enérgicamente para evitar "
                "malos efectos. Si se le consiente seguir, habrá infortunio."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Hay un pez en el estanque. Sin reproches. Los huéspedes "
                "no prosperan”.\n"
                "El elemento inferior se supera manteniéndolo bajo un control moderado, no por violencia. "
                "Se debe vigilar que no entre en contacto con los más alejados para que no despliegue su "
                "aspecto negativo."
            ),
            3: (
                "Nueve en el tercer lugar significa: “No hay piel en sus muslos y la marcha resulta penosa. Si "
                "uno está consciente del peligro, no puede cometer una falta grave”.\n"
                "Existe la tentación interior de contactar con el elemento dañino. Es una situación peligrosa "
                "con indecisión de conducta, pero tener clara conciencia del riesgo evita incurrir en "
                "errores serios."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “No hay peces en el estanque. De ello resulta el infortunio”.\n"
                "La gente insignificante debe ser tolerada para mantenerla bien dispuesta y poder usarla en "
                "el momento debido. Ser indiferente o rehusar reunirse con ella causará que no esté a "
                "disposición cuando se necesite, siendo culpa propia."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Un melón cubierto con hojas de sauce. Líneas ocultas. "
                "Entonces eso nos cae del cielo”.\n"
                "El fuerte y superior protege a los inferiores a su cargo sin agobiarlos con advertencias "
                "fastidiosas, confiando en su poder de transformación. Los inferiores responden a su "
                "influencia y permanecen a su disposición."
            ),
            6: (
                "Nueve en la cima significa: “Viene a reunirnos con cuernos. Humillación. Sin reproches”.\n"
                "Un hombre retirado del mundo puede rechazar con brusquedad lo bajo. Aunque se le reproche "
                "ser orgulloso y distante, al no estar ligado al deber de actuar en el mundo, esto no tiene "
                "gran importancia."
            )
        },
        "lineas": {
            1: "Detén cualquier influencia negativa de inmediato antes de que gane fuerza.",
            2: "Mantén bajo control moderado los elementos inferiores; no permitas que se propaguen.",
            3: "Aunque sientas la tentación de ceder, la conciencia del peligro te evitará errores graves.",
            4: "No ignores a la gente insignificante; podrías necesitar su apoyo más adelante.",
            5: "Protege y guía a tus subordinados con confianza y belleza interior, sin presionarlos.",
            6: "Alejarse de lo bajo con firmeza puede parecer orgullo, pero es lícito si ya no tienes deberes mundanos."
        }
    },
    45: {
        "nombre": "TS'UI / LA REUNIÓN (La concentración, el acopio)",
        "trigrama_sup": "Tui Lo Gozoso, Lago",
        "trigrama_inf": "K’un Lo Receptivo, Tierra.",
        "exposicion": (
            "Este hexagrama se emparenta por forma y significado al Nº 8, Pi (La Solidaridad). "
            "Mientras en Pi el agua está sobre la tierra, aquí el lago está sobre la tierra. El lago "
            "es el punto donde se reúnen las aguas, expresando la idea de reunión con más fuerza. "
            "La unión se realiza mediante dos trazos fuertes en el 4º y 5º lugar."
        ),
        "juicio": (
            "“La reunión. Éxito. El rey se aproxima al templo. Es ventajoso ver al gran hombre. "
            "Eso trae éxito. La perseverancia es ventajosa. Hacer grandes sacrificios trae buena "
            "fortuna. Es beneficioso emprender algo”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La reunión de los hombres es natural (familia) o artificial (estado). Se perpetúa "
            "mediante el culto y la piedad colectiva. Se requiere una autoridad humana como centro "
            "de la reunión, quien debe concordar moralmente consigo mismo para acrecentar su fuerza "
            "y unir a la gente. Las grandes unificaciones fructifican en grandes obras."
        ),
        "imagen": (
            "“Sobre la tierra, está el lago: la imagen de la reunión. El hombre noble renueva sus "
            "armas previniendo encontrarse con lo imprevisto”.\n\n"
            "Donde las aguas se reúnen hay peligro de desborde. Igualmente, donde los hombres se "
            "reúnen en número elevado pueden surgir conflictos o atraer a quienes buscan lo ajeno. "
            "Es necesario precaverse de lo inesperado renovando las defensas; estar preparado "
            "permite prevenir el sufrimiento."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Si eres sincero, pero no lo suficiente, a veces habrá "
                "confusión, a veces colaboración. Si pides ayuda, puedes reír de nuevo después de "
                "que te hayan dado una mano. Sin remordimientos. Marchar no tiene reproches”.\n"
                "Describe a quien busca reunirse con un guía pero se deja influenciar por otros, "
                "vacilando en sus resoluciones. Basta con pedir ayuda al guía para superar el "
                "desamparo. La actitud justa es plegarse a la fuerza de reunir."
            ),
            2: (
                "Seis en el segundo lugar significa: “Dejarse arrastrar trae buena fortuna y permanece "
                "sin reproches. Si se es sincero, es ventajoso ofrecer un sacrificio aunque sea "
                "pequeño”.\n"
                "En la reunión actúan fuerzas secretas que unen a seres con afinidad. Se debe "
                "obedecer a esa atracción. Si hay relaciones íntimas, no hacen falta grandes "
                "preparativos; la sinceridad hace que las pequeñas ofrendas sean aceptadas."
            ),
            3: (
                "Seis en el tercer lugar significa: “Reuniendo entre los suspiros. Nada puede "
                "aprovecharse. Irse no tiene reproches, pequeña humillación”.\n"
                "Se siente la urgencia de unirse a otros que ya han formado grupos cerrados, "
                "quedando uno aislado. Se debe elegir a un hombre cerca del centro del grupo que "
                "pueda ayudar a ser admitido, aunque al principio la posición de extraño sea "
                "humillante."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Gran fortuna. Sin reproches”.\n"
                "Describe a un hombre que reúne al pueblo en nombre del guía. Mientras no busque "
                "ventajas personales y trabaje por la unidad general, su trabajo será coronado "
                "por el éxito."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Si una reunión se forma alrededor de alguien "
                "por el justo valor que éste tiene ello no ocasiona reproches. Pero si ello no es "
                "sincero, se requiere actuar con una perseverancia sublime y duradera. Así los "
                "remordimientos desaparecen”.\n"
                "Ganarse la confianza sincera de la gente solo se logra mediante una fidelidad "
                "constante al deber. Así se supera la desconfianza secreta de quienes se reúnen "
                "solo por la posición influyente del líder."
            ),
            6: (
                "Seis en la cima significa: “Lamentos y suspiros, diluvio de lágrimas. Sin "
                "reproches”.\n"
                "Ocurre cuando las buenas intenciones de aliarse son mal interpretadas. El lamento "
                "y la tristeza en el buen camino pueden llevar al otro a reflexionar, reconsiderar "
                "la situación y finalmente realizar la unión deseada."
            )
        },
        "lineas": {
            1: "Busca un guía confiable y no te dejes confundir por la multitud; pide ayuda si vacilas.",
            2: "Sigue tu afinidad natural hacia los demás; la sinceridad vale más que las formas complejas.",
            3: "Si te sientes excluido, busca a alguien cercano al centro que facilite tu integración.",
            4: "Trabaja desinteresadamente por la unidad del grupo y alcanzarás el éxito.",
            5: "Consolida la confianza de los demás a través de una conducta ejemplar y constante.",
            6: "No te desanimes si te rechazan; tu persistencia y dolor pueden conmover al otro para la unión."
        }
    },
    46: {
        "nombre": "SHENG / EMPUJANDO HACIA ARRIBA (Levantando)",
        "trigrama_sup": "K'un Lo Receptivo, Tierra.",
        "trigrama_inf": "Sun Lo Suave Viento, Madera.",
        "exposicion": (
            "El trigrama inferior Sun (madera/bosque) crece hacia arriba a través del trigrama superior "
            "K'un (tierra). A diferencia del progreso (Nº 35), este empuje está ligado al esfuerzo "
            "voluntario, como las raíces de una planta que necesitan fuerza para crecer en la tierra. "
            "Indica un ascenso desde la oscuridad y la sumisión hacia el poder mediante la voluntad."
        ),
        "juicio": (
            "“El empuje hacia arriba posee un éxito sublime. Debe ver al gran hombre. Sin temor. "
            "Partida hacia el sur trae buena fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El ascenso de elementos valiosos no encuentra obstáculos, por lo que el éxito está asegurado. "
            "La actitud necesaria no es violenta, sino humilde y acomodante. Es momento de avanzar y "
            "buscar a las autoridades; el trabajo y la actividad constante (simbolizada por el sur y el verano) "
            "son fuentes de fortuna."
        ),
        "imagen": (
            "“En el medio de la tierra crece el bosque: imagen del empuje hacia arriba. Así el hombre "
            "noble se abandona a la naturaleza, acumula pequeñas cosas para hacer cosas grandes y "
            "elevadas”.\n\n"
            "El bosque crece sin prisa, contorneando dócilmente los obstáculos. El hombre noble hace "
            "lo mismo, avanzando sin pausa ni descanso, abandonándose a la corriente natural de las cosas."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “El empuje hacia arriba que encuentra la confianza trae una "
                "gran fortuna”.\n"
                "Es el comienzo del ascenso. El poder de realizar viene desde lo más profundo; "
                "si hay afinidad entre el designio y la fuerza interior, se genera la confianza necesaria "
                "para lograr lo propuesto."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Si uno es sincero, es ventajoso presentar una "
                "ofrenda aunque sea pequeña. Sin reproches”.\n"
                "Describe a un hombre fuerte y brusco que no se adapta a las formalidades exteriores. "
                "Sin embargo, es correcto interiormente y su rectitud emana de cualidades sólidas, lo que "
                "le permite encontrar una buena respuesta a pesar de su negligencia en las formas."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Alguien empuja hacia arriba en una ciudad vacía”.\n"
                "Todas las obstrucciones caen y las cosas fluyen con notable facilidad. No se debe "
                "vacilar ante este éxito, pero tampoco dejarse llevar por reflexiones que inhiban la "
                "propia fuerza; hay que aprovechar rápidamente las circunstancias favorables."
            ),
            4: (
                "Seis en el cuarto lugar significa: “El rey lo ofrece al Monte Ch'i. Fortuna. Sin reproches”.\n"
                "Evoca la época en que la dinastía Chou llegó al poder y sus aliados fueron honrados. "
                "Indica que el ascenso ha alcanzado su meta, logrando la gloria tanto entre los hombres "
                "como en la vida espiritual, obteniendo una fortuna perdurable."
            ),
            5: (
                "Seis en el quinto lugar significa: “Perseverancia trae fortuna. Se empuja hacia arriba "
                "gradualmente”.\n"
                "Al experimentar un gran éxito, es vital permanecer sobrio y no intentar saltar etapas. "
                "El progreso debe ser calmado, juicioso y paso a paso; solo este avance prudente lleva "
                "realmente a la meta final."
            ),
            6: (
                "Seis en la cima significa: “Empujando hacia arriba en la oscuridad. Aprovecha perseverar "
                "sin desmayo”.\n"
                "Quien empuja a ciegas sin saber detenerse se dispersa interiormente y llega al agotamiento. "
                "Es crucial ser consciente y consecuente para preservarse de impulsos ciegos que no "
                "conducen a nada productivo."
            )
        },
        "lineas": {
            1: "La confianza interior y la afinidad con el entorno garantizan un inicio exitoso del ascenso.",
            2: "La sinceridad y solidez interior compensan la falta de formas o protocolos externos.",
            3: "Aprovecha la ausencia de obstáculos para avanzar sin vacilaciones innecesarias.",
            4: "Has alcanzado una posición de honor y reconocimiento que perdurará en el tiempo.",
            5: "No te dejes cegar por el éxito; avanza paso a paso con sobriedad y prudencia.",
            6: "Evita el avance ciego; la perseverancia solo es útil si eres consciente de tus límites."
        }
    },
    47: {
        "nombre": "K'UN / EL AGOBIO (El abatimiento, el agotamiento)",
        "trigrama_sup": "Tui Lo Gozoso, lago",
        "trigrama_inf": "K´an El Abismo, Agua.",
        "exposicion": (
            "El lago está arriba y el agua abajo; el lago está vacío, agotado, seco. "
            "Simboliza una época donde los hombres superiores se encuentran oprimidos y sometidos "
            "a las restricciones que les oponen los hombres inferiores. El trigrama "
            "superior (oscuridad) oprime al inferior (luz)."
        ),
        "juicio": (
            "“Abatimiento. Éxito. Perseverancia. El gran hombre realiza una feliz fortuna. Sin "
            "reproches. Cuando alguien tiene algo que decir no es creído”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Los tiempos de adversidad pueden llevar al éxito si se enfrenta con serenidad y alerta. "
            "La firmeza del hombre fuerte debe ser más poderosa que el destino. En estas épocas, "
            "la influencia del noble no es reconocida y sus palabras no tienen efecto; por ello es vital "
            "permanecer interiormente fuerte y sobrio en el hablar."
        ),
        "imagen": (
            "“No hay agua en el lago: la imagen del agotamiento. El hombre noble arriesga su vida "
            "para cumplir sus propósitos”.\n\n"
            "Cuando el agua se agota, el lago se seca. Ante la suerte adversa, no queda más "
            "que asumir el destino y permanecer fiel a la naturaleza más profunda del ser, que es "
            "superior a cualquier circunstancia exterior."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Uno está sentado deprimido bajo un árbol desnudo y se "
                "llega a un valle oscuro. Por tres años no ve nada”.\n"
                "La adversidad supera a quien es débil interiormente. En lugar de avanzar, "
                "se hunde en la melancolía y la tiniebla por una ceguera interior que debe ser "
                "superada a todo precio."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Uno está deprimido cerca del vino y de los "
                "alimentos. Y llega el hombre de las rodilleras escarlatas. Es ventajoso ofrecer un "
                "sacrificio. Partir apresuradamente es fuente de infortunio. No hay reproches”.\n"
                "Describe una depresión interior pese a que externamente todo marcha bien. La "
                "ayuda viene de arriba (un príncipe), pero existen obstáculos invisibles que deben "
                "afrontarse con paciencia y recogimiento, no con acciones precipitadas."
            ),
            3: (
                "Seis en el tercer lugar significa: “Uno se deja oprimir por una piedra y se apoya "
                "sobre espinas y cardos. Entra a su casa y no ve a su esposa. Desgracia”.\n"
                "Muestra inquietud e indecisión. El individuo se golpea contra obstáculos que solo "
                "son agobiantes si se enfrentan irracionalmente, buscando apoyo en cosas que no "
                "ofrecen seguridad. Esto lleva a decepciones profundas."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Viene muy lentamente, agobiado en un carruaje "
                "dorado. Humillación, pero finalmente llega”.\n"
                "Un hombre pudiente desea ayudar a los necesitados, pero actúa de forma titubeante y "
                "calculada, atraído por sus propios círculos sociales. Aunque hay desconcierto, "
                "la adversidad es pasajera y la meta se alcanza finalmente."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Se tiene la nariz y los pies cortados. Se está "
                "agobiado por los hombres de rodilleras púrpuras. La alegría viene lentamente. Es "
                "ventajoso presentar ofrendas y libaciones”.\n"
                "Alguien desea el bien general pero está presionado por arriba y por abajo, sin apoyo "
                "de sus ministros. Se requiere un recogimiento interior firme y plegarias; "
                "eventualmente, las cosas progresarán hacia una mejoría."
            ),
            6: (
                "Seis en la cima significa: “Está agobiado por los juramentos. Se mueve con dificultad "
                "y dice: ‘El movimiento trae remordimientos’. Si se sienten remordimientos por ello y "
                "que uno se pone en marcha se obtiene la buena fortuna”.\n"
                "Se está presionado por lazos que pueden romperse fácilmente. Aunque el agotamiento "
                "termina, queda la irresolución. Si uno se deshace de esa actitud interior y toma "
                "una firme resolución, logrará superar las dificultades."
            )
        },
        "lineas": {
            1: "No te hundas en la melancolía; la ceguera interior solo agrava la desesperación.",
            2: "Supera la opresión espiritual mediante el recogimiento y la paciencia, no con prisas.",
            3: "No busques apoyo en lo que no tiene solidez; enfrentar los problemas irracionalmente solo trae desgracia.",
            4: "Supera las dudas y las distracciones sociales para cumplir con tu deber de ayuda.",
            5: "Mantén tu fe y propósito ante la falta de apoyo; la ayuda y la alegría llegarán con el tiempo.",
            6: "Libérate de los lazos del pasado y toma una resolución firme para dejar atrás el agobio."
        }
    },
    48: {
        "nombre": "CHING / EL POZO",
        "trigrama_sup": "K'an El Abismo, Agua",
        "trigrama_inf": "Sun Lo Suave, Viento, Madera.",
        "exposicion": (
            "Arriba está el agua (K'an) y abajo el bosque o la madera (Sun). La madera se entierra "
            "para hacer subir el agua, evocando los antiguos pozos de China donde se extraía el "
            "agua con cubos suspendidos de pértigas de madera. Representa la nutrición "
            "prodigada de manera inagotable."
        ),
        "juicio": (
            "“El pozo. El pueblo puede ser cambiado, pero no el pozo. Este no aumenta ni disminuye. "
            "Van y vienen del pozo. Si se llega casi hasta el agua y la soga no es suficiente para "
            "alcanzarla o si el cántaro se rompe, eso trae desgracia”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Mientras las formas políticas y las naciones cambian, la vida de los hombres y sus "
            "exigencias vitales permanecen eternamente iguales. Una buena organización requiere "
            "descender hasta los fundamentos de la vida misma. Es peligroso ser superficial o "
            "negligente (que se rompa el cántaro), lo cual equivale a la destrucción del Estado "
            "o al fracaso del individuo en su formación."
        ),
        "imagen": (
            "“Agua sobre madera: la imagen del pozo. El hombre noble anima a la gente a su trabajo y "
            "los exhorta a ayudar a los demás”.\n\n"
            "Así como el bosque aspira el agua hacia lo alto para el bien de todas las partes de la "
            "planta, el hombre noble organiza la sociedad para que sus miembros cooperen con el "
            "bien de todos."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “El barro del pozo no es bebido. Ni siquiera los "
                "animales van a un pozo viejo”.\n"
                "Si alguien se hunde en el cieno de una vida sin significado, nadie se preocupa "
                "de él. Representa el abandono y el desprecio de uno mismo."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Alguien pesca en la boca del pozo. El "
                "cántaro se rompe y gotea”.\n"
                "El agua es clara pero no se utiliza. Describe a alguien con buenas cualidades que "
                "las descuida, degradándose interiormente al asociarse con seres ordinarios."
            ),
            3: (
                "Nueve en el tercer lugar significa: “El pozo está limpio, pero nadie bebe en él. "
                "Esta es la pena de mi corazón, que nadie lo aproveche. Si el rey tuviera un "
                "entendimiento claro la buena fortuna se lograría en común”.\n"
                "Se refiere a una persona de valor no utilizada. Es el deseo de que quien tiene "
                "el poder se dé cuenta de este potencial para beneficio de todos."
            ),
            4: (
                "Seis en el cuarto lugar significa: “El pozo fue revestido. Sin reproches”.\n"
                "Durante el mantenimiento del pozo no se puede beber el agua, pero el trabajo no es "
                "en vano. Representa períodos de desarrollo interior donde uno pone orden en sí "
                "mismo para actuar mejor después."
            ),
            5: (
                "Nueve en el quinto lugar significa: “En el pozo hay una fuente clara y fresca, "
                "uno puede beber de él”.\n"
                "Describe a un hombre con virtudes nacido para guiar. Lo esencial es que su fuente "
                "sea extraída y que sus palabras se transformen en vida para los demás."
            ),
            6: (
                "Seis en la cima significa: “Saca el agua del pozo sin obstáculos. Es seguro. "
                "Gran fortuna”.\n"
                "El pozo es fiable y su fuente nunca se seca. Representa al hombre realmente grande "
                "que posee un tesoro inagotable de excelencia interior; mientras más se obtenga "
                "de él, más rico se hace."
            )
        },
        "lineas": {
            1: "Evita caer en la negligencia y el desprecio propio que te vuelven inútil para los demás.",
            2: "No desperdicies tus talentos asociándote con lo ordinario; mantén tu cántaro sano.",
            3: "El valor personal sin reconocimiento es una pena; se busca un líder que sepa aprovecharlo.",
            4: "Usa los tiempos de retiro para organizar tu interior y fortalecer tus capacidades.",
            5: "Posees una fuente de sabiduría; asegúrate de que otros puedan acceder a ella para nutrirse.",
            6: "Has alcanzado la excelencia inagotable; compartir tu riqueza interior trae gran fortuna."
        }
    },
    49: {
        "nombre": "KO / LA REVOLUCIÓN (La muda)",
        "trigrama_sup": "Tui, Lo Gozoso, Lago.",
        "trigrama_inf": "Li, Lo Oscilante, Fuego.",
        "exposicion": (
            "El sentido primitivo es el de la piel que muda transformando al animal. Se aplica a "
            "los cambios en la vida del Estado y grandes revoluciones de régimen. Formado por Tui "
            "(lago) arriba y Li (fuego) abajo. A diferencia del hexagrama 38, aquí la hija más "
            "joven está arriba; las fuerzas del fuego y el agua se combaten buscando destruirse "
            "mutuamente, lo que genera la idea de revolución."
        ),
        "juicio": (
            "“Revolución. En tu propio día eres creído. La perseverancia favorece el mayor éxito. "
            "Los remordimientos se disipan”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Las revoluciones son graves y solo deben emprenderse en caso de extrema necesidad. "
            "Requieren de alguien que goce de la confianza del pueblo y que actúe en la época "
            "propicia. Se debe proceder correctamente, sin egoísmo, para complacer las necesidades "
            "reales del pueblo. Así como cambian las estaciones, las naciones exigen transformaciones "
            "sociales cuando los tiempos cambian."
        ),
        "imagen": (
            "“Fuego en el Lago. La imagen de la revolución. Así el hombre noble regula el "
            "calendario y aclara el tiempo”.\n\n"
            "El fuego arriba y el lago abajo se destruyen mutuamente, similar al combate entre "
            "fuerzas luminosas y oscuras que da lugar al cambio de estaciones. El hombre noble "
            "introduce orden en el caos temporal al reconocer la regularidad de la naturaleza, "
            "adaptándose por anticipado a las exigencias de cada época."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Uno está envuelto en el cuero de una vaca amarilla”.\n"
                "Los cambios solo deben hacerse cuando no quede otra posibilidad. Al principio es "
                "necesaria la reserva, moderación (amarillo) y firmeza interior (vaca/docilidad). "
                "Nada debe emprenderse precipitadamente, pues la ofensiva prematura trae malas consecuencias."
            ),
            2: (
                "Seis en el segundo lugar significa: “En el día propicio se puede emprender una "
                "revolución. Partir trae buena fortuna. Sin reproches”.\n"
                "Cuando las reformas previas han fallado, la revolución se hace necesaria. Debe "
                "estar bien preparada por alguien con méritos y la confianza del pueblo. Lo que "
                "importa es la actitud interior hacia el nuevo orden que ha de establecerse."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Partir trae desgracia. La perseverancia acarrea "
                "el peligro. Si el discurso de la revolución ha dado la vuelta tres veces, uno "
                "puede confiar en él y hallará la fe”.\n"
                "Se deben evitar dos errores: la prisa excesiva y la hesitación conservadora. No "
                "se debe escuchar cualquier invitación al cambio, pero tras reflexionar sobre "
                "quejas repetidas y fundadas (tres veces), se puede actuar en consecuencia."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “El remordimiento se disipa. La fe se reencuentra. "
                "Cambiar el orden del estado trae buena fortuna”.\n"
                "Los cambios radicales requieren autoridad, fuerza de carácter y posición de "
                "influencia. Deben emanar de una verdad superior; si falta esta verdad interior, "
                "el resultado es el fracaso. Los hombres apoyan empresas que sienten legítimas."
            ),
            5: (
                "Nueve en el quinto lugar significa: “El gran hombre cambia como un tigre. Incluso "
                "antes de interrogar el oráculo encuentra la convicción”.\n"
                "Como las rayas de un tigre sobre fondo amarillo, las directivas de un gran hombre "
                "son claras y visibles desde lejos. El pueblo acude espontáneamente hacia él, por lo "
                "que no necesita consultar oráculos para confirmar su camino."
            ),
            6: (
                "Seis en la cima significa: “El hombre noble cambia como una pantera. El hombre cambia "
                "de rostro. Partir trae desgracia. Permanecer perseverante trae buena fortuna”.\n"
                "Tras arreglar lo fundamental, quedan detalles menores (manchas de pantera). El "
                "cambio llega también a los hombres vulgares, aunque no sea profundo. No hay que "
                "esperar demasiado ni ir más allá de lo posible para evitar la inquietud e infortunio."
            )
        },
        "lineas": {
            1: "Mantén la moderación y espera el momento justo; no actúes por impulso prematuro.",
            2: "Prepárate con alguien capaz; el cambio radical es lícito cuando se tiene el apoyo popular.",
            3: "Evita la precipitación; solo actúa cuando la necesidad de cambio haya sido confirmada varias veces.",
            4: "Asegúrate de que tus motivos sean legítimos y superiores para garantizar el éxito del cambio.",
            5: "Tu liderazgo es claro y evidente para todos; la convicción interna guía el éxito.",
            6: "Consolida los logros fundamentales y no presiones por cambios superficiales imposibles."
        }
    },
    50: {
        "nombre": "TING / EL CALDERO",
        "trigrama_sup": "Li Lo Oscilante, Fuego.",
        "trigrama_inf": "Sun Lo Suave, Viento, Madera.",
        "exposicion": (
            "El hexagrama ofrece la imagen física del caldero: abajo los pies, luego la panza, "
            "las asas y arriba el anillo para llevarlo. Evoca la alimentación y la civilización "
            "refinada. Mientras el pozo (Nº 48) se refiere a la distribución para el pueblo, "
            "el caldero representa los cuidados y la alimentación que el gobierno brinda a los "
            "hombres de valor. Simboliza la llama (Li) encendida sobre la madera (Sun), "
            "preparando el alimento."
        ),
        "juicio": (
            "“El caldero. Suprema fortuna. Éxito”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Representa la superestructura cultural de la sociedad y la culminación de la cultura "
            "en la religión. Lo más elevado en el orden terrestre debe ser ofrecido a la "
            "divinidad. La manifestación suprema de Dios se encuentra en los profetas y los "
            "santos; honrarlos con humildad produce una iluminación interior y una inteligencia "
            "verdadera que conducen a una gran fortuna."
        ),
        "imagen": (
            "“Sobre la leña está el fuego. La imagen del caldero. Así el hombre noble asegura su "
            "destino manteniendo una posición correcta”.\n\n"
            "La leña es el destino del fuego; así como arde el fuego mientras haya leña, el hombre "
            "tiene un destino que da fuerza a su vida. El destino se fortifica cuando se pone la "
            "vida íntimamente de acuerdo con él, cultivándola según las enseñanzas del yoga "
            "práctico chino."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Un caldero con patas hacia arriba es ventajoso para "
                "vaciarlo de sus restos. Se toma una concubina por amor a su hijo. Sin reproches”.\n"
                "Invertir el caldero para limpiarlo antes de usarlo no es dañino; permite purificarse "
                "de restos del pasado. No importa cuán baja sea la posición original, se tendrá "
                "éxito al estar listo para la purificación y ocuparse eficazmente de las tareas."
            ),
            2: (
                "Nueve en el segundo lugar significa: “En el caldero hay comida. Mis camaradas tienen "
                "envidia pero no pueden hacerme daño. Fortuna”.\n"
                "En épocas de alta cultura es crucial efectuar tareas positivas. La envidia de otros "
                "no es peligrosa mientras uno se limite a sus labores constructivas y se concentre "
                "en lo que es exitoso."
            ),
            3: (
                "Nueve en el tercer lugar significa: “El asa del caldero fue cambiada. Uno encuentra "
                "su camino obstaculizado. La grasa del faisán no se come. Desde que cae la lluvia "
                "los remordimientos se disipan. Finalmente llega la fortuna”.\n"
                "Representa a alguien de talento en una posición donde nadie lo reconoce, desperdiciando "
                "sus dones. Sin embargo, si mantiene sus bienes espirituales, los obstáculos "
                "desaparecerán con el tiempo (simbolizado por la caída de la lluvia) y llegará la fortuna."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Los pies del caldero se rompen. La comida del "
                "príncipe se derrama y su persona se ensucia. Desgracia”.\n"
                "Se enfrenta una tarea grave sin tener la capacidad o la dedicación necesaria, "
                "prefiriendo rodearse de gente inferior. El fracaso de la ejecución lleva a una "
                "situación de humillación y oprobio."
            ),
            5: (
                "Seis en el quinto lugar significa: “El caldero tiene asas amarillas, anillos dorados. "
                "La perseverancia es ventajosa”.\n"
                "Describe a un hombre en autoridad que es humilde y asequible, logrando así encontrar "
                "asistentes fuertes y capaces que lo complementen. Requiere mantener una abnegación "
                "constante y firmeza en esta actitud."
            ),
            6: (
                "Nueve en la cima significa: “El caldero tiene asas de jade. Inmensa fortuna. Nada "
                "puede dejar de ser ventajoso”.\n"
                "El jade simboliza la combinación de dureza con suavidad. Representa al sabio que "
                "da consejos suaves y puros. La obra encuentra gracia ante lo divino y ante los "
                "hombres, resultando en una situación donde todo va bien."
            )
        },
        "lineas": {
            1: "Purifícate de los errores del pasado para estar listo para nuevas y mejores tareas.",
            2: "Concéntrate en tus logros positivos; la envidia ajena no podrá dañarte si eres productivo.",
            3: "Aunque tus talentos no sean reconocidos ahora, cultiva tu valor espiritual y el éxito llegará.",
            4: "No aceptes responsabilidades que superen tu fuerza o carácter; el descuido trae desgracia.",
            5: "La humildad en el poder te permite atraer colaboradores capaces para cumplir tu misión.",
            6: "Actúa con la sabiduría del jade (firmeza y suavidad); esto garantiza una fortuna inmensa."
        }
    },
    51: {
        "nombre": "CHEN / LA EXCITACIÓN (La conmoción, el Trueno)",
        "trigrama_sup": "Chen El Despertar, Trueno",
        "trigrama_inf": "Chen El Despertar, Trueno",
        "exposicion": (
            "Representa al hijo mayor que toma el comando con energía y poder. Un trazo yang "
            "aparece sobre dos trazos yin y ejerce un potente empuje hacia arriba. Este movimiento "
            "es tan violento que suscita el terror. Tiene por imagen el trueno que surge de la "
            "tierra y cuya conmoción provoca el pánico y el temblor."
        ),
        "juicio": (
            "“La conmoción trae éxito. La conmoción viene -oh, oh! Riendo- ah, ah! La conmoción "
            "aterroriza por cien millas y no hay que dejar caer la cuchara de los sacrificios y el cáliz”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La conmoción que proviene de las manifestaciones de Dios hace temer al hombre, pero es "
            "bueno que tema, pues la alegría puede venir a continuación. Quien aprende lo que "
            "significa el temor está a salvo de influencias exteriores. Aunque el trueno siembre el "
            "terror, el guía debe permanecer interiormente lleno de calma y veneración, sin "
            "interrumpir sus ritos."
        ),
        "imagen": (
            "“Trueno repetido: la imagen de la conmoción. A través del temor y el temblor el hombre "
            "noble pone su vida en orden y se examina a sí mismo”.\n\n"
            "El hombre noble observa una actitud de reverencia ante las manifestaciones de Dios. "
            "Examina su corazón para preservar que nada se oponga a la voluntad divina; así, el "
            "temor es el fundamento de la verdadera vida."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “La conmoción viene - oh, oh! Le suceden las palabras "
                "risibles -ah, ah! Fortuna”.\n"
                "El temor engendrado por una conmoción coloca al individuo en desventaja transitoria. "
                "Al atravesar la prueba del juicio, se produce un alivio. Cuando el terror inicial "
                "se disipa, trae la fortuna."
            ),
            2: (
                "Seis en el segundo lugar significa: “La conmoción viene trayendo peligro. Cien mil "
                "veces pierdes tus tesoros y debes trepar las nueve colinas. No los persigas. Después "
                "de siete días volverán otra vez”.\n"
                "Ante una conmoción que trae peligros y perjuicios graves, la resistencia es "
                "infructuosa. Se debe aceptar el retiro y la pérdida temporal de bienes sin "
                "lamentarse; estos se recuperarán naturalmente una vez pase la época de conmoción."
            ),
            3: (
                "Seis en el tercer lugar significa: “La conmoción viene y provoca el desamparo. Si se "
                "actúa en consecuencia de la conmoción uno estará libre de disgustos”.\n"
                "Existen conmociones del cielo, del destino y del corazón. Si uno permite que la "
                "conmoción del destino se transforme en una reacción del corazón (acción "
                "consciente), se superarán los golpes sin grandes dificultades."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La conmoción se empantana”.\n"
                "El éxito depende parcialmente de las circunstancias. Cuando no hay resistencia ni "
                "presencia de ánimo para combatir enérgicamente, todo se vuelve viscoso como el "
                "fango y el movimiento se paraliza."
            ),
            5: (
                "Seis en el quinto lugar significa: “La conmoción va de aquí para allá: peligro. Pero "
                "finalmente nada se pierde, solo hay cosas para hacer”.\n"
                "No se trata de una sola conmoción sino de muchas. Sin embargo, no ocasionan "
                "pérdidas si uno toma la precaución de permanecer en el centro del movimiento, "
                "liberándose del riesgo de ser lanzado de un lado a otro por el destino."
            ),
            6: (
                "Seis en la cima significa: “La conmoción trae ruina y miradas angustiadas a todo lo "
                "que rodea. Avanzar trae el infortunio. Si éste todavía no ha alcanzado nuestro "
                "cuerpo, pero comienza a tocar a nuestro vecino, no hay reproches. Los compañeros "
                "tienen de qué hablar”.\n"
                "Cuando la conmoción llega al máximo, se pierde la facultad de reflexión. La actitud "
                "justa es guardar silencio hasta recuperar la calma. Si uno se retira a tiempo de "
                "la acción antes de sufrir los efectos nefastos, permanece libre de faltas, aunque "
                "otros no comprendan esta actitud."
            )
        },
        "lineas": {
            1: "Superada la prueba inicial de temor, el alivio y la fortuna aparecerán.",
            2: "No luches contra pérdidas inevitables durante el caos; lo que es tuyo volverá a su tiempo.",
            3: "Transforma la sacudida externa en una reflexión interna para superar el desamparo.",
            4: "Evita la pasividad; si dejas que el ánimo decaiga, te quedarás estancado en el fango.",
            5: "Mantente firme en tu centro durante las crisis repetidas; así evitarás pérdidas mayores.",
            6: "Retírate a tiempo si el caos es extremo; guarda silencio y espera a que la claridad regrese."
        }
    },
    52: {
        "nombre": "KEN / LA INMOVILIDAD, LA MONTAÑA",
        "trigrama_sup": "Ken, La Inmovilidad, la Montaña.",
        "trigrama_inf": "Ken, La Inmovilidad, la Montaña.",
        "exposicion": (
            "La imagen del hexagrama es la montaña, el más joven de los hijos del cielo y de la "
            "tierra. El principio masculino está arriba y sigue su dirección natural; el femenino "
            "está abajo, conforme al sentido de su movimiento. Así, un estado de reposo se ha "
            "establecido. Aplicado al hombre, trata de conseguir la paz del corazón. El reposo "
            "constituye un estado polar que siempre tiene como complemento el movimiento."
        ),
        "juicio": (
            "“La espalda está tan bien inmovilizada que ya no siente más su cuerpo. Entra en la "
            "corte y no ve más a los suyos. Sin reproches”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El verdadero reposo es aquel donde el hombre se detiene cuando el movimiento cesa y se "
            "mueve cuando es momento de hacerlo. La espalda es la sede de los centros nerviosos; "
            "al aquietarlos, el ego y su inquietud se desvanecen. Quien alcanza esta paz interior "
            "deja de percibir el tumulto del mundo y comprende las leyes universales, actuando sin "
            "cometer faltas."
        ),
        "imagen": (
            "“Las montañas reunidas, la imagen de la inmovilidad. Así el hombre superior no deja "
            "que sus pensamientos desborden su situación”.\n\n"
            "El corazón piensa constantemente, pero los pensamientos deben restringirse a la "
            "situación vital inmediata. Las especulaciones y sueños que van demasiado lejos solo "
            "sirven para herir el corazón."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Inmovilidad de sus dedos del pie. Sin reproches. La "
                "perseverancia perdurable es ventajosa”.\n"
                "Mantenerse quieto antes de comenzar a moverse evita errores. En este inicio se está "
                "en armonía con la inocencia original, sin influencias de intereses o deseos. Se "
                "requiere firmeza constante para no dejarse bambolear sin voluntad."
            ),
            2: (
                "Seis en el segundo lugar significa: “Inmovilidad de sus pantorrillas. No se puede "
                "rescatar al que sigue. Su corazón no está contento”.\n"
                "La pierna depende del movimiento del cuerpo; si este se mueve rápido y la pierna "
                "se interrumpe bruscamente, el hombre cae. Así, quien está al servicio de alguien "
                "poderoso y es arrastrado hacia la injusticia no puede detenerse por sí solo, "
                "aunque tenga buenas intenciones."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Inmovilidad de sus caderas. Entumecimiento del "
                "hueso sacro. Peligro. El corazón se sofoca”.\n"
                "Se refiere al reposo obtenido por la fuerza. Si se intenta imponer la calma mediante "
                "una rigidez artificial en lugar de dejar que surja naturalmente del recogimiento "
                "interior, la meditación solo conducirá a resultados deplorables y sofocará el espíritu."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Inmovilidad del tronco. Sin reproches”.\n"
                "Mantener la espalda en reposo significa olvidar el ego. Aunque todavía no se ha "
                "alcanzado la liberación completa de los deseos egoístas, la disposición interior "
                "que abre el camino a una etapa más elevada no es una falta."
            ),
            5: (
                "Seis en el quinto lugar significa: “Inmovilidad de sus mandíbulas. Las palabras "
                "tienen un orden. Los remordimientos desaparecen”.\n"
                "En situaciones peligrosas, el uso de palabras presuntuosas o imprudentes lleva al "
                "arrepentimiento. Mantener la reserva en el discurso hace que las palabras tengan "
                "un significado consistente, eliminando todo motivo de lamentación."
            ),
            6: (
                "Nueve en la cima significa: “Inmovilidad magnánima. Fortuna!”.\n"
                "Representa la consumación del esfuerzo por obtener la tranquilidad. Se alcanza la "
                "paz tanto en los detalles mínimos como en un renunciamiento general que produce "
                "paz en todos los dominios y buena fortuna en todos los asuntos."
            )
        },
        "lineas": {
            1: "Detente antes de actuar; la quietud inicial te mantiene en el camino correcto.",
            2: "Si estás ligado a un movimiento general erróneo, tus buenas intenciones no bastarán para frenar.",
            3: "No fuerces la calma con rigidez; la verdadera paz debe fluir naturalmente, no por imposición.",
            4: "Busca aquietar el ego; aunque no seas libre de deseos, vas por el camino correcto.",
            5: "Mide tus palabras y mantén la reserva; el orden en el habla evita futuros remordimientos.",
            6: "Has alcanzado la paz suprema y la tranquilidad total; el éxito está asegurado en todo."
        }
    },
    53: {
        "nombre": "CHIEN / EL DESARROLLO (El progreso gradual)",
        "trigrama_sup": "Sun, Lo Suave, Viento, Madera",
        "trigrama_inf": "Ken, La Inmovilidad, la Montaña.",
        "exposicion": (
            "Se compone arriba de Sun, la madera o lo suave, y abajo de Ken, la montaña o la "
            "inmovilidad. Un árbol sobre una montaña se desarrolla lentamente y siguiendo un orden; "
            "por eso se erige sólidamente enraizado. Representa un desarrollo que progresa "
            "gradualmente, paso a paso. Al interior se encuentra el reposo que preserva de acciones "
            "precipitadas y al exterior la penetración que hace posible el progreso."
        ),
        "juicio": (
            "“El desarrollo. La doncella fue dada en matrimonio. Buena fortuna. La perseverancia es "
            "ventajosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El desarrollo de los acontecimientos que llevan a una muchacha al hogar de su esposo "
            "es lento y requiere formalidades. Este principio de progreso gradual se aplica a "
            "relaciones correctas, cooperación y al desarrollo de la propia personalidad. La "
            "precipitación no conduce a nada duradero. La evolución interior debe proceder de la "
            "paz interior para obtener resultados duraderos y no perderse en la arena."
        ),
        "imagen": (
            "“En la montaña, un árbol. La imagen del desarrollo. El hombre noble se sostiene en la "
            "dignidad y la virtud para mejorar las costumbres”.\n\n"
            "El árbol en la montaña crece lentamente y modifica el paisaje de forma duradera. De "
            "igual forma, la influencia sobre los hombres solo puede ser gradual. Para mejorar la "
            "mentalidad pública, es indispensable que la personalidad adquiera influencia y aplomo "
            "mediante un trabajo minucioso y perseverante."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “El ganso salvaje gradualmente se acerca a la orilla. El "
                "hijo joven esta en peligro. Hay habladurías. Sin reproches”.\n"
                "Representa la primera estación de un ave acuática al volar hacia el cielo. Es la "
                "situación de un joven solitario que comienza su camino. Sus pasos son lentos y "
                "vacilantes, rodeados de críticas, pero precisamente estas dificultades le impiden "
                "una prisa excesiva y aseguran su éxito final."
            ),
            2: (
                "Seis en el segundo lugar significa: “El ganso salvaje se dirige progresivamente "
                "hacia el acantilado. Comer y beber en paz y concordia. Buena fortuna”.\n"
                "El acantilado es un lugar seguro. Se ha superado la incertidumbre inicial y se tiene "
                "lo suficiente para vivir. El ganso llama a sus compañeros para compartir el "
                "alimento, imagen de la paz y la disposición a compartir la felicidad con otros."
            ),
            3: (
                "Nueve en el tercer lugar significa: “El ganso salvaje gradualmente se acerca a la "
                "meseta. El hombre sale y no vuelve. La mujer lleva un niño (en su vientre) pero no "
                "da a luz. Desgracia. Es conveniente defenderse contra los ladrones”.\n"
                "La meseta es un lugar seco inapropiado; indica que se ha avanzado demasiado lejos "
                "o por iniciativa propia precipitada, transgrediendo la ley del desarrollo natural. "
                "Esto atrae infortunio y lucha. Es mejor mantenerse en su lugar defendiéndose de "
                "ataques injustos."
            ),
            4: (
                "Seis en el cuarto lugar significa: “El ganso salvaje se acerca gradualmente al árbol. "
                "Puede que encuentre una rama plana. Sin reproches”.\n"
                "Un árbol no es el lugar natural para un ganso, pero si es inteligente encontrará "
                "una rama donde posarse. En la vida, uno enfrenta situaciones inadecuadas donde es "
                "vital ser flexible para encontrar un lugar seguro donde vivir."
            ),
            5: (
                "Nueve en el quinto lugar significa: “El ganso salvaje gradualmente se acerca a la "
                "cumbre. Por tres años la mujer no tiene hijos. Al final nada puede impedírselo. "
                "Buena fortuna”.\n"
                "En la cumbre es fácil quedar aislado y no ser reconocido por los allegados. Esto "
                "sucede a menudo por malentendidos o medios fraudulentos. Sin embargo, el "
                "desarrollo gradual permite que a la larga los malentendidos se resuelvan y llegue "
                "la reconciliación."
            ),
            6: (
                "Nueve en la cima significa: “El ganso salvaje gradualmente se acerca a las cumbres "
                "entre las nubes. Sus plumas pueden ser usadas para las danzas sagradas. Buena fortuna”.\n"
                "Representa el trabajo terminado y la vida que se eleva hacia el cielo. El hombre que "
                "se ha perfeccionado a sí mismo se convierte en una luz y un modelo para los demás. "
                "Sus actos (sus plumas) sirven de ornamento y guía incluso después de su camino."
            )
        },
        "lineas": {
            1: "Progreso inicial lento y criticado; la cautela ante el peligro asegura el éxito.",
            2: "Posición segura y éxito inicial; momento de compartir la concordia con los demás.",
            3: "Evita la precipitación y la lucha innecesaria; no te alejes del camino natural.",
            4: "Usa la flexibilidad e inteligencia para encontrar seguridad en situaciones incómodas.",
            5: "Paciencia ante el aislamiento o malentendidos; la constancia traerá la unión final.",
            6: "Éxito total y perfeccionamiento; tu ejemplo sirve de guía inspiradora para otros."
        }
    },
    54: {
        "nombre": "KUEI MEI / LA DONCELLA CASADERA",
        "trigrama_sup": "Chen Lo que Despierta, Trueno",
        "trigrama_inf": "Tui Lo Gozoso. Lago.",
        "exposicion": (
            "Arriba está Chen, el trueno o hijo mayor, y abajo Tui, el lago o hija menor. El hombre "
            "conduce y la muchacha lo sigue con satisfacción. Representa la entrada de una joven en "
            "la casa de un hombre mayor. Es uno de los signos que describen las relaciones "
            "conyugales, pero en este caso muestra una unión basada en la inclinación personal "
            "donde la joven debe someterse modestamente a la dueña de casa como una hermana menor."
        ),
        "juicio": (
            "“La doncella casadera. Las empresas traen desgracia. Nada que sea ventajoso”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Una muchacha que entra en una familia sin ser la esposa principal debe actuar con "
            "circunspección y reserva; no debe intentar suplantar a la dueña de casa. Esto se "
            "aplica a todas las relaciones libres: mientras que las uniones legales se basan en el "
            "deber y el derecho, las relaciones fundadas en la inclinación dependen de una reserva "
            "llena de tacto para durar. La libre inclinación es el principio de unión en el universo."
        ),
        "imagen": (
            "“Trueno sobre el lago: la imagen de la doncella casadera. Así el hombre noble comprende "
            "las cosas pasajeras a la luz de la eternidad final”.\n\n"
            "El trueno remueve el agua del lago, imagen de la joven que sigue al hombre por elección. "
            "Toda unión humana conlleva el peligro de malentendidos si se cede solo a los impulsos "
            "del momento. Es vital mantener siempre presente la finalidad última para evitar los "
            "escollos inevitables en las relaciones recíprocas."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “La doncella casadera como concubina. Un cojo que es "
                "capaz de caminar. Las empresas traen fortuna”.\n"
                "Representa a una joven que entra en una familia aceptando un rango inferior con "
                "modestia. Al adaptarse al conjunto, encuentra un lugar satisfactorio. Es como un "
                "servidor a quien el señor testimonia amistad; aunque su situación sea limitada "
                "como la de un cojo, es capaz de cumplir obras excelentes gracias a su naturaleza."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Un tuerto es capaz de ver. La perseverancia de "
                "un hombre solitario es ventajosa”.\n"
                "Describe a una mujer cuyo marido la desilusiona, ha sido infiel o ha muerto. Ella "
                "se queda sola, pero no pierde su luz interna. A pesar de que su 'segundo ojo' se ha "
                "apagado, permanece resueltamente leal y mantiene su integridad en la soledad."
            ),
            3: (
                "Seis en el tercer lugar significa: “La doncella casadera como una esclava. Ella se "
                "casa como concubina”.\n"
                "Muestra a alguien en una posición inferior que, al no hallar marido, acepta un rol "
                "de refugio por deseo ardiente de lo inalcanzable. Se somete a una situación "
                "incompatible con la estima propia. El oráculo no juzga, solo expone la situación "
                "para que uno aprenda la lección y elija por sí mismo."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La doncella casadera retarda el momento. Un "
                "matrimonio tardío viene a su debido tiempo”.\n"
                "Se trata de una joven virtuosa que deja pasar el momento normal de casarse para "
                "no fallar a sus principios. Esta pureza es recompensada al final, encontrando al "
                "esposo destinado a pesar de la época tardía."
            ),
            5: (
                "Seis en el quinto lugar significa: “El soberano I dio a su hija en matrimonio. Las "
                "vestimentas bordadas no eran tan bellas como las de aquéllas que la seguían. La Luna "
                "casi llena trae fortuna”.\n"
                "Una joven de alto rango hace un matrimonio modesto y sabe adaptarse con gracia. "
                "Libre de vanidad, se somete a su esposo como la Luna que no se ubica directamente "
                "frente al Sol, olvidando su rango en favor de la armonía de la unión."
            ),
            6: (
                "Seis en la cima significa: “La mujer tiene un cesto pero no hay frutas en él. El "
                "hombre apuñala a la oveja pero no mana sangre. Nada que sea ventajoso”.\n"
                "Representa una actitud impía y frívola donde las formas se respetan solo "
                "superficialmente. El sacrificio es vacío y el acto carece de esencia. No es un "
                "buen presagio para los esposos, pues la unión carece de contenido real."
            )
        },
        "lineas": {
            1: "Acepta con modestia un lugar secundario; tu excelencia natural te permitirá avanzar.",
            2: "Aunque te sientas solo o decepcionado, mantén tu lealtad y tu luz interior.",
            3: "Cuidado con someterte a situaciones indignas por deseo; evalúa tu propia estima.",
            4: "No te precipites; la pureza y la espera correcta traerán la unión destinada a tiempo.",
            5: "La sencillez y la falta de vanidad en una nueva posición aseguran el éxito y la fortuna.",
            6: "Evita las relaciones vacías que solo guardan las apariencias; carecen de fruto y sangre."
        }
    },
    55: {
        "nombre": "FENG / LA ABUNDANCIA (La plenitud)",
        "trigrama_sup": "Chen, Lo que Despierta, Trueno",
        "trigrama_inf": "Li, Lo Oscilante, Llama.",
        "exposicion": (
            "Se compone de Chen (movimiento) arriba y Li (llama/claridad) abajo. La "
            "claridad adentro y el movimiento afuera producen crecimiento y abundancia. "
            "Representa una época de civilización avanzada; sin embargo, al tratarse de un pico "
            "máximo, estas condiciones excepcionales no pueden ser permanentes."
        ),
        "juicio": (
            "“La abundancia tiene éxito. El rey alcanza la plenitud. No debes estar triste sino que "
            "debes ser como el sol a mediodía”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Instaurar una era de grandeza es un destino para quienes tienen una voluntad dirigida "
            "hacia lo grande. Aunque el tiempo de plenitud suele ser corto y seguirle la "
            "decadencia, no conviene estar triste. Solo un hombre interiormente libre de "
            "inquietud puede iluminar y reconfortar a todos como el sol en su punto más alto."
        ),
        "imagen": (
            "“Rayo y trueno vienen juntos: la imagen de la abundancia. El hombre noble decide en los "
            "litigios y aplica los castigos”.\n\n"
            "Al interior, la claridad permite un estudio exacto de los hechos; al exterior, el "
            "estremecimiento asegura la rigurosa ejecución del castigo. A diferencia del "
            "Hexagrama 21 donde las leyes se dictan, aquí se aplican y ejecutan."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Cuando un hombre encuentra al gobernante que le estaba "
                "destinado pueden permanecer juntos diez días y no hay reproches. Si se avanza, se "
                "encuentra el reconocimiento”.\n"
                "Para la abundancia es necesaria la unión de claridad y movimiento enérgico. "
                "Si dos personas con estas propiedades se encuentran durante una época de plenitud, "
                "su unión es correcta y deben actuar juntas para encontrar reconocimiento."
            ),
            2: (
                "Seis en el segundo lugar significa: “El telón es tan denso que puede verse la estrella "
                "polar a mediodía. Avanzando se encuentra la desconfianza y el odio. Cuando uno los "
                "suscita con la verdad, viene la fortuna”.\n"
                "Intrigas ensombrecen la relación entre el soberano y quien puede realizar la grandeza, "
                "como un eclipse de sol. En tal momento, la acción enérgica es imposible por "
                "la envidia. Es crucial mantenerse firme en la fuerza de la verdad interior "
                "hasta que todo se arregle."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Las malezas son de tal abundancia que permiten "
                "ver las pequeñas estrellas a mediodía. Rompe su brazo derecho. Sin reproches”.\n"
                "La imagen es de un eclipse total donde el sol se oculta progresivamente. En "
                "lo social, el príncipe está tan eclipsado que hombres insignificantes pasan sobre él, "
                "haciendo que el hombre capaz (el brazo derecho) no pueda actuar. No es su "
                "culpa si queda impedido por esta causa."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “El telón es tan espeso que la estrella polar "
                "puede ser vista a mediodía. Encuentra un gobernante semejante. Buena fortuna”.\n"
                "Aquí la oscuridad comienza a decrecer y los elementos afines se reúnen. Es "
                "necesario encontrar el complemento (la sabiduría para la energía) para procurarse la "
                "satisfacción de actuar y que todo mejore."
            ),
            5: (
                "Seis en el quinto lugar significa: “Las líneas vienen, la bendición y la gloria se "
                "acercan. Fortuna!”.\n"
                "El gobernante es humilde y está abierto al consejo de personas competentes. "
                "Al rodearse de hombres que le indican las líneas directas de acción, llega la "
                "bendición y la fortuna tanto para él como para el pueblo."
            ),
            6: (
                "Seis en la cima significa: “Su casa está en la abundancia. Esconde su familia. Fisga "
                "a través de la puerta y ya no ve a nadie. Por tres años no ve nada. Desgracia”.\n"
                "Describe a un hombre que, por arrogancia y obstinación, alcanza lo opuesto a su meta "
                ". Busca el lujo y ser el amo absoluto de su hogar con tal empeño que termina "
                "totalmente aislado de los demás."
            )
        },
        "lineas": {
            1: "Encuentro de fuerzas complementarias; actúa con decisión para obtener reconocimiento.",
            2: "Ante la desconfianza y las intrigas (eclipse), mantén tu verdad interior.",
            3: "Impedimento total por causas externas; aunque no puedas actuar, no es tu culpa.",
            4: "La oscuridad decrece; busca aliados sabios para complementar tu energía.",
            5: "Humildad y apertura al consejo traen gloria y bendición general.",
            6: "La ambición egoísta y la arrogancia conducen al aislamiento total y la desgracia."
        }
    },
    56: {
        "nombre": "LU / EL VIAJERO (El peregrino)",
        "trigrama_sup": "Li, Lo Oscilante, Fuego",
        "trigrama_inf": "Ken, La Inmovilidad, la Montaña.",
        "exposicion": (
            "La montaña (Ken) se mantiene inmóvil; sobre ella, flamea el fuego (Li) que no "
            "permanece en su lugar. No permanecen juntos. Alejamiento y separación, tal "
            "es lo propio del viajero."
        ),
        "juicio": (
            "“El viajero. Éxito a través de lo pequeño. La perseverancia es ventajosa para "
            "el viajero”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Cuando uno es viajero y extranjero no debe ser hosco ni pretencioso. Al no "
            "tener un círculo de relaciones estable, debe ser prudente y reservado para "
            "preservarse del mal. Si es cortés con los demás, tendrá éxito. El "
            "camino es su hogar; debe estar atento a ser interiormente justo y firme, "
            "deteniéndose solo en lugares propicios y tratando con buena gente."
        ),
        "imagen": (
            "“Sobre la montaña hay fuego, la imagen del viajero. Así el hombre noble "
            "tiene el espíritu claro y es prudente imponiendo penas y no deja prolongar "
            "ningún diferendo”.\n\n"
            "El fuego sobre la montaña se desplaza buscando combustible y es de corta duración. "
            "De igual modo, las penas y sentencias deben superarse rápidamente y no "
            "prolongarse indefinidamente. Las prisiones deben ser lugares de paso "
            "temporal y no residencias permanentes."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Si un peregrino se ocupa en cosas triviales atrae "
                "el infortunio sobre sí”.\n"
                "Un viajero no debe envilecerse con pequeñeces; al estar exteriormente "
                "desarmado, debe defender con más energía su dignidad interior. Buscar "
                "recepción amistosa rebajándose en burlas solo atraerá desprecio e insultos."
            ),
            2: (
                "Seis en el segundo lugar significa: “El viajero llega al albergue. Tiene sus "
                "bienes con él. Gana la perseverancia de un joven sirviente”.\n"
                "El viajero modesto y reservado no pierde el contacto con su esencia interior y "
                "por ello encuentra reposo. Conserva la estima ajena, adquiere bienes y "
                "cuenta con un servidor fiel, lo cual es un tesoro inestimable."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Se incendia el albergue del viajero. "
                "Pierde la perseverancia de su joven sirviente. Peligro”.\n"
                "Un extranjero rudo que se mezcla en asuntos que no le conciernen pierde su "
                "lugar de reposo. Si trata a los demás con arrogancia, pierde la confianza "
                "y se queda sin nadie en quien contar, volviendo su situación muy peligrosa."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “El peregrino reposa en un refugio. "
                "Obtiene sus bienes y un hacha. Mi corazón no está contento”.\n"
                "Describe a quien sabe limitar sus deseos y encuentra albergue y bienes, pero "
                "no está en seguridad con sus posesiones. Debe mantenerse en guardia con "
                "las armas en la mano, consciente de que sigue siendo un extranjero."
            ),
            5: (
                "Seis en el quinto lugar significa: “Le tira a un faisán. Lo alcanza con la "
                "primera flecha. Al final eso le trae alabanzas y una carga”.\n"
                "Como los hombres de estado que regalaban un faisán a los príncipes, el viajero "
                "logra entrar al servicio de uno. Encuentra amigos que lo recomiendan y "
                "finalmente recibe un cargo, logrando una esfera de acción en país extraño."
            ),
            6: (
                "Nueve en la cima significa: “El nido del pájaro se quema. El viajero ríe "
                "primero, pero después tendrá que lamentarse y gemir. Por descuido perdió la "
                "vaca. Desgracia”.\n"
                "Muestra la pérdida del lugar de reposo por imprudencia. Si el viajero se deja "
                "llevar por burlas y olvida su condición, terminará gimiendo. Perder la vaca "
                "simboliza perder la modesta facultad de adaptación, lo que trae malos resultados."
            )
        },
        "lineas": {
            1: "No te pierdas en trivialidades; mantén tu dignidad para evitar el desprecio.",
            2: "La modestia y la reserva te aseguran un lugar de descanso y apoyo fiel.",
            3: "La arrogancia y la intromisión destruyen tu seguridad y te dejan aislado.",
            4: "Has logrado estabilidad material, pero mantente alerta; no estás en tu hogar.",
            5: "Tu habilidad y buen comportamiento te abrirán puertas y te otorgarán un cargo.",
            6: "El descuido y la pérdida de la capacidad de adaptación llevan a la desgracia."
        }
    },
    57: {
        "nombre": "SUN / LO DOCIL (Lo penetrante, el viento)",
        "trigrama_sup": "Sun, Lo Suave, Viento, Madera",
        "trigrama_inf": "Sun, Lo Suave, Viento, Madera",
        "exposicion": (
            "Sun es un hexagrama doble que corresponde a la hija mayor. Tiene como "
            "imagen el viento o el bosque y como propiedad la suavidad que, a pesar de "
            "ser suave, penetra con persistencia como la del viento que sopla, o la de los "
            "árboles del bosque que desarrollan sus raíces. El principio oscuro, que está "
            "en él rígido e inmóvil, está disuelto por la penetración del principio luminoso "
            "que lo somete suavemente. En la naturaleza, es el viento que dispersa las "
            "nubes acumuladas, dejando el cielo claro y sereno. En la vida humana es la "
            "claridad penetrante del juicio que aniquila los sombríos motivos ocultos."
        ),
        "juicio": (
            "“Lo penetrante. Éxito a través de lo pequeño. Es ventajoso tener un lugar "
            "donde ir. Es ventajoso ver al gran hombre”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "La penetración produce efectos graduales y que pasan desapercibidos. No se "
            "la debe realizar por medios violentos sino por una influencia ininterrumpida. "
            "Para poder actuar así hay que tener una meta claramente determinada, puesto que solo una "
            "influencia penetrante actuando siempre en la misma dirección logra un resultado. "
            "Una fuerza de débil intensidad solo puede producir un efecto si ella se pone bajo "
            "la autoridad de un hombre eminente que sea capaz de crear el orden."
        ),
        "imagen": (
            "“Los vientos que se siguen. La imagen de la suave penetración. Así el hombre "
            "noble difunde sus ordenes por todas partes y ejecuta sus empresas”.\n\n"
            "La cualidad penetrante del viento reside en su carácter continuo. Toma el "
            "tiempo como un medio de acción. Es igualmente de esta manera que el pensamiento "
            "del soberano debe penetrar el alma del pueblo. Ello requiere también una acción "
            "duradera en el dominio de las explicaciones y de las órdenes. Una acción no "
            "preparada previamente provoca solo terror y repulsión."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “En el avance y en la retirada es ventajoso tener "
                "la perseverancia de un guerrero”.\n"
                "Una naturaleza suave llega a veces hasta la indecisión. Uno no se siente con "
                "la fuerza de ir resueltamente adelante. En tal caso, una resolución militar "
                "es la actitud justa para permitir de hacer con decisión lo que exige el orden "
                "de las cosas. Una disciplina resuelta es mucho más preferible que el "
                "abandono y la indecisión."
            ),
            2: (
                "Nueve en la segunda línea significa: “Penetrar bajo la cama. Se necesitan "
                "sacerdotes y magos en gran cantidad. Fortuna. Sin reproches”.\n"
                "Aquí sucede que se está tratando con enemigos ocultos, que tienen "
                "influencias secretas y que permanecen escondidos en los ángulos más "
                "oscuros. Es necesario de perseguir esos elementos hasta los rincones más "
                "secretos para determinar de qué influencias se trata. Estas acciones "
                "requieren una energía particularmente infatigable que, sin embargo, encuentra "
                "su recompensa."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Repetida penetración. Humillación”.\n"
                "La reflexión penetrante no debe ir demasiado lejos, sino ella puede interferir "
                "la capacidad de decisión. Cuando un asunto ha sido examinado a fondo, es "
                "importante de decidir y actuar. Una reflexión repetida lleva siempre a la "
                "duda y, por consiguiente, a la humillación, puesto que uno se encuentra en "
                "la incapacidad de actuar."
            ),
            4: (
                "Seis en el cuarto lugar significa: “El remordimiento se desvanece. "
                "Durante la cacería se capturan tres clases de cazas silvestres”.\n"
                "Cuando una posición de responsabilidad y la acumulación de experiencia "
                "llevan a alguien a combinar la modestia innata con la acción enérgica, se "
                "encuentra asegurado un gran éxito. Las tres clases de animales silvestres "
                "sirven de ofrenda, de presentes de hospitalidad y de alimento para consumo "
                "cotidiano; satisfacer estos tres propósitos era considerado particularmente bueno."
            ),
            5: (
                "Nueve en el quinto lugar significa: “La perseverancia trae buena fortuna. "
                "El remordimiento se desvanece. Nada de lo que se haga será desperdiciado. "
                "Sin comienzo pero con final. Antes del cambio, tres días, después del "
                "cambio, tres días. Fortuna!”.\n"
                "Aquí se trata solamente de una reforma. Un cambio y una mejora se imponen "
                "con persistencia y actitud correcta, entonces el remordimiento desaparece. "
                "Antes de efectuar el cambio, es necesario reflexionarlo escrupulosamente. "
                "Y después se debe vigilar atentamente el efecto que ese cambio produce."
            ),
            6: (
                "Nueve en la cima significa: “Penetración bajo la cama. Pierde sus bienes y "
                "su hacha. La perseverancia trae desgracia”.\n"
                "El conocimiento es suficientemente penetrante y se persiguen las malas "
                "influencias hasta en los rincones más secretos, pero ya no se tiene la fuerza "
                "para combatirlos de manera decisiva. En este caso, todo intento por "
                "penetrar en el dominio propio de la oscuridad solo puede tener consecuencias "
                "nefastas."
            )
        },
        "lineas": {
            1: "Vence la indecisión con la disciplina y resolución firme de un guerrero.",
            2: "Persigue las influencias ocultas con energía infatigable para desarmarlas.",
            3: "Evita el exceso de reflexión; una vez analizado el asunto, actúa para no humillarte.",
            4: "Combina modestia con acción enérgica para asegurar un éxito de múltiples beneficios.",
            5: "Reflexiona antes del cambio y vigila después; la persistencia correcta trae fortuna.",
            6: "No intentes penetrar en la oscuridad si ya no tienes fuerza para combatirla; trae desgracia."
        }
    },
    58: {
        "nombre": "TUI / LO PLACENTERO, EL LAGO",
        "trigrama_sup": "Tui, Lo Gozoso, Lago.",
        "trigrama_inf": "Tui, Lo Gozoso, Lago.",
        "exposicion": (
            "Tui es como Sun uno de los ocho hexagramas dobles. Tui representa la hija "
            "menor; su imagen es un lago sonriente, su propiedad es la alegría. La alegría "
            "no reside, como podría creerse, en la maleabilidad que se manifiesta en el "
            "trazo superior. En efecto, la propiedad del principio maleable y oscuro no es "
            "la alegría sino la melancolía. La alegría reside más bien sobre la presencia, "
            "en el interior, de dos trazos fuertes que se exteriorizan por intermedio de un "
            "trazo débil. La verdadera alegría proviene entonces de la firmeza y la fuerza que se "
            "encuentran al interior y que se exteriorizan bajo una forma tierna y dulce."
        ),
        "juicio": (
            "“Lo gozoso. Éxito. La perseverancia es favorable”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El ánimo gozoso es contagioso y comunicativo, es por eso que conduce al "
            "éxito. Pero es necesario que la alegría esté fundada sobre la firmeza para no "
            "degenerar en algo desenfrenado. La verdad y la fuerza deben residir en el "
            "corazón mientras que la dulzura se manifiesta en las relaciones con los "
            "demás. De esa manera se adopta una actitud correcta hacia Dios y hacia "
            "nuestros semejantes que conduce a un cierto resultado. Si se conquistan los "
            "corazones de nuestros semejantes con amistad, se conseguirá que ellos "
            "acepten las cosas penosas de buen grado e incluso podrán enfrentar a la "
            "muerte sin espantarse. Tan grande es el poder de la alegría sobre los "
            "humanos."
        ),
        "imagen": (
            "“Lagos descansando unos sobre otros. La imagen de la alegría. Así procede el "
            "hombre noble reuniendo sus amigos para deliberar y para actuar”.\n\n"
            "Un lago se evapora y se seca gradualmente. Pero cuando dos lagos se hallan "
            "en comunicación entre ellos no se secan tan fácilmente puesto que ellos se "
            "enriquecen mutuamente. Lo mismo sucede en el dominio del conocimiento. "
            "El saber debe ser una fuerza vivificante y refrescante. Esto se logra "
            "solamente a través de un intercambio estimulante con amigos con quienes "
            "discutir y practicar las verdades vitales. El saber se convierte así en un "
            "asunto de muchas facetas, dotado de una alegre sutileza que esclarece y "
            "pondera el mundo exterior."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Alegría gozosa. Buena fortuna”.\n"
                "Una alegría serena, sin palabras y contenida, que no desea nada exterior y "
                "se muestra contenta con lo que tiene, permanece exenta de todo deseo o "
                "rechazo egoísta. En esta libertad radica la buena fortuna, porque emana de "
                "la tranquila seguridad del corazón que se fortalece a sí mismo."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Sincera alegría. Buena fortuna. Los "
                "remordimientos desaparecen”.\n"
                "Sucede a menudo que uno se encuentre rodeado de seres vulgares con los "
                "cuales uno se siente tentado por placeres indignos de un hombre noble. "
                "Si uno está fortalecido por tal conocimiento, no dejará desviar la voluntad y "
                "rehusará encontrar el placer en tales maneras de actuar. En consecuencia "
                "uno evitará así toda ocasión de arrepentimiento."
            ),
            3: (
                "Seis en el tercer lugar significa: “Alegría que viene. Desgracia”.\n"
                "La verdadera alegría debe emanar de una fuente interior. Pero si uno está "
                "interiormente vacío y si uno se pierde en el mundo exterior, las alegrías "
                "provienen de afuera. Esto es lo que mucha gente llama diversión. Los seres "
                "que como consecuencia de su inconsistencia interior necesitan diversiones "
                "tendrán siempre ocasión de distraerse. Así se pierden "
                "cada vez más y eso tiene naturalmente malas consecuencias."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La serenidad deliberada no es apacible. "
                "Después de superar los errores uno se siente contento”.\n"
                "Sucede a menudo que uno se siente en suspenso entre diferentes clases de "
                "alegría. Mientras que no se haya decidido qué clase se elegirá, uno "
                "permanece interiormente inquieto. Es solamente cuando se ha reconocido "
                "claramente que las pasiones llevan al sufrimiento que uno puede decidir "
                "deshacerse de lo que es inferior y puede buscar las alegrías superiores. "
                "Entonces uno encuentra en sí mismo la verdadera serenidad y el verdadero reposo."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Oponer lo verdadero a lo destructivo "
                "es peligroso”.\n"
                "Los elementos de peligro se acercan incluso a los mejores hombres. Si "
                "alguien se permite componer con ellos, su influencia destructora obrará "
                "sigilosa pero seguramente y traerá con ella el peligro. Pero quien reconozca "
                "la situación y sepa discernir el peligro sabrá precaverse y permanecerá ileso."
            ),
            6: (
                "Seis en la cima significa: “Seductora serenidad”.\n"
                "Quien sea interiormente vanidoso atrae hacia sí mismo los placeres de la "
                "disipación, y con ellos experimentará el sufrimiento. Si uno no está "
                "afirmado interiormente, los placeres exteriores ejercerán una acción tan fuerte "
                "que uno se dejará arrastrar por ellos. Aquí ya no es cuestión de peligro, de "
                "fortuna o de infortunio. Se ha dejado escapar el timón de su propia vida y lo que "
                "acontecerá dependerá del azar y de las influencias externas."
            )
        },
        "lineas": {
            1: "Alegría serena y contenida que nace de la autosuficiencia y seguridad interior.",
            2: "Evita placeres vulgares mediante la firmeza de voluntad; así evitarás remordimientos.",
            3: "Cuidado con buscar diversión afuera por vacío interior; solo trae inconsistencia y pérdida.",
            4: "Decídete por alegrías superiores sobre las pasiones para hallar verdadera paz y reposo.",
            5: "No pactes con influencias destructivas; reconócelas a tiempo para mantenerte ileso.",
            6: "La vanidad te hace vulnerable a placeres que te arrastran y te quitan el control de tu vida."
        }
    },
    59: {
        "nombre": "HUAN / LA DISOLUCIÓN (La dispersión)",
        "trigrama_sup": "Sun Lo Suave, Viento",
        "trigrama_inf": "Kan El Abismo, Agua.",
        "exposicion": (
            "El viento que sopla sobre el agua la dispersa, disolviéndola en niebla y "
            "espuma. Se sugiere que cuando la energía vital de un hombre se encuentra "
            "obstruida en su interior, la suavidad sirve para despertarla y traerla a luz."
        ),
        "juicio": (
            "“Disolución. Éxito. El rey se acerca al templo. Será provechoso cruzar las "
            "grandes aguas. La perseverancia es ventajosa”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Aquí se trata de la dispersión y de la disolución del egoísmo que separa. "
            "Para vencerlo, el hombre necesita una fuerza religiosa; la celebración en "
            "común de ritos sagrados era el medio para hacer comulgar los corazones en las "
            "mismas emociones. Otro medio era el trabajo en común en grandes "
            "empresas colectivas que proponen una gran meta a la voluntad, superando las "
            "barreras que separan."
        ),
        "imagen": (
            "“El viento sopla sobre el agua: La imagen de la disolución. Así, los reyes "
            "antiguos rendían sacrificios al Señor y construían templos”.\n\n"
            "Cuando llegan las suaves brisas de la primavera, la rigidez del hielo cesa y lo "
            "que estaba disperso se funde y se reúne. Es lo mismo en el espíritu del pueblo: "
            "la codicia y el egoísmo aíslan a los humanos; por eso es necesaria una emoción "
            "religiosa que se apodere de los corazones para experimentar la unidad gracias al "
            "poder del sentimiento de comunión."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Fortuna. Trae ayuda con la fuerza de un caballo”.\n"
                "Se trata de superar la desunión antes de que se haya realizado completamente, "
                "venciendo los primeros síntomas. Hay que actuar con rapidez y vigor "
                "para disipar las incomprensiones y la desconfianza recíproca."
            ),
            2: (
                "Nueve en el segundo lugar significa: “En la disolución se recurre a su "
                "apoyo. Los remordimientos desaparecen”.\n"
                "Cuando alguien descubre en sí mismo los comienzos de una alienación de los demás, "
                "es importante procurar disolver esos bloqueos buscando un soporte en un juicio "
                "moderado y justo aliado con la buena voluntad."
            ),
            3: (
                "Seis en el tercer lugar significa: “Se disuelve a sí mismo. Sin "
                "remordimientos”.\n"
                "En circunstancias de trabajo arduo, se debe dejar completamente de lado la "
                "propia personalidad y dispersar todo lo que el yo quisiera reunir a su "
                "alrededor. Solo mediante un gran renunciamiento se adquiere la fuerza "
                "necesaria para realizar grandes tareas."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Se destaca de su grupo. Sublime fortuna. "
                "Por la disolución se pasa a la acumulación. Es algo en lo que la gente común "
                "no piensa”.\n"
                "Al trabajar en tareas de alcance colectivo, uno debe apartarse de las amistades "
                "privadas. Solo manteniéndose por encima de los grupos se puede cumplir "
                "una obra decisiva, ganando lo que está alejado al renunciar a lo que es próximo."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Sus fuertes gritos disuelven como el "
                "sudor. Disolución. El rey permanece sin reproches”.\n"
                "Una gran idea es el punto alrededor del cual se organiza la recuperación en "
                "tiempos de dispersión general. Como una enfermedad que termina su "
                "crisis con sudor, las ideas estimulantes constituyen una verdadera liberación "
                "bajo un hombre capaz de disipar los malentendidos."
            ),
            6: (
                "Nueve en la cima significa: “Disuelve su sangre. Irse, manteniéndose a "
                "distancia, salir, permanecen sin reproches”.\n"
                "Significa disolver lo que podría traer sangre y heridas para evitar el peligro. "
                "El pensamiento aquí es liberar a los seres queridos ayudándoles a partir antes "
                "que llegue el peligro, o a salir de uno que ya los ha atacado."
            )
        },
        "lineas": {
            1: "Actúa con rapidez y fuerza para disipar malentendidos antes de que crezcan.",
            2: "Busca apoyo en un juicio justo y buena voluntad para disolver tu alienación.",
            3: "Renuncia al egoísmo para ganar la fuerza necesaria en grandes tareas.",
            4: "Elévate por encima de los grupos privados para cumplir una obra de alcance colectivo.",
            5: "Organiza la recuperación mediante una gran idea que disipe la obstrucción general.",
            6: "Aleja a los seres queridos y a ti mismo del peligro inminente para evitar heridas."
        }
    },
    60: {
        "nombre": "CHIEH / LA LIMITACIÓN",
        "trigrama_sup": "K'an El Abismo, Agua",
        "trigrama_inf": "Tui Lo Gozoso, Lago.",
        "exposicion": (
            "El lago ocupa un espacio limitado. Si recibe más agua se desborda. Es por "
            "eso que se debe ponérsele límites. La imagen muestra agua arriba y abajo, "
            "limitando el firmamiento entre ellas. La palabra china que expresa la "
            "limitación designa claramente los nudos que demarcan una caña de bambú. "
            "En la vida corriente, la misma palabra designa la economía que fija límites "
            "para los gastos. En la vida moral, son los límites rigurosos que el hombre "
            "noble impone a sus actos, que son la lealtad y el desinterés."
        ),
        "juicio": (
            "“Limitación. Éxito. Una limitación amarga no debe practicarse con "
            "perseverancia”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Las limitaciones son molestas pero efectivas. Si vivimos económicamente en "
            "tiempos normales estaremos preparados para los tiempos de penuria. Ser "
            "prudentes nos salvará de la humillación. Las limitaciones son "
            "indispensables para regular el orden del mundo. De la misma manera, la "
            "economía que pone límites precisos a los dispendios preserva los bienes e "
            "impide perjuicios a la gente. Sin embargo, en la limitación también hay que "
            "observar mesura. Si alguien impone a su propia naturaleza limitaciones "
            "demasiado severas, ella sufriría."
        ),
        "imagen": (
            "“Agua sobre el lago. La imagen de la limitación. El hombre noble crea "
            "número y medida y examina la naturaleza de la virtud y la conducta "
            "correcta”.\n\n"
            "Un lago puede contener sólo una parte definida de la infinita cantidad de "
            "agua; esa es su peculiaridad. El individuo adquiere su significado con el "
            "establecimiento y el trazado de límites en la vida. Es por eso que aquí se "
            "trata de fijar claramente esos límites que son como la columna vertebral de "
            "la moralidad. Su vida se fundiría en lo indefinido sin límites que sean "
            "establecidos libremente y que configuren el deber."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “No salir de la puerta y del patio de la corte "
                "es sin reproches”.\n"
                "A menudo un hombre puede emprender algo y encontrarse enfrentado a una "
                "situación insuperable. Debe saber cuando detenerse. Si esto se entiende "
                "correctamente, se acumula en nosotros una fuerza que nos capacita para "
                "actuar enérgicamente cuando llegue la época apropiada. La discreción tiene "
                "una importancia fundamental para preparar empresas importantes."
            ),
            2: (
                "Nueve en el segundo lugar significa: “No salir del portal y del patio de la "
                "corte trae desgracia”.\n"
                "Cuando ha llegado el tiempo de actuar hay que hacerlo rápidamente. Es bueno "
                "hesitar hasta que el momento de actuar no ha llegado, pero no demasiado. "
                "Cuando los obstáculos han sido separados de tal suerte que la acción ha "
                "devenido posible, la hesitación ansiosa es una falta que lleva seguramente "
                "al infortunio porque se ha perdido la oportunidad justa."
            ),
            3: (
                "Seis en el tercer lugar significa: “Quien no conoce limitaciones tendrá "
                "motivo para lamentarse. Sin reproches”.\n"
                "Si un individuo busca sólo los placeres y la diversión es fácil que pierda el "
                "sentido de la limitación necesaria. Pero cuando se abandona a la disipación "
                "tendrá que sufrir las consecuencias junto con el remordimiento. Es solamente "
                "examinando sus propias errores que uno devendrá exento de faltas."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Limitación satisfecha. Éxito”.\n"
                "Toda limitación tiene su valor, pero cuando requiere un esfuerzo persistente "
                "exige un gasto de energía demasiado grande. Cuando se trata de una "
                "limitación natural necesariamente eso lleva al éxito, en cuanto significa "
                "un ahorro de energía. La energía no debe consumirse en lucha vana con los "
                "objetos, sino aplicarla al provecho del asunto y así se asegura el éxito."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Dulces limitaciones traen buena "
                "fortuna. Ir trae estima”.\n"
                "Las limitaciones deben ser conducidas de manera correcta para que sean "
                "efectivas. Si un hombre que ocupa una alta posición se aplica primero las "
                "limitaciones a sí mismo exigiendo poco de los demás y consigue un resultado "
                "con medios modestos, obtendrá así la fortuna. Cuando así ocurre, su "
                "ejemplo es emulado y todo lo que emprende triunfa."
            ),
            6: (
                "Seis en la cima significa: “Limitación amarga: la perseverancia trae "
                "desgracia. Los remordimientos desaparecen”.\n"
                "Cuando se imponen límites demasiado severos, los hombres no los soportan. "
                "Mientras más se aplique esta severidad con lógica, más malo será el resultado. "
                "Pero, si esta severidad implacable no es usada con persistencia y de manera "
                "normal, hay momentos en que ella constituye el único medio de preservarse "
                "del error. Hay situaciones donde la ausencia de piedad con respecto a sí "
                "mismo es el solo medio de salvar su alma."
            )
        },
        "lineas": {
            1: "Saber cuándo detenerse y guardar discreción prepara para actuar con fuerza después.",
            2: "No pierdas la oportunidad justa por hesitación ansiosa cuando el camino está despejado.",
            3: "Sin límites en el placer se llega a la disipación; reconoce tus errores para enmendarte.",
            4: "La limitación natural ahorra energía y asegura el éxito al aplicarla con provecho.",
            5: "Impón límites primero a ti mismo para que tu ejemplo sea emulado y logres el triunfo.",
            6: "La severidad extrema es insostenible, pero a veces es el único medio para salvar el alma."
        }
    },
    61: {
        "nombre": "CHUNG FU / LA VERDAD INTERIOR",
        "trigrama_sup": "Sun Lo Suave, Viento",
        "trigrama_inf": "Tui Lo Gozoso, Lago.",
        "exposicion": (
            "El viento sopla sobre el lago y ondea su superficie. Los efectos visibles de lo "
            "invisible se manifiestan por sí mismos. El hexagrama se compone de trazos "
            "llenos en las partes superior e inferior, mientras que al centro él es libre. "
            "Indica un corazón libre de prejuicios y en consecuencia abierto a la verdad. "
            "Por el contrario, cada uno de los trigramas tiene un trazo lleno en su centro. "
            "Así se encuentra traducida la fuerza de la verdad interior en los efectos que "
            "ella opera. El hexagrama es la imagen de una pata de pájaro sobre una cría. "
            "Sugiere la idea de incubación."
        ),
        "juicio": (
            "“La verdad interior. Cerdos y peces. Buena fortuna. Será provechoso cruzar la "
            "gran corriente. La perseverancia es conveniente”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Los cerdos y los peces son los animales menos espirituales y más difíciles de "
            "influir. La fuerza de la verdad interior debe alcanzar un alto grado antes de "
            "extender su acción a ellos. El secreto del éxito reside en liberarse interiormente "
            "de todo prejuicio y dejar que la psiquis de la otra persona entre en nosotros "
            "sin restricciones. Solo así podremos comprenderlo y ganar poder sobre él. "
            "Toda asociación basada en un interés común puede cesar en cualquier momento; "
            "sólo cuando los lazos se basan en lo correcto pueden superar firmemente "
            "todos los obstáculos."
        ),
        "imagen": (
            "“Viento sobre el lago: la imagen de la verdad interior. El hombre noble discute "
            "el caso criminal para retardar la ejecución de las penas”.\n\n"
            "El hombre noble, cuando está obligado a juzgar los errores del prójimo, procura "
            "comprender con profundidad el sentido interior para formarse así un juicio "
            "lleno de simpatía sobre las circunstancias. Una comprensión profunda que sabe "
            "perdonar era considerada como la suprema justicia; emanaba de un sentido "
            "moral superior y buscaba provocar una fuerte impresión moral."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Estar preparado trae buena fortuna. Si hay "
                "pensamientos ocultos, es inquietante”.\n"
                "La fuerza de la verdad interior exige que uno esté en sí mismo fuerte y "
                "preparado. Si por el contrario uno quisiera cultivar relaciones secretas de "
                "naturaleza particular, ello lo privaría de su autonomía interior y aumentaría "
                "la inquietud y la preocupación."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Una grulla llamando en la oscuridad. "
                "Su cría le contesta. Tengo una buena copa. Yo la compartiré contigo”.\n"
                "Se trata de la influencia involuntaria de la naturaleza interior sobre seres "
                "que abrigan las mismas disposiciones. Allí donde se expresa un sentimiento "
                "con sinceridad y pureza, se ejerce una influencia secreta a lo lejos. La "
                "influencia es el reflejo de lo que sale de nuestro corazón; una voluntad "
                "deliberada por producirla no hará otra cosa que destruirla."
            ),
            3: (
                "Seis en el tercer lugar significa: “Encuentra un compañero. Algunas "
                "veces toca el tambor, otras veces se detiene. Algunas veces solloza, otras "
                "veces canta”.\n"
                "Aquí la fuerza no se encuentra en la esencia de la persona sino en las "
                "relaciones con otras personas. Al depender de un acuerdo interior con otros, "
                "es inevitable ser bamboleado entre la alegría y la pena. La cuestión de "
                "saber si este estado es resentido como penoso o feliz se deja al libre "
                "arbitrio de la persona concernida."
            ),
            4: (
                "Seis en el cuarto lugar significa: “La Luna está casi llena. El caballo del "
                "atelaje va perdido. Sin reproches”.\n"
                "Para aumentar la fuerza de la verdad interior uno debe dirigirse hacia lo alto "
                "con humildad, como la luna recibe iluminación del sol. Se debe también "
                "renunciar a los clanes. Solamente cuando se prosigue el camino sin mirar "
                "de soslayo a los compañeros, se posee la libertad interior que hace avanzar."
            ),
            5: (
                "Nueve en el quinto lugar significa: “Se posee la verdad que une. Sin "
                "reproches”.\n"
                "Se muestra al soberano que reúne todas las cosas gracias a la fuerza de su "
                "naturaleza. Su fuerza de sugestión debe emanar de una fuerza de carácter tan "
                "amplia que pueda influenciar y unir a todos con firmeza. Sin esta fuerza "
                "central, toda unión exterior será engañosa y se romperá en el momento decisivo."
            ),
            6: (
                "Nueve en la cima significa: “El canto del gallo penetra hasta el cielo. La "
                "perseverancia trae desgracia”.\n"
                "Se puede suscitar la fe con simples palabras, como el gallo canta al amanecer, "
                "pero el gallo no puede por sí mismo volar hasta el cielo. Si se persiste "
                "en tratar de alcanzar efectos superiores solo con palabras, sin una realidad "
                "interior que las respalde, las consecuencias son enojosas."
            )
        },
        "lineas": {
            1: "Mantente fuerte y autónomo en ti mismo; evita lazos secretos que quitan libertad.",
            2: "La sinceridad del corazón ejerce una influencia natural y atrae a seres afines.",
            3: "No dependas servilmente de otros para tu equilibrio emocional o estabilidad.",
            4: "Busca la iluminación superior con humildad y avanza sin distraerte por vínculos sociales.",
            5: "La verdadera unidad nace de una fuerza de carácter capaz de influenciar a los demás.",
            6: "Las palabras sin fundamento interior no logran resultados duraderos; no persistas en ello."
        }
    },
    62: {
        "nombre": "HSIAO KUO / LA PREPONDERANCIA DE LO PEQUEÑO",
        "trigrama_sup": "Chen Lo que Despierta, Trueno",
        "trigrama_inf": "Ken La Inmovilidad, la Montaña.",
        "exposicion": (
            "En este hexagrama los trazos débiles, ubicados en el exterior, son los que "
            "predominan sobre los trazos fuertes que están en el interior. Es allí "
            "donde reside la situación excepcional descripta. Si uno ocupa una situación "
            "de autoridad para la que no está adaptado por naturaleza, una prudencia "
            "extraordinaria es indispensable."
        ),
        "juicio": (
            "“Preponderancia de lo pequeño. Éxito. La perseverancia es ventajosa. Se "
            "pueden hacer cosas pequeñas, no se pueden hacer cosas grandes. El pájaro "
            "que vuela trae el mensaje. No es bueno empeñarse en subir, es bueno "
            "permanecer en lo bajo. Gran fortuna”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Una humildad y una delicadeza de conciencia excepcionales serán seguramente "
            "recompensadas por el éxito. Es importante que estas aptitudes permanezcan "
            "ligadas a la dignidad para no envilecerse. No debe dejarse ilusionar con la "
            "idea de un gran éxito porque falta la energía para ello; el mensaje es "
            "contentarse con las realidades más bajas. El signo ofrece la imagen de un "
            "pájaro que planea y que debe descender a la tierra donde está su nido."
        ),
        "imagen": (
            "“Trueno sobre la montaña. La imagen de la preponderancia de lo pequeño. "
            "En su conducta el hombre noble da preponderancia al respeto; en el luto da "
            "preponderancia a la aflicción; en sus gastos da preponderancia a la "
            "economía”.\n\n"
            "El trueno en la montaña es mucho más cercano y exige tener presente su deber "
            "de una manera más directa e inmediata. El hombre noble debe ser "
            "excepcionalmente preciso en sus acciones; la verdadera compasión debe tener "
            "más valor que las formas exteriores y sus gastos personales deben ser "
            "extremadamente simples."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Volando el pájaro encuentra el infortunio”.\n"
                "El pájaro debe permanecer en su nido hasta que sus plumas hayan crecido. "
                "Si quiere volar demasiado temprano atrae la desgracia. Las medidas "
                "extraordinarias solo deben emplearse como último recurso, conformándose "
                "a las reglas tradicionales tanto como sea posible."
            ),
            2: (
                "Seis en el segundo lugar significa: “Ella pasa delante de sus antepasados "
                "y encuentra la matriarca. No llega hasta su príncipe, pero sí a un oficial. "
                "Sin reproches”.\n"
                "Se trata de casos excepcionales donde un desvío de la regla no es una falta. "
                "Si un funcionario no encuentra al príncipe, no debe forzar los "
                "acontecimientos sino cumplir cuidadosamente su deber acomodándose entre "
                "los funcionarios; esta reserva extraordinaria está justificada."
            ),
            3: (
                "Nueve en el tercer lugar significa: “Si uno no es extraordinariamente "
                "cauteloso alguien puede venir por detrás y golpearlo. Desgracia”.\n"
                "En situaciones excepcionales, una prudencia extraordinaria es indispensable. "
                "Quien, por orgullo o descuido, desdeña tomar precauciones pensando que "
                "es una actitud mezquina, se expone a peligros que se acercan por detrás "
                "y que no es capaz de evitar."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “Sin reproches. Sin pasar delante de él "
                "se lo encuentra. Ir acarrea el peligro. Uno debe estar en guardia. No actuar. "
                "Ser constantemente perseverante”.\n"
                "La dureza de carácter debe ser temperada por una posición condescendiente. "
                "Nada debe emprenderse por sí mismo para alcanzar lo que se desea; actuar "
                "por la fuerza expondría al peligro. Es necesario ponerse en guardia "
                "y conservar la perseverancia interior."
            ),
            5: (
                "Seis en el quinto lugar significa: “Nubes densas, no hay lluvia del "
                "territorio de oeste. El príncipe dispara y alcanza quienes están en la "
                "caverna”.\n"
                "En épocas excepcionales puede existir un soberano nato impotente por estar "
                "solo y sin ayudantes. Debe buscar asistentes con humildad en el secreto "
                "donde ellos se han retirado. Gracias a esa humildad se encuentra al hombre "
                "conveniente para lograr una obra excepcional a pesar de las dificultades."
            ),
            6: (
                "Seis en la cima significa: “Pasa junto a él sin encontrarlo. El pájaro que "
                "vuela lo abandona. Desgracia. Eso significa infortunio y daño”.\n"
                "Si alguien pasa más allá de la meta, no acierta. Quien no sabe pasar por alto "
                "lo pequeño y quiere ir siempre más lejos en épocas extraordinarias, "
                "atrae sobre sí la desgracia porque se aleja del orden natural."
            )
        },
        "lineas": {
            1: "No intentes logros prematuros; espera a estar preparado para evitar el infortunio.",
            2: "En situaciones excepcionales, cumple tu deber con reserva y sin forzar los hechos.",
            3: "Mantén una cautela extrema para evitar peligros ocultos que surgen por descuidos.",
            4: "No actúes por la fuerza; mantén la perseverancia y una actitud reservada.",
            5: "Busca con humildad a los colaboradores adecuados para realizar una obra excepcional.",
            6: "No te excedas en tus ambiciones; ir más allá de la meta natural trae daño y desgracia."
        }
    },
    63: {
        "nombre": "CHI CHI / DESPUÉS DE LA TERMINACIÓN",
        "trigrama_sup": "K'an El Abismo, Agua",
        "trigrama_inf": "Li Lo Oscilante, Fuego.",
        "exposicion": (
            "Este signo es el derivado del hexagrama N° 11, Tai, 'la paz'. El pasaje de la "
            "confusión al orden se ha terminado, ahora todo está en su justo lugar hasta "
            "el más mínimo detalle. Es un aspecto muy favorable, aunque todavía ofrece "
            "materia para reflexionar. Es precisamente cuando se ha logrado el equilibrio "
            "perfecto que cada movimiento puede engendrar la aparición de la decadencia. "
            "Este hexagrama indica las condiciones de un apogeo que hacen necesaria "
            "una extrema prudencia."
        ),
        "juicio": (
            "“Después de la terminación. Éxito en asuntos pequeños. La perseverancia es "
            "ventajosa. Al comienzo fortuna, al final disturbios”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "El pasaje de la vieja época a la nueva ya se ha realizado. En principio, todo "
            "está ya puesto en orden y las cosas marchan por ellas mismas. Eso conduce "
            "fácilmente a relajarse y a dejar que las cosas sigan su camino sin "
            "preocuparse por ellas en detalle. Esta negligencia es la raíz de todos los "
            "males y provoca necesariamente la aparición de los síntomas de decadencia. "
            "Quien lo comprende puede evitar los efectos gracias a una perseverancia "
            "y una prudencia infalibles."
        ),
        "imagen": (
            "“Agua sobre el fuego: la imagen de la situación después de la terminación. "
            "Así el hombre noble reflexiona sobre la desgracia y se prepara por anticipado "
            "contra ella”.\n\n"
            "Cuando el agua está en un hervidor sobre el fuego, los dos elementos se "
            "relacionan entre sí y crean energía (vapor). Sin embargo, la tensión que "
            "resulta exige una vigilancia: si el agua desborda apaga el fuego; si el "
            "calor es demasiado grande, el agua se evapora. Sólo una grande prudencia "
            "puede prevenir los daños cuando todas las fuerzas se equilibran. El sabio "
            "sabe reconocer los momentos que encierran peligro y evitarlos gracias a las "
            "precauciones tomadas a tiempo."
        ),
        "lineas_detalle": {
            1: (
                "Nueve en la base significa: “Frena sus ruedas. Mete su cola en el agua. Sin "
                "reproches”.\n"
                "Después de una gran transición, la presión ávida de emprender no es buena "
                "y conduce a la caída porque apunta más allá de la meta. Un carácter firme "
                "no se deja ganar por el vértigo general sino que frena a tiempo su carrera. "
                "Aunque sea afectado por las consecuencias generales, no recibirá gran daño "
                "porque sabe adoptar la actitud correcta."
            ),
            2: (
                "Seis en el segundo lugar significa: “La mujer pierde la cortina de su "
                "carruaje. No corras tras ella; al séptimo día la encontrarás”.\n"
                "Después de la terminación, los gobernantes pueden mostrarse arrogantes y "
                "dejar de apoyar talentos desconocidos. Si alguien no recibe la confianza "
                "necesaria, no debe buscar por todos los medios ponerse en valor (arribismo). "
                "Debe esperar apaciblemente y desarrollar su valor personal. Lo que "
                "pertenece a alguien no puede ser perdido a lo largo del tiempo."
            ),
            3: (
                "Nueve en el tercer lugar significa: “El ilustre antepasado castiga el país "
                "del diablo. Al cabo de tres años lo conquista. No hay que emplear gente "
                "vulgar”.\n"
                "Después de la terminación y cuando el interior está en orden, comienza a "
                "manifestarse una necesidad de expansión. Se deben prever largos combates "
                "y una política justa es importante. Toda empresa ambiciosa comporta un "
                "impulso hacia la expansión con todos los peligros que le son asociados "
                "."
            ),
            4: (
                "Seis en el cuarto lugar significa: “Las mejores vestimentas se vuelven "
                "harapos. Sé cuidadoso durante todo el día”.\n"
                "En tiempos florecientes pueden ocurrir convulsiones ocasionales que pongan "
                "al descubierto males ocultos de la sociedad. Si la situación global es "
                "favorable, esos males pueden ser superados y disimulados, pero el hombre "
                "inteligente toma esos incidentes como serias advertencias que no hay que "
                "descuidar para evitar malas consecuencias."
            ),
            5: (
                "Seis en el quinto lugar significa: “El vecino del Este que mata un buey no "
                "alcanza la felicidad verdadera que puede esperar el vecino del Oeste con su "
                "pequeña ofrenda”.\n"
                "Después de la terminación, las viejas formas simples suelen ser reemplazadas "
                "por ritos elaborados y fasto exterior desprovisto de seriedad interior. "
                "Mientras el hombre ve lo que aparece ante sus ojos, Dios mira el corazón. "
                "Un sacrificio simple ofrecido con piedad es fuente de más grandes bendiciones "
                "que un culto fastuoso pero frío."
            ),
            6: (
                "Seis en la cima significa: “Mete la cabeza en el agua. Peligro”.\n"
                "Después de haber cruzado la corriente no es necesario volver a meter la "
                "cabeza en el agua intentando regresar. Mirar hacia atrás por una "
                "admiración de sí mismo frívola o por fascinación ante el peligro superado "
                "no conduce a nada agradable. Si uno se expone así al peligro sin avanzar, "
                "será víctima de él."
            )
        },
        "lineas": {
            1: "Frena a tiempo tu carrera para no exceder la meta por el vértigo del progreso.",
            2: "No te precipites buscando reconocimiento; desarrolla tu valor personal y espera.",
            3: "Las empresas de expansión requieren tiempo, firmeza y evitar el uso de gente vulgar.",
            4: "No descuides los pequeños males que surgen; tómalos como advertencias serias.",
            5: "La sinceridad y sencillez interior valen más que las ceremonias fastuosas pero vacías.",
            6: "No te detengas a mirar hacia atrás por vanidad; sigue adelante para evitar el peligro."
        }
    },
    64: {
        "nombre": "WE I CHI / ANTES DE LA TERMINACIÓN",
        "trigrama_sup": "Li Lo Oscilante, Llama.",
        "trigrama_inf": "K'an El Abismo, Agua",
        "exposicion": (
            "Este hexagrama indica una época de transición todavía no completa del "
            "desorden al orden. Sin duda, el cambio ya está preparado: todas las líneas "
            "del trigrama superior se encuentran en efecto relacionadas con las del "
            "trigrama inferior, pero ellas no están todavía en su lugar. Mientras "
            "que el hexagrama precedente es análogo al otoño, el hexagrama presente es "
            "semejante a la primavera que lleva de la estancación del invierno a la "
            "fecundidad del verano. Con esta perspectiva se cierra el Libro de los Cambios."
        ),
        "juicio": (
            "“Antes de la terminación. Éxito. Pero si el pequeño zorro mete su cola en el "
            "agua antes de completar el cruce, no hay nada que sea ventajoso”.\n\n"
            "NOTAS DEL JUICIO:\n"
            "Las condiciones son difíciles y la tarea es grande: llevar el mundo de la "
            "confusión al orden. Para lograrlo, hay que moverse cautelosamente como un "
            "zorro joven que cruza sobre el hielo, alerta a los crujidos y buscando los "
            "lugares seguros. Si se avanza intrépidamente sin prudencia, se fracasará "
            "justo antes de terminar. En los momentos que preceden el cumplimiento de una "
            "tarea, la reflexión y la cautela son condiciones fundamentales del éxito."
        ),
        "imagen": (
            "“Fuego sobre el agua. La imagen de las condiciones antes del cumplimiento. "
            "El hombre noble es cuidadoso en diferenciar las cosas con el fin de que cada "
            "una encuentre su lugar”.\n\n"
            "Cuando el fuego está arriba y el agua abajo, sus efectos van en sentido diferente "
            "y permanecen sin relación. Si deseamos lograr algo, debemos investigar la "
            "naturaleza de las fuerzas en cuestión y asignarles a cada una el lugar "
            "apropiado. Para disponer de las fuerzas exteriores, es necesario ante todo "
            "adoptar uno mismo el punto de vista correcto."
        ),
        "lineas_detalle": {
            1: (
                "Seis en la base significa: “Mete su cola en el agua. Humillación”.\n"
                "En tiempos de desorden es tentador avanzar con prisa para realizar algo "
                "visible, pero este entusiasmo lleva al fracaso y a la humillación si no "
                "ha llegado el momento oportuno de actuar. Es pertinente ahorrarse la "
                "humillación del fracaso por medio de una actitud de reserva."
            ),
            2: (
                "Nueve en el segundo lugar significa: “Frena sus ruedas. La perseverancia "
                "trae buena fortuna”.\n"
                "El tiempo de actuar todavía no ha llegado, pero la paciencia necesaria no "
                "es una espera perezosa. Hay que desarrollar en nosotros las fuerzas "
                "que nos hagan avanzar, como un carro listo para el pasaje que todavía se "
                "debe frenar. Si uno se mantiene firme en su resolución, al final todo "
                "irá bien."
            ),
            3: (
                "Seis en el tercer lugar significa: “Antes de la terminación el ataque trae "
                "desgracia. Es ventajoso atravesar las grandes aguas”.\n"
                "La hora de la travesía ha llegado, pero no se tiene la fuerza de realizar el "
                "pasaje por sí solo; forzarlo llevaría al colapso. Se debe crear una nueva "
                "situación atrayendo energías asistentes capaces para dar el paso decisivo. "
                "Entonces la realización completa será posible."
            ),
            4: (
                "Nueve en el cuarto lugar significa: “La perseverancia trae buena fortuna. "
                "Los remordimientos desaparecen. Conmoción para castigar el país del "
                "diablo. Durante tres años se es premiado con grandes reinos”.\n"
                "Es la época del combate y el pasaje debe ser realizado con una resolución "
                "firme que silencie toda duda. Se trata de una lucha ardiente para "
                "sacudir las fuerzas de la decadencia. Ahora es el momento de poner los "
                "fundamentos del poder y de la soberanía para el futuro."
            ),
            5: (
                "Seis en el quinto lugar significa: “La perseverancia trae buena fortuna. "
                "Sin remordimientos. La luz de un hombre noble es verdadera. Fortuna”.\n"
                "Se gana la victoria y el éxito ha justificado la acción. La luz de una "
                "personalidad superior brilla de nuevo e influye sobre los hombres que se "
                "reúnen a su alrededor. El esplendor de la nueva era aumenta por el "
                "contraste con la miseria de la vieja época, como el sol después de la lluvia."
            ),
            6: (
                "Nueve en la cima significa: “Se bebe vino en plena confianza. Sin "
                "reproches. Pero si uno se hace mojar la cabeza, la perderá en verdad”.\n"
                "En el umbral de los nuevos tiempos, el hombre se reúne en confianza mutua "
                "con los suyos bebiendo felizmente. Pero hay que mantener la justa "
                "medida; si por exceso uno se deja llevar por la ebriedad, pierde por su "
                "desmesura lo que la situación tiene de favorable."
            )
        },
        "lineas": {
            1: "No te apresures por entusiasmo; actuar antes de tiempo solo trae fracaso y humillación.",
            2: "Mantén una espera activa y desarrolla tu fuerza interior sin perder de vista la meta.",
            3: "No fuerces el pasaje solo; busca apoyo y nuevas energías para lograr la realización.",
            4: "Es tiempo de luchar con resolución absoluta para eliminar la decadencia y fundar el futuro.",
            5: "La victoria está asegurada y tu luz personal guiará a otros hacia la nueva era.",
            6: "Disfruta del éxito con mesura; el exceso y la pérdida de control anulan la fortuna lograda."
        }
      }
   }
mapeo_hexagramas = {
        # 1 - 10
        "111111": 1,  "000000": 2,  "010001": 3,  "100010": 4,  "111010": 5, 
        "010111": 6,  "000010": 7,  "010000": 8,  "111011": 9,  "110111": 10,
        # 11 - 20
        "111000": 11, "000111": 12, "111101": 13, "101111": 14, "000100": 15,
        "001000": 16, "011011": 17, "110110": 18, "000011": 19, "110000": 20,
        # 21 - 30
        "101001": 21, "100101": 22, "100000": 23, "000001": 24, "011001": 25,
        "100110": 26, "100001": 27, "011110": 28, "010010": 29, "101101": 30,
        # 31 - 40
        "011100": 31, "001110": 32, "111100": 33, "001111": 34, "000101": 35,
        "101000": 36, "101011": 37, "110101": 38, "001010": 39, "010100": 40,
        # 41 - 50
        "110001": 41, "100011": 42, "111110": 43, "011111": 44, "011000": 45,
        "000110": 46, "010110": 47, "011010": 48, "101110": 49, "011101": 50,
        # 51 - 60
        "100100": 51, "001001": 52, "001011": 53, "110100": 54, "101100": 55,
        "001101": 56, "011011": 57, "110110": 58, "010011": 59, "110010": 60,
        # 61 - 64
        "110011": 61, "001100": 62, "101010": 63, "010101": 64
    }
 
# --- 2. FUNCIONES DEL SISTEMA ---
# --- 2. FUNCIONES DEL SISTEMA (MODIFICADAS PARA SER COMPATIBLES) ---
def tirar_monedas():
    """Tu lógica original de monedas"""
    opciones = [("Cara", 2), ("Cruz", 3)]
    tirada = [random.choice(opciones) for _ in range(3)]
    nombres = [t[0] for t in tirada]
    suma = sum([t[1] for t in tirada])
    return suma, nombres

def obtener_hexagrama(valores):
    """NUEVA: Esta función es el puente para la Web"""
    binario = "".join(["1" if v in [7, 9] else "0" for v in valores[::-1]])
    return mapeo_hexagramas.get(binario, 0)

def calcular_pasado_nuclear(valores):
    """NUEVA: Calcula el pasado para la Web"""
    lineas_nucleares = [valores[1], valores[2], valores[3], valores[2], valores[3], valores[4]]
    bin_pasado = "".join(["1" if v in [7, 9] else "0" for v in lineas_nucleares[::-1]])
    return mapeo_hexagramas.get(bin_pasado, 0)

def mostrar_hexagrama_completo(id_hex, libro, titulo_temporal):
    """Tu lógica original de impresión en terminal"""
    if id_hex in libro:
        h = libro[id_hex]
        print(f"\n" + "="*60)
        print(f" ⏳ {titulo_temporal}: HEXAGRAMA {id_hex} - {h['nombre']}")
        print("="*60)
        
        desc = h.get('descripcion') or h.get('exposicion') or "No disponible"
        print(f"\n[DESCRIPCIÓN DEL HEXAGRAMA]:\n{desc}")
        print(f"\n[EL JUICIO]:\n{h.get('juicio', 'No disponible')}")
        
        if 'notas_juicio' in h:
            print(f"\nNOTAS DEL JUICIO:\n{h.get('notas_juicio')}")
            
        print(f"\n[LA IMAGEN]:\n{h.get('imagen', 'No disponible')}")
def ejecutar_oraculo():
    # 1. Limpiamos la pantalla para que se vea ordenado (opcional)
    import os
    os.system('clear')

    print("\n" + "="*60)
    print("         ☯️  SISTEMA ORACULAR I CHING: SOBERANO ☯️")
    print("="*60)
    print(" 1. CONSULTA GENERAL (Pasado, Presente, Futuro)")
    print(" 2. PREGUNTA ESPECÍFICA (Respuesta Directa)")
    print("-" * 60)
    
    opcion = input(" Seleccione una opción (1 o 2): ")

    if opcion == "2":
        print("\n" + "*"*60)
        print(" MODO: PREGUNTA ESPECÍFICA")
        print(" Concentrate en la pregunta y presiona ENTER...")
        input("*"*60)
    else:
        print("\n" + "*"*60)
        print(" MODO: CONSULTA GENERAL")
        print(" Concentrate en tu intencion y presiona ENTER...")
        input("*"*60)
    valores = []
    regiones = ["TIERRA ", "TIERRA ", "HOMBRES", "HOMBRES", "CIELO  ", "CIELO  "]
    
    # 1. TIRADAS (De abajo hacia arriba según Captura 2026-04-30 22-14-33.jpg)
    for i in range(1, 7):
        suma, monedas = tirar_monedas()
        valores.append(suma)
        
        # Símbolos según el método del libro
        if suma == 7: simbolo = "————— (Joven Yang)"
        elif suma == 8: simbolo = "-- -- (Joven Yin)"
        elif suma == 9: simbolo = "— o — (Viejo Yang)"
        elif suma == 6: simbolo = "-- x -- (Viejo Yin)"
        
        # Mostramos el proceso de suma (Cara=2, Cruz=3)
        print(f"[{regiones[i-1]}] Línea {i}: {' + '.join(monedas)} = {suma}")
        print(f"            Dibujando: {simbolo}")
        time.sleep(0.4)

    # 2. CONSTRUCCIÓN DEL ID BINARIO (Cima a Base)
    # Convertimos 7 y 9 en '1' (Yang), 6 y 8 en '0' (Yin)
        
    # ====================================================== 
    # 🔥 INICIO PRUEBA DE FUEGO 🔥 
    # Descomenta la línea de abajo para forzar un binario específico: 
    # binario = "010101" # Debería dar el 64: WEI CHI
    # binario = "110001"  # Debería dar el 41 (SUN)
    # ======================================================
    id_hex = obtener_hexagrama(valores)
    #id_hex = 42  # LÍNEA TEMPORAL DE PRUEBA  

    if id_hex in LIBRO_ICHING:
        h = LIBRO_ICHING[id_hex]
        print(f"\n" + "*"*50)
        print(f"*** HEXAGRAMA {id_hex}: {h['nombre']} ***")
        print("*"*50 + "\n")
        
        # 3. DIBUJO FINAL (Cima 6 arriba, Base 1 abajo)
        for i in [5, 4, 3, 2, 1, 0]:
            v = valores[i]
            if v == 7: graf = "      —————      "
            elif v == 8: graf = "      -- --      "
            elif v == 9: graf = "      — o —      "
            elif v == 6: graf = "      -- x --      "
            print(f" Línea {i+1}: {graf}")
            
        print(f"\n{'='*60}")
        print(f"       ESTRUCTURA DEL SIGNO: {h['nombre']}")
        print(f"{'='*60}")
        
        print(f"\n[DESCRIPCIÓN DEL HEXAGRAMA]:")
        print(h.get('exposicion', 'Descripción en proceso de carga...'))
        
        print(f"\n[EL JUICIO]:")
        print(h['juicio'])
        
        print(f"\n[LA IMAGEN]:")
        print(h['imagen'])
        
        print(f"\n[LAS LÍNEAS MUTANTES]:")
        hay_mutacion = False
        for i, v in enumerate(valores):
            if v in [6, 9]:
                hay_mutacion = True
                # Intenta buscar el detalle largo; si no existe, usa la línea corta
                detalle = h.get('lineas_detalle', {}).get(i+1, h['lineas'].get(i+1))
                print(f"-> LÍNEA {i+1}: {detalle}")
        
        if not hay_mutacion:
            print("No hay líneas mutantes. El hexagrama es estable.")
        # ======================================================
        # 🟢 ANÁLISIS TEMPORAL COMPLETO: PASADO Y FUTURO
        # ======================================================
        
        # 1. EL PASADO (Nuclear)
        # Usamos la función optimizada que creamos para la web
        id_pasado = calcular_pasado_nuclear(valores)
        mostrar_hexagrama_completo(id_pasado, LIBRO_ICHING, "EL PASADO / LO OCULTO")

        # 2. EL FUTURO (Tendencial)
        if hay_mutacion:
            # Transformamos líneas: 6->7 (viejo yin a joven yang) y 9->8 (viejo yang a joven yin)
            val_futuro = [7 if v == 6 else 8 if v == 9 else v for v in valores]
            id_futuro = obtener_hexagrama(val_futuro)

            mostrar_hexagrama_completo(id_futuro, LIBRO_ICHING, "EL FUTURO / TENDENCIA")
        else:
            print("\n✨ DESTINO ESTABLE: No hay cambios inminentes hacia un nuevo hexagrama.")

        print(f"\n{'='*60}\n")
    else:
        # Mensaje de error seguro (sin llamar a variables inexistentes)
        print(f"\n[!] Error: El hexagrama resultante no se encuentra en el libro.")

# --- 3. INICIO ---
if __name__ == "__main__":
    ejecutar_oraculo()
