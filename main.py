import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

from hloc import extract_features, match_features, reconstruction, visualization, pairs_from_exhaustive
from hloc.visualization import plot_images, read_image
from hloc.utils import viz_3d

import os
import cv2
import pycolmap

import numpy as np
import mediapy as media
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from glob import glob
from pathlib import Path
from time import time

scene_value = int(input("\nAvailable Scenes:\n\t1. Brandenburg Gate\n\t2. British Museum\n\t3. Buckingham Palace\n\t4. Colosseum Exterior\n\t5. Grand Palace Brussels\n\t6. Lincoln Memorial Statue\n\t7. Notre Dame Front Facade\n\t8. Pantheon Exterior\n\t9. Piazza San Marco\n\t10. Sacre Coeur\n\t11. Sagrada_familia\n\t12. St Pauls Cathedral\n\t13. St Peters Square\n\t14. Taj Mahal\n\t15. Temple Nara Japan\n\t16. Trevi Fountain\n\nChoose scene: "))

switcher = {
    1: "brandenburg_gate",
    2: "british_museum",
    3: "buckingham_palace",
    4: "colosseum_exterior",
    5: "grand_place_brussels",
    6: "lincoln_memorial_statue",
    7: "notre_dame_front_facade",
    8: "pantheon_exterior",
    9: "piazza_san_marco",
    10: "sacre_coeur",
    11: "sagrada_familia",
    12: "st_pauls_cathedral",
    13: "st_peters_square",
    14: "taj_mahal",
    15: "temple_nara_japan",
    16: "trevi_fountain",
}

scene = switcher.get(scene_value, "nothing")
src = f'images/{scene}'

print("Creating Scene")
rec_gt = pycolmap.Reconstruction(f'{src}/sfm')
cameras = input("Do you want to plot cameras (y/n): ")

fig = viz_3d.init_figure()

if cameras == 'y':
    viz_3d.plot_cameras(fig, rec_gt, color='rgba(50,255,50, 0.5)', name="Ground Truth", size=10) 

viz_3d.plot_reconstruction(fig, rec_gt, cameras = False, color='rgba(201,56,110,0.5)', name="Ground Truth", cs=5)
fig.show()
print("Scene Created")