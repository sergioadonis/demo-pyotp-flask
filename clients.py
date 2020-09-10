from dataclasses import dataclass


@dataclass
class Client:
    id: int
    name: str
    phone: str
    secret: str


class ClientRepository:
    clients = []
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    @classmethod
    def get_clients(cls):
        return cls.clients

    @classmethod
    def get_client_index(cls, id):
        for i in range(len(cls.clients)):
            obj = cls.clients[i]
            if (obj.id == id):
                return i
        return -1

    @classmethod
    def get_client_by_id(cls, id):
        i = cls.get_client_index(id)
        if (i >= 0):
            return cls.clients[i]
        return None

    @classmethod
    def save_client(cls, client):
        i = cls.get_client_index(client.id)
        if (i >= 0):
            cls.clients[i] = client
        else:
            cls.clients.append(client)
