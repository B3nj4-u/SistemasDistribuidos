import sys
import rpyc

def ClienteParaExamen(p1, p2, t1, ne):
    conn = rpyc.connect("servidor", 12345)  # Cambiar "localhost" por la dirección del servidor remoto
    notas_master = conn.root.NotasMaster()

    nota_final = notas_master.calcularNotaCurso(p1, p2, t1, ne)
    if nota_final >= 3.95:
        print("Alumno aprueba con una nota final de", round(nota_final, 2))
    else:
        print("Lamentablemente, alumno reprueba con una nota final de", round(nota_final, 2))

if __name__ == "__main__":
    

    p1 = float(sys.argv[1])
    p2 = float(sys.argv[2])
    t1 = float(sys.argv[3])
    ne = float(sys.argv[4])

    ClienteParaExamen(p1, p2, t1, ne)
