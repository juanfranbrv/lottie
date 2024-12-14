# Prueba de Animaciones Lottie con Streamlit

Este proyecto es una aplicación interactiva desarrollada en **Streamlit** que utiliza animaciones Lottie para enriquecer la experiencia del usuario. Incluye un ejemplo práctico de cómo cargar y mostrar animaciones, así como la integración de un spinner para procesos en curso.

## Características

- **Interfaz intuitiva**: diseño en columnas para mostrar dos animaciones simultáneamente.
- **Animaciones Lottie**: integración mediante la librería `streamlit_lottie`.
- **Spinner animado**: representación visual de procesos en curso con feedback al usuario.

https://lottie2.streamlit.app/

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes paquetes:

- `streamlit`
- `streamlit_lottie`

Puedes instalarlos ejecutando:

```bash
pip install streamlit streamlit-lottie
```

## Archivos

- `app.py`: código fuente de la aplicación.
- `Animation - 1734201788003.json`: archivo JSON de la animación Lottie para la columna izquierda.
- `Animation - 1734202264690.json`: archivo JSON de la animación Lottie para la columna derecha y el spinner.

## Cómo ejecutar

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/prueba-lottie-streamlit.git
   cd prueba-lottie-streamlit
   ```

2. Asegúrate de tener instalados todos los requisitos mencionados anteriormente.

3. Ejecuta la aplicación con el siguiente comando:

   ```bash
   streamlit run app.py
   ```

4. Abre tu navegador en `http://localhost:8501` para interactuar con la aplicación.

## Funcionamiento

### Diseño de la interfaz
La aplicación utiliza dos columnas:

- **Columna izquierda**: muestra una animación Lottie.
- **Columna derecha**: contiene un spinner animado que se muestra durante 5 segundos para simular un proceso en curso. Una vez completado, muestra un mensaje de éxito.

### Función para cargar animaciones
Las animaciones Lottie se cargan desde archivos JSON mediante la función `load_lottiefile`, que utiliza el módulo `json` para leer los datos.

### Uso de `streamlit_lottie`
La librería `streamlit_lottie` permite integrar animaciones Lottie en aplicaciones de Streamlit de manera sencilla. La función `st_lottie` se utiliza para mostrar las animaciones, mientras que `st_lottie_spinner` añade soporte para animaciones durante la ejecución de tareas.

## Personalización

Puedes personalizar este proyecto:

- Cambiando los archivos JSON para utilizar tus propias animaciones.
- Ajustando las configuraciones de velocidad, altura o bucle en las animaciones.

## Recursos

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [LottieFiles](https://lottiefiles.com/): colección gratuita de animaciones Lottie.
- [streamlit-lottie](https://github.com/andfanilo/streamlit-lottie): librería utilizada en este proyecto.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por utilizar esta aplicación! 🎉

