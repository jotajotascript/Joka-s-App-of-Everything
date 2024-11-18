from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.spinner import Spinner
from kivymd.uix.label import MDLabel
from kivy.uix.behaviors import ButtonBehavior
import random

class ManipulaJanela:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def ajustar_tamanho_janela(self):
        Window.size = (self.altura, self.largura)

class DadosClicaveis(ButtonBehavior,Image):
  def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.keep_ratio = True
        self.allow_stretch = False
        self.size_hint = (None, None)  
        self.size = kwargs.get('size', (80, 80))  

class BotaoPersonalizado(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self.size = (dp(45), dp(45))  
        self.pos = (dp(10), dp(10))  

        
        self.image = Image(source='backarrow.png', size=self.size)
        self.add_widget(self.image)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.on_press()
            return True
        return super().on_touch_down(touch)

    def on_press(self):
        app = MDApp.get_running_app()
        app.root.current = "Menu"

class JokasAppOfEverything(MDApp):
    def build(self):
        manipulador = ManipulaJanela(600, 600)
        manipulador.ajustar_tamanho_janela()

        sm = ScreenManager()
        tela_menu = Screen(name="Menu")

        root = AnchorLayout(anchor_y='center')

        layout = FloatLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        background = Image(source="mapa.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        box_layout = MDBoxLayout(
            orientation="vertical", 
            padding=20, 
            spacing=20, 
            size_hint=(0.8,None),
            height=dp(200), 
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )


        logo = Image(
            source="logo_dado_texto.png",  
            size_hint=(1, None),
            height=dp(200)
        )
        box_layout.add_widget(logo)

        botao_atributo = MDRaisedButton(
            text='Calcula Atributos',
            size_hint=(None, None),
            size=(dp(200), dp(50)),
            pos_hint={'center_x':0.5,'center_y':0.5},
            on_release=self.muda_tela,
            md_bg_color=[0, 0, 0, 1]
        )
        box_layout.add_widget(botao_atributo)
        

        botao_dados = MDRaisedButton(
            text='Lança Dados',
            size_hint=(None, None),
            size=(dp(200), dp(50)),
            pos_hint={'center_x':0.5,'y':0.5},
            on_release=self.muda_tela,
            md_bg_color=[0, 0, 0, 1]
        )
        box_layout.add_widget(botao_dados)
        

        botao_secreto = MDRaisedButton(
            text='Progresso XP',
            size_hint=(None, None),
            size=(dp(200), dp(50)),
            pos_hint={'center_x':0.5,'y':0.5},
            on_release=self.muda_tela,
            md_bg_color=[0, 0, 0, 1]
        )
        box_layout.add_widget(botao_secreto)
        
        root.add_widget(box_layout)
        layout.add_widget(root)
        tela_menu.add_widget(layout)
        sm.add_widget(tela_menu)

        sm.add_widget(TelaCalculaStats(name='Calcula Atributos'))
        sm.add_widget(TelaRolaDados(name='Lança Dados'))
        sm.add_widget(TelaCalculaXP(name='Progresso XP'))
       
        
        

        return sm

    def muda_tela(self, instance):
        self.root.current = instance.text

class TelaCalculaStats(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

        box_layout = MDBoxLayout(orientation='vertical',padding=20,spacing=20,pos_hint={'center_x': 0.5})

        layout = FloatLayout(pos_hint={'center_x':0.5,'center_y':0.5})
        background = Image(source='statsbg.png',allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        
        self.races = ['Humano', 'Anão da Colina', 'Anão da Montanha', 'Elfo Alto', 'Elfo da Floresta', 'Elfo Drow', 'Halfling Pés-leves', 'Halfling Robusto', 'Draconato', 'Gnomo da Floresta', 'Gnomo das Rochas', 'Meio Elfo', 'Meio Orc', 'Tiefling']
        self.classes = ['Bárbaro', 'Bardo', 'Clérigo', 'Druida', 'Guerreiro', 'Monge', 'Paladino', 'Patrulheiro', 'Ladino', 'Feiticeiro', 'Bruxo', 'Mago']

        self.race_dropdown = Spinner(text='Selecione a raça', values=self.races, size_hint=(0.3, None), height=44, pos_hint={'center_x': 0.5,'center_y':0.95})
        self.class_dropdown = Spinner(text='Selecione a classe', values=self.classes, size_hint=(0.3, None), height=44, pos_hint ={'center_x': 0.5,'center_y':0.9})

        layout.add_widget(self.race_dropdown)
        layout.add_widget(self.class_dropdown)

        def create_input_row(label_text, hint_text):
            row = MDBoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=100, padding = 10)
            label = MDLabel(text=label_text, halign="center", size_hint_y=None, height=20)
            horizontal_layout = MDBoxLayout(orientation='horizontal', spacing=10)
            text_field = MDTextField(hint_text=hint_text,input_filter="float", size_hint_x=0.5)
            mod_label = MDLabel(text="0", halign="center", size_hint=(None, None), width=50, height=50,theme_text_color="Custom",text_color=(1,1,1,1), bold=True)
            horizontal_layout.add_widget(text_field)
            horizontal_layout.add_widget(mod_label)
            row.add_widget(label)
            row.add_widget(horizontal_layout)
            return row, text_field, mod_label

        self.rows = []
        self.forca_row, self.forca, self.mod_forca = create_input_row("Força", "Digite o valor de FOR.")
        self.destreza_row, self.destreza, self.mod_destreza = create_input_row("Destreza", "Digite o valor para DES")
        self.constituicao_row, self.constituicao, self.mod_constituicao = create_input_row("Constituição", "Digite o valor de CONST.")
        self.inteligencia_row, self.inteligencia, self.mod_inteligencia = create_input_row("Inteligência", "Digite o valor para INT")
        self.sabedoria_row, self.sabedoria, self.mod_sabedoria = create_input_row("Sabedoria", "Digite o valor de SAB.")
        self.carisma_row, self.carisma, self.mod_carisma = create_input_row("Carisma", "Digite o valor para CARS")

        self.rows.extend([self.forca_row, self.destreza_row, self.constituicao_row, self.inteligencia_row, self.sabedoria_row, self.carisma_row])
        
        for row in self.rows:
            box_layout.add_widget(row)

        self.botao_calcular = MDRaisedButton(text="Calcular")
        self.botao_calcular.pos_hint = {'center_x': 0.5}
        self.botao_calcular.bind(on_release=self.calcular_resultado)
        box_layout.add_widget(self.botao_calcular)
        layout.add_widget(BotaoPersonalizado())
        layout.add_widget(box_layout)
        self.add_widget(layout)

    def calcular_resultado(self, instance):
        modificadores_raca = {
            'humano': [1, 1, 1, 1, 1, 1],
            'Anão da Colina': [0, 0, 2, 0, 1, 0],
            'Anão da Montanha': [2, 0, 2, 0, 0, 0],
            'Elfo Alto': [0, 2, 0, 1, 0, 0],
            'Elfo da Floresta': [0, 2, 0, 0, 1, 0],
            'Elfo Drow': [0, 2, 0, 0, 0, 1],
            'Halfling Pés-leves': [0, 2, 0, 0, 0, 1],
            'Halfling Robusto': [0, 2, 2, 0, 0, 0],
            'Draconato': [2, 0, 0, 0, 0, 1],
            'Gnomo da Floresta': [0, 1, 0, 2, 0, 0],
            'Gnomo da Rochas': [0, 0, 1, 0, 2, 0],
            'Meio Elfo': [0, 1, 1, 0, 0, 2],
            'Meio Orc': [2, 0, 1, 0, 0, 0],
            'Tiefling': [0, 0, 0, 1, 0, 2]
        }

        modificadores_classe = {
            'Bárbaro': [2, 0, 2, 0, 0, 0],
            'Bardo': [0, 0, 0, 0, 0, 2],
            'Clérigo': [0, 0, 0, 0, 2, 0],
            'Druida': [0, 0, 0, 0, 2, 0],
            'Guerreiro': [2, 0, 2, 0, 0, 0],
            'Monge': [0, 2, 0, 0, 2, 0],
            'Paladino': [2, 0, 0, 0, 0, 2],
            'Patrulheiro': [0, 2, 0, 0, 2, 0],
            'Ladino': [0, 2, 0, 0, 0, 0],
            'Feiticeiro': [0, 0, 0, 0, 0, 2],
            'Bruxo': [0, 0, 0, 0, 0, 2],
            'Mago': [0, 0, 0, 1, 0, 0]
        }

        atributos = [self.forca, self.destreza, self.constituicao, self.inteligencia, self.sabedoria, self.carisma]
        mods = [self.mod_forca, self.mod_destreza, self.mod_constituicao, self.mod_inteligencia, self.mod_sabedoria, self.mod_carisma]

        raca = self.race_dropdown.text
        classe = self.class_dropdown.text

        mod_raca = modificadores_raca.get(raca, [0, 0, 0, 0, 0, 0])
        mod_classe = modificadores_classe.get(classe, [0, 0, 0, 0, 0, 0])

        valores = [int(attr.text) if attr.text != '' else 0 for attr in atributos]
        valores_modificados = [v + r + c for v, r, c in zip(valores, mod_raca, mod_classe)]

        calculos = [(valor - 10) // 2 for valor in valores_modificados]

        for attr, mod, calc, val_mod in zip(atributos, mods, calculos, valores_modificados):
            attr.text = str(val_mod)
            attr.halign = 'left'
            mod.text = str(calc)
            attr.hint_text = 'Valor final do atributo:'
            

        
        self.botao_calcular.text = "Reiniciar"
        self.botao_calcular.unbind(on_release=self.calcular_resultado)
        self.botao_calcular.bind(on_release=self.zerar_atributos)

    def zerar_atributos(self, instance):
        atributos = [self.forca, self.destreza, self.constituicao, self.inteligencia, self.sabedoria, self.carisma]
        mods = [self.mod_forca, self.mod_destreza, self.mod_constituicao, self.mod_inteligencia, self.mod_sabedoria, self.mod_carisma]

        for attr, mod in zip(atributos, mods):
            attr.text = ''
            attr.halign = "left"
            mod.text = '0'

        self.forca.hint_text = "Digite o valor de FOR."
        self.destreza.hint_text = "Digite o valor para DES"
        self.constituicao.hint_text = "Digite o valor de CONST."
        self.inteligencia.hint_text = "Digite o valor para INT"
        self.sabedoria.hint_text = "Digite o valor de SAB."
        self.carisma.hint_text = "Digite o valor para CARS"
        self.race_dropdown.text = 'Selecione a raça'
        self.class_dropdown.text = 'Selecione a classe'

        self.botao_calcular.text = "Calcular"
        self.botao_calcular.unbind(on_release=self.zerar_atributos)
        self.botao_calcular.bind(on_release=self.calcular_resultado)

class TelaRolaDados(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

        self.total_rolagem = 0
        self.labels_resultado=[]

        box_layout = MDBoxLayout(orientation='vertical',padding=10,spacing=5,pos_hint={'center_x':0.5,'center_y':0.5})

        layout = FloatLayout(pos_hint={'center_x':0.5,'center_y':0.5})
        background = Image(source='diceroll.png',allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)


        horizontal_layout = MDBoxLayout(orientation='horizontal', spacing=3)

        ranges = [0,4,6,8,10,12,20]

        self.labelExplica = MDLabel(text='Total da rolagem: 0', pos_hint={'center_y':0.4}, halign='center')
        botaoReinicia = MDRaisedButton(text='Reiniciar', pos_hint={'center_x':0.5,'center_y':0.3})
        botaoReinicia.bind(on_release=self.reiniciar_rolagem)

        for i in range(1,7):
            linhaDadoValor = MDBoxLayout(orientation='horizontal', spacing=10)

            imagem_dado=DadosClicaveis(source=f'dado{i}.png',pos_hint={'center_x':0.5,'center_y':0.5})
            
            labelResultado = MDLabel(text="0", halign='center')
            
            self.labels_resultado.append(labelResultado)

            imagem_dado.bind(on_press=lambda instance, i=ranges[i], label=labelResultado: self.on_dice_image_click(i, label))
            linhaDadoValor.add_widget(imagem_dado)

            linhaDadoValor.add_widget(labelResultado)

            horizontal_layout.add_widget(linhaDadoValor)
           

        box_layout.add_widget(horizontal_layout)
        layout.add_widget(self.labelExplica)
        layout.add_widget(botaoReinicia)
        box_layout.add_widget(BotaoPersonalizado())
        layout.add_widget(box_layout)
        self.add_widget(layout)

    
    def on_dice_image_click(self,i,label): 
        valor = random.randint(1, i) 
        label.text = f'{valor}'
        self.total_rolagem += valor
        self.labelExplica.text=f'Total da rolagem: {self.total_rolagem}'

    def reiniciar_rolagem(self,instance):
        self.total_rolagem = 0
        self.labelExplica.text = 'Total da rolagem: 0'

        for label in self.labels_resultado:
            label.text = '0'

class TelaCalculaXP(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)


        self.xp_inicio = 0
        self.total_xp = 0
        self.nivel_xp = [300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000]

        box_layout = MDBoxLayout(orientation='vertical',padding=20,spacing=20)

        layout = FloatLayout(pos_hint={'center_x':0.5,'center_y':0.5})
        background = Image(source='colunas3.png',allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        self.xp_inicial = MDTextField(hint_text='XP inicial do Personagem', input_filter='int', size_hint_x=None, width=300,pos_hint={'center_x':0.5})
        self.xp_encontro = MDTextField(hint_text="XP do Encontro", input_filter='int', size_hint_x=None, width=300,pos_hint={'center_x':0.5}) 
        self.num_personagens = MDTextField(hint_text="Número de Personagens", input_filter='int', size_hint_x=None, width=300,pos_hint={'center_x': 0.5}) 
        self.resultado_xp = MDLabel(text="XP por Personagem: ",halign="center") 
        self.progresso_nivel = MDLabel(text="Progresso de Nível: ",halign="center")
        

        adiciona_xp_inicial = MDRaisedButton(text='Adiconar XP Inicial', on_release=self.entra_xp_inicial, pos_hint={'center_x': 0.5})
        adicionar_encontro_button = MDRaisedButton(text="Adicionar Encontro", on_release=self.adicionar_encontro,pos_hint={'center_x':0.5}) 
        distribuir_xp_button = MDRaisedButton(text="Distribuir XP", on_release=self.distribuir_xp,pos_hint={'center_x': 0.5})
        self.botao_reiniciar =MDRaisedButton(text='Reiniciar', on_release=self.reinicia_campos,pos_hint={'center_x':0.5})

        box_layout.add_widget(self.xp_inicial)
        box_layout.add_widget(adiciona_xp_inicial)
        box_layout.add_widget(self.xp_encontro)
        box_layout.add_widget(adicionar_encontro_button)
        box_layout.add_widget(self.num_personagens)
        box_layout.add_widget(distribuir_xp_button)
        box_layout.add_widget(self.resultado_xp)
        box_layout.add_widget(self.progresso_nivel)
        box_layout.add_widget(self.botao_reiniciar)
        
        box_layout.add_widget(BotaoPersonalizado())
        layout.add_widget(box_layout)
        self.add_widget(layout)

    def entra_xp_inicial(self,instance):
        varIntermediaria = int(self.xp_inicial.text)
        if varIntermediaria > 0:
            self.xp_inicio = int(self.xp_inicial.text)

    def adicionar_encontro(self, instance):
        try:
            xp_encontro = int(self.xp_encontro.text)
            self.total_xp += xp_encontro
            self.xp_encontro.text = ""
            self.resultado_xp.text = f"Total de XP: {self.total_xp}"
        except ValueError:
            self.resultado_xp.text = "Por favor, insira um valor válido."

    def distribuir_xp(self, instance):
        try:
            num_personagens = int(self.num_personagens.text)
            if num_personagens > 0:
                xp_por_personagem = self.total_xp / num_personagens
                self.resultado_xp.text = f"XP por Personagem: {xp_por_personagem:.2f}"
                xp_por_personagem += self.xp_inicio
                self.calcular_progresso_nivel(xp_por_personagem)
            else:
                self.resultado_xp.text = "Número de personagens deve ser maior que 0."
        except ValueError:
            self.resultado_xp.text = "Por favor, insira um valor válido."

    def calcular_progresso_nivel(self, xp_por_personagem):
        for i, xp in enumerate(self.nivel_xp):
            if xp_por_personagem < xp:
                self.progresso_nivel.text = f"Próximo Nível: {i + 1} ({xp_por_personagem}/{xp} XP)"
                break
    
    def reinicia_campos(self,instance):
        self.xp_inicio = 0
        self.total_xp = 0
        self.xp_inicial.text = ""
        self.xp_encontro.text =""
        self.num_personagens.text = ""
        self.resultado_xp.text = "XP por Personagem:"
        self.progresso_nivel.text = "Progresso de Nível:"


JokasAppOfEverything().run()
