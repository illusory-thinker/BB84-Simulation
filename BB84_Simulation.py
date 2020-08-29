# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:50:31 2020

@author: Quantum Mechanics

Perseverance always pays off
"""

import random as rd


class BB84_Simulation_Terminal:
    def __init__(self,bit_len):
        self.bit_len = bit_len
        self.base_dic = {0:['V','H'],1:['N','P']}
        self.bit_dic = {'H':1,'V':0,'P':1,'N':0}
        self.Alice_1st_sequence = []
        self.Alice_2nd_sequence = []
        self.Alice_polarization = []
        self.Alice_base = []
        self.Bob_polarization = []
        self.Bob_sequence = []
        self.Bob_base = []
        self.Bob_bit = []
        self.Bob_H = [0]*self.bit_len
        self.Bob_V = [0]*self.bit_len
        self.Bob_P = [0]*self.bit_len
        self.Bob_N = [0]*self.bit_len
        self.key_bit = []
        self.keys = []
        
    def rand_bit_generator(self):
        bit_sequence = []
        for i in range(self.bit_len):
            bit_sequence.append(rd.choice([0,1]))
        return bit_sequence
   
    def base_choice(self,bit_lst):
        base_lst = []
        for i in range(len(bit_lst)):
            base_lst.append(self.base_dic[bit_lst[i]])
        return base_lst
    
    def base_comparison(self):
        base_correct = []
        for i in range(self.bit_len):
            if self.Alice_1st_sequence[i] == self.Bob_sequence[i]:
                base_correct.append(1)
            else:
                base_correct.append(0)
        return base_correct
    
    def printkey(self):
        for i in self.keys:
            self.key_bit.append(i[0])
        print(self.key_bit)
    
    def Alice_init(self):
        self.Alice_1st_sequence = self.rand_bit_generator()
        self.Alice_base = self.base_choice(self.Alice_1st_sequence)
        self.Alice_2nd_sequence = self.rand_bit_generator()

        for i in range(self.bit_len):
            self.Alice_polarization.append(self.base_dic[self.Alice_1st_sequence[i]][self.Alice_2nd_sequence[i]])
    
    def standard_simulation(self):
        self.Alice_init()

        for i in range(self.bit_len):
            self.Bob_sequence.append(rd.choice([0,1]))
            if self.Alice_polarization[i] in self.base_dic[self.Bob_sequence[i]]:
                if self.Alice_polarization[i] == 'H':
                    self.Bob_H[i] = 1
                if self.Alice_polarization[i] == 'V':
                    self.Bob_V[i] = 1
                if self.Alice_polarization[i] == 'P':
                    self.Bob_P[i] = 1
                if self.Alice_polarization[i] == 'N':
                    self.Bob_N[i] = 1
            else:
                Wrong_base=self.base_dic[self.Bob_sequence[i]]
                Wrong_polariztion=rd.choice(Wrong_base)
                if Wrong_polariztion == 'H':
                    self.Bob_H[i] = 1
                if Wrong_polariztion == 'V':
                    self.Bob_v[i] = 1
                if Wrong_polariztion == 'p':
                    self.Bob_p[i] = 1
                if Wrong_polariztion == 'N':
                    self.Bob_N[i] = 1                    

        self.Bob_base=self.base_choice(self.Bob_sequence)

        for i in range(self.bit_len):
            if self.Bob_H[i] == 1:
                self.Bob_polarization.append('H')            
            if self.Bob_V[i] == 1:
                self.Bob_polarization.append('V')
            if self.Bob_P[i] == 1:
                self.Bob_polarization.append('P')
            if self.Bob_N[i] == 1:
                self.Bob_polarization.append('N')

        for i in range(self.bit_len):    
            self.Bob_bit.append(self.bit_dic[self.Bob_polarization[i]])
        

        base_correct=self.base_comparison()
        for i in range(self.bit_len):
            if base_correct[i] == 1:
                self.keys.append([self.Bob_bit[i],i])
        #print(self.keys)
        #self.printkey()

        