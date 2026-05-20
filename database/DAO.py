from database.DB_connect import DBConnect
from model.genere import Genere
from model.artista import Artista



class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_genre(self):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM genre g "
        cursor.execute(query)

        for row in cursor:
            result.append(Genere(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllartistaPerGenere(self, genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT(a.ArtistId), aa.Name, SUM (i.Quantity) as Popolarita
                FROM track t , album a , artist aa, invoiceline i
                WHERE t.AlbumId = a.AlbumId and t.TrackId= i.TrackId and a.ArtistId = aa.ArtistId and t.GenreId = %s
                group by a.ArtistId ,aa.Name """
        cursor.execute(query)

        for row in cursor:
            result.append(Artista(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCollegamento(self, genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select t1.ArtistID , t2.ArtistId
                    from 
                    (select distinct a.ArtistID , i.CustomerId 
                    from artist a, album al,track t,invoiceline il,invoice i
                    where a.ArtistId=al.ArtistId and al.AlbumId=t.AlbumId and t.TrackId= il.TrackId
                    and i.InvoiceId=il.InvoiceId and t.GenreId = 1
                    )t1 ,
                    (select distinct a.ArtistID, i.CustomerId 
                    from artist a, album al,track t,invoiceline il,invoice i
                    where a.ArtistId=al.ArtistId and al.AlbumId=t.AlbumId and t.TrackId= il.TrackId
                    and i.InvoiceId=il.InvoiceId and t.GenreId = 1
                    )t2
                    where t1.CustomerId=t2.CustomerId and t1.ArtistID < t2.ArtistId
                    """
        cursor.execute(query)

        for row in cursor:
            result.append(Artista(**row))
        cursor.close()
        conn.close()
        return result

