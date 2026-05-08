import streamlit as st
import time
if "consulta_hecha" not in st.session_state:
    st.session_state.consulta_hecha = False
def renderizar_dibujo_hexagrama(lista_valores, data_hex):
    html_lineas = ""
    for i, v in enumerate(lista_valores):
        num_linea = i + 1
        marca_html = ""
        if v == 9: 
            marca_html = f'<div class="mutant-mark">○ <span style="font-size: 0.8em; margin-left: 5px;">(9)</span></div>'
        elif v == 6: 
            marca_html = f'<div class="mutant-mark">✘ <span style="font-size: 0.8em; margin-left: 5px;">(6)</span></div>'
        
        if v in [7, 9]: cuerpo = '<div class="yang-line"></div>'
        else: cuerpo = '<div class="yin-half"></div><div class="yin-gap"></div><div class="yin-half"></div>'
        
        html_lineas += f'<div class="line-container"><div class="line-label">{num_linea}.</div>{cuerpo}{marca_html}</div>'

    html_final = f'''
        <div class="master-container">
            <div class="hexagram-col">{html_lineas}</div>
            <div class="structure-col">
                <div class="trigrama-card"><span class="trigrama-label">Superior</span><strong>{data_hex.get('trigrama_sup')}</strong></div>
                <div class="trigrama-card"><span class="trigrama-label">Inferior</span><strong>{data_hex.get('trigrama_inf')}</strong></div>
            </div>
        </div>
    '''
    # ¡IMPORTANTE! Sin la palabra 'return'
    st.markdown(html_final, unsafe_allow_html=True)

from oraculo_pro import LIBRO_ICHING, tirar_monedas, obtener_hexagrama, calcular_pasado_nuclear

# 1. CONFIGURACIÓN Y CSS (Diseño "Soberano" corregido)
st.set_page_config(page_title="I Ching Soberano", page_icon="☯️", layout="wide")

#2. AQUÍ ES EL MEJOR LUGAR PARA LA BARRA LATERAL
with st.sidebar:
    st.header("🙏 Apoya el Proyecto")
    st.info("Si este oráculo te ha servido, tu pequeña donación ayuda a la soberania.")
    
   # st.markdown("### 🇦🇷 Argentina")
   # st.link_button("☕ Invítame un Cafecito", "https://cafecito.app/tu-usuario", use_container_width=True)
   # st.link_button("💳 Mercado Pago", "https://link.mercadopago.com.ar/tu-perfil", use_container_width=True)
    
    st.divider() 
    
    st.subheader("🪙 Donar en USDT")
    st.caption("Dirección de la billetera:")
    st.code("0x19ac0fcf272a25ef3193db44189774187fb880ff", language="text")
    st.warning("⚠️ Red: BSC BNB smart chain (Bep20) únicamente")
    
    st.divider()
    st.caption("Hecho con ❤️ para la comunidad.")

