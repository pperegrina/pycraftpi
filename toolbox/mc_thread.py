#!env python
# -*- coding: utf-8 -*-

from mcpi.minecraft import Minecraft
from threading import Thread
from time import time, sleep

# For coordinates to be correct, you need to run
# setworldspawn 0 0 0 in server console
# or manually set delta values

class MCThread(Thread):

    def __init__(self, server, player):
        self.server = server
        self.player = player
        self.player_id = None
        self.players = {}
        self.mc = Minecraft.create(self.server)
        super().__init__()

    def console(self, text):
        print('>>'+text)
        print('>')

    def update_players(self):
        players = {}
        try:
            for player_id in self.mc.getPlayerEntityIds():
                players[self.mc.entity.getName(player_id)] = player_id  
        except:
            pass
        self.players = players

    def send_message(self, message):
        self.console('Sending '+message)
        self.mc.postToChat('\u00A79\u00A7lShirka\u00A7r '+message)
            
    def check_player_connected(self):
        if self.player in self.players:
            if not self.player_id:
                self.send_message('Hello !')
            self.player_id = self.players[self.player]
        else:
            if self.player_id:
                self.send_message('Bye !')            
            self.player_id = None

    def get_entities(self, distance):
        if self.player_id:
            self.entities = self.mc.entity.getEntities(self.player_id,distance)
        else:
            self.entities = []
        return self.entities

    def get_pos(self):
        if self.player_id:
            self.pos = self.mc.entity.getTilePos(self.player_id)
        else:
            self.pos = None
        return self.pos

    def proximity_alert(self, entity_name, distance):
        entities = self.get_entities(distance)
        if self.player_id:
            for entity in entities:
                if entity[2] == entity_name:
                    mc.postToChat ('\u00A7aCreeper alert !')

    def spawn_block(self):
        if self.player_id:
            pos = self.get_pos()
            self.mc.setBlock(pos.x+1,pos.y,pos.z+1,98)            

    def get_relative_pos(self,x,y,z):
        if self.player_id:
            pos = self.get_pos()
            px = round(pos.x)
            py = round(pos.y)
            pz = round(pos.z)        
            ex = round(x)
            ey = round(y)
            ez = round(z)
            return [ex-px, ey-py, ez-pz]
        return [0,0,0]

    def handle_chat(self):
        posts = self.mc.events.pollChatPosts()
        for post in posts:
            entity_id = post.entityId
            message = post.message
            if entity_id == self.player_id and message.lower().startswith('sk'):
                if 'mypos' in message:
                    pos = self.get_pos()
                    self.send_message('Pos: %d,%d,%d'%(int(pos.x),int(pos.y),int(pos.z)))
                elif 'pos' in message:
                    entities = self.get_entities(20)
                    self.console('--------------------------------------')
                    for entity in entities:
                        ex, ey, ez = round(entity[3:6])
                        rx, ry, rz = self.get_relative_pos(ex, ey, ez)
                        self.console('abs %d %d %d / rel %d %d %d'%(ex, ey, ez, rx, ry, rz))
                    self.console('--------------------------------------')
                    self.send_message('done')
                elif 'block' in message:
                    self.spawn_block()
                    self.send_message('done')
                else:
                    self.send_message('Sorry, I don''t understand "'+message+'"')         


    def run(self):
        while not self.stopped:        
            self.update_players()
            self.check_player_connected()
            self.proximity_alert('CREEPER', 10)
            self.handle_chat()
            sleep(0.5)

