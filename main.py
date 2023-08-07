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

scene_value = int(input("\nAvailable Scenes:\n\t
                        1. Brandenburg Gate\n\t
                        2. British Museum\n\t
                        3. Buckingham Palace\n\t
                        4. Colosseum Exterior\n\t
                        5. Grand Palace Brussels\n\t
                        6. Lincoln Memorial Statue\n\t
                        7. Notre Dame Front Facade\n\t
                        8. Pantheon Exterior\n\t
                        9. Piazza San Marco\n\t
                        10. Sacre Coeur\n\t
                        11. Sagrada_familia\n\t
                        12. St Pauls Cathedral\n\t
                        13. St Peters Square\n\t
                        14. Taj Mahal\n\t
                        15. Temple Nara Japan\n\t
                        16. Trevi Fountain\n\n
                        Choose scene: "))

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