st.markdown("""
    <style>
    /* Contenedor que agrupa el dibujo y el texto */
    .master-container {
        display: flex;
        align-items: flex-end; /* Cambiamos de center a flex-end para nivelar las bases */
        gap: 50px;
        margin: 20px 0;
        padding-bottom: 10px; /* Espacio extra abajo */
    }
    
    /* Columna del Hexagrama */
    .hexagram-col {
        display: flex;
        flex-direction: column-reverse;
        gap: 18px; /* Antes 14px - Más espacio entre líneas */
    }
    
    .line-container {
        display: flex;
        align-items: center;
        height: 18px; /* Antes 14px - Ajustado al nuevo grosor de 16px */
    }
    
    .line-label {
        width: 25px;
        font-size: 14px;
        color: #888;
        margin-right: 15px;
        text-align: right;
    }
    
    .yang-line { 
        width: 250px; /* Antes 160px */
        height: 16px; /* Antes 12px - Le da más cuerpo */
        background-color: #1a1a1a; 
    }
    
    .yin-half { 
        width: 110px; /* Antes 70px */
        height: 16px; /* Antes 12px */
        background-color: #1a1a1a; 
    }
    
    .yin-gap { 
        width: 30px; /* Antes 20px */
        height: 16px; /* Antes 12px */
        background-color: transparent; 
    }
    .mutant-mark {
        margin-left: 20px;
        font-size: 20px;
        color: #3498db;
        display: flex;
        align-items: center;
        gap: 5px;
        min-width: 60px;
    }

    /* Columna de Texto (Estructura) */
    .structure-col {
        display: flex;
        flex-direction: column;
        /* Ajuste de precisión: 25px suele ser el equivalente a una línea de texto 
           más el espacio entre líneas del hexagrama */
        margin-top: 25px; 
    }
    
    .structure-title {
        font-size: 1.3em;
        font-weight: bold;
        color: #2c3e50;
        margin: 0 0 10px 0; /* Solo 10px abajo para mantener el grupo unido */
        line-height: 1.2;
    }
    
    .trigrama-card {
        background: #f8f9fa;
        padding: 15px 20px;
        border-radius: 6px;
        border-left: 5px solid #2c3e50;
        margin-bottom: 10px;
        width: 320px; /* Ancho fijo para prolijidad */
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .trigrama-label {
        font-size: 11px;
        color: #95a5a6;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: block;
        margin-bottom: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☯️ Oráculo I Ching Soberano")

modo = st.radio("Seleccione el tipo de consulta:", ["1. CONSULTA GENERAL", "2. PREGUNTA ESPECÍFICA"], horizontal=True)
if modo == "2. PREGUNTA ESPECÍFICA":
    st.text_input("Escribe tu pregunta específica aquí:")

if st.button("✨ Consultar al Oráculo", use_container_width=True):
    with st.status("🛠️ Consultando...", expanded=False) as status:
        # Guardamos TODO en session_state para que no se pierda
        st.session_state.tiradas = [tirar_monedas()[0] for _ in range(6)]
        st.session_state.num_presente = obtener_hexagrama(st.session_state.tiradas)
        
        tirada_f = [(7 if v == 6 else (8 if v == 9 else v)) for v in st.session_state.tiradas]
        st.session_state.num_futuro = obtener_hexagrama(tirada_f)
        st.session_state.tirada_futura = tirada_f
        
        time.sleep(0.5)
        st.session_state.consulta_hecha = True # Marcamos que ya hay una consulta activa
        status.update(label="¡Tirada completa!", state="complete")

# --- MOSTRAR RESULTADOS (Si existe una consulta en memoria) ---
if st.session_state.get("consulta_hecha"):
        data_p = LIBRO_ICHING.get(st.session_state.num_presente)
        
        st.divider()
        
        # Bloque de Donación
        with st.container(border=True):
            st.markdown("### 🙏 Intercambio y Soberanía")
            st.write("Si esta consulta te brinda claridad, te invitamos a realizar una donación mínima en USDT.")
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.code("0x19ac0fcf272a25ef3193db44189774187fb880ff", language="text")
            with col2:
                st.warning("Red BSC (Bep20)")
            
            confirmacion = st.checkbox("He leído sobre la importancia del intercambio y deseo ver mi consulta.")

        # --- NIVEL 1: Si el usuario confirmó la donación ---
        if confirmacion:
            st.balloons()
            tab_pres, tab_fut, tab_pas = st.tabs(["✨ PRESENTE", "🔮 FUTURO", "⌛ PASADO"])

            # Pestaña PRESENTE
            with tab_pres:
                st.markdown(f"## {st.session_state.num_presente}. {data_p.get('nombre')}")
                renderizar_dibujo_hexagrama(st.session_state.tiradas, data_p)
                
                sub_tabs = st.tabs(["📜 Descripción", "⚖️ El Juicio", "🖼️ La Imagen", "🔥 Líneas"])
                with sub_tabs[0]: st.write(data_p.get('exposicion') or data_p.get('descripcion'))
                with sub_tabs[1]: st.info(data_p.get('juicio'))
                with sub_tabs[2]: st.write(data_p.get('imagen'))
                with sub_tabs[3]:
                    mutantes = [i + 1 for i, v in enumerate(st.session_state.tiradas) if v in [6, 9]]
                    if mutantes:
                        for n in mutantes:
                            sentencia = data_p.get('lineas', {}).get(n) or data_p.get('lineas', {}).get(str(n))
                            detalle = data_p.get('lineas_detalle', {}).get(n) or data_p.get('lineas_detalle', {}).get(str(n))
                            with st.container(border=True):
                                st.markdown(f"**Línea {n}**")
                                if sentencia: st.markdown(f"*{sentencia}*")
                                if detalle: st.write(detalle)
                    else:
                        st.write("No hay líneas en movimiento.")

            # Pestaña FUTURO
            with tab_fut:
                if st.session_state.num_futuro != st.session_state.num_presente:
                    data_f = LIBRO_ICHING.get(st.session_state.num_futuro)
                    st.markdown(f"## {st.session_state.num_futuro}. {data_f.get('nombre')}")
                    renderizar_dibujo_hexagrama(st.session_state.tirada_futura, data_f)
                    
                    f_tabs = st.tabs(["📜 Descripción", "⚖️ El Juicio", "🖼️ La Imagen"])
                    with f_tabs[0]: st.write(data_f.get('exposicion') or data_f.get('descripcion'))
                    with f_tabs[1]: st.info(data_f.get('juicio'))
                    with f_tabs[2]: st.write(data_f.get('imagen'))
                else:
                    st.info("La situación es estable. No hay cambio proyectado.")

            # Pestaña PASADO
            with tab_pas:
                num_pasado = calcular_pasado_nuclear(st.session_state.tiradas)
                data_pasado = LIBRO_ICHING.get(num_pasado)
                if data_pasado:
                    st.markdown(f"## {num_pasado}. {data_pasado.get('nombre')}")
                    
                    lineas_n = [
                        (7 if st.session_state.tiradas[1] in [7, 9] else 8),
                        (7 if st.session_state.tiradas[2] in [7, 9] else 8),
                        (7 if st.session_state.tiradas[3] in [7, 9] else 8),
                        (7 if st.session_state.tiradas[2] in [7, 9] else 8),
                        (7 if st.session_state.tiradas[3] in [7, 9] else 8),
                        (7 if st.session_state.tiradas[4] in [7, 9] else 8)
                    ]
                    renderizar_dibujo_hexagrama(lineas_n, data_pasado)
                    
                    p_tabs = st.tabs(["📜 Descripción", "⚖️ El Juicio", "🖼️ La Imagen"])
                    with p_tabs[0]: st.write(data_pasado.get('exposicion') or data_pasado.get('descripcion'))
                    with p_tabs[1]: st.info(data_pasado.get('juicio'))
                    with p_tabs[2]: st.write(data_pasado.get('imagen'))

        # --- ESTE ES EL ELSE QUE DABA ERROR ---
        else:
            st.warning("Por favor, confirma que has leído el mensaje superior para ver los resultados.")
