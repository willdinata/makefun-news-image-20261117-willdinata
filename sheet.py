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
font_masthead = get_font(FONT_SERIF_BOLD, 80)
font_dateline = get_font(FONT_SANS_BOLD, 15)
font_breaking = get_font(FONT_SANS_BOLD, 18)
font_lead_head = get_font(FONT_SERIF_BOLD, 34)
font_lead_desc = get_font(FONT_SERIF, 16)
font_tile_label = get_font(FONT_SANS_BOLD, 12)
font_tile_head = get_font(FONT_SERIF_BOLD, 17)
font_tile_desc = get_font(FONT_SANS, 12)
font_footer = get_font(FONT_SANS, 10)

def draw_icon(draw, icon_name, x, y, size=26):
    cx = x + size / 2.0
    cy = y + size / 2.0
    
    if icon_name == "burst":
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x2 = cx + 8 * math.cos(rad)
            y2 = cy + 8 * math.sin(rad)
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
    y += 8
    masthead_text = "The Daily Herald"
    bbox = draw.textbbox((0, 0), masthead_text, font=font_masthead)
    mw = bbox[2] - bbox[0]
    mh = bbox[3] - bbox[1]
    mx = (WIDTH - mw) / 2
    draw.text((mx, y), masthead_text, fill=COLOR_INK, font=font_masthead)
    
    y += mh + 16
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=5)
    y += 6
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=2)
    
    # 3. Dateline bar
    y += 5
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 3
    dateline_h = 22
    
    left_date = "TUESDAY 17 NOVEMBER 2026"
    mid_info = "15 STORIES · 4 CONTINENTS"
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
    y += 5
    break_h = 28
    draw.rectangle([margin, y, WIDTH - margin, y + break_h], fill=COLOR_RED)
    break_text = "BREAKING NEWS — CRIMEAN BRIDGE ARCH FALLS IN SECOND-DAY STRIKE"
    bbox_b = draw.textbbox((0, 0), break_text, font=font_breaking)
    bw = bbox_b[2] - bbox_b[0]
    bh = bbox_b[3] - bbox_b[1]
    bx = (WIDTH - bw) / 2
    by = y + (break_h - bh) / 2 - 2
    draw.text((bx, by), break_text, fill=COLOR_WHITE, font=font_breaking)
    
    y += break_h + 4
    
    # 5. LEAD block (rebalanced vertical padding and panel height)
    lead_start_y = y
    lead_left_w = 600
    lead_right_x = 660
    lead_right_w = 328
    
    lead_data = stories.LEAD
    reg_key = lead_data["label"].split("·")[0].strip()
    reg_color = stories.REGION_COLORS.get(reg_key, COLOR_INK)
    
    chip_size = 26
    draw.rounded_rectangle([margin, y, margin + chip_size, y + chip_size], radius=4, fill=reg_color)
    draw_icon(draw, lead_data["icon"], margin, y, size=chip_size)
    
    draw.text((margin + chip_size + 10, y + 4), lead_data["label"], fill=reg_color, font=font_tile_label)
    
    y += chip_size + 3
    
    # Lead headline (3 lines)
    lead_head_lines = ["Ukraine fells the Crimean", "Bridge arch in a", "second-day strike"]
    for line in lead_head_lines:
        draw.text((margin, y), line, fill=COLOR_INK, font=font_lead_head)
        y += 34
        
    y += 1
    # Lead description
    lead_desc_lines = wrap_text_to_lines(draw, lead_data["desc"], font_lead_desc, lead_left_w)
    for line in lead_desc_lines[:3]:
        draw.text((margin, y), line, fill=COLOR_DARK_GREY, font=font_lead_desc)
        y += 18
        
    lead_end_y = y
    
    # Right column: symbolic bridge scene panel (reduced panel_h from 165 to 115)
    panel_y = lead_start_y
    panel_h = 115
    draw.rectangle([lead_right_x, panel_y, lead_right_x + lead_right_w, panel_y + panel_h], outline=COLOR_INK, width=1, fill=(240, 235, 220))
    
    px1 = lead_right_x + 12
    py1 = panel_y + 8
    px2 = lead_right_x + lead_right_w - 12
    py2 = panel_y + panel_h - 8
    
    # Sea band at bottom
    sea_top = py2 - 30
    draw.rectangle([px1, sea_top, px2, py2], fill=(130, 150, 170))
    
    # Pylons
    pylon_w = 18
    pylon1_x = px1 + 60
    pylon2_x = px2 - 78
    draw.rectangle([pylon1_x, py1 + 16, pylon1_x + pylon_w, sea_top], fill=(90, 95, 100))
    draw.rectangle([pylon2_x, py1 + 16, pylon2_x + pylon_w, sea_top], fill=(90, 95, 100))
    
    # Deck with unmistakable gap between pylons and fallen arch half-sunk in the sea band
    deck_y = py1 + 28
    draw.rectangle([px1 + 10, deck_y, pylon1_x, deck_y + 7], fill=COLOR_INK)
    draw.rectangle([pylon2_x + pylon_w, deck_y, px2 - 10, deck_y + 7], fill=COLOR_INK)
    
    arch_pts = [
        (pylon1_x, deck_y + 7),
        ((pylon1_x + pylon2_x) / 2 - 20, sea_top + 4),
        ((pylon1_x + pylon2_x) / 2 + 20, sea_top + 8),
        (pylon2_x + pylon_w, deck_y + 7)
    ]
    draw.line(arch_pts, fill=COLOR_RED, width=4)
    
    # Smoke puffs
    draw.ellipse([pylon1_x - 10, deck_y - 18, pylon1_x + 10, deck_y + 2], fill=(200, 195, 190))
    draw.ellipse([pylon1_x + 2, deck_y - 26, pylon1_x + 26, deck_y - 6], fill=(215, 210, 205))
    
    # Small red starburst at the break
    sx = (pylon1_x + pylon2_x) / 2
    sy = deck_y + 10
    for a in range(0, 360, 60):
        rad = math.radians(a)
        draw.line([(sx, sy), (sx + 8 * math.cos(rad), sy + 8 * math.sin(rad))], fill=COLOR_RED, width=2)
        
    y_after_lead = max(lead_end_y, panel_y + panel_h) + 6
    draw.line([(margin, y_after_lead), (WIDTH - margin, y_after_lead)], fill=COLOR_INK, width=1)
    y = y_after_lead + 6
    
    # 6. GRID of 12 stories (3 cols x 4 rows) with tightened row height and description line spacing
    grid_items = stories.GRID
    cols = 3
    rows = 4
    col_w = 292
    col_gap = 38
    row_h = 112
    
    start_grid_y = y
    tile_bottoms = []
    
    for idx, item in enumerate(grid_items):
        c = idx % cols
        r = idx // cols
        
        cx_pos = margin + c * (col_w + col_gap)
        cy_pos = start_grid_y + r * row_h
        
        reg_k = item["label"].split("·")[0].strip()
        r_col = stories.REGION_COLORS.get(reg_k, COLOR_INK)
        
        # Chip + label
        draw.rounded_rectangle([cx_pos, cy_pos, cx_pos + 20, cy_pos + 20], radius=3, fill=r_col)
        draw_icon(draw, item["icon"], cx_pos, cy_pos, size=20)
        draw.text((cx_pos + 26, cy_pos + 3), item["label"], fill=r_col, font=font_tile_label)
        
        # Headline (up to 2 lines)
        head_lines = wrap_text_to_lines(draw, item["head"], font_tile_head, col_w)
        th_y = cy_pos + 23
        for hline in head_lines[:2]:
            draw.text((cx_pos, th_y), hline, fill=COLOR_INK, font=font_tile_head)
            th_y += 18
            
        # Description (up to 3 lines)
        desc_lines = wrap_text_to_lines(draw, item["desc"], font_tile_desc, col_w)
        td_y = th_y + 1
        d_lines_drawn = 0
        for dline in desc_lines[:3]:
            draw.text((cx_pos, td_y), dline, fill=COLOR_DARK_GREY, font=font_tile_desc)
            td_y += 15
            d_lines_drawn += 1
            
        desc_last_line_bottom = td_y if d_lines_drawn > 0 else th_y
        tile_bottoms.append((r, desc_last_line_bottom))
            
    # Programmatic verification assertions: keep at least 4 px clear under each tile's last description line
    for r in range(rows):
        row_tiles = [bot for row_idx, bot in tile_bottoms if row_idx == r]
        max_desc_bottom = max(row_tiles)
        if r < rows - 1:
            next_row_label_top = start_grid_y + (r + 1) * row_h
            clearance = next_row_label_top - max_desc_bottom
            assert clearance >= 4, f"Row {r} description bottom ({max_desc_bottom}) is too close to next row label top ({next_row_label_top}), clearance={clearance}px < 4px"
        else:
            grid_total_h = rows * row_h
            brief_start_y = start_grid_y + grid_total_h + 3
            clearance = brief_start_y - max_desc_bottom
            assert clearance >= 4, f"Last row description bottom ({max_desc_bottom}) is too close to brief strip start ({brief_start_y}), clearance={clearance}px < 4px"

    # Draw grid dividing rules
    grid_total_h = rows * row_h
    v1_x = margin + col_w + col_gap / 2
    v2_x = margin + 2 * col_w + 1.5 * col_gap
    draw.line([(v1_x, start_grid_y - 4), (v1_x, start_grid_y + grid_total_h - 4)], fill=(210, 205, 195), width=1)
    draw.line([(v2_x, start_grid_y - 4), (v2_x, start_grid_y + grid_total_h - 4)], fill=(210, 205, 195), width=1)
    
    for r in range(1, rows):
        hr_y = start_grid_y + r * row_h - 4
        draw.line([(margin, hr_y), (WIDTH - margin, hr_y)], fill=(210, 205, 195), width=1)
        
    y = start_grid_y + grid_total_h + 3
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 6
    
    # 7. BRIEF strip (2 items side by side)
    brief_items = stories.BRIEF
    brief_col_w = 450
    brief_gap = 52
    
    brief_top_pad = 8
    brief_label_h = 26
    brief_head_h = 24
    brief_desc_h = 17
    brief_bottom_pad = 8
    
    y += brief_top_pad
    for idx, item in enumerate(brief_items):
        bx = margin + idx * (brief_col_w + brief_gap)
        by = y
        
        reg_k = item["label"].split("·")[0].strip()
        r_col = stories.REGION_COLORS.get(reg_k, COLOR_INK)
        
        draw.rounded_rectangle([bx, by, bx + 18, by + 18], radius=3, fill=r_col)
        draw_icon(draw, item["icon"], bx, by, size=18)
        draw.text((bx + 24, by + 2), item["label"], fill=r_col, font=font_tile_label)
        
        head_lines = wrap_text_to_lines(draw, item["head"], font_tile_head, brief_col_w - 26)
        bh_y = by + brief_label_h
        for hline in head_lines[:1]:
            draw.text((bx, bh_y), hline, fill=COLOR_INK, font=font_tile_head)
            
        desc_lines = wrap_text_to_lines(draw, item["desc"], font_tile_desc, brief_col_w)
        bd_y = bh_y + brief_head_h
        for dline in desc_lines[:1]:
            draw.text((bx, bd_y), dline, fill=COLOR_DARK_GREY, font=font_tile_desc)
            
    y += brief_label_h + brief_head_h + brief_desc_h + brief_bottom_pad
    draw.line([(margin, y), (WIDTH - margin, y)], fill=COLOR_INK, width=1)
    y += 6
    
    # 8. Footer
    footer_text = "Every story happened or was first reported on Tuesday 17 November 2026. Contested claims are marked as claims. Sources: Reuters, AP, AFP, BBC, Al Jazeera, WHO, UN. Original drawings."
    footer_lines = wrap_text_to_lines(draw, footer_text, font_footer, content_width)
    ft_y = y
    for fline in footer_lines:
        draw.text((margin, ft_y), fline, fill=COLOR_MUTED_GREY, font=font_footer)
        ft_y += 13
        
    footer_bottom = ft_y
    
    # Layout assertion: raises if computed footer bottom exceeds y=1010
    assert footer_bottom <= 1010, f"Footer bottom y={footer_bottom} exceeds y=1010!"
    
    # Save output
    output_path = "entry.png"
    img.save(output_path, "PNG")

if __name__ == "__main__":
    generate_broadsheet()
