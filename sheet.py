import os
import math
from PIL import Image, ImageDraw, ImageFont
import stories

# Canvas dimensions
WIDTH = 1024
HEIGHT = 1024

# Colors
COLOR_PAPER = (248, 243, 230)
COLOR_INK = (27, 24, 21)
COLOR_RED = (166, 43, 31)
COLOR_DARK_GREY = (58, 63, 69)
COLOR_MUTED_GREY = (110, 105, 95)
COLOR_WHITE = (255, 255, 255)

# Fonts paths
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
FONT_SERIF_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
FONT_SERIF = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
FONT_SANS_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
FONT_SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

font_top_left = get_font(FONT_SANS_BOLD, 13)
font_masthead = get_font(FONT_SERIF_BOLD, 62)
font_dateline = get_font(FONT_SANS_BOLD, 11)
font_breaking = get_font(FONT_SANS_BOLD, 16)
font_lead_head = get_font(FONT_SERIF_BOLD, 30)
font_lead_desc = get_font(FONT_SERIF, 15)
font_tile_label = get_font(FONT_SANS_BOLD, 12)
font_tile_head = get_font(FONT_SERIF_BOLD, 16)
font_tile_desc = get_font(FONT_SANS, 11)
font_map_head = get_font(FONT_SANS_BOLD, 13)
font_map_sub = get_font(FONT_SANS, 10)
font_badge_lead = get_font(FONT_SANS_BOLD, 13)
font_badge_grid = get_font(FONT_SANS_BOLD, 10)
font_badge_brief = get_font(FONT_SANS_BOLD, 9)
font_badge_pin = get_font(FONT_SANS_BOLD, 9)
font_brief_tag = get_font(FONT_SANS_BOLD, 11)
font_brief_tag_sm = get_font(FONT_SANS_BOLD, 10)
font_brief_text = get_font(FONT_SANS, 11)
font_brief_text_sm = get_font(FONT_SANS, 10)
font_footer = get_font(FONT_SANS, 10)

font_num_head = get_font(FONT_SANS_BOLD, 12)
font_stat_fig = get_font(FONT_SERIF_BOLD, 19)
font_stat_cap = get_font(FONT_SANS, 10)

LAND = [
    [(-168,66), (-140,70), (-125,72), (-110,68), (-95,69), (-85,66), (-80,62), (-76,58), (-70,62), (-65,60), (-60,52), (-65,48), (-70,44), (-74,40), (-76,35), (-80,32), (-81,26), (-84,28), (-87,30), (-90,29), (-94,29), (-97,26), (-97,22), (-94,18), (-90,20), (-87,21), (-86,16), (-83,10), (-79,9), (-83,14), (-87,16), (-92,15), (-97,16), (-102,18), (-105,22), (-110,24), (-114,29), (-117,33), (-122,37), (-124,44), (-124,48), (-130,54), (-140,60), (-155,60), (-165,60)],
    [(-79,9), (-72,12), (-64,10), (-55,6), (-50,0), (-44,-3), (-35,-8), (-39,-13), (-40,-20), (-46,-24), (-52,-28), (-57,-34), (-62,-39), (-65,-41), (-65,-45), (-67,-50), (-69,-52), (-71,-54), (-74,-50), (-74,-44), (-73,-37), (-71,-30), (-70,-20), (-70,-15), (-75,-12), (-79,-6), (-81,-3), (-80,1), (-77,4), (-78,7)],
    [(-17,15), (-10,29), (-6,34), (0,36), (10,37), (11,34), (20,32), (30,31), (35,28), (38,22), (40,16), (43,12), (48,11), (51,12), (48,6), (44,0), (40,-6), (40,-14), (38,-20), (35,-24), (32,-29), (26,-33), (20,-35), (17,-32), (15,-27), (13,-20), (12,-14), (13,-8), (9,-1), (9,4), (4,6), (-3,5), (-8,5), (-13,8), (-17,12)],
    [(-10,36), (-9,43), (-2,44), (-9,48), (-2,50), (3,52), (7,54), (8,56), (5,58), (10,59), (18,56), (21,60), (25,61), (23,65), (30,70), (45,68), (60,69), (75,72), (90,73), (105,77), (120,73), (135,72), (150,70), (162,70), (170,67), (178,66), (178,62), (162,60), (158,54), (150,50), (142,50), (140,44), (135,40), (130,38), (127,40), (122,38), (120,34), (122,30), (118,26), (110,20), (108,16), (105,9), (103,6), (100,8), (98,14), (94,17), (90,22), (88,21), (85,19), (80,15), (77,8), (72,20), (66,25), (60,25), (54,26), (50,29), (48,30), (50,24), (55,24), (58,22), (56,19), (52,15), (45,12), (43,12), (40,16), (38,22), (36,28), (34,31), (33,36), (30,36), (27,37), (22,37), (19,40), (15,38), (12,38), (10,37), (3,37), (-2,37)],
    [(-5,50), (-3,53), (-5,56), (-3,57), (-6,58), (-8,55), (-6,52)],
    [(130,31), (133,34), (137,35), (140,36), (141,40), (142,44), (140,45), (138,39), (135,35), (131,33)],
    [(95,5), (100,0), (106,-6), (110,-7), (114,-8), (119,-9), (124,-10), (131,-3), (136,-3), (141,-4), (141,-8), (135,-5), (128,-4), (120,-3), (113,-3), (105,-3), (99,2)],
    [(113,-22), (114,-28), (115,-34), (118,-35), (124,-33), (129,-32), (132,-32), (135,-35), (138,-36), (140,-38), (145,-38), (150,-37), (153,-32), (153,-27), (151,-24), (146,-19), (142,-15), (142,-11), (140,-17), (136,-15), (135,-12), (132,-11), (130,-13), (126,-14), (122,-17), (118,-20)],
    [(167,-45), (172,-41), (174,-39), (176,-38), (174,-36), (171,-39), (169,-43), (167,-46)]
]

