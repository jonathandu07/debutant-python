# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 13:05:15 2026

@author: alpha
"""

mot = input("Entrez un mot : \n")

lettre_a_verifier =  "a"

if lettre_a_verifier in mot:
    print(f"La lettre '{lettre_a_verifier}' est présente dans le '{mot}'.")
else:
    print(f"La lettre '{lettre_a_verifier}' n'est pas présente dans le '{mot}'.")