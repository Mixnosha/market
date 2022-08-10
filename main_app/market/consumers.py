import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from market.models import Profile, Favorites, Product


class FavoriteAddConsumer(WebsocketConsumer):
    def connect(self):
        print('Вошел!')
        self.accept()

    def disconnect(self, close_code):
        print('Вышел')

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        id = text_data_json['product_id']
        user = text_data_json['user']
        try:
            user = Profile.objects.get(user__username=user)
            fav = Favorites.objects.get(user=user)
            fav.products.add(Product.objects.get(id=id))
            self.send(text_data="true   ")
        except Exception as e:
            print(e)
            self.send(text_data="false")

