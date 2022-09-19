from prettytable import PrettyTable
from Token import Token

class Analizador:

    def __init__(self,ruta:str) -> None:
        self.ruta = ruta

        self.listaElementos=[]
        self.listaTokens=[]
        self.listaErrores=[]

        self.palabras_reservadas_etiquetas_apertura=['Tipo','Operacion','Numero','Texto','Funcion','Titulo','Descripcion','Contenido','Estilo']
        self.palabras_reservadas_etiquetas_cierre = ['/Tipo','/Operacion','/Numero','/Texto','/Funcion','/Titulo','/Descripcion','/Contenido','/Estilo']
        self.palabras_reservadas_operaciones=['SUMA','RESTA','MULTIPLICACION','DIVISION','POTENCIA','RAIZ','INVERSO','SENO','COSENO','TANGENTE','MOD','TEXTO','TIPO','Color','Tamanio']
        self.palabras_reservadas_colores=['AZUL','VERDE','GRIS']

        self.linea=1
        self.columna=0

        self.bufer = '' #es el caracter que agarro y concateno para la palabra, etc

        self.estado=0
        self.contador=0

        self.etiquetas_arriba = 0
        self.etiquetas_cierre =0
        self.cadena_con_la_operacion = []

    

    def E_q0(self,caracter:str): #en este estado veo que viene para armar el patron 
        if caracter =='/':
            self.estado=1
            self.bufer+=caracter
            self.columna+=1
        elif caracter.isalpha():
            self.estado=1
            self.bufer+=caracter
            self.columna+=1
        elif caracter.isdigit():
            self.estado=1
            self.bufer+=caracter
            self.columna+=1
        elif caracter=='<':
            # print("entro")
            self.estado=2
            self.bufer+=caracter
            self.columna+=1
        elif caracter=='>':
            self.estado=3
            self.bufer+=caracter
            self.columna+=1
        elif caracter=='=':
            self.estado=4
            self.bufer+=caracter
            self.columna+=1
        elif caracter=='[':
            self.estado=5
            self.bufer+=caracter
            self.columna+=1
        elif caracter==']':
            self.estado=6
            self.bufer+=caracter
            self.columna+=1
        elif caracter=='\n': #salto de linea
            self.linea+=1
            self.columna=0
        elif caracter in ['\t',' ']: #\t significa TABULACION que es un gran espacio en blanco, lo tomo como un espacio por eso si viene una tabulacion agrego 1 a al columna
            self.columna+=1
        elif caracter=='#':
            print("Termino")
            self.imprimirTokens()
            self.Definicion_Elementos(0)
        # else:
        #     self.A_Error(caracter,self.linea,self.columna)
        #     self.columna+=1

    def E_q1(self,caracter:str):
        if caracter.isalpha() or caracter.isdigit() or caracter == " " or caracter == '.' or caracter == ',':

            if caracter== ' ':
                if self.bufer in self.palabras_reservadas_etiquetas_apertura:
                    self.A_Token(self.bufer,self.linea,self.columna,'Etiqueta Apertura')
                elif self.bufer in self.palabras_reservadas_etiquetas_cierre:
                    self.A_Token(self.bufer,self.linea,self.columna,'Etiqueta Cierre')
                elif self.bufer in self.palabras_reservadas_operaciones:
                    self.A_Token(self.bufer,self.linea,self.columna,'Operacion')
                elif self.bufer in self.palabras_reservadas_colores:
                    self.A_Token(self.bufer,self.linea,self.columna,'Color')
                else:
                    self.estado=1
                    self.columna+=1
                    self.bufer+=caracter                    
            else:
                self.estado=1
                self.columna+=1
                self.bufer+=caracter
        # palabras reservadas 
        else:
            if self.bufer in self.palabras_reservadas_etiquetas_apertura:
                self.A_Token(self.bufer,self.linea,self.columna,'Etiqueta Apertura')
            elif self.bufer in self.palabras_reservadas_etiquetas_cierre:
                self.A_Token(self.bufer,self.linea,self.columna,'Etiqueta Cierre')
            elif self.bufer in self.palabras_reservadas_operaciones:
                self.A_Token(self.bufer,self.linea,self.columna,'Operacion')
            elif self.bufer in self.palabras_reservadas_colores:
                self.A_Token(self.bufer,self.linea,self.columna,'Color')
            else:
                self.A_Token(self.bufer,self.linea,self.columna,'Dato/Cadena')
            self.estado=0
            self.contador-=1

    def E_q2(self,caracter):
        self.A_Token(self.bufer,self.linea,self.columna,'Simbolo menor')
        self.estado=0
        self.contador-=1 # regreso uno porque puede que el caracter que no cumpla con el patron se de otro y como en el form aumento, aca le regreso para que lo analice

    
    def E_q3(self,caracter):
        self.A_Token(self.bufer,self.linea,self.columna,'Simbolo mayor')
        self.estado=0
        self.contador-=1
    
    def E_q4(self,caracter):
        self.A_Token(self.bufer,self.linea,self.columna,'Simbolo igual')
        self.estado=0
        self.contador-=1
    
    def E_q5(self,caracter):
        self.A_Token(self.bufer,self.linea,self.columna,'Corchete izquierdo')
        self.estado=0
        self.contador-=1
    
    def E_q6(self,caracter):
        self.A_Token(self.bufer,self.linea,self.columna,'Corchete derecho')
        self.estado=0
        self.contador-=1


    def A_Token(self,lexema:str,linea:int,columna:int,tipo:str):
        self.listaTokens.append(Token(lexema,linea,columna,tipo))
        self.bufer=''

    def imprimirTokens(self):
        x = PrettyTable()
        x.field_names=['Lexema','Linea','Columna','Tipo','Numero']
        cont=0
        for token in self.listaTokens:
            x.add_row([token.lexema,token.linea,token.columna,token.tipo,cont])
            cont +=1
        print(x)    

    def analizar(self,cadena:str):
        cadena = cadena + '#'
        self.listaTokens=[]
        # self.listaErrores=[]
        self.contador = 0
        while self.contador < len(cadena):            
            if self.estado == 0:
                self.E_q0(cadena[self.contador])
            elif self.estado == 1:
                self.E_q1(cadena[self.contador])
            elif self.estado == 2:
                self.E_q2(cadena[self.contador])
            elif self.estado == 3:
                self.E_q3(cadena[self.contador])
            elif self.estado == 4:
                self.E_q4(cadena[self.contador])
            elif self.estado == 5:
                self.E_q5(cadena[self.contador])
            elif self.estado == 6:
                self.E_q6(cadena[self.contador])
            self.contador+=1


    def Definicion_Elementos(self,posicion):#<Tipo> </Tipo> funcion recursiva, etiquetas simples
        # self.listaElementos=[]
        fin_raiz = False
        posicion_final = 0
        for i in range(posicion,len(self.listaTokens)):

            # Elemento={}
            if self.listaTokens[i].lexema=='<' and self.listaTokens[i+1].tipo=='Etiqueta Apertura' and self.listaTokens[i+2].lexema=='>':
                apertura = self.listaTokens[i+1].lexema # aca veo que etique empieza y por ende que va a taener adentro. (etiqueta de apertura)
                print(self.listaTokens[i].lexema + self.listaTokens[i+1].lexema + self.listaTokens[i+2].lexema)
                for e in range(i,len(self.listaTokens)):

                    if self.listaTokens[e].lexema=='<'and self.listaTokens[e+1].tipo=='Etiqueta Cierre': #(etiqueta de cierre)
                        if (self.listaTokens[e+1].lexema).replace('/','')==apertura:

                            # veo los elementos que hay dentro de la etiqueta
                            #i+2 es la etiqueta de > empiezo con otra cosa despues del >, por eso i+3
                            #e es < de la etiquet de cierre en el for no llego a esa posicion, llego a la anterior
                            if self.listaTokens[i+1].lexema == 'Tipo':
                                self.operaciones((i+3),e)
                  
                            print(self.listaTokens[e].lexema + self.listaTokens[e+1].lexema + self.listaTokens[e+2].lexema)
                            fin_raiz = True  
                            posicion_final = e+2                        
                            break
          
            if posicion_final == (len(self.listaTokens)-1):
                break
            elif fin_raiz:
                self.Definicion_Elementos(posicion_final)
                break




    def operaciones(self,posicion_inicial,posicion_final):       

        fin_raiz_accion = False
        posicion_final_bucle = 0
        for i in range(posicion_inicial,posicion_final):

            if self.listaTokens[i].lexema=='<' and self.listaTokens[i+1].tipo=='Etiqueta Apertura' and self.listaTokens[i+1].lexema=='Numero' and self.listaTokens[i+2].lexema=='>': #para numeros
                apertura = self.listaTokens[i+1].lexema
                # print(self.listaTokens[i].lexema + self.listaTokens[i+1].lexema + (self.listaTokens[i+2].lexema))
                for e in range(i,posicion_final):                        
                    if self.listaTokens[e].lexema=='<'and self.listaTokens[e+1].tipo=='Etiqueta Cierre' and self.listaTokens[e+2].lexema=='>': 
                        if (self.listaTokens[e+1].lexema).replace('/','')==apertura:

                            #por si no viene nada entre las etiquetas de apertura y cierre
                            # print(self.listaTokens[e-1].lexema) #valor

                            # print(self.listaTokens[e].lexema + self.listaTokens[e+1].lexema + self.listaTokens[e+2].lexema)

                            
                            self.cadena_con_la_operacion.append(self.listaTokens[e-1].lexema)

                            fin_raiz_accion = True  
                            posicion_final_bucle = e+2 
                            break
                    
            elif  self.listaTokens[i].lexema=='<' and self.listaTokens[i+1].tipo=='Etiqueta Apertura' and self.listaTokens[i+1].lexema=='Operacion': 
                apertura = self.listaTokens[i+1].lexema
                # print(" --------" + self.listaTokens[i+3].lexema +" --------")

                self.etiquetas_arriba +=1
                self.etiquetas_cierre +=1
                self.cadena_con_la_operacion.append(self.listaTokens[i+3].lexema)

                fin_raiz_accion = True  
                posicion_final_bucle = i+4                


            elif self.listaTokens[i].lexema=='<'and self.listaTokens[i+1].tipo=='Etiqueta Cierre' and self.listaTokens[i+2].lexema=='>': 
                        if (self.listaTokens[i+1].lexema).replace('/','')=='Operacion':
                            # print('Fin Operacion')
                            # print(self.listaTokens[i].lexema + self.listaTokens[i+1].lexema + self.listaTokens[i+2].lexema)
                            self.etiquetas_cierre +=1

                            if (self.etiquetas_cierre%2)==0 and self.etiquetas_cierre==(self.etiquetas_arriba*2):
                                self.etiquetas_cierre=0
                                self.etiquetas_arriba=0
                                print(self.cadena_con_la_operacion)
                                self.cadena_con_la_operacion = []
                                # print('--------Final Operacion--------')
                            else:
                                pass
                                # print('--------Cierre Operacion--------')
                            fin_raiz_accion = True  
                            posicion_final_bucle = i+2 

                            # break

            if posicion_final_bucle == (posicion_final-1):
                break
            elif fin_raiz_accion:
                self.operaciones(posicion_final_bucle,posicion_final)
                break

        

