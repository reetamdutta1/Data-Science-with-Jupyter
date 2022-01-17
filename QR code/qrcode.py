# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:40:04 2020

@author: REETAM
"""
#if you are using Anaconda, then you have to pip install two python libraries -> pyqrcode and pypng

import pyqrcode
x="https://www.youtube.com/channel/UCwpOnf144tZdz5FOaYbRFKg/featured?view_as=subscriber"
qr=pyqrcode.create(x)
qr.png("qr.png", scale =2)
qr.show()