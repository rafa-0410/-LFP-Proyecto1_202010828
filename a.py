# x= "/afaf"
# p =x.replace('/',"")


# if x.replace('/',"")=='afaf':
#     print('entro')
#     print(p)



print(11*2)


                        
 #si hay numeros o cadenas de texto solo los guardo y les agrego a que tipo de operacion pertenecen (SUMA,RESTA ETC)
 #Si hay otra funcion  de operacion, vuelvo a llamar a la funcion para que aga lo mismo
    def operaciones1(self,posicion_inicial,posicion_final,tipo_accion):
        print(tipo_accion)

        if tipo_accion == 'Tipo':
            fin_raiz = False
            posicion_final_bucle = 0
            for i in range(posicion_inicial,posicion_final):

                if self.listaTokens[i].lexema=='<' and self.listaTokens[i+1].tipo=='Etiqueta Apertura' and self.listaTokens[i+1].lexema=='Numero' and self.listaTokens[i+2].lexema=='>': #para numeros
                    apertura = self.listaTokens[i+1].lexema
                    print(self.listaTokens[i+1].lexema)
                    for e in range(i,posicion_final):                        
                        if self.listaTokens[e].lexema=='<'and self.listaTokens[e+1].tipo=='Etiqueta Cierre' and self.listaTokens[e+2].lexema=='>': 
                            if (self.listaTokens[e+1].lexema).replace('/','')==apertura:
                                #por si no viene nada entre las etiquetas de apertura y cierre
                                fin_raiz = True  
                                posicion_final_bucle = e+3 
                                break

                if posicion_final_bucle == (posicion_final-1):
                    break
                elif fin_raiz:
                    self.operaciones(posicion_final_bucle,posicion_final,tipo_accion)
                    break


                # elif self.listaTokens[i].lexema=='<' and self.listaTokens[i+1].tipo!='Etiqueta Apertura' and self.listaTokens[i+2].lexema=='Operacion': #para numeros
                #     apertura = self.listaTokens[i+1].lexema
                #     print(self.listaTokens[i+1].lexema)
                #     for e in range(i,len(posicion_final)):                        
                #         if self.listaTokens[e].lexema=='<'and self.listaTokens[e+1].tipo=='Etiqueta Cierre' and self.listaTokens[e+2].lexema!='>': 
                #             pass

        else:
            for i in range(posicion_inicial,posicion_final):
                if self.listaTokens[i].tipo=='Dato/Cadena' or self.listaTokens[i].tipo=='Coma' and self.listaTokens[i].lexema!='/': #para un texto
                    print(self.listaTokens[i].lexema)