PIN_NUDGES = {
    1: (0, 0),
    2: (6, 4),
    3: (0, 0),
    4: (0, 0),
    5: (-6, -5),
    6: (0, 0),
    7: (7, -5),
    8: (-4, 7),
    9: (0, 0),
    10: (0, 0),
    11: (0, 0),
    12: (0, 0),
    13: (-8, 7),
}

def draw_icon(draw, icon_name, x, y, size=26):
    cx = x + size / 2.0
    cy = y + size / 2.0
    
    if icon_name == "burst":
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x2 = cx + (size * 0.35) * math.cos(rad)
            y2 = cy + (size * 0.35) * math.sin(rad)
            draw.line([(cx, cy), (x2, y2)], fill=COLOR_WHITE, width=2)
        draw.ellipse([cx-3, cy-3, cx+3, cy+3], fill=COLOR_WHITE)
        
    elif icon_name == "drone":
        draw.rectangle([cx-6, cy-2, cx+6, cy+2], fill=COLOR_WHITE)
        draw.ellipse([cx-9, cy-9, cx-5, cy-5], outline=COLOR_WHITE, width=1)
        draw.ellipse([cx+5, cy-9, cx+9, cy-5], outline=COLOR_WHITE, width=1)
        draw.ellipse([cx-9, cy+5, cx-5, cy+9], outline=COLOR_WHITE, width=1)
        draw.ellipse([cx+5, cy+5, cx+9, cy+9], outline=COLOR_WHITE, width=1)
        
    elif icon_name == "flag":
        draw.line([(cx-4, cy+9), (cx-4, cy-9)], fill=COLOR_WHITE, width=2)
        draw.polygon([(cx-4, cy-9), (cx+8, cy-5), (cx-4, cy-1)], fill=COLOR_WHITE)
        
    elif icon_name == "cross":
        draw.rectangle([cx-2, cy-8, cx+2, cy+8], fill=COLOR_WHITE)
        draw.rectangle([cx-8, cy-2, cx+8, cy+2], fill=COLOR_WHITE)
        
    elif icon_name == "leaf":
        draw.arc([cx-8, cy-8, cx+8, cy+8], start=30, end=210, fill=COLOR_WHITE, width=2)
        draw.line([(cx-6, cy+6), (cx+4, cy-4)], fill=COLOR_WHITE, width=2)
        
    elif icon_name == "chart":
        draw.rectangle([cx-8, cy+2, cx-4, cy+8], fill=COLOR_WHITE)
        draw.rectangle([cx-2, cy-2, cx+2, cy+8], fill=COLOR_WHITE)
        draw.rectangle([cx+4, cy-6, cx+8, cy+8], fill=COLOR_WHITE)
        draw.line([(cx-9, cy+9), (cx+9, cy+9)], fill=COLOR_WHITE, width=2)
        
    elif icon_name == "pin":
        draw.ellipse([cx-5, cy-9, cx+5, cy+1], fill=COLOR_WHITE)
        draw.polygon([(cx-5, cy-2), (cx+5, cy-2), (cx, cy+9)], fill=COLOR_WHITE)
        
    elif icon_name == "sun":
        draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill=COLOR_WHITE)
        for a in range(0, 360, 45):
            r1, r2 = 6, 9
            rad = math.radians(a)
            draw.line([(cx + r1*math.cos(rad), cy + r1*math.sin(rad)),
                       (cx + r2*math.cos(rad), cy + r2*math.sin(rad))], fill=COLOR_WHITE, width=2)
                       
    elif icon_name == "people":
        draw.ellipse([cx-7, cy-8, cx-3, cy-4], fill=COLOR_WHITE)
        draw.arc([cx-9, cy-2, cx-1, cy+8], start=180, end=360, fill=COLOR_WHITE, width=2)
        draw.ellipse([cx+3, cy-8, cx+7, cy-4], fill=COLOR_WHITE)
        draw.arc([cx+1, cy-2, cx+9, cy+8], start=180, end=360, fill=COLOR_WHITE, width=2)
        
    elif icon_name == "warning":
        draw.polygon([(cx, cy-9), (cx-9, cy+8), (cx+9, cy+8)], outline=COLOR_WHITE, width=2)
        draw.line([(cx, cy-4), (cx, cy+2)], fill=COLOR_WHITE, width=2)
        draw.ellipse([cx-1, cy+5, cx+1, cy+7], fill=COLOR_WHITE)
        
    elif icon_name == "chip":
        draw.rectangle([cx-6, cy-6, cx+6, cy+6], outline=COLOR_WHITE, width=2)
        draw.line([(cx-9, cy-3), (cx-6, cy-3)], fill=COLOR_WHITE, width=2)
        draw.line([(cx-9, cy+3), (cx-6, cy+3)], fill=COLOR_WHITE, width=2)
        draw.line([(cx+6, cy-3), (cx+9, cy-3)], fill=COLOR_WHITE, width=2)
        draw.line([(cx+6, cy+3), (cx+9, cy+3)], fill=COLOR_WHITE, width=2)
        
    elif icon_name == "scale":
        draw.line([(cx, cy-8), (cx, cy+8)], fill=COLOR_WHITE, width=2)
        draw.line([(cx-8, cy-5), (cx+8, cy-5)], fill=COLOR_WHITE, width=2)
        draw.arc([cx-9, cy-1, cx-5, cy+7], start=0, end=180, fill=COLOR_WHITE, width=1)
        draw.arc([cx+5, cy-1, cx+9, cy+7], start=0, end=180, fill=COLOR_WHITE, width=1)
        
    elif icon_name == "train":
        draw.rectangle([cx-8, cy-6, cx+8, cy+6], outline=COLOR_WHITE, width=2)
        draw.rectangle([cx-5, cy-4, cx-1, cy-1], fill=COLOR_WHITE)
        draw.rectangle([cx+1, cy-4, cx+5, cy-1], fill=COLOR_WHITE)
        draw.ellipse([cx-6, cy+6, cx-2, cy+10], fill=COLOR_WHITE)
        draw.ellipse([cx+2, cy+6, cx+6, cy+10], fill=COLOR_WHITE)
        
    elif icon_name == "ball":
        draw.ellipse([cx-8, cy-8, cx+8, cy+8], outline=COLOR_WHITE, width=2)
        draw.line([(cx-6, cy-6), (cx+6, cy+6)], fill=COLOR_WHITE, width=1)
        draw.line([(cx-6, cy+6), (cx+6, cy-6)], fill=COLOR_WHITE, width=1)
    else:
        draw.rectangle([cx-4, cy-4, cx+4, cy+4], fill=COLOR_WHITE)

