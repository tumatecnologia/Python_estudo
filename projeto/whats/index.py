import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
import sqlite3
import urllib.parse
from kivy.clock import Clock

# Configurar tamanho da janela menor
Window.size = (400, 600)

class ModernButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = '14sp'
        self.bold = False
        
        with self.canvas.before:
            Color(0.2, 0.6, 0.9, 1)  # Azul moderno
            self.rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[10]
            )
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class RemoveButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = '12sp'
        self.size_hint_x = None
        self.width = 80
        
        with self.canvas.before:
            Color(0.9, 0.3, 0.3, 1)  # Vermelho
            self.rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[8]
            )
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class WhatsAppSender(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [15, 10, 15, 10]
        self.spacing = 10
        
        self.create_database()
        self.build_ui()
    
    def create_database(self):
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT UNIQUE,
                name TEXT
            )
        ''')
        conn.commit()
        conn.close()
    
    def build_ui(self):
        # Título moderno
        title = Label(
            text='[b]WhatsApp Sender[/b]',
            font_size='20sp',
            size_hint_y=None,
            height=40,
            markup=True,
            color=(0.2, 0.2, 0.2, 1)
        )
        self.add_widget(title)
        
        # Card para adicionar contatos
        add_card = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=100,
            padding=[10, 5, 10, 5],
            spacing=5
        )
        
        # Adicionar fundo ao card
        with add_card.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            RoundedRectangle(
                size=add_card.size,
                pos=add_card.pos,
                radius=[12]
            )
        
        add_card.add_widget(Label(
            text='[b]Novo Contato[/b]',
            size_hint_y=None,
            height=25,
            font_size='14sp',
            markup=True,
            color=(0.3, 0.3, 0.3, 1)
        ))
        
        phone_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)
        self.phone_input = TextInput(
            hint_text='Número com DDD...',
            multiline=False,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            padding=[10, 8],
            size_hint_x=0.7
        )
        
        self.add_phone_button = ModernButton(
            text='ADD',
            size_hint_x=0.3
        )
        self.add_phone_button.bind(on_press=self.add_contact)
        
        phone_layout.add_widget(self.phone_input)
        phone_layout.add_widget(self.add_phone_button)
        add_card.add_widget(phone_layout)
        
        self.add_widget(add_card)
        
        # Card de contatos
        contacts_card = BoxLayout(
            orientation='vertical',
            size_hint_y=0.4,
            padding=[10, 5, 10, 5],
            spacing=5
        )
        
        with contacts_card.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            RoundedRectangle(
                size=contacts_card.size,
                pos=contacts_card.pos,
                radius=[12]
            )
        
        contacts_card.add_widget(Label(
            text='[b]Contatos[/b]',
            size_hint_y=None,
            height=25,
            font_size='14sp',
            markup=True,
            color=(0.3, 0.3, 0.3, 1)
        ))
        
        # Lista de contatos
        self.contacts_scroll = ScrollView(
            bar_width=8,
            bar_color=(0.6, 0.6, 0.6, 0.8)
        )
        self.contacts_layout = GridLayout(
            cols=1,
            spacing=5,
            size_hint_y=None,
            padding=[0, 5, 0, 5]
        )
        self.contacts_layout.bind(minimum_height=self.contacts_layout.setter('height'))
        self.contacts_scroll.add_widget(self.contacts_layout)
        contacts_card.add_widget(self.contacts_scroll)
        
        self.add_widget(contacts_card)
        
        # Card da mensagem
        message_card = BoxLayout(
            orientation='vertical',
            size_hint_y=0.35,
            padding=[10, 5, 10, 5],
            spacing=5
        )
        
        with message_card.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            RoundedRectangle(
                size=message_card.size,
                pos=message_card.pos,
                radius=[12]
            )
        
        message_card.add_widget(Label(
            text='[b]Mensagem[/b]',
            size_hint_y=None,
            height=25,
            font_size='14sp',
            markup=True,
            color=(0.3, 0.3, 0.3, 1)
        ))
        
        self.message_input = TextInput(
            hint_text='Digite sua mensagem aqui...',
            size_hint_y=1,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            padding=[10, 8],
            multiline=True
        )
        message_card.add_widget(self.message_input)
        
        self.add_widget(message_card)
        
        # Botão principal
        self.send_button = ModernButton(
            text='[b]ENVIAR PARA TODOS[/b]',
            size_hint_y=None,
            height=50,
            font_size='16sp',
            background_color=(0.2, 0.8, 0.4, 1)
        )
        self.send_button.bind(on_press=self.send_to_all_contacts)
        self.add_widget(self.send_button)
        
        # Carregar contatos existentes
        self.load_contacts()
    
    def add_contact(self, instance):
        phone = self.phone_input.text.strip()
        
        if phone:
            try:
                # Remove caracteres não numéricos
                phone = ''.join(filter(str.isdigit, phone))
                
                if len(phone) < 10:
                    self.show_message("Número muito curto!")
                    return
                
                conn = sqlite3.connect('contacts.db')
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT OR IGNORE INTO contacts (phone_number) VALUES (?)',
                    (phone,)
                )
                conn.commit()
                conn.close()
                
                self.phone_input.text = ''
                self.load_contacts()
                self.show_message("✓ Contato adicionado")
                
            except Exception as e:
                self.show_message(f"Erro: {str(e)}")
        else:
            self.show_message("Digite um número!")
    
    def remove_contact(self, instance):
        phone = instance.phone_number
        
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contacts WHERE phone_number = ?', (phone,))
        conn.commit()
        conn.close()
        
        self.load_contacts()
        self.show_message("✓ Contato removido")
    
    def load_contacts(self):
        # Limpa a lista de contatos atual
        self.contacts_layout.clear_widgets()
        self.contacts_layout.height = 0
        
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('SELECT phone_number FROM contacts ORDER BY phone_number')
        contacts = cursor.fetchall()
        conn.close()
        
        for phone, in contacts:
            contact_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=35,
                spacing=10,
                padding=[5, 0]
            )
            
            # Fundo do item de contato
            with contact_item.canvas.before:
                Color(1, 1, 1, 1)
                RoundedRectangle(
                    size=contact_item.size,
                    pos=contact_item.pos,
                    radius=[8]
                )
            
            contact_label = Label(
                text=phone,
                size_hint_x=0.7,
                color=(0.2, 0.2, 0.2, 1)
            )
            
            remove_button = RemoveButton(text='Remover')
            remove_button.phone_number = phone
            remove_button.bind(on_press=self.remove_contact)
            
            contact_item.add_widget(contact_label)
            contact_item.add_widget(remove_button)
            self.contacts_layout.add_widget(contact_item)
            
            # Atualiza a altura do layout
            self.contacts_layout.height += contact_item.height + self.contacts_layout.spacing[1]
    
    def send_to_all_contacts(self, instance):
        message = self.message_input.text.strip()
        
        if not message:
            self.show_message("Digite uma mensagem!")
            return
        
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('SELECT phone_number FROM contacts')
        contacts = cursor.fetchall()
        conn.close()
        
        if not contacts:
            self.show_message("Nenhum contato!")
            return
        
        # Animação do botão
        self.send_button.disabled = True
        self.send_button.text = '[b]ENVIANDO...[/b]'
        self.send_button.canvas.before.clear()
        with self.send_button.canvas.before:
            Color(0.5, 0.5, 0.5, 1)
            RoundedRectangle(
                size=self.send_button.size,
                pos=self.send_button.pos,
                radius=[10]
            )
        
        self.show_message(f"📤 Enviando para {len(contacts)} contatos...")
        
        # Simula o envio
        for phone, in contacts:
            self.send_whatsapp_message(phone, message)
        
        # Restaura o botão após 2 segundos
        Clock.schedule_once(self.enable_send_button, 2)
    
    def send_whatsapp_message(self, phone, message):
        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{phone}?text={encoded_message}"
        print(f"📱 Enviando para {phone}")
        # Para usar realmente: import webbrowser + webbrowser.open(whatsapp_url)
    
    def enable_send_button(self, dt):
        self.send_button.disabled = False
        self.send_button.text = '[b]ENVIAR PARA TODOS[/b]'
        self.send_button.canvas.before.clear()
        with self.send_button.canvas.before:
            Color(0.2, 0.8, 0.4, 1)
            RoundedRectangle(
                size=self.send_button.size,
                pos=self.send_button.pos,
                radius=[10]
            )
        self.show_message("✓ Mensagens enviadas!")
    
    def show_message(self, message):
        print(f"💬 {message}")

class WhatsAppApp(App):
    def build(self):
        # Cor de fundo da aplicação
        Window.clearcolor = (0.92, 0.94, 0.96, 1)
        return WhatsAppSender()

if __name__ == '__main__':
    WhatsAppApp().run()