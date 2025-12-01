from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    pass

    @staticmethod
    def num_nodes():

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        nodi=[]

        if cnx is None:
            print("No database connected")
            return None

        query= """select *
                from hub """
        cursor.execute(query)

        for row in cursor:
            hub = Hub(
                id=row['id'],
                codice=row['codice'],
                nome=row['nome'],
                citta=row['citta'],
                stato=row['stato'],
                latitudine=row['latitudine'],
                longitudine=row['longitudine'])

            nodi.append(hub.id)

        return nodi

    @staticmethod
    def nome():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        tratte = {}
        query = """select id,nome from hub"""
        cursor.execute(query)
        for row in cursor:
            tratte[row["id"]] = row['nome']

        return tratte



    @staticmethod
    def num_edges():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        nomi = DAO.nome()

        tratte={}
        query= """select *
        from spedizione"""
        cursor.execute(query)
        for row in cursor:
            spedizione = Spedizione(
                id=row['id'],
                id_compagnia=row['id_compagnia'],
                numero_tracking= row['numero_tracking'],
                id_hub_origine= row['id_hub_origine'],
                id_hub_destinazione= row['id_hub_destinazione'],
                data_ritiro_programmata= row['data_ritiro_programmata'],
                distanza= row['distanza'],
                data_consegna= row['data_consegna'],
                valore_merce= row['valore_merce'])

            nome_u = nomi.get(spedizione.id_hub_origine, str(spedizione.id_hub_origine))
            nome_v = nomi.get(spedizione.id_hub_destinazione, str(spedizione.id_hub_destinazione))

            tratta= tuple(sorted((nome_u,nome_v)))

            if tratta not in tratte:
                tratte[tratta] = []

            tratte[tratta].append(spedizione.valore_merce)

        edges={}
        for tratta, valori in tratte.items():
            edges[tratta]= sum(valori)/ len(valori)

        return edges






