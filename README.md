# P3
 Video Streaming

##EX1

En el primer ejercicio he guardado todos los archivos generados con HLS en la carpeta HLS_ex1

Referencia: http://underpop.online.fr/f/ffmpeg/help/hls-2.htm.gz


##EX2

He guardado todos los archivos generados en la carpeta bento4_ex2
Referencia: https://ottverse.com/bento4-mp4dash-for-mpeg-dash-packaging/


##EX3

En este ejercicio he creado una comanda con ffmpeg para retransmitir en directo el video BBB de 10 segundos.
Para retransmitir en directo me he creado un canal de Youtube con el correo de la UPF, pero necesitaba la confirmación para retransmitir, que tarda 24 horas.
Así que no he podido probarlo. La key '1jgb-37u3-5wsa-0908-1d13' la he inventado como ejemplo. La key me saldría cuando configurara el stream en youtube.

Referencia: https://gist.github.com/abhinanddhandapani/36292399cc9d9ef47b291269edadbbed


##EX4

He buscado qué protocolo se usa principalmente para streaming en Youtube. 
He encontrado la web (developers.google.com/youtube/v3/live/guides/hls-ingestion), donde explican que la difusión de contenidos en directo de YouTube es a través de HLS. 

Indican que los video codecs válidos son H.264 and HEVC, se permiten frame rates de más de 60 fps, 
y el codec de audio soportado es AAC con un solo track de audio, entre otras especificaciones.

A parte de especificar las características del protocolo, también se explica su funcionamiento, por ejemplo explican como se genera la URL con HLS.


