import sys
import rpyc

def ClienteSeExime(p1, p2, t1):
    conn = rpyc.connect("servidor", 12345)  # Cambiar "localhost" por la dirección del servidor remoto
    notas_master = conn.root.NotasMaster()

    if notas_master.seExime(p1, p2, t1):
        print("Alumno se exime.")
        nota_presentacion = notas_master.calcularNotaPresentacion(p1, p2, t1)
        print("Nota Final:", round(nota_presentacion, 2))
    else:
        print("Alumno debe dar examen, pues una de sus notas es menor que 4.0.")
        nota_presentacion = notas_master.calcularNotaPresentacion(p1, p2, t1)
        print("Su nota final depende del examen y su nota de presentación es", round(nota_presentacion, 2))

if __name__ == "__main__":
  

    p1 = float(sys.argv[1])
    p2 = float(sys.argv[2])
    t1 = float(sys.argv[3])

    ClienteSeExime(p1, p2, t1)
