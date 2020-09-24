####################################################################
# Alejandro Tejada 17584
####################################################################
# Curso: Redes
# Programa: sleekBot.py
# Propósito: Programa de pruebas
# Fecha: 09/2020
####################################################################
import sys
import logging
import getpass
import xmpp
import time
import threading
import binascii
import sleekxmpp
from optparse import OptionParser
from sleekxmpp.util.misc_ops import setdefaultencoding
from sleekxmpp.exceptions import IqError, IqTimeout
from sleekxmpp.xmlstream.stanzabase import ElementBase
import xml.etree.ElementTree as ET

# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    from sleekxmpp.util.misc_ops import setdefaultencoding
    setdefaultencoding('utf8')
else:
    raw_input = input


class ClientXMPP(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password):
        #ClientXMPP.__init__(self, jid, password)
        super(ClientXMPP, self).__init__(jid, password)

        self.auto_authorize = True
        self.auto_subscribe = True
        self.contact_dict = {}
        self.user_dict = {}
        self.username = jid
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.received_message)
        self.add_event_handler("changed_subscription", self.getRosterForUser)
        self.add_event_handler("changed_status", self.wait_for_presences)

        self.received = set()
        self.contacts = []
        self.presences_received = threading.Event()

        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0199')  # XMPP Ping
        self.register_plugin('xep_0004')  # Data forms
        self.register_plugin('xep_0077')  # In-band Registration
        self.register_plugin('xep_0045')  # Mulit-User Chat (MUC)
        self.register_plugin('xep_0096')  # Jabber Search
        self.register_plugin('xep_0065')
        self.register_plugin('xep_0066')
        self.register_plugin('xep_0050')
        self.register_plugin('xep_0047')
        self.register_plugin('xep_0231')
        self.add_event_handler("unregistered_user", self.unreg)
        self.add_event_handler("registered_user", self.reg)
        #!we try to connect
        if self.connect():
            print("You have succesfully Loged In")
            self.process(block=False)
        else:
            print("We could not connect to redes2020.xyz")

    def start(self, event):
        # we send a notification
        self.send_presence(pshow='chat',
                           pstatus='Available')
        # We get the roster
        roster = self.get_roster()
        for rosterItem in roster['roster']['items'].keys():
            # we add the team members
            self.contacts.append(rosterItem)
        for ID in self.contacts:
            # send a notificaton to all
            self.sendNotification(ID,
                                  'Hi fellow!!!!!!!!!!! I am ready for chat Dude',
                                  'active')

    def received_message(self, msg):
        sender = str(msg['from'])
        jid = sender.split('/')[0]
        username = jid.split('@')[0]
        if msg['type'] in ('chat', 'normal', 'groupchat'):
            print("\n")
            print(f'You have a new Message/RoomMessage from: {jid}')
            print("Message:  " + msg['body'])
            print("")
            #msg.reply("Thanks for sending\n%(body)s" % msg).send()

    def sendMessage(self, destiny, messageToSend):
        # We send a notification for writing to the other person
        self.sendNotification(
            destiny, 'Someone is writing for you fellow...', 'composing')
        # we set a time out
        time.sleep(5)
        self.send_message(
            mto=destiny,
            mbody=messageToSend,
            mtype="chat",
            mfrom=self.boundjid.bare)

        print("Message sended!!!")

    def unreg(self, iq):
        msg = "Bye! %s" % iq['register']['username']
        self.send_message(mto=iq['from'],
                          mbody=msg,
                          mtype="chat",
                          mfrom=self.fulljid)

    def reg(self, iq):
        msg = "Welcome! %s" % iq['register']['username']
        self.send_message(mto=iq['from'],
                          mbody=msg,
                          mtype="chat",
                          mfrom=self.fulljid)

    def addJIDToRoster(self, contactToAdd):
        try:
            # We send a notification for writing to the other person
            self.send_message(
                mto=contactToAdd,
                mbody="I Just added you to my roster",
                mtype="chat",
                mfrom=self.boundjid.bare)
            self.send_presence_subscription(pto=contactToAdd)
            return True
        except IqError:
            raise Exception("Unable to add user to rooster")
            sys.exit(1)
        except IqTimeout:
            raise Exception("Server not responding")

    def disconnectFromServer(self):
        self.disconnect(wait=False)

    def getRosterForUser(self):
        self.get_roster()

    # Extracted from : https://github.com/fritzy/SleekXMPP/blob/develop/sleekxmpp/clientxmpp.py

    def wait_for_presences(self, pres):
        "#! we expect some entries"
        self.received.add(pres['from'].bare)
        # if we get some presences not equals, its better other way
        if len(self.received) >= len(self.client_roster.keys()):
            self.presences_received.set()
        else:
            self.presences_received.clear()

    def Joinchatroom(self, room, nickname):
        try:
            # we try to connect
            self.plugin['xep_0045'].joinMUC(room, nickname)
            print("You have succesfully connected to: " +
                  room + "with NickName: "+nickname)
            message = self.Message()

            itemStanza = ET.fromstring(
                "<active xmlns='http://jabber.org/protocol/chatstates'/>")

            # Send a notification
            message.append(itemStanza)
            message['to'] = room
            message['type'] = 'groupchat'
            jid = str(self.boundjid.full).split('/')[0]
            username = jid.split('@')[0]
            message['body'] = username + " has just entered the room!!!!"
            message.send(now=True)
        except IqError as e:
            raise Exception("The room could not been created/entered", e)
        except IqTimeout:
            raise Exception("Server redes2020.xyz not RESPONDING")

    def createNewChatRoom(self, room, nickname):
        try:
            # we create a satus
            status = "Joining the room..."
            self.plugin['xep_0045'].joinMUC(
                room,
                nickname,
                pstatus=status,
                pfrom=self.boundjid.full,
                wait=True)

            # we create the affiliiation
            self.plugin['xep_0045'].setAffiliation(
                room,
                self.boundjid.full,
                affiliation="owner"
            )

            # publicate chat room
            self.plugin['xep_0045'].configureRoom(
                room,
                ifrom=self.boundjid.full
            )
            print("You have succesfully connected to: " +
                  room + "with NickName: "+nickname)
        except IqError as e:
            raise Exception("The room could not been created/entered", e)
        except IqTimeout:
            raise Exception("Server redes2020.xyz not RESPONDING")

    def sendMessageToRoom(self, room, body):
        self.send_message(mto=room,
                          mbody=body,
                          mtype='groupchat')

    def deleteUserFromServer(self, userToDelete):
        StanzaForDelete = self.Iq()
        StanzaForDelete['type'] = 'set'
        StanzaForDelete['from'] = self.fulljid
        StanzaForDelete['register']['remove'] = True
        try:
            StanzaForDelete.send(now=True)
            print("Account deleted succesfuly")
        except IqError as e:
            raise Exception("We could not Delete the account", e)
            sys.exit(1)
        except IqTimeout:
            raise Exception("Server redes2020.xyz not responding")

    def listALLServerUsers(self):
        users = self.Iq()
        users['type'] = 'set'
        users['to'] = 'search.redes2020.xyz'
        users['from'] = self.boundjid.bare
        users['id'] = 'search_result'
        itemStanza = ET.fromstring("<query xmlns='jabber:iq:search'>\
                                 <x xmlns='jabber:x:data' type='submit'>\
                                    <field type='hidden' var='FORM_TYPE'>\
                                        <value>jabber:iq:search</value>\
                                    </field>\
                                    <field var='Username'>\
                                        <value>1</value>\
                                    </field>\
                                    <field var='search'>\
                                        <value>*</value>\
                                    </field>\
                                    <field var='Name'>\
                                        <value>1</value>\
                                    </field>\
                                    <field var='Email'>\
                                        <value>1</value>\
                                    </field>\
                                </x>\
                                </query>")
        users.append(itemStanza)
        try:
            response = users.send()
            tree = ET.fromstring(str(response))
            root = tree.getroot()

            for child in root:
                print(child.tag, child.attrib)
        except IqError as e:
            raise Exception("Unable list users", e)
            sys.exit(1)
        except IqTimeout:
            raise Exception("Server not responding")

    def sendNotification(self, receiver, MessageBody, ntype):
        message = self.Message()
        if (ntype == 'active'):
            itemStanza = ET.fromstring(
                "<active xmlns='http://jabber.org/protocol/chatstates'/>")
        elif (ntype == 'composing'):
            itemStanza = ET.fromstring(
                "<composing xmlns='http://jabber.org/protocol/chatstates'/>")
        elif (ntype == 'inactive'):
            itemStanza = ET.fromstring(
                "<inactive xmlns='http://jabber.org/protocol/chatstates'/>")

        # Send a notification
        message.append(itemStanza)
        message['to'] = receiver
        message['type'] = 'chat'
        message['body'] = MessageBody
        try:
            message.send(now=True)
        except IqError as e:
            raise Exception("Notification not sended", e)
            sys.exit(1)
        except IqTimeout:
            raise Exception("Server redes2020.xyz not responding")

    # extracted from: https://github.com/fritzy/SleekXMPP/blob/develop/examples/roster_browser.py
    def getInformationFromUsersAtRoster(self):
        try:
            self.get_roster()
        except IqError as err:
            print('Error: %s' % err.iq['error']['condition'])
        except IqTimeout:
            print('Error: Request timed out')
        self.send_presence()
        groups = self.client_roster.groups()
        print
        for group in groups:
            print('\n%s' % group)
            print('-' * 72)
            for JID in groups[group]:
                subscription = self.client_roster[JID]['subscription']
                name = self.client_roster[JID]['name']
                if self.client_roster[JID]['name']:
                    print(' %s (%s) [%s]' % (name, JID, subscription))
                else:
                    print('Nombre:  %s y con tipo de suscripción: %s' %
                          (JID, subscription))

                connections = self.client_roster.presence(JID)
                for res, pres in connections.items():
                    show = 'available'
                    if pres['show']:
                        show = pres['show']
                    print('At server   - %s with type: (%s)' % (res, show))
                    if pres['status']:
                        print('Status:       %s' % pres['status'])
        print("")
        print('-' * 72)


''' if __name__ == '__main__':
    xmpp = ClientXMPP(opts.jid, opts.password)
    xmpp.register_plugin('xep_0030')  # Service Discovery
    xmpp.register_plugin('xep_0004')  # Data Forms
    xmpp.register_plugin('xep_0060')  # PubSub
    xmpp.register_plugin('xep_0199')  # XMPP Ping

    if xmpp.connect():
        xmpp.process(block=False)
        print("Done")
    else:
        print("Unable to connect.")
 '''


#! Registro
def registerNewUser(user, passw):
    usuario = user
    password = passw
    jid = xmpp.JID(usuario)
    cli = xmpp.Client(jid.getDomain(), debug=[])
    cli.connect()

    if xmpp.features.register(cli, jid.getDomain(), {'username': jid.getNode(), 'password': password}):
        return True
    else:
        return False
