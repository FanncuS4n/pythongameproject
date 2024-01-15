#GAME SETUP
WIDTH    = 1280 
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
 
#UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '1 - level/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

#GENERAL COLORS
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#UI COLORS
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#WEAPONS
weapon_data = {
  'sword': {'cooldown': 100, 'damage': 15, 'graphic': '7 - Weapon/graphics/weapons/sword/full.png'},
  'lance': {'cooldown': 400, 'damage': 30, 'graphic': '7 - Weapon/graphics/weapons/lance/full.png'},
  'axe': {'cooldown': 300, 'damage': 20, 'graphic': '7 - Weapon/graphics/weapons/axe/full.png'},
  'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '7 - Weapon/graphics/weapons/rapier/full.png'},
  'sai': {'cooldown': 80, 'damage': 10, 'graphic': '7 - Weapon/graphics/weapons/sai/full.png'}
}
 
#MAGIC
magic_data = {
  'flame': {'strenght': 5, 'cost': 20, 'graphic': '1 - level/graphics/particles/flame/fire.png'},
  'heal': {'strenght': 20, 'cost': 10, 'graphic': '1 - level/graphics/particles/heal/heal.png'}
}

#ENEMY 
monster_data = {
  'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': '10 - Enemies/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
  'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': '10 - Enemies/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
  'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': '10 - Enemies/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
  'bamboo': {'health': 700, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': '10 - Enemies/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}

# # OLD MAP DISPLAY
# WORLD_MAP = [
# ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
# ]