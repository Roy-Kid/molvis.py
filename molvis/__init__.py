# author: Roy Kid
# contact: lijichen365@126.com
# date: 2023-01-29
# version: 0.0.1

from typing import Optional
from .molcom import Molcom, MethodsCollection
import numpy as np

class Molvis:

    def __init__(self, host:Optional[str] = None, port:Optional[int] = None):
        self.host = host
        self.port = port
        self.com = Molcom(host, port)
        self.register_methods(Connect())

        self.com.run()

    def __repr__(self):
        return f'<Molvis({self.host}:{self.port})>'

    def clear(self):
        """
        clear the canvas of molvis
        """
        self.com.send('clear')

    def add_molecule(self):
        self.com.send("add_molecule", {
            "coordinates": np.array([
    [4.485786, 6.470829, 0.945954],  
    [4.497160, 5.858652, 1.681713],  
    [3.560061, 6.553797, 0.717081]   
]).tolist(),

'type': ["O", "H", "H"],
        })

    def register_methods(self, methods:MethodsCollection):
        """
        register methods to molvis
        """
        self.com.register_methods(methods)


class Connect(MethodsCollection):

    def on_connect(self, sid, environ):
        print('connect!')
        self.emit('add_molecule',{
            "coordinates": np.array([
    [8.485786, 6.470829, 0.945954],  
    [4.497160, 5.858652, 1.681713],  
    [3.560061, 6.553797, 0.717081]   
]).tolist(),

'type': ["O", "H", "H"],
        })
        print("add_mocl")

    def on_disconnect(self, sid):
        print('disconnect ', sid)

    def get_version(self, sid):
        print('get_+verssion')
        self.emit('get_version', '0.0.1')

    