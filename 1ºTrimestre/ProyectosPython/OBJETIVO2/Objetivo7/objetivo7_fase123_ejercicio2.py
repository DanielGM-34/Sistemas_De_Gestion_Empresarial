# Daniel García Méndez 2ºDAM

class Video():
    def __init__(self, titulo, duracion, categoria):
        self.t = titulo
        self.dura = duracion
        self.cat = categoria


# Da información sobre el vídeo.
    def mirarVideo(self):
        print("Iniciando el vídeo...")
        print("El vídeo que estás viendo se titula", self.t, "de la categoría", self.cat, "con una duración de", self.dura, "minutos.")

# Imprime un mensaje de detención.
    def detener_video(self):
        print("Deteniendo la reproducción del video.")

class Audio():
    def __init__(self, titulo, nombre_artista):
        self.tit = titulo
        self.nomb = nombre_artista


# Da información sobre el audio.
    def escuchar_audio(self):
        print("El audio que estás escuchando es", self.tit, "producido por el artista", self.nomb)


# Imprime un mensaje de detención de audio.
    def detener_audio(self):
        print("Deteniendo la reproducción del audio.")

class Media(Video, Audio):
    def __init__(self, titulo, duracion, categoria, nombre_artista):
        Video.__init__(self, titulo, duracion, categoria)
        Audio.__init__(self, titulo, nombre_artista)
        self.tituM = titulo
        self.catE = categoria
        self.durA = duracion
        self.nomArt = nombre_artista

# Pruebas
medio_1 = Media("Título 1", 180, "Infantil", "Artista 1")
medio_1.escuchar_audio()
medio_1.mirarVideo()
medio_1.detener_audio()
medio_1.detener_video()
