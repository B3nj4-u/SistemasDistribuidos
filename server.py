import rpyc

class NotasMaster(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_calcularNotaPresentacion(self, p1, p2, t1):
        nota_presentacion = (p1 + p2) * 0.3 + t1 * 0.4
        return nota_presentacion

    def exposed_seExime(self, p1, p2, t1):
        return p1 >= 4.0 and p2 >= 4.0 and t1 >= 4.0

    def exposed_calcularNotaFinal(self, np, ne):
        nota_final = np * 0.7 + ne * 0.3
        return nota_final

    def exposed_calcularNotaCurso(self, p1, p2, t1, ne):
        nota_presentacion = self.exposed_calcularNotaPresentacion(p1, p2, t1)
        nota_final = self.exposed_calcularNotaFinal(nota_presentacion, ne)
        return nota_final

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(NotasMaster, port=12345)
    t.start()