def wrap_text_to_lines(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width or not current_line:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def lon_lat_to_xy(lon, lat, map_x, map_y, map_w, map_h):
    x = map_x + (lon + 180.0) / 360.0 * map_w
    y = map_y + (78.0 - lat) / 136.0 * map_h
    return (x, y)

def generate_broadsheet():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=COLOR_PAPER)
    draw = ImageDraw.Draw(img)
    
    margin = 36
    content_width = WIDTH - 2 * margin # 952
    
    # 1. Top line
    y = 16
    draw.text((margin, y), "LATE EDITION", fill=COLOR_INK, font=font_top_left)
    right_text = "THE WORLD IN ONE PAGE"
    bbox = draw.textbbox((0, 0), right_text, font=font_top_left)
    rw = bbox[2] - bbox[0]
    draw.text((WIDTH - margin - rw, y), right_text, fill=COLOR_INK, font=font_top_left)
    
    y += 18
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    
    # 2. Masthead
    y += 4
    masthead_text = "The Daily Herald"
    bbox = draw.textbbox((0, 0), masthead_text, font=font_masthead)
    mw = bbox[2] - bbox[0]
    mh = bbox[3] - bbox[1]
    mx = (WIDTH - mw) / 2
    draw.text((mx, y), masthead_text, fill=COLOR_INK, font=font_masthead)
    
    y += mh + 10
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=5)
    y += 5
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=2)
    
    # 3. Dateline bar
    y += 4
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 3
    dateline_h = 20
    
    left_date = "TUESDAY 17 NOVEMBER 2026"
    mid_info = "33 STORIES · 6 CONTINENTS"
    right_info = "ONE IMAGE, THE WHOLE DAY"
    
    draw.text((margin, y), left_date, fill=COLOR_INK, font=font_dateline)
    
    bbox_mid = draw.textbbox((0, 0), mid_info, font=font_dateline)
    mid_w = bbox_mid[2] - bbox_mid[0]
    draw.text(((WIDTH - mid_w) / 2, y), mid_info, fill=COLOR_INK, font=font_dateline)
    
    bbox_right = draw.textbbox((0, 0), right_info, font=font_dateline)
    right_w = bbox_right[2] - bbox_right[0]
    draw.text((WIDTH - margin - right_w, y), right_info, fill=COLOR_INK, font=font_dateline)
    
    y += dateline_h
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    
    # 4. BREAKING strip
    y += 4
    break_h = 26
    draw.rectangle([margin, y, WIDTH - margin, y + break_h], fill=COLOR_RED)
    break_text = "BREAKING NEWS — CRIMEAN BRIDGE ARCH FALLS IN SECOND-DAY STRIKE"
    bbox_b = draw.textbbox((0, 0), break_text, font=font_breaking)
    bw = bbox_b[2] - bbox_b[0]
    bh = bbox_b[3] - bbox_b[1]
    bx = (WIDTH - bw) / 2
    by = y + (break_h - bh) / 2 - 2
    draw.text((bx, by), break_text, fill=COLOR_WHITE, font=font_breaking)
    
    y += break_h + 5
    
    # 5. LEAD block & Richer Lead Art Panel
    lead_start_y = y
    lead_left_w = 580
    lead_right_w = 340
    lead_right_x = WIDTH - margin - lead_right_w
    
    lead_data = stories.LEAD
    reg_key = lead_data["label"].split("·")[0].strip()
    reg_color = stories.REGION_COLORS.get(reg_key, COLOR_INK)
    
    # Lead badge (diameter 26) at left of label row
    badge_d = 26
    draw.ellipse([margin, y, margin + badge_d, y + badge_d], fill=reg_color)
    num_txt = str(lead_data["num"])
    bbox_n = draw.textbbox((0, 0), num_txt, font=font_badge_lead)
    nw = bbox_n[2] - bbox_n[0]
    nh = bbox_n[3] - bbox_n[1]
    draw.text((margin + (badge_d - nw) / 2, y + (badge_d - nh) / 2 - 2), num_txt, fill=COLOR_WHITE, font=font_badge_lead)
    
    chip_size = 26
    chip_x = margin + badge_d + 6
    draw.rounded_rectangle([chip_x, y, chip_x + chip_size, y + chip_size], radius=4, fill=reg_color)
    draw_icon(draw, lead_data["icon"], chip_x, y, size=chip_size)
    
    draw.text((chip_x + chip_size + 8, y + 5), lead_data["label"], fill=reg_color, font=font_tile_label)
    
    y += badge_d + 6
    
    # Lead headline (3 lines)
    lead_head_lines = ["Ukraine fells the Crimean", "Bridge arch in a", "second-day strike"]
    for line in lead_head_lines:
        draw.text((margin, y), line, fill=COLOR_INK, font=font_lead_head)
        y += 34
        
    y += 2
    lead_desc_lines = wrap_text_to_lines(draw, lead_data["desc"], font_lead_desc, lead_left_w)
    for line in lead_desc_lines[:3]:
        draw.text((margin, y), line, fill=COLOR_DARK_GREY, font=font_lead_desc)
        y += 18
        
    lead_end_y = y
    
    # Right lead art panel (~340 wide, 140 tall)
    panel_y = lead_start_y
    panel_h = 130
    draw.rectangle([lead_right_x, panel_y, lead_right_x + lead_right_w, panel_y + panel_h], outline=COLOR_INK, width=1, fill=(240, 235, 220))
    
    px1 = lead_right_x + 10
    py1 = panel_y + 8
    px2 = lead_right_x + lead_right_w - 10
    py2 = panel_y + panel_h - 8
    
    # Sky bands (3 soft horizontal bands)
    band_h = (py2 - 40 - py1) / 3
    draw.rectangle([px1, py1, px2, py1 + band_h], fill=(232, 227, 215))
    draw.rectangle([px1, py1 + band_h, px2, py1 + 2*band_h], fill=(224, 218, 205))
    draw.rectangle([px1, py1 + 2*band_h, px2, py2 - 32], fill=(215, 208, 195))
    
    # Pale sun disc
    draw.ellipse([px2 - 60, py1 + 14, px2 - 36, py1 + 38], fill=(245, 238, 210))
    
    # Tiny bird strokes (small "v" polylines) in sky
    for bx_off, by_off in [(35, 20), (55, 12), (80, 25)]:
        bx_center = px1 + bx_off
        by_center = py1 + by_off
        draw.line([(bx_center - 4, by_center - 3), (bx_center, by_center), (bx_center + 4, by_center - 3)], fill=COLOR_INK, width=1)
    
    # Sea band at bottom with white wave arcs
    sea_top = py2 - 32
    draw.rectangle([px1, sea_top, px2, py2], fill=(135, 155, 175))
    for wx in range(px1 + 15, px2 - 15, 30):
        draw.arc([wx, sea_top + 6, wx + 20, sea_top + 22], start=0, end=180, fill=COLOR_WHITE, width=1)
        
    # Bridge structure: two pylons, deck, suspension cables, broken span tilted into sea, smoke, red starburst
    pylon_w = 16
    pylon1_x = px1 + 75
    pylon2_x = px2 - 95
    pylon_top_y = py1 + 35
    
    draw.rectangle([pylon1_x, pylon_top_y, pylon1_x + pylon_w, sea_top], fill=(85, 90, 95))
    draw.rectangle([pylon2_x, pylon_top_y, pylon2_x + pylon_w, sea_top], fill=(85, 90, 95))
    
    deck_y = pylon_top_y + 25
    # Left deck span
    draw.rectangle([px1 + 10, deck_y, pylon1_x, deck_y + 6], fill=COLOR_INK)
    # Right deck span
    draw.rectangle([pylon2_x + pylon_w, deck_y, px2 - 10, deck_y + 6], fill=COLOR_INK)
    
    # Suspension cables from pylon tops to deck
    draw.line([(pylon1_x + pylon_w/2, pylon_top_y), (px1 + 15, deck_y)], fill=COLOR_INK, width=1)
    draw.line([(pylon1_x + pylon_w/2, pylon_top_y), (pylon1_x, deck_y)], fill=COLOR_INK, width=1)
    draw.line([(pylon2_x + pylon_w/2, pylon_top_y), (pylon2_x + pylon_w, deck_y)], fill=COLOR_INK, width=1)
    draw.line([(pylon2_x + pylon_w/2, pylon_top_y), (px2 - 15, deck_y)], fill=COLOR_INK, width=1)
    
    # Broken center span tilted down into sea
    break_left_x = pylon1_x + pylon_w
    break_right_x = pylon2_x
    draw.line([(break_left_x, deck_y), ((break_left_x + break_right_x)/2, sea_top - 6), (break_right_x, deck_y)], fill=COLOR_RED, width=3)
    
    # Three layered grey smoke ellipses rising from the break
    smoke_cx = (break_left_x + break_right_x) / 2
    smoke_cy = deck_y - 10
    draw.ellipse([smoke_cx - 24, smoke_cy - 22, smoke_cx + 4, smoke_cy + 2], fill=(210, 205, 200))
    draw.ellipse([smoke_cx - 8, smoke_cy - 34, smoke_cx + 20, smoke_cy - 8], fill=(225, 220, 215))
    draw.ellipse([smoke_cx - 16, smoke_cy - 44, smoke_cx + 12, smoke_cy - 20], fill=(240, 235, 230))
    
    # Small red starburst at the break point
    star_x = smoke_cx
    star_y = deck_y
    for a in range(0, 360, 45):
        rad = math.radians(a)
        draw.line([(star_x, star_y), (star_x + 9 * math.cos(rad), star_y + 9 * math.sin(rad))], fill=COLOR_RED, width=2)
        
    y_after_lead = max(lead_end_y, panel_y + panel_h) + 4
    draw.line([(margin, y_after_lead), (WIDTH - margin, y_after_lead)], fill=COLOR_INK, width=1)
    y = y_after_lead + 5
    
    # 6. GRID of 12 stories (3 cols x 4 rows)
    grid_items = stories.GRID
    cols = 3
    rows = 4
    col_w = 292
    col_gap = 38
    start_grid_y = y
    
    # Pass 1: Measure content and compute row heights
    measured_tiles = []
    for item in grid_items:
        head_lines = wrap_text_to_lines(draw, item["head"], font_tile_head, col_w)
        desc_lines = wrap_text_to_lines(draw, item["desc"], font_tile_desc, col_w)
        content_h = 21 + (len(head_lines) * 18) + 1 + (len(desc_lines) * 13)
        measured_tiles.append({
            "item": item,
            "head_lines": head_lines,
            "desc_lines": desc_lines,
            "content_h": content_h
        })
        
    row_heights = [0] * rows
    for r in range(rows):
        row_tile_hs = [measured_tiles[r * cols + c]["content_h"] for c in range(cols)]
        row_heights[r] = max(row_tile_hs) + 4
        
    # Verify clearance assertions (pass 1 measurements)
    for r in range(rows):
        row_tile_hs = [measured_tiles[r * cols + c]["content_h"] for c in range(cols)]
        max_content_h = max(row_tile_hs)
        row_top = start_grid_y + sum(row_heights[:r])
        max_desc_bottom = row_top + max_content_h
        if r < rows - 1:
            next_row_top = start_grid_y + sum(row_heights[:r+1])
            clearance = next_row_top - max_desc_bottom
            assert clearance >= 4, f"Row {r} clearance {clearance}px < 4px"
        else:
            grid_total_h = sum(row_heights)
            brief_start_y = start_grid_y + grid_total_h + 3
            clearance = brief_start_y - max_desc_bottom
            assert clearance >= 4, f"Last row clearance {clearance}px < 4px"

    # Pass 2: Draw each tile at y = grid_top + sum of final row heights above it
    for idx, tile in enumerate(measured_tiles):
        item = tile["item"]
        c = idx % cols
        r = idx // cols
        
        cx_pos = margin + c * (col_w + col_gap)
        cy_pos = start_grid_y + sum(row_heights[:r])
        
        reg_k = item["label"].split("·")[0].strip()
        r_col = stories.REGION_COLORS.get(reg_k, COLOR_INK)
        
        # Grid badge (diameter 19)
        badge_d19 = 19
        draw.ellipse([cx_pos, cy_pos, cx_pos + badge_d19, cy_pos + badge_d19], fill=r_col)
        num_t = str(item["num"])
        bbox_nt = draw.textbbox((0, 0), num_t, font=font_badge_grid)
        ntw = bbox_nt[2] - bbox_nt[0]
        nth = bbox_nt[3] - bbox_nt[1]
        draw.text((cx_pos + (badge_d19 - ntw) / 2, cy_pos + (badge_d19 - nth) / 2 - 2), num_t, fill=COLOR_WHITE, font=font_badge_grid)
        
        chip_sz19 = 19
        chip_x19 = cx_pos + badge_d19 + 5
        draw.rounded_rectangle([chip_x19, cy_pos, chip_x19 + chip_sz19, cy_pos + chip_sz19], radius=3, fill=r_col)
        draw_icon(draw, item["icon"], chip_x19, cy_pos, size=chip_sz19)
        
        draw.text((chip_x19 + chip_sz19 + 6, cy_pos + 2), item["label"], fill=r_col, font=font_tile_label)
        
        th_y = cy_pos + 21
        for hline in tile["head_lines"]:
            draw.text((cx_pos, th_y), hline, fill=COLOR_INK, font=font_tile_head)
            th_y += 18
            
        td_y = th_y + 1
        for dline in tile["desc_lines"]:
            draw.text((cx_pos, td_y), dline, fill=COLOR_DARK_GREY, font=font_tile_desc)
            td_y += 13

    grid_total_h = sum(row_heights)

    # Draw grid rules
    v1_x = margin + col_w + col_gap / 2
    v2_x = margin + 2 * col_w + 1.5 * col_gap
    draw.line([(v1_x, start_grid_y - 3), (v1_x, start_grid_y + grid_total_h - 3)], fill=(210, 205, 195), width=1)
    draw.line([(v2_x, start_grid_y - 3), (v2_x, start_grid_y + grid_total_h - 3)], fill=(210, 205, 195), width=1)
    
    for r_idx in range(1, rows):
        hr_y = start_grid_y + sum(row_heights[:r_idx]) - 3
        draw.line([(margin, hr_y), (WIDTH - margin, hr_y)], fill=(210, 205, 195), width=1)
        
    y = start_grid_y + grid_total_h + 3
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 5
    
    # 7. Map Zone & THE DAY IN NUMBERS
    map_head_y = y
    draw.text((margin, map_head_y), "WHERE IT HAPPENED", fill=COLOR_RED, font=font_map_head)
    right_map_text = "Pins 1–13 — the main stories"
    bbox_rm = draw.textbbox((0, 0), right_map_text, font=font_map_sub)
    rmw = bbox_rm[2] - bbox_rm[0]
    draw.text((WIDTH - margin - rmw, map_head_y + 2), right_map_text, fill=COLOR_MUTED_GREY, font=font_map_sub)
    
    y += 18
    map_panel_x = margin
    map_panel_y = y
    map_panel_w = 470
    map_panel_h = 92
    
    # Draw Map Panel
    draw.rectangle([map_panel_x, map_panel_y, map_panel_x + map_panel_w, map_panel_y + map_panel_h], outline=COLOR_INK, width=1, fill=(233, 238, 240))
    
    # Draw LAND polygons
    land_fill = (213, 219, 204)
    land_outline = (168, 174, 158)
    for poly in LAND:
        screen_pts = [lon_lat_to_xy(lon, lat, map_panel_x, map_panel_y, map_panel_w, map_panel_h) for lon, lat in poly]
        draw.polygon(screen_pts, fill=land_fill, outline=land_outline)
        
    # Draw pins for main stories (1 to 13)
    all_main_stories = [stories.LEAD] + stories.GRID
    for st in all_main_stories:
        num = st["num"]
        lat, lon = st["pin"]
        dx, dy = PIN_NUDGES.get(num, (0, 0))
        
        px, py = lon_lat_to_xy(lon, lat, map_panel_x, map_panel_y, map_panel_w, map_panel_h)
        px += dx
        py += dy
        
        reg_k = st["label"].split("·")[0].strip()
        r_col = stories.REGION_COLORS.get(reg_k, COLOR_INK)
        
        pin_d = 15
        draw.ellipse([px - pin_d/2, py - pin_d/2, px + pin_d/2, py + pin_d/2], fill=r_col)
        num_str = str(num)
        bbox_ps = draw.textbbox((0, 0), num_str, font=font_badge_pin)
        psw = bbox_ps[2] - bbox_ps[0]
        psh = bbox_ps[3] - bbox_ps[1]
        draw.text((px - psw/2, py - psh/2 - 1), num_str, fill=COLOR_WHITE, font=font_badge_pin)
        
    # Draw "THE DAY IN NUMBERS" box to the right of the map
    box_x = margin + 486
    box_y = map_panel_y
    box_w = (WIDTH - margin) - box_x
    box_h = map_panel_h
    
    draw.rectangle([box_x, box_y, box_x + box_w, box_y + box_h], outline=COLOR_INK, width=1, fill=(240, 235, 220))
    draw.text((box_x + 12, box_y + 8), "THE DAY IN NUMBERS", fill=COLOR_RED, font=font_num_head)
    
    stats_data = [
        {"fig": "1,441", "cap": "drones Russia claims downed overnight"},
        {"fig": "$115.8bn", "cap": "Nvidia sales, doubled on AI demand"},
        {"fig": "11,000+", "cap": "Ebola cases in DR Congo, rising"},
        {"fig": "5,400", "cap": "US measles cases this year"}
    ]
    
    cell_w = 210
    col_positions = [box_x + 12, box_x + 238]
    row_positions = [box_y + 24, box_y + 57]
    
    for i, stat in enumerate(stats_data):
        sc = i % 2
        sr = i // 2
        cx_s = col_positions[sc]
        cy_s = row_positions[sr]
        
        draw.text((cx_s, cy_s), stat["fig"], fill=COLOR_INK, font=font_stat_fig)
        cap_lines = wrap_text_to_lines(draw, stat["cap"], font_stat_cap, cell_w)
        cy_cap = cy_s + 20
        for cline in cap_lines[:2]:
            draw.text((cx_s, cy_cap), cline, fill=COLOR_DARK_GREY, font=font_stat_cap)
            cy_cap += 12

    y = map_panel_y + map_panel_h + 4
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 5
    
    # 8. Briefs block ("ALSO ON TUESDAY")
    brief_head_y = y
    draw.text((margin, brief_head_y), "ALSO ON TUESDAY", fill=COLOR_RED, font=font_map_head)
    y += 18
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 5
    
    briefs = stories.BRIEF # 20 items (14 to 33)
    b_cols = 2
    b_rows = 10
    b_col_w = 460
    b_col_gap = 32
    b_line_h = 13
    
    for idx, item in enumerate(briefs):
        col = idx // b_rows
        row = idx % b_rows
        
        bx = margin + col * (b_col_w + b_col_gap)
        by = y + row * b_line_h
        
        reg_k = item["region"]
        r_col = stories.REGION_COLORS.get(reg_k, COLOR_INK)
        
        # Brief circle badge (diameter 13 or 14)
        bd_sz = 14
        draw.ellipse([bx, by + 1, bx + bd_sz, by + 1 + bd_sz], fill=r_col)
        b_num = str(item["num"])
        bbox_bn = draw.textbbox((0, 0), b_num, font=font_badge_brief)
        bnw = bbox_bn[2] - bbox_bn[0]
        bnh = bbox_bn[3] - bbox_bn[1]
        draw.text((bx + (bd_sz - bnw)/2, by + 1 + (bd_sz - bnh)/2 - 1), b_num, fill=COLOR_WHITE, font=font_badge_brief)
        
        tag_text = item["tag"] + ":"
        body_text = item["text"]
        
        tag_x = bx + bd_sz + 6
        
        full_line = tag_text + " " + body_text
        bbox_line11 = draw.textbbox((0, 0), full_line, font=font_brief_tag)
        w11 = bbox_line11[2] - bbox_line11[0]
        
        f_tag = font_brief_tag if w11 <= (b_col_w - (tag_x - bx)) else font_brief_tag_sm
        f_text = font_brief_text if w11 <= (b_col_w - (tag_x - bx)) else font_brief_text_sm
        
        draw.text((tag_x, by), tag_text, fill=COLOR_INK, font=f_tag)
        bbox_tag = draw.textbbox((0, 0), tag_text, font=f_tag)
        tw = bbox_tag[2] - bbox_tag[0]
        
        draw.text((tag_x + tw + 4, by), body_text, fill=COLOR_DARK_GREY, font=f_text)
        
    y += b_rows * b_line_h + 3
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 5
    
    # 9. Footer
    footer_text = "Every story happened or was first reported on Tuesday 17 November 2026. Contested claims are marked as claims. Sources: Reuters, AP, AFP, BBC, Al Jazeera, WHO, UN. Original drawings."
    footer_lines = wrap_text_to_lines(draw, footer_text, font_footer, content_width)
    ft_y = y
    for fline in footer_lines:
        draw.text((margin, ft_y), fline, fill=COLOR_MUTED_GREY, font=font_footer)
        ft_y += 13
        
    footer_bottom = ft_y
    
    # Print calculated footer bottom for reporting
    print(f"FOOTER_BOTTOM={footer_bottom}")
    
    # Layout assertion: raises if computed footer bottom exceeds y=1012
    assert footer_bottom <= 1012, f"Footer bottom y={footer_bottom} exceeds y=1012!"
    
    output_path = "entry.png"
    img.save(output_path, "PNG")

if __name__ == "__main__":
    generate_broadsheet()
