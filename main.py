import math
import random
import sys
import pygame

# ============================================================================
# NASA PALETTE
# ============================================================================
SCREEN_W, SCREEN_H = 1280, 760
FPS = 60

BLACK = (0, 0, 0)
PANEL_BLACK = (8, 12, 22)
NASA_NAVY = (11, 61, 145)
NASA_BLUE = (30, 144, 255)
LIGHT_BLUE = (135, 195, 255)
WHITE = (255, 255, 255)
MUTED_GRAY = (160, 175, 195)
BORDER_BLUE = (40, 95, 180)
ALERT_RED = (220, 45, 55)
OK_GREEN = (40, 220, 110)
GOLD = (255, 200, 60)

# ============================================================================
# LANGUAGE SUPPORT (TR/EN)
# ============================================================================
TEXTS = {
    "TR": {
        "title": "NASA GÖREV MİMARİ",
        "total_money": "TOPLAM PARA",
        "completed_missions": "TAMAMLANAN GÖREV",
        "esc_hint": "ESC: tam ekran aç/kapa",
        "next_step": "SONRAKİ ADIM >>",
        "skip_tutorial": "EĞİTİMİ ATLA",
        "restart": "YENİDEN BAŞLA",
        "shop": "SHOP",
        "exit": "ÇIKIŞ",
        "return_design": "TASARIMA DÖN",
        "return_lobby": "LOBİYE DÖN (PARA İADE)",
        "launch_flight": "UÇUŞU BAŞLAT (WASD) >>",
        "free_launch": "ÜCRETSİZ UÇUŞ BAŞLAT >>",
        "critical_error": "KRİTİK HATA — FIRLATMA KİLİTLİ",
        "insufficient_funds": "YETERSİZ PARA",
        "locked": "KİLİTLİ",
        "requires": "gerekir",
        "free": "ÜCRETSİZ",
        "budget": "Bütçe",
        "completed": "TAMAMLANDI",
        "owned": "SAHİP",
        "buy": "SATIN AL",
        "mission_cost": "görev maliyeti",
        "tab1": "1. GÖREV & BİLİM",
        "tab2": "2. GÜÇ & KALKAN",
        "tab3": "3. İLETİŞİM",
        "tab4": "4. İTKİ & ROKET",
        "select_mission": "NASA GÖREVİ SEÇİN:",
        "select_instruments": "BİLİM YÜKÜ SEÇİN (çoklu):",
        "power_system": "GÜÇ SİSTEMİ:",
        "bus_shield": "GÖVDE & RADYASYON KALKANI:",
        "dsn_antenna": "DEEP SPACE NETWORK ANTENİ:",
        "distance_attenuation": "Mesafe zayıflaması",
        "data_generation": "Enstrüman veri üretimi",
        "downlink_capacity": "DSN indirme kapasitesi",
        "capture_ratio": "Veri yakalama oranı",
        "thruster": "1. İTKİ MOTORU:",
        "fuel_tank": "2. YAKIT TANKI:",
        "launch_vehicle": "3. FIRLATMA ARACI:",
        "spacecraft_schematic": "UZAY ARACI ŞEMASI",
        "mission_objectives": "GÖREV HEDEFLERİ (3 GEZEGEN):",
        "system_telemetry": "SİSTEM TELEMETRİSİ",
        "cost_vs_budget": "MALİYET vs BÜTÇE",
        "mass_vs_rocket": "KÜTLE vs ROKET",
        "power_vs_load": "GÜÇ ÜRETİM vs YÜK",
        "delta_v_vs_req": "DELTA-V vs GEREKSİNİM",
        "data_transfer": "VERİ AKTARIMI",
        "flight_readiness": "UÇUŞA HAZIRLIK:",
        "all_systems_nominal": "TÜM SİSTEMLER NORMAL",
        "design_science": "Tasarım bilim puanı",
        "launch_cost": "Fırlatma maliyeti",
        "free_paren": "(ÜCRETSİZ)",
        "error": "HATA",
        "tutorial_title": "NASA GÖREV EĞİTİMİ",
        "tutorial_1": "HOŞ GELDİNİZ KOMUTAN!\n\nNASA görevlerini yönetiyorsunuz. İlk görev (Artemis)\nTAMAMEN ÜCRETSİZDİR — hiç paranız bitse bile çalışabilirsiniz.",
        "tutorial_2": "1. TASARIM: Üst sekmelerden parça seçin.\nSağ paneldeki göstergeleri mavi tutun.\nKırmızı varsa fırlatma kilitlidir.",
        "tutorial_3": "2. SHOP: Kazandığınız parayla yeni donanım SATIN ALIN.\nAldığınız parça kalıcı olarak açık kalır.\nShop'ta fare tekerleği ile kaydırın.",
        "tutorial_4": "3. UÇUŞ: [W] itki, [A/D] dönüş, [S] fren, [E] tarama.\nKesikli çizgi en yakın hedefi gösterir.\n3 gezegeni tarayınca görev biter ve para kazanırsınız.\nDİKKAT: Her uçuş için 60 saniye süreniz var!",
        "tutorial_5": "4. DİKKAT: Gezegene sert çarparsanız veya sınıra\nçarparsanız yatırdığınız para YANAR.\nSüre dolarsa görev başarısız sayılır.\n'LOBİYE DÖN' derseniz para iade edilir.",
        "step": "Adım",
        "of": "/",
        "victory_title": "TÜM NASA GÖREVLERİ TAMAMLANDI!",
        "total_missions": "Toplam görev",
        "remaining_budget": "Kalan bütçe",
        "victory_desc": "Ay, Mars, Venüs, Psyche, Europa, Titan ve L2 keşfedildi.",
        "shop_title": "NASA TEDARİK MERKEZİ (SHOP)",
        "shop_hint": "Fare tekerleği / OK TUŞLARI / ▲▼ ile kaydırın — satın alınan parça kalıcı açılır",
        "scroll": "Kaydırma",
        "flight_controls": "[W] itki  [S] fren  [A/D] dönüş  [E] tarama",
        "speed": "HIZ",
        "landing_limit": "iniş limiti",
        "delta_v": "DELTA-V",
        "battery": "BATARYA",
        "target": "HEDEF",
        "score": "PUAN",
        "time": "SÜRE",
        "sector_map": "SEKTÖR HARİTASI",
        "surface_telemetry": "YÜZEY TELEMETRİSİ",
        "task": "GÖREV",
        "completed_lift": "TAMAMLANDI — [W] ile kalkış",
        "hold_e": "[E] basılı tutarak tara",
        "scanning": "TARAMA",
        "launch_complete": "FIRLATMA TAMAM — [W/A/S/D] UÇUŞ, [E] TARAMA",
        "scan_complete": "TARAMA TAMAM",
        "takeoff": "KALKIŞ",
        "landing": "İNİŞ",
        "hard_impact": "SERT ÇARPMA",
        "boundary_hit": "SEKTÖR SINIRINA ÇARPIŞ",
        "time_up": "SÜRE DOLDU",
        "mission_complete": "TAMAMLANDI",
        "repeat_mission": "(tekrar görevi)",
        "crash_report": "KAZA",
        "burned": "yandı",
        "sponsor": "sponsor",
        "refund": "iade edildi",
        "cancel_flight": "Uçuş iptal edildi",
        "target_label": "HEDEF",
    },
    "EN": {
        "title": "NASA MISSION ARCHITECT",
        "total_money": "TOTAL FUNDS",
        "completed_missions": "COMPLETED MISSIONS",
        "esc_hint": "ESC: toggle fullscreen",
        "next_step": "NEXT STEP >>",
        "skip_tutorial": "SKIP TUTORIAL",
        "restart": "RESTART",
        "shop": "SHOP",
        "exit": "EXIT",
        "return_design": "RETURN TO DESIGN",
        "return_lobby": "RETURN TO LOBBY (REFUND)",
        "launch_flight": "LAUNCH FLIGHT (WASD) >>",
        "free_launch": "LAUNCH FREE FLIGHT >>",
        "critical_error": "CRITICAL ERROR — LAUNCH LOCKED",
        "insufficient_funds": "INSUFFICIENT FUNDS",
        "locked": "LOCKED",
        "requires": "required",
        "free": "FREE",
        "budget": "Budget",
        "completed": "COMPLETED",
        "owned": "OWNED",
        "buy": "BUY",
        "mission_cost": "mission cost",
        "tab1": "1. MISSION & SCIENCE",
        "tab2": "2. POWER & SHIELD",
        "tab3": "3. COMMS",
        "tab4": "4. PROPULSION & ROCKET",
        "select_mission": "SELECT NASA MISSION:",
        "select_instruments": "SELECT SCIENCE PAYLOAD (multiple):",
        "power_system": "POWER SYSTEM:",
        "bus_shield": "BUS & RADIATION SHIELD:",
        "dsn_antenna": "DEEP SPACE NETWORK ANTENNA:",
        "distance_attenuation": "Distance attenuation",
        "data_generation": "Instrument data generation",
        "downlink_capacity": "DSN downlink capacity",
        "capture_ratio": "Data capture ratio",
        "thruster": "1. THRUSTER:",
        "fuel_tank": "2. FUEL TANK:",
        "launch_vehicle": "3. LAUNCH VEHICLE:",
        "spacecraft_schematic": "SPACECRAFT SCHEMATIC",
        "mission_objectives": "MISSION OBJECTIVES (3 PLANETS):",
        "system_telemetry": "SYSTEM TELEMETRY",
        "cost_vs_budget": "COST vs BUDGET",
        "mass_vs_rocket": "MASS vs ROCKET",
        "power_vs_load": "POWER GEN vs LOAD",
        "delta_v_vs_req": "DELTA-V vs REQUIREMENT",
        "data_transfer": "DATA TRANSFER",
        "flight_readiness": "FLIGHT READINESS:",
        "all_systems_nominal": "ALL SYSTEMS NOMINAL",
        "design_science": "Design science score",
        "launch_cost": "Launch cost",
        "free_paren": "(FREE)",
        "error": "ERROR",
        "tutorial_title": "NASA MISSION TUTORIAL",
        "tutorial_1": "WELCOME COMMANDER!\n\nYou manage NASA missions. The first mission (Artemis)\nis COMPLETELY FREE — you can play even with zero funds.",
        "tutorial_2": "1. DESIGN: Select parts from top tabs.\nKeep right panel gauges blue.\nRed means launch is locked.",
        "tutorial_3": "2. SHOP: BUY new hardware with earned funds.\nPurchased parts stay unlocked permanently.\nUse mouse wheel to scroll in shop.",
        "tutorial_4": "3. FLIGHT: [W] thrust, [A/D] rotate, [S] brake, [E] scan.\nDashed line shows nearest target.\nScan 3 planets to complete mission and earn funds.\nWARNING: Each flight has a 60-second time limit!",
        "tutorial_5": "4. WARNING: Hard impact on planet or boundary\nBURNS your invested funds.\nTime running out = mission failure.\n'RETURN TO LOBBY' refunds your money.",
        "step": "Step",
        "of": "/",
        "victory_title": "ALL NASA MISSIONS COMPLETED!",
        "total_missions": "Total missions",
        "remaining_budget": "Remaining budget",
        "victory_desc": "Moon, Mars, Venus, Psyche, Europa, Titan and L2 explored.",
        "shop_title": "NASA SUPPLY CENTER (SHOP)",
        "shop_hint": "Mouse wheel / ARROW KEYS / ▲▼ to scroll — purchased parts stay unlocked",
        "scroll": "Scroll",
        "flight_controls": "[W] thrust  [S] brake  [A/D] rotate  [E] scan",
        "speed": "SPEED",
        "landing_limit": "landing limit",
        "delta_v": "DELTA-V",
        "battery": "BATTERY",
        "target": "TARGET",
        "score": "SCORE",
        "time": "TIME",
        "sector_map": "SECTOR MAP",
        "surface_telemetry": "SURFACE TELEMETRY",
        "task": "TASK",
        "completed_lift": "COMPLETED — [W] to lift off",
        "hold_e": "Hold [E] to scan",
        "scanning": "SCANNING",
        "launch_complete": "LAUNCH COMPLETE — [W/A/S/D] FLY, [E] SCAN",
        "scan_complete": "SCAN COMPLETE",
        "takeoff": "TAKEOFF",
        "landing": "LANDING",
        "hard_impact": "HARD IMPACT",
        "boundary_hit": "HIT SECTOR BOUNDARY",
        "time_up": "TIME'S UP",
        "mission_complete": "COMPLETED",
        "repeat_mission": "(repeat mission)",
        "crash_report": "CRASH",
        "burned": "burned",
        "sponsor": "sponsor",
        "refund": "refunded",
        "cancel_flight": "Flight cancelled",
        "target_label": "TARGET",
    }
}

# ============================================================================
# NASA MISSIONS
# ============================================================================
NASA_MISSIONS = [
    {
        "name": "Artemis CLPS: Lunar South Pole",
        "short": "Artemis CLPS (Ay)",
        "short_en": "Artemis CLPS (Moon)",
        "budget": 240, "req_dv": 850, "solar_flux": 1.00, "dist_factor": 1.8,
        "rad_hazard": 0.25, "min_life": 2, "base_sci": 180, "gravity": 18.0,
        "unlock_cost": 0, "free": True,
        "desc": "Shackleton Krateri'ndeki su-buzu uçucularını haritalayın.",
        "desc_en": "Map water-ice volatiles in Shackleton Crater.",
        "bodies": [
            {"name": "Gateway Staging Node", "x": 1250, "y": 1750, "r": 46, "color": (130, 165, 220), "task": "Derin Uzay Atomik Saat Kalibrasyonu", "task_en": "Deep Space Atomic Clock Calibration"},
            {"name": "Shackleton Crater Rim", "x": 2950, "y": 700, "r": 98, "color": (200, 210, 225), "task": "Su Buzu Çekirdek Sondajı", "task_en": "Water Ice Core Drilling"},
            {"name": "Malapert Massif Peak", "x": 4550, "y": 1900, "r": 80, "color": (175, 188, 205), "task": "Lazer Retroreflektör Yerleşimi", "task_en": "Laser Retroreflector Deployment"},
        ],
    },
    {
        "name": "Psyche: Metal Asteroid Explorer",
        "short": "Psyche (Metal Asteroit)",
        "short_en": "Psyche (Metal Asteroid)",
        "budget": 320, "req_dv": 1400, "solar_flux": 0.75, "dist_factor": 3.2,
        "rad_hazard": 0.30, "min_life": 3, "base_sci": 240, "gravity": 20.0,
        "unlock_cost": 300, "free": False,
        "desc": "16 Psyche'nin demir-nikel çekirdeğini araştırın.",
        "desc_en": "Explore 16 Psyche's iron-nickel core.",
        "bodies": [
            {"name": "Mars Flyby", "x": 1300, "y": 800, "r": 58, "color": (185, 95, 65), "task": "Yerçekimi Yardımı Manevrası", "task_en": "Gravity Assist Maneuver"},
            {"name": "Psyche Surface Alpha", "x": 3000, "y": 1900, "r": 90, "color": (165, 155, 140), "task": "Manyetometre Taraması", "task_en": "Magnetometer Survey"},
            {"name": "Psyche Crater Beta", "x": 4600, "y": 750, "r": 76, "color": (145, 135, 125), "task": "Nikel-Demir Örneklemesi", "task_en": "Nickel-Iron Sampling"},
        ],
    },
    {
        "name": "Mars Sample Return: Jezero Delta",
        "short": "Mars Sample Return",
        "short_en": "Mars Sample Return",
        "budget": 440, "req_dv": 1950, "solar_flux": 0.43, "dist_factor": 7.5,
        "rad_hazard": 0.45, "min_life": 4, "base_sci": 340, "gravity": 28.0,
        "unlock_cost": 600, "free": False,
        "desc": "Jezero Krateri'ndeki Perseverance örneklerini toplayın.",
        "desc_en": "Collect Perseverance samples in Jezero Crater.",
        "bodies": [
            {"name": "Phobos Staging Orbit", "x": 1200, "y": 1650, "r": 54, "color": (145, 135, 130), "task": "Yerçekimi Araştırması", "task_en": "Gravity Survey"},
            {"name": "Jezero River Delta", "x": 2900, "y": 650, "r": 115, "color": (185, 95, 65), "task": "Örnek Tüplerini Topla", "task_en": "Collect Sample Tubes"},
            {"name": "Nili Fossae Trough", "x": 4650, "y": 1850, "r": 88, "color": (165, 80, 55), "task": "Metan Plumesi Örneklemesi", "task_en": "Methane Plume Sampling"},
        ],
    },
    {
        "name": "DAVINCI: Venus Atmosphere Probe",
        "short": "DAVINCI (Venüs)",
        "short_en": "DAVINCI (Venus)",
        "budget": 540, "req_dv": 2400, "solar_flux": 0.65, "dist_factor": 5.8,
        "rad_hazard": 0.55, "min_life": 2, "base_sci": 420, "gravity": 32.0,
        "unlock_cost": 1000, "free": False,
        "desc": "Venüs'ün yoğun atmosferinden geçerek basıncı ölçün.",
        "desc_en": "Probe Venus's dense atmosphere.",
        "bodies": [
            {"name": "Venus Orbit Insertion", "x": 1350, "y": 750, "r": 62, "color": (220, 180, 90), "task": "Atmosfer Yoğunluk Profili", "task_en": "Atmosphere Density Profile"},
            {"name": "Aphrodite Terra", "x": 3050, "y": 1900, "r": 105, "color": (200, 160, 80), "task": "Yüzey Basınç & Sıcaklık", "task_en": "Surface Pressure & Temperature"},
            {"name": "Ishtar Terra Maxwell", "x": 4600, "y": 800, "r": 92, "color": (180, 140, 70), "task": "Volkanik Gaz Örneklemesi", "task_en": "Volcanic Gas Sampling"},
        ],
    },
    {
        "name": "Europa Clipper: Jovian Ocean World",
        "short": "Europa Clipper",
        "short_en": "Europa Clipper",
        "budget": 700, "req_dv": 3100, "solar_flux": 0.04, "dist_factor": 24.0,
        "rad_hazard": 0.85, "min_life": 6, "base_sci": 580, "gravity": 22.0,
        "unlock_cost": 1500, "free": False,
        "desc": "Europa'nın yüzey altı tuzlu su okyanusunu araştırın.",
        "desc_en": "Explore Europa's subsurface saltwater ocean.",
        "bodies": [
            {"name": "Callisto Gravity Assist", "x": 1250, "y": 1900, "r": 82, "color": (110, 125, 145), "task": "Manyetometre Kalibrasyonu", "task_en": "Magnetometer Calibration"},
            {"name": "Conamara Chaos", "x": 2950, "y": 700, "r": 105, "color": (175, 220, 255), "task": "Buz Penetrasyon Radarı", "task_en": "Ice Penetrating Radar"},
            {"name": "Pwyll Cryo-Plume", "x": 4650, "y": 1950, "r": 94, "color": (200, 235, 255), "task": "Kriyo-Plume Geçişi", "task_en": "Cryo-Plume Flythrough"},
        ],
    },
    {
        "name": "LUVOIR: Exoplanet Hunter Telescope",
        "short": "LUVOIR (L2 Teleskop)",
        "short_en": "LUVOIR (L2 Telescope)",
        "budget": 820, "req_dv": 2800, "solar_flux": 0.90, "dist_factor": 1.2,
        "rad_hazard": 0.15, "min_life": 10, "base_sci": 720, "gravity": 12.0,
        "unlock_cost": 2100, "free": False,
        "desc": "L2 noktasından ötegezegen atmosferlerini inceleyin.",
        "desc_en": "Study exoplanet atmospheres from L2 point.",
        "bodies": [
            {"name": "L2 Halo Orbit", "x": 1300, "y": 800, "r": 50, "color": (100, 140, 200), "task": "Teleskop Kalibrasyonu", "task_en": "Telescope Calibration"},
            {"name": "TRAPPIST-1e Analog", "x": 3000, "y": 1850, "r": 96, "color": (140, 180, 220), "task": "Atmosfer Spektroskopisi", "task_en": "Atmosphere Spectroscopy"},
            {"name": "Proxima Centauri b", "x": 4600, "y": 750, "r": 86, "color": (160, 200, 240), "task": "Biyosignatür Araması", "task_en": "Biosignature Search"},
        ],
    },
    {
        "name": "Dragonfly: Titan Prebiotic Explorer",
        "short": "Dragonfly (Titan)",
        "short_en": "Dragonfly (Titan)",
        "budget": 820, "req_dv": 3500, "solar_flux": 0.01, "dist_factor": 32.0,
        "rad_hazard": 0.60, "min_life": 8, "base_sci": 750, "gravity": 16.0,
        "unlock_cost": 2700, "free": False,
        "desc": "Titan'ın organik kum tepelerini ve kraterlerini keşfedin.",
        "desc_en": "Explore Titan's organic dunes and craters.",
        "bodies": [
            {"name": "Shangri-La Dunes", "x": 1250, "y": 1800, "r": 95, "color": (210, 155, 75), "task": "Hidrokarbon Kimyası", "task_en": "Hydrocarbon Chemistry"},
            {"name": "Kraken Mare Shore", "x": 2950, "y": 700, "r": 110, "color": (70, 130, 175), "task": "Sıvı Metan Analizi", "task_en": "Liquid Methane Analysis"},
            {"name": "Selk Crater Floor", "x": 4650, "y": 1900, "r": 92, "color": (185, 140, 90), "task": "Buz/Organik Sondaj", "task_en": "Ice/Organic Drilling"},
        ],
    },
]

# ============================================================================
# HARDWARE
# ============================================================================
INSTRUMENTS = [
    {"name": "HiRISE-II Multispectral Imager", "cost": 35, "mass": 45, "power": 50, "data": 40, "sci": 100, "unlock_cost": 0},
    {"name": "SHERLOC UV Raman Spectrometer", "cost": 30, "mass": 28, "power": 35, "data": 15, "sci": 95, "unlock_cost": 0},
    {"name": "JPL Fluxgate Magnetometer", "cost": 18, "mass": 14, "power": 12, "data": 8, "sci": 60, "unlock_cost": 0},
    {"name": "GEDI-Space Laser Altimeter", "cost": 38, "mass": 50, "power": 70, "data": 24, "sci": 110, "unlock_cost": 200},
    {"name": "MASPEX Quadrupole Mass Spec", "cost": 44, "mass": 38, "power": 48, "data": 18, "sci": 125, "unlock_cost": 350},
    {"name": "REASON Ice-Penetrating Radar", "cost": 52, "mass": 70, "power": 110, "data": 30, "sci": 145, "unlock_cost": 500},
    {"name": "PIXL X-Ray Lithochemistry", "cost": 34, "mass": 32, "power": 42, "data": 20, "sci": 105, "unlock_cost": 280},
    {"name": "EIS Wide-Angle Plasma Camera", "cost": 28, "mass": 22, "power": 28, "data": 26, "sci": 88, "unlock_cost": 160},
]

POWER_SYSTEMS = [
    {"name": "ROSA Roll-Out Solar Array", "cost": 22, "mass": 35, "base_watts": 320, "solar_dep": True, "unlock_cost": 0},
    {"name": "Deep-Space Quad Solar Wings", "cost": 54, "mass": 92, "base_watts": 850, "solar_dep": True, "unlock_cost": 0},
    {"name": "eMMRTG Radioisotope Unit", "cost": 85, "mass": 56, "base_watts": 220, "solar_dep": False, "unlock_cost": 450},
    {"name": "Dual eMMRTG + Kilopower Core", "cost": 155, "mass": 115, "base_watts": 460, "solar_dep": False, "unlock_cost": 800},
    {"name": "Triple Kilopower Fission Pack", "cost": 210, "mass": 165, "base_watts": 720, "solar_dep": False, "unlock_cost": 1250},
]

BUS_CHASSIS = [
    {"name": "SmallSat Explorer Bus", "cost": 30, "mass": 135, "base_pwr": 40, "shield": 0.25, "max_life": 3, "unlock_cost": 0},
    {"name": "JPL Mariner-Class Bus", "cost": 60, "mass": 245, "base_pwr": 65, "shield": 0.55, "max_life": 6, "unlock_cost": 0},
    {"name": "JPL Titanium Radiation Vault", "cost": 120, "mass": 400, "base_pwr": 85, "shield": 0.92, "max_life": 10, "unlock_cost": 700},
    {"name": "Orion Heritage Pressure Bus", "cost": 95, "mass": 320, "base_pwr": 72, "shield": 0.78, "max_life": 12, "unlock_cost": 520},
]

COMMS_SYSTEMS = [
    {"name": "DSN S-Band Low-Gain Omni", "cost": 15, "mass": 12, "power": 20, "base_rate": 50, "unlock_cost": 0},
    {"name": "DSN X-Band 1.8m Dish", "cost": 36, "mass": 34, "power": 45, "base_rate": 240, "unlock_cost": 0},
    {"name": "DSN Ka-Band 3.0m Dish", "cost": 72, "mass": 62, "power": 88, "base_rate": 780, "unlock_cost": 400},
    {"name": "DSOC Deep Space Optical Laser", "cost": 110, "mass": 46, "power": 115, "base_rate": 1950, "unlock_cost": 650},
    {"name": "Psyche Laser Array (DSOC-II)", "cost": 140, "mass": 52, "power": 130, "base_rate": 3200, "unlock_cost": 980},
]

PROPULSION_SYSTEMS = [
    {"name": "Aerojet Hydrazine Monoprop", "cost": 18, "dry_mass": 25, "isp": 260, "pwr": 10, "unlock_cost": 0},
    {"name": "R-4D Hypergolic Biprop", "cost": 42, "dry_mass": 58, "isp": 325, "pwr": 20, "unlock_cost": 0},
    {"name": "NASA NEXT-C Xenon Ion", "cost": 88, "dry_mass": 84, "isp": 1750, "pwr": 95, "unlock_cost": 550},
    {"name": "HERMeS Hall-Effect Cluster", "cost": 120, "dry_mass": 96, "isp": 2400, "pwr": 140, "unlock_cost": 1100},
    {"name": "VASIMR VX-200 Plasma", "cost": 175, "dry_mass": 120, "isp": 3600, "pwr": 210, "unlock_cost": 1600},
]

FUEL_TANKS = [
    {"name": "120 kg Propellant Tank", "fuel_mass": 120, "tank_cost": 10, "unlock_cost": 0},
    {"name": "320 kg Propellant Tank", "fuel_mass": 320, "tank_cost": 20, "unlock_cost": 0},
    {"name": "700 kg Propellant Tank", "fuel_mass": 700, "tank_cost": 38, "unlock_cost": 350},
    {"name": "1,300 kg Propellant Tank", "fuel_mass": 1300, "tank_cost": 65, "unlock_cost": 600},
    {"name": "2,200 kg Cryo Depot Tank", "fuel_mass": 2200, "tank_cost": 95, "unlock_cost": 1050},
]

LAUNCH_VEHICLES = [
    {"name": "Falcon 9 Block 5", "cost": 62, "max_mass": 750, "unlock_cost": 0},
    {"name": "Vulcan Centaur VC4", "cost": 115, "max_mass": 1650, "unlock_cost": 0},
    {"name": "Falcon Heavy Expendable", "cost": 190, "max_mass": 3200, "unlock_cost": 500},
    {"name": "SLS Block 1B Cargo", "cost": 310, "max_mass": 6500, "unlock_cost": 900},
    {"name": "Starship Cargo (Super Heavy)", "cost": 240, "max_mass": 9000, "unlock_cost": 1400},
]

SHOP_CATEGORIES = [
    ("instruments", "BİLİM ENSTRÜMANLARI", "SCIENCE INSTRUMENTS", INSTRUMENTS),
    ("power", "GÜÇ SİSTEMLERİ", "POWER SYSTEMS", POWER_SYSTEMS),
    ("bus", "GÖVDE & RADYASYON KALKANI", "BUS & RADIATION SHIELD", BUS_CHASSIS),
    ("comms", "İLETİŞİM (DEEP SPACE NETWORK)", "COMMS (DEEP SPACE NETWORK)", COMMS_SYSTEMS),
    ("propulsion", "İTKİ SİSTEMLERİ", "PROPULSION SYSTEMS", PROPULSION_SYSTEMS),
    ("fuel", "YAKIT TANKLARI", "FUEL TANKS", FUEL_TANKS),
    ("launch", "FIRLATMA ARAÇLARI", "LAUNCH VEHICLES", LAUNCH_VEHICLES),
]


def item_stat_line(cat, it, lang):
    if cat == "instruments":
        sci_txt = "Bilim" if lang == "TR" else "Science"
        return f"{it['mass']}kg | {it['power']}W | {it['data']}Mbps | {sci_txt} {it['sci']}"
    if cat == "power":
        if lang == "TR":
            kind = "Güneş" if it["solar_dep"] else "Nükleer"
        else:
            kind = "Solar" if it["solar_dep"] else "Nuclear"
        return f"{it['mass']}kg | {it['base_watts']}W | {kind}"
    if cat == "bus":
        if lang == "TR":
            shield_txt, life_txt, year_txt = "Kalkan", "Ömür", "yıl"
        else:
            shield_txt, life_txt, year_txt = "Shield", "Life", "yrs"
        return f"{it['mass']}kg | {shield_txt} %{int(it['shield']*100)} | {life_txt} {it['max_life']}{year_txt}"
    if cat == "comms":
        return f"{it['mass']}kg | {it['power']}W | {it['base_rate']}Mbps"
    if cat == "propulsion":
        return f"Isp {it['isp']}s | {it['dry_mass']}kg | {it['pwr']}W"
    if cat == "fuel":
        fuel_txt = "yakıt" if lang == "TR" else "fuel"
        return f"{it['fuel_mass']}kg {fuel_txt}"
    return f"Max {it['max_mass']}kg"


def item_use_cost(cat, it):
    return it.get("cost", it.get("tank_cost", 0))


# ============================================================================
# MISSION DESIGN & PHYSICS
# ============================================================================
class MissionDesign:
    def __init__(self):
        self.active_tab = 0
        self.mission_idx = 0
        self.selected_inst = {0, 1}
        self.power_idx = 0
        self.bus_idx = 0
        self.comms_idx = 0
        self.prop_idx = 0
        self.fuel_idx = 0
        self.lv_idx = 0

    def compute_telemetry(self):
        m = NASA_MISSIONS[self.mission_idx]
        pwr = POWER_SYSTEMS[self.power_idx]
        bus = BUS_CHASSIS[self.bus_idx]
        com = COMMS_SYSTEMS[self.comms_idx]
        prp = PROPULSION_SYSTEMS[self.prop_idx]
        fl = FUEL_TANKS[self.fuel_idx]
        lv = LAUNCH_VEHICLES[self.lv_idx]

        inst_cost = sum(INSTRUMENTS[i]["cost"] for i in self.selected_inst)
        inst_mass = sum(INSTRUMENTS[i]["mass"] for i in self.selected_inst)
        inst_pwr = sum(INSTRUMENTS[i]["power"] for i in self.selected_inst)
        inst_data = sum(INSTRUMENTS[i]["data"] for i in self.selected_inst)
        inst_sci = sum(INSTRUMENTS[i]["sci"] for i in self.selected_inst)

        total_cost = inst_cost + pwr["cost"] + bus["cost"] + com["cost"] + prp["cost"] + fl["tank_cost"] + lv["cost"]
        dry_mass = inst_mass + pwr["mass"] + bus["mass"] + com["mass"] + prp["dry_mass"] + int(fl["fuel_mass"] * 0.1)
        wet_mass = dry_mass + fl["fuel_mass"]

        gen_power = int(pwr["base_watts"] * m["solar_flux"]) if pwr["solar_dep"] else pwr["base_watts"]
        req_power = bus["base_pwr"] + com["power"] + prp["pwr"] + inst_pwr

        g0 = 9.80665
        achieved_dv = int(prp["isp"] * g0 * math.log(wet_mass / max(1, dry_mass)))

        downlink = round(com["base_rate"] / m["dist_factor"], 1)
        data_eff = 1.0 if inst_data == 0 else min(1.0, downlink / max(1.0, inst_data))

        rad_gap = max(0.0, m["rad_hazard"] - bus["shield"])
        life_gap = max(0, m["min_life"] - bus["max_life"])
        reliability = max(0.10, 0.98 - rad_gap * 0.65 - life_gap * 0.07)

        issues = []
        if total_cost > m["budget"]:
            issues.append(f"BÜTÇE AŞIMI: ${total_cost}M > ${m['budget']}M")
        if wet_mass > lv["max_mass"]:
            issues.append(f"KÜTLE AŞIMI: {wet_mass}kg > {lv['max_mass']}kg")
        if gen_power < req_power:
            issues.append(f"GÜÇ AÇIĞI: {gen_power}W < {req_power}W")
        if achieved_dv < m["req_dv"]:
            issues.append(f"DELTA-V AÇIĞI: {achieved_dv} < {m['req_dv']} m/s")
        if not self.selected_inst:
            issues.append("BİLİM YÜKÜ YOK: en az 1 enstrüman seçin")

        design_sci = int((m["base_sci"] + inst_sci) * data_eff * reliability)

        return {
            "total_cost": total_cost, "budget": m["budget"], "dry_mass": dry_mass, "wet_mass": wet_mass,
            "max_mass": lv["max_mass"], "gen_power": gen_power, "req_power": req_power,
            "achieved_dv": achieved_dv, "req_dv": m["req_dv"], "inst_data": inst_data,
            "downlink": downlink, "data_eff": data_eff, "reliability": int(reliability * 100),
            "issues": issues, "design_sci": design_sci,
        }


# ============================================================================
# INTERACTIVE FLIGHT
# ============================================================================
class InteractiveFlightSession:
    def __init__(self, mission_state, telemetry):
        self.ms = mission_state
        self.tele = telemetry
        self.mission_data = NASA_MISSIONS[mission_state.mission_idx]
        self.world_w = 5200
        self.world_h = 2600
        self.completed_tasks = set()
        self.flight_score_bonus = 0
        self.crashed = False
        self.crash_reason = ""
        self.x = 420.0
        self.y = 1300.0
        self.vx = 0.0
        self.vy = 0.0
        self.angle = 0.0
        self.dv_remaining = float(telemetry["achieved_dv"])
        self.battery_pct = 100.0
        self.landed_body = None
        self.scan_progress = 0.0
        self.status_banner = "FIRLATMA TAMAM — [W/A/S/D] UÇUŞ, [E] TARAMA"
        self.banner_timer = 200
        self.flight_timer = 60.0
        rnd = random.Random(1958)
        self.stars = [(rnd.randint(20, self.world_w - 20), rnd.randint(20, self.world_h - 20), rnd.choice([1, 1, 2])) for _ in range(700)]

    def nearest_target(self):
        best, best_d = None, 1e18
        for b in self.mission_data["bodies"]:
            if b["name"] in self.completed_tasks:
                continue
            d = math.hypot(b["x"] - self.x, b["y"] - self.y)
            if d < best_d:
                best, best_d = b, d
        return best, best_d

    def update(self, keys, dt):
        if self.crashed:
            return
        
        # YENİ: Süre sayacı - her frame'de azalt
        self.flight_timer -= dt
        if self.flight_timer <= 0:
            self.flight_timer = 0
            self.crashed = True
            self.crash_reason = "SÜRE DOLDU"
            return
        
        if self.banner_timer > 0:
            self.banner_timer -= 1
        margin_ratio = self.tele["gen_power"] / max(1, self.tele["req_power"])

        if self.landed_body is not None:
            if keys[pygame.K_e] or keys[pygame.K_SPACE]:
                if self.landed_body["name"] not in self.completed_tasks and self.battery_pct > 2.0:
                    self.scan_progress += dt * 18.0 * min(1.3, max(0.4, margin_ratio))
                    self.battery_pct = max(0.0, self.battery_pct - dt * 3.0)
                    if self.scan_progress >= 100.0:
                        self.scan_progress = 100.0
                        self.completed_tasks.add(self.landed_body["name"])
                        self.flight_score_bonus += 75
                        self.status_banner = f"TARAMA TAMAM: {self.landed_body['name'].upper()} — [W] KALKIŞ"
                        self.banner_timer = 220
            else:
                self.battery_pct = min(100.0, self.battery_pct + 6.0 * dt * max(0.4, margin_ratio))
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                nx = (self.x - self.landed_body["x"]) / max(1.0, self.landed_body["r"])
                ny = (self.y - self.landed_body["y"]) / max(1.0, self.landed_body["r"])
                self.x += nx * 16.0
                self.y += ny * 16.0
                self.vx, self.vy = nx * 50.0, ny * 50.0
                self.angle = math.atan2(ny, nx)
                self.landed_body = None
                self.scan_progress = 0.0
                self.status_banner = "KALKIŞ ONAYLANDI — SONRAKİ HEDEFE GİDİN"
                self.banner_timer = 140
            return

        rot = 2.6
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.angle -= rot * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.angle += rot * dt

        thrusting = False
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.dv_remaining > 0:
            self.vx += math.cos(self.angle) * 130.0 * dt
            self.vy += math.sin(self.angle) * 130.0 * dt
            self.dv_remaining = max(0.0, self.dv_remaining - 14.0 * dt)
            self.battery_pct = max(0.0, self.battery_pct - 1.5 * dt)
            thrusting = True
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.dv_remaining > 0:
            damp = max(0.0, 1.0 - 2.4 * dt)
            self.vx *= damp
            self.vy *= damp
            self.dv_remaining = max(0.0, self.dv_remaining - 9.0 * dt)
            thrusting = True
        if not thrusting:
            self.battery_pct = min(100.0, self.battery_pct + 6.0 * dt * max(0.4, margin_ratio))

        for body in self.mission_data["bodies"]:
            dx, dy = body["x"] - self.x, body["y"] - self.y
            dist = math.hypot(dx, dy)
            if dist < body["r"] * 3.2 and dist > 1.0:
                g = (self.mission_data["gravity"] * body["r"]) / max(60.0, dist)
                self.vx += (dx / dist) * g * dt
                self.vy += (dy / dist) * g * dt
            if dist <= body["r"] + 12:
                speed = math.hypot(self.vx, self.vy)
                if speed <= 95.0:
                    nx = (self.x - body["x"]) / max(1.0, dist)
                    ny = (self.y - body["y"]) / max(1.0, dist)
                    self.x = body["x"] + nx * (body["r"] + 12)
                    self.y = body["y"] + ny * (body["r"] + 12)
                    self.vx = self.vy = 0.0
                    self.angle = math.atan2(ny, nx)
                    self.landed_body = body
                    self.scan_progress = 100.0 if body["name"] in self.completed_tasks else 0.0
                    self.status_banner = f"İNİŞ: {body['name'].upper()} ({int(speed)} m/s) — [E] TARA"
                    self.banner_timer = 200
                else:
                    self.crashed = True
                    self.crash_reason = f"SERT ÇARPMA: {body['name']} ({int(speed)} m/s > 95 m/s)"
                return

        self.x += self.vx * dt
        self.y += self.vy * dt
        m = 28
        if self.x < m or self.x > self.world_w - m or self.y < m or self.y > self.world_h - m:
            self.crashed = True
            self.crash_reason = "SEKTÖR SINIRINA ÇARPIŞ"


# ============================================================================
# UI HELPERS
# ============================================================================
class Button:
    def __init__(self, rect, text, callback, selected=False, style="default", disabled=False, sub=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.selected = selected
        self.style = style
        self.disabled = disabled
        self.sub = sub

    def draw(self, surf, font, mouse_pos, subfont=None):
        hovered = self.rect.collidepoint(mouse_pos) and not self.disabled
        if self.disabled:
            bg, fg, border = (26, 28, 34), MUTED_GRAY, (55, 60, 70)
        elif self.style == "primary":
            bg = NASA_BLUE if (hovered or self.selected) else NASA_NAVY
            border = WHITE if (hovered or self.selected) else NASA_BLUE
            fg = WHITE
        elif self.style == "alert":
            bg = ALERT_RED if hovered else (120, 20, 30)
            border = WHITE if hovered else ALERT_RED
            fg = WHITE
        elif self.style == "shop":
            bg = (20, 90, 45) if not hovered else (30, 130, 65)
            border = OK_GREEN
            fg = WHITE
        elif self.style == "owned":
            bg, fg, border = (14, 40, 30), OK_GREEN, (30, 110, 70)
        elif self.style == "lang":
            bg = GOLD if (hovered or self.selected) else (180, 140, 30)
            border = WHITE if (hovered or self.selected) else GOLD
            fg = BLACK
        else:
            bg = NASA_NAVY if self.selected else ((22, 42, 78) if hovered else PANEL_BLACK)
            border = WHITE if self.selected else (NASA_BLUE if hovered else BORDER_BLUE)
            fg = WHITE if (self.selected or hovered) else MUTED_GRAY
        pygame.draw.rect(surf, bg, self.rect)
        pygame.draw.rect(surf, border, self.rect, 2 if self.selected else 1)
        if self.sub and subfont:
            t = font.render(self.text, True, fg)
            surf.blit(t, (self.rect.x + 12, self.rect.y + 5))
            s = subfont.render(self.sub, True, MUTED_GRAY)
            surf.blit(s, (self.rect.x + 12, self.rect.y + 22))
        else:
            t = font.render(self.text, True, fg)
            surf.blit(t, (self.rect.centerx - t.get_width() // 2, self.rect.centery - t.get_height() // 2))


def draw_telemetry_bar(surf, x, y, w, h, label, value_text, ratio, must_exceed=False, font=None):
    pygame.draw.rect(surf, BLACK, (x, y, w, h))
    clamped = max(0.0, min(1.0, ratio))
    healthy = ratio >= 1.0 if must_exceed else ratio <= 1.0
    fill_w = int((w - 4) * clamped)
    if fill_w > 0:
        pygame.draw.rect(surf, NASA_BLUE if healthy else ALERT_RED, (x + 2, y + 2, fill_w, h - 4))
    pygame.draw.rect(surf, BORDER_BLUE if healthy else ALERT_RED, (x, y, w, h), 1)
    surf.blit(font.render(label, True, MUTED_GRAY), (x, y - 17))
    v = font.render(value_text, True, WHITE if healthy else ALERT_RED)
    surf.blit(v, (x + w - v.get_width(), y - 17))


def draw_blueprint(surf, rect, ms):
    pygame.draw.rect(surf, BLACK, rect)
    for gx in range(rect.x + 20, rect.right, 25):
        pygame.draw.line(surf, (10, 22, 45), (gx, rect.y), (gx, rect.bottom), 1)
    for gy in range(rect.y + 20, rect.bottom, 25):
        pygame.draw.line(surf, (10, 22, 45), (rect.x, gy), (rect.right, gy), 1)
    pygame.draw.rect(surf, BORDER_BLUE, rect, 1)
    cx, cy = rect.centerx, rect.centery + 8
    if ms.power_idx in (0, 1):
        span = 80 if ms.power_idx == 0 else 130
        for side in (-1, 1):
            px = cx + 38 if side > 0 else cx - 38 - span
            pr = pygame.Rect(px, cy - 20, span, 40)
            pygame.draw.rect(surf, NASA_NAVY, pr)
            pygame.draw.rect(surf, NASA_BLUE, pr, 2)
            for c in range(1, 5):
                lx = px + (span * c) // 5
                pygame.draw.line(surf, LIGHT_BLUE, (lx, cy - 20), (lx, cy + 20), 1)
    else:
        for side in (-1, 1):
            rr = pygame.Rect(cx + side * 56 - 16, cy - 14, 32, 28)
            pygame.draw.rect(surf, (25, 55, 105), rr)
            pygame.draw.rect(surf, WHITE, rr, 2)
    tr = 15 + ms.fuel_idx * 4
    pygame.draw.circle(surf, NASA_NAVY, (cx, cy + 36), tr)
    pygame.draw.circle(surf, LIGHT_BLUE, (cx, cy + 36), tr, 1)
    noz = [(cx - 10, cy + 42 + tr // 2), (cx + 10, cy + 42 + tr // 2), (cx + 17, cy + 58 + tr // 2), (cx - 17, cy + 58 + tr // 2)]
    pygame.draw.polygon(surf, BLACK, noz)
    pygame.draw.polygon(surf, WHITE, noz, 2)
    bw = 62 + ms.bus_idx * 8
    br = pygame.Rect(cx - bw // 2, cy - 28, bw, 56)
    pygame.draw.rect(surf, PANEL_BLACK, br)
    pygame.draw.rect(surf, WHITE, br, 2)
    dr = 16 + ms.comms_idx * 6
    pygame.draw.arc(surf, WHITE, (cx - dr, cy - 28 - dr - 6, dr * 2, dr * 2), math.pi, 2 * math.pi, 2)
    pygame.draw.line(surf, NASA_BLUE, (cx, cy - 28), (cx, cy - 28 - dr - 4), 2)
    offs = [(-16, -12), (16, -12), (-16, 9), (16, 9), (0, -3), (0, 14), (-8, 18), (8, -18)]
    for i in ms.selected_inst:
        ox, oy = offs[i % len(offs)]
        pygame.draw.rect(surf, NASA_BLUE, (cx + ox - 4, cy + oy - 4, 8, 8))
        pygame.draw.rect(surf, WHITE, (cx + ox - 4, cy + oy - 4, 8, 8), 1)


def dashed_line(surf, color, start, end, dash=14, gap=10, width=2):
    x1, y1 = start
    x2, y2 = end
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    if dist < 1:
        return
    ux, uy = dx / dist, dy / dist
    pos = 0.0
    while pos < dist:
        seg = min(dash, dist - pos)
        a = (x1 + ux * pos, y1 + uy * pos)
        b = (x1 + ux * (pos + seg), y1 + uy * (pos + seg))
        pygame.draw.line(surf, color, a, b, width)
        pos += dash + gap


# ============================================================================
# MAIN GAME
# ============================================================================
class NASASpaceAppsGame:
    def __init__(self):
        pygame.init()
        self.fullscreen = True
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.FULLSCREEN)
        pygame.display.set_caption("NASA MISSION ARCHITECT & FLIGHT SIMULATOR")
        self.clock = pygame.time.Clock()
        self.font_xs = pygame.font.SysFont("arial", 13)
        self.font_sm = pygame.font.SysFont("arial", 14, bold=True)
        self.font_md = pygame.font.SysFont("arial", 17, bold=True)
        self.font_lg = pygame.font.SysFont("arial", 22, bold=True)

        self.ms = MissionDesign()
        self.mode = "TUTORIAL"
        self.flight = None
        self.buttons = []
        self.shop_buttons = []

        self.company_funds = 350
        self.unlocked_missions = {0}
        self.completed_missions = set()
        self.launch_paid = 0
        self.last_report = ""

        self.owned_items = {
            "instruments": {0, 1, 2},
            "power": {0, 1},
            "bus": {0, 1},
            "comms": {0, 1},
            "propulsion": {0, 1},
            "fuel": {0, 1},
            "launch": {0, 1},
        }

        self.language = "TR"

        self.shop_scroll = 0.0
        self.shop_target = 0.0
        self.shop_content_h = 1
        self.shop_view = pygame.Rect(30, 150, SCREEN_W - 60, SCREEN_H - 205)
        self.shop_entries = []

        self.tutorial_step = 0

    def T(self, key):
        return TEXTS[self.language].get(key, key)

    def mission_short(self, m):
        return m["short_en"] if self.language == "EN" else m["short"]

    def mission_desc(self, m):
        return m["desc_en"] if self.language == "EN" else m["desc"]

    def body_task(self, b):
        return b["task_en"] if self.language == "EN" else b["task"]

    def sanitize_owned(self):
        self.ms.selected_inst = {i for i in self.ms.selected_inst if i in self.owned_items["instruments"]}
        for attr, cat, table in (
            ("power_idx", "power", POWER_SYSTEMS), ("bus_idx", "bus", BUS_CHASSIS),
            ("comms_idx", "comms", COMMS_SYSTEMS), ("prop_idx", "propulsion", PROPULSION_SYSTEMS),
            ("fuel_idx", "fuel", FUEL_TANKS), ("lv_idx", "launch", LAUNCH_VEHICLES),
        ):
            cur = getattr(self.ms, attr)
            if cur not in self.owned_items[cat]:
                setattr(self.ms, attr, min(self.owned_items[cat]))

    def build_buttons(self):
        self.buttons.clear()
        self.shop_buttons.clear()

        if self.mode == "TUTORIAL":
            lang_text = "EN" if self.language == "TR" else "TR"
            self.buttons.append(Button((18, 10, 45, 32), lang_text, self.toggle_language, style="lang"))
            self.buttons.append(Button((SCREEN_W // 2 - 110, SCREEN_H - 118, 220, 40), self.T("next_step"), self.next_tutorial, style="primary"))
            self.buttons.append(Button((SCREEN_W // 2 - 110, SCREEN_H - 70, 220, 38), self.T("skip_tutorial"), self.skip_tutorial, style="alert"))
            return

        if self.mode == "VICTORY":
            lang_text = "EN" if self.language == "TR" else "TR"
            self.buttons.append(Button((18, 10, 45, 32), lang_text, self.toggle_language, style="lang"))
            self.buttons.append(Button((SCREEN_W // 2 - 110, SCREEN_H // 2 + 110, 220, 48), self.T("restart"), self.restart_game, style="primary"))
            return

        if self.mode == "FLIGHT":
            self.buttons.append(Button((SCREEN_W - 250, 13, 235, 36), self.T("return_lobby"), self.return_to_lobby_refund, style="primary"))
            return

        if self.mode == "SHOP":
            lang_text = "EN" if self.language == "TR" else "TR"
            self.buttons.append(Button((18, 10, 45, 32), lang_text, self.toggle_language, style="lang"))
            self.buttons.append(Button((SCREEN_W - 250, 10, 235, 32), self.T("return_design"), lambda: setattr(self, "mode", "DESIGN"), style="primary"))
            self.buttons.append(Button((SCREEN_W - 130, 100, 55, 28), "▲", lambda: self.scroll_shop(-160), style="primary"))
            self.buttons.append(Button((SCREEN_W - 70, 100, 55, 28), "▼", lambda: self.scroll_shop(160), style="primary"))
            self.build_shop_entries()
            return

        lang_text = "EN" if self.language == "TR" else "TR"
        self.buttons.append(Button((18, 10, 45, 32), lang_text, self.toggle_language, style="lang"))
        self.buttons.append(Button((SCREEN_W - 250, 10, 110, 32), self.T("shop"), self.open_shop, style="shop"))
        self.buttons.append(Button((SCREEN_W - 130, 10, 115, 32), self.T("exit"), self.quit_game, style="alert"))

        tabs = [self.T("tab1"), self.T("tab2"), self.T("tab3"), self.T("tab4")]
        for t in range(4):
            self.buttons.append(Button((16 + t * 316, 76, 308, 34), tabs[t], lambda t=t: setattr(self.ms, "active_tab", t), selected=(self.ms.active_tab == t)))

        x0 = 28
        tab = self.ms.active_tab

        if tab == 0:
            for i, m in enumerate(NASA_MISSIONS):
                locked = i not in self.unlocked_missions
                if locked:
                    txt = f"[{self.T('locked')}] {self.mission_short(m)} — ${m['unlock_cost']}M {self.T('requires')}"
                elif m.get("free"):
                    txt = f"{self.mission_short(m)} — {self.T('free')}"
                else:
                    txt = f"{self.mission_short(m)} — {self.T('budget')} ${m['budget']}M"
                if i in self.completed_missions:
                    txt = f"[{self.T('completed')}] " + txt
                self.buttons.append(Button((x0, 148 + i * 36, 464, 32), txt, lambda i=i: self.select_mission(i), selected=(self.ms.mission_idx == i), disabled=locked))
            owned = sorted(self.owned_items["instruments"])
            for k, i in enumerate(owned):
                inst = INSTRUMENTS[i]
                sel = i in self.ms.selected_inst
                txt = f"{'[X]' if sel else '[  ]'} {inst['name']} (${inst['cost']}M)"
                self.buttons.append(Button((x0, 458 + k * 34, 464, 30), txt, lambda i=i: self.toggle_instrument(i), selected=sel))

        elif tab == 1:
            for k, i in enumerate(sorted(self.owned_items["power"])):
                p = POWER_SYSTEMS[i]
                self.buttons.append(Button((x0, 148 + k * 40, 464, 36), f"{p['name']} (${p['cost']}M | {p['base_watts']}W)", lambda i=i: setattr(self.ms, "power_idx", i), selected=(self.ms.power_idx == i)))
            for k, i in enumerate(sorted(self.owned_items["bus"])):
                b = BUS_CHASSIS[i]
                self.buttons.append(Button((x0, 348 + k * 40, 464, 36), f"{b['name']} (${b['cost']}M | Kalkan %{int(b['shield']*100)})", lambda i=i: setattr(self.ms, "bus_idx", i), selected=(self.ms.bus_idx == i)))

        elif tab == 2:
            for k, i in enumerate(sorted(self.owned_items["comms"])):
                c = COMMS_SYSTEMS[i]
                self.buttons.append(Button((x0, 148 + k * 44, 464, 40), f"{c['name']} (${c['cost']}M | {c['base_rate']}Mbps)", lambda i=i: setattr(self.ms, "comms_idx", i), selected=(self.ms.comms_idx == i)))

        elif tab == 3:
            for k, i in enumerate(sorted(self.owned_items["propulsion"])):
                pr = PROPULSION_SYSTEMS[i]
                self.buttons.append(Button((x0, 148 + k * 36, 464, 32), f"{pr['name']} (${pr['cost']}M | Isp {pr['isp']}s)", lambda i=i: setattr(self.ms, "prop_idx", i), selected=(self.ms.prop_idx == i)))
            for k, i in enumerate(sorted(self.owned_items["fuel"])):
                fl = FUEL_TANKS[i]
                self.buttons.append(Button((x0 + (k % 2) * 236, 294 + (k // 2) * 38, 228, 34), f"{fl['name']} (+${fl['tank_cost']}M)", lambda i=i: setattr(self.ms, "fuel_idx", i), selected=(self.ms.fuel_idx == i)))
            for k, i in enumerate(sorted(self.owned_items["launch"])):
                lv = LAUNCH_VEHICLES[i]
                self.buttons.append(Button((x0, 412 + k * 38, 464, 34), f"{lv['name']} (${lv['cost']}M | {lv['max_mass']}kg)", lambda i=i: setattr(self.ms, "lv_idx", i), selected=(self.ms.lv_idx == i)))

        tele = self.ms.compute_telemetry()
        cost = self.launch_cost(tele)
        ok = (not tele["issues"]) and cost <= self.company_funds
        if ok:
            txt = self.T("launch_flight") if cost else self.T("free_launch")
        elif tele["issues"]:
            txt = self.T("critical_error")
        else:
            txt = f"{self.T('insufficient_funds')} (${cost}M)"
        self.buttons.append(Button((912, SCREEN_H - 62, 352, 46), txt, self.launch_flight, selected=True, style="primary", disabled=not ok))

    def build_shop_entries(self):
        self.shop_entries = []
        y = 0
        for cat, title_tr, title_en, table in SHOP_CATEGORIES:
            title = title_en if self.language == "EN" else title_tr
            self.shop_entries.append(("header", title, y))
            y += 34
            for i, it in enumerate(table):
                owned = i in self.owned_items[cat]
                price = it["unlock_cost"]
                afford = self.company_funds >= price
                self.shop_entries.append(("item", cat, i, it, owned, price, afford, y))
                y += 46
            y += 14
        self.shop_content_h = y
        max_scroll = max(0, self.shop_content_h - self.shop_view.h)
        self.shop_target = max(0.0, min(float(max_scroll), self.shop_target))

        self.shop_scroll += (self.shop_target - self.shop_scroll) * 0.35
        if abs(self.shop_target - self.shop_scroll) < 0.6:
            self.shop_scroll = self.shop_target

        v = self.shop_view
        for e in self.shop_entries:
            if e[0] != "item":
                continue
            _, cat, i, it, owned, price, afford, cy = e
            sy = v.y + cy - int(self.shop_scroll)
            h = 42
            if sy < v.y or sy + h > v.bottom:
                continue
            use = item_use_cost(cat, it)
            if owned:
                label = f"[{self.T('owned')}] {it['name']}"
                sub = f"{item_stat_line(cat, it, self.language)}  |  {self.T('mission_cost')} ${use}M"
                self.shop_buttons.append(Button((v.x + 12, sy, v.w - 40, h), label, lambda: None, style="owned", disabled=False, sub=sub))
            else:
                label = f"{self.T('buy')}  ${price}M  —  {it['name']}"
                sub = f"{item_stat_line(cat, it, self.language)}  |  {self.T('mission_cost')} ${use}M"
                self.shop_buttons.append(Button((v.x + 12, sy, v.w - 40, h), label, lambda c=cat, k=i, p=price: self.buy_item(c, k, p), style="shop", disabled=not afford, sub=sub))

    def scroll_shop(self, delta):
        max_scroll = max(0, self.shop_content_h - self.shop_view.h)
        self.shop_target = max(0.0, min(float(max_scroll), self.shop_target + delta))

    def launch_cost(self, tele):
        return 0 if NASA_MISSIONS[self.ms.mission_idx].get("free") else tele["total_cost"]

    def next_tutorial(self):
        if self.tutorial_step < 4:
            self.tutorial_step += 1
        else:
            self.mode = "DESIGN"

    def skip_tutorial(self):
        self.mode = "DESIGN"

    def restart_game(self):
        self.company_funds = 350
        self.unlocked_missions = {0}
        self.completed_missions = set()
        self.ms = MissionDesign()
        self.owned_items = {
            "instruments": {0, 1, 2}, "power": {0, 1}, "bus": {0, 1},
            "comms": {0, 1}, "propulsion": {0, 1}, "fuel": {0, 1}, "launch": {0, 1},
        }
        self.shop_scroll = self.shop_target = 0.0
        self.last_report = ""
        self.mode = "DESIGN"

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
            self.fullscreen = False
        else:
            self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.FULLSCREEN)
            self.fullscreen = True

    def toggle_language(self):
        self.language = "EN" if self.language == "TR" else "TR"

    def open_shop(self):
        self.mode = "SHOP"
        self.shop_scroll = self.shop_target = 0.0

    def buy_item(self, cat, idx, price):
        if idx in self.owned_items[cat] or self.company_funds < price:
            return
        self.company_funds -= price
        self.owned_items[cat].add(idx)

    def select_mission(self, idx):
        if idx in self.unlocked_missions:
            self.ms.mission_idx = idx

    def toggle_instrument(self, idx):
        if idx not in self.owned_items["instruments"]:
            return
        if idx in self.ms.selected_inst:
            self.ms.selected_inst.remove(idx)
        else:
            self.ms.selected_inst.add(idx)

    def launch_flight(self):
        tele = self.ms.compute_telemetry()
        cost = self.launch_cost(tele)
        if tele["issues"] or cost > self.company_funds:
            return
        self.company_funds -= cost
        self.launch_paid = cost
        self.flight = InteractiveFlightSession(self.ms, tele)
        self.mode = "FLIGHT"

    def return_to_lobby_refund(self):
        self.company_funds += self.launch_paid
        self.last_report = f"{self.T('cancel_flight')} — ${self.launch_paid}M {self.T('refund')}"
        self.launch_paid = 0
        self.flight = None
        self.mode = "DESIGN"

    def finish_mission(self):
        tele = self.flight.tele
        idx = self.ms.mission_idx
        m = NASA_MISSIONS[idx]
        repeat = idx in self.completed_missions
        reward = int(tele["budget"] * 0.22) + int(tele["design_sci"] * 0.18) + self.flight.flight_score_bonus + 60
        if repeat:
            reward = int(reward * 0.55)
        self.company_funds += reward
        self.completed_missions.add(idx)
        for i, mm in enumerate(NASA_MISSIONS):
            if self.company_funds >= mm["unlock_cost"]:
                self.unlocked_missions.add(i)
        self.last_report = f"{self.mission_short(m)} {self.T('mission_complete')}: +${reward}M" + (f" {self.T('repeat_mission')}" if repeat else "")
        self.launch_paid = 0
        self.flight = None
        if len(self.completed_missions) == len(NASA_MISSIONS):
            self.mode = "VICTORY"
        else:
            self.mode = "DESIGN"

    def crash_mission(self):
        lost = self.launch_paid
        sponsor = 40 if lost > 0 else 0
        self.company_funds += sponsor
        self.last_report = f"{self.T('crash_report')}: {self.flight.crash_reason} — ${lost}M {self.T('burned')}" + (f", +${sponsor}M {self.T('sponsor')}" if sponsor else "")
        self.launch_paid = 0
        self.flight = None
        self.mode = "DESIGN"

    def draw_header(self, subtitle=""):
        pygame.draw.rect(self.screen, NASA_NAVY, (0, 0, SCREEN_W, 70))
        pygame.draw.line(self.screen, WHITE, (0, 70), (SCREEN_W, 70), 2)
        self.screen.blit(self.font_lg.render(self.T("title"), True, WHITE), (75, 6))
        money = self.font_md.render(f"{self.T('total_money')}: ${self.company_funds}M", True, OK_GREEN)
        self.screen.blit(money, (75, 40))
        done = self.font_xs.render(f"{self.T('completed_missions')}: {len(self.completed_missions)}/{len(NASA_MISSIONS)}", True, LIGHT_BLUE)
        self.screen.blit(done, (310, 45))
        if subtitle:
            s = self.font_xs.render(subtitle, True, MUTED_GRAY)
            self.screen.blit(s, (530, 45))
        hint = self.font_xs.render(self.T("esc_hint"), True, (150, 180, 220))
        self.screen.blit(hint, (SCREEN_W - 250, 46))

    def draw_tutorial(self):
        ov = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 210))
        self.screen.blit(ov, (0, 0))
        box = pygame.Rect(SCREEN_W // 2 - 420, SCREEN_H // 2 - 200, 840, 330)
        pygame.draw.rect(self.screen, PANEL_BLACK, box)
        pygame.draw.rect(self.screen, NASA_BLUE, box, 2)
        t = self.font_lg.render(self.T("tutorial_title"), True, LIGHT_BLUE)
        self.screen.blit(t, (box.centerx - t.get_width() // 2, box.y + 22))
        y = box.y + 78
        tutorial_key = f"tutorial_{self.tutorial_step + 1}"
        for line in self.T(tutorial_key).split("\n"):
            s = self.font_sm.render(line, True, WHITE)
            self.screen.blit(s, (box.centerx - s.get_width() // 2, y))
            y += 30
        p = self.font_xs.render(f"{self.T('step')} {self.tutorial_step + 1} {self.T('of')} 5", True, MUTED_GRAY)
        self.screen.blit(p, (box.centerx - p.get_width() // 2, box.bottom - 34))

    def draw_victory(self):
        ov = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 225))
        self.screen.blit(ov, (0, 0))
        box = pygame.Rect(SCREEN_W // 2 - 340, SCREEN_H // 2 - 170, 680, 340)
        pygame.draw.rect(self.screen, (10, 35, 25), box)
        pygame.draw.rect(self.screen, OK_GREEN, box, 3)
        t = self.font_lg.render(self.T("victory_title"), True, OK_GREEN)
        self.screen.blit(t, (box.centerx - t.get_width() // 2, box.y + 40))
        lines = [
            f"{self.T('total_missions')}: {len(self.completed_missions)}",
            f"{self.T('remaining_budget')}: ${self.company_funds}M",
            self.T("victory_desc"),
        ]
        for i, line in enumerate(lines):
            s = self.font_md.render(line, True, WHITE)
            self.screen.blit(s, (box.centerx - s.get_width() // 2, box.y + 110 + i * 34))

    def draw_shop(self):
        v = self.shop_view
        pygame.draw.rect(self.screen, PANEL_BLACK, v)
        pygame.draw.rect(self.screen, BORDER_BLUE, v, 2)
        self.screen.blit(self.font_lg.render(self.T("shop_title"), True, LIGHT_BLUE), (30, 96))
        self.screen.blit(self.font_xs.render(self.T("shop_hint"), True, MUTED_GRAY), (30, 126))

        old_clip = self.screen.get_clip()
        self.screen.set_clip(v)
        mouse = pygame.mouse.get_pos()
        for e in self.shop_entries:
            if e[0] == "header":
                sy = v.y + e[2] - int(self.shop_scroll)
                if v.y - 30 < sy < v.bottom:
                    pygame.draw.rect(self.screen, NASA_NAVY, (v.x + 8, sy, v.w - 32, 28))
                    self.screen.blit(self.font_md.render(e[1], True, WHITE), (v.x + 18, sy + 5))
        for b in self.shop_buttons:
            b.draw(self.screen, self.font_sm, mouse, self.font_xs)
        self.screen.set_clip(old_clip)

        max_scroll = max(0, self.shop_content_h - v.h)
        if max_scroll > 0:
            track = pygame.Rect(v.right - 16, v.y + 4, 10, v.h - 8)
            pygame.draw.rect(self.screen, (20, 30, 50), track)
            knob_h = max(30, int(track.h * v.h / self.shop_content_h))
            knob_y = track.y + int((track.h - knob_h) * (self.shop_scroll / max_scroll))
            pygame.draw.rect(self.screen, NASA_BLUE, (track.x, knob_y, track.w, knob_h))
        pct = int(100 * self.shop_scroll / max_scroll) if max_scroll else 100
        self.screen.blit(self.font_xs.render(f"{self.T('scroll')} %{pct}", True, MUTED_GRAY), (v.x, v.bottom + 6))

    def draw_design(self, tele):
        m = NASA_MISSIONS[self.ms.mission_idx]
        pygame.draw.rect(self.screen, PANEL_BLACK, (16, 118, 488, SCREEN_H - 134))
        pygame.draw.rect(self.screen, BORDER_BLUE, (16, 118, 488, SCREEN_H - 134), 1)

        if self.ms.active_tab == 0:
            self.screen.blit(self.font_md.render(self.T("select_mission"), True, LIGHT_BLUE), (28, 124))
            self.screen.blit(self.font_md.render(self.T("select_instruments"), True, LIGHT_BLUE), (28, 430))
        elif self.ms.active_tab == 1:
            self.screen.blit(self.font_md.render(self.T("power_system"), True, LIGHT_BLUE), (28, 124))
            self.screen.blit(self.font_md.render(self.T("bus_shield"), True, LIGHT_BLUE), (28, 320))
        elif self.ms.active_tab == 2:
            self.screen.blit(self.font_md.render(self.T("dsn_antenna"), True, LIGHT_BLUE), (28, 124))
            y = 400
            stats = [
                f"{self.T('distance_attenuation')}: {m['dist_factor']}x",
                f"{self.T('data_generation')}: {tele['inst_data']} Mbps",
                f"{self.T('downlink_capacity')}: {tele['downlink']} Mbps",
                f"{self.T('capture_ratio')}: %{int(tele['data_eff'] * 100)}",
            ]
            for line in stats:
                self.screen.blit(self.font_sm.render(line, True, WHITE), (32, y))
                y += 26
        elif self.ms.active_tab == 3:
            self.screen.blit(self.font_md.render(self.T("thruster"), True, LIGHT_BLUE), (28, 124))
            self.screen.blit(self.font_md.render(self.T("fuel_tank"), True, LIGHT_BLUE), (28, 266))
            self.screen.blit(self.font_md.render(self.T("launch_vehicle"), True, LIGHT_BLUE), (28, 384))

        draw_blueprint(self.screen, pygame.Rect(516, 118, 384, 300), self.ms)
        self.screen.blit(self.font_sm.render(self.T("spacecraft_schematic"), True, LIGHT_BLUE), (528, 126))

        info = pygame.Rect(516, 428, 384, SCREEN_H - 444)
        pygame.draw.rect(self.screen, PANEL_BLACK, info)
        pygame.draw.rect(self.screen, BORDER_BLUE, info, 1)
        self.screen.blit(self.font_md.render(self.mission_short(m), True, WHITE), (528, 436))
        desc = self.mission_desc(m)
        for i in range(0, min(len(desc), 120), 52):
            self.screen.blit(self.font_xs.render(desc[i:i + 52], True, MUTED_GRAY), (528, 460 + (i // 52) * 16))
        pygame.draw.line(self.screen, BORDER_BLUE, (528, 500), (888, 500), 1)
        self.screen.blit(self.font_sm.render(self.T("mission_objectives"), True, LIGHT_BLUE), (528, 508))
        for i, b in enumerate(m["bodies"]):
            self.screen.blit(self.font_xs.render(f"- {b['name']}", True, WHITE), (528, 532 + i * 34))
            self.screen.blit(self.font_xs.render(f"  {self.body_task(b)}", True, MUTED_GRAY), (528, 548 + i * 34))
        if self.last_report:
            col = OK_GREEN if self.T("mission_complete") in self.last_report else (GOLD if self.T("refund") in self.last_report else ALERT_RED)
            for i in range(0, min(len(self.last_report), 100), 50):
                self.screen.blit(self.font_xs.render(self.last_report[i:i + 50], True, col), (528, 650 + (i // 50) * 16))

        tr = pygame.Rect(912, 118, 352, SCREEN_H - 190)
        pygame.draw.rect(self.screen, PANEL_BLACK, tr)
        pygame.draw.rect(self.screen, BORDER_BLUE, tr, 1)
        self.screen.blit(self.font_md.render(self.T("system_telemetry"), True, LIGHT_BLUE), (926, 126))
        gx, gw = 926, 324
        rows = [
            (178, self.T("cost_vs_budget"), f"${tele['total_cost']}M / ${tele['budget']}M", tele["total_cost"] / max(1, tele["budget"]), False),
            (235, self.T("mass_vs_rocket"), f"{tele['wet_mass']} / {tele['max_mass']} kg", tele["wet_mass"] / max(1, tele["max_mass"]), False),
            (292, self.T("power_vs_load"), f"{tele['gen_power']}W / {tele['req_power']}W", tele["gen_power"] / max(1, tele["req_power"]), True),
            (349, self.T("delta_v_vs_req"), f"{tele['achieved_dv']} / {tele['req_dv']} m/s", tele["achieved_dv"] / max(1, tele["req_dv"]), True),
            (406, self.T("data_transfer"), f"{tele['downlink']} / {tele['inst_data']} Mbps", tele["data_eff"], True),
        ]
        for y, lab, val, ratio, exc in rows:
            draw_telemetry_bar(self.screen, gx, y, gw, 20, lab, val, ratio, must_exceed=exc, font=self.font_xs)

        self.screen.blit(self.font_sm.render(self.T("flight_readiness"), True, WHITE), (926, 440))
        if not tele["issues"]:
            pygame.draw.rect(self.screen, (10, 38, 82), (926, 464, 324, 78))
            pygame.draw.rect(self.screen, NASA_BLUE, (926, 464, 324, 78), 1)
            self.screen.blit(self.font_sm.render(self.T("all_systems_nominal"), True, LIGHT_BLUE), (938, 472))
            self.screen.blit(self.font_xs.render(f"{self.T('design_science')}: {tele['design_sci']}", True, WHITE), (938, 494))
            c = self.launch_cost(tele)
            free_txt = f" {self.T('free_paren')}" if c == 0 else ""
            self.screen.blit(self.font_xs.render(f"{self.T('launch_cost')}: ${c}M{free_txt}", True, OK_GREEN), (938, 514))
        else:
            for i, err in enumerate(tele["issues"][:5]):
                self.screen.blit(self.font_xs.render(f"[{self.T('error')}] {err}", True, ALERT_RED), (926, 466 + i * 20))

    def draw_flight(self, keys):
        fl = self.flight
        cam_x = max(0, min(fl.world_w - SCREEN_W, int(fl.x - SCREEN_W // 2)))
        cam_y = max(0, min(fl.world_h - SCREEN_H, int(fl.y - SCREEN_H // 2)))
        self.screen.fill(BLACK)
        for sx, sy, sr in fl.stars:
            if cam_x <= sx <= cam_x + SCREEN_W and cam_y <= sy <= cam_y + SCREEN_H:
                pygame.draw.circle(self.screen, (170, 195, 235), (sx - cam_x, sy - cam_y), sr)
        pygame.draw.rect(self.screen, ALERT_RED, pygame.Rect(28 - cam_x, 28 - cam_y, fl.world_w - 56, fl.world_h - 56), 3)

        for b in fl.mission_data["bodies"]:
            bx, by = int(b["x"] - cam_x), int(b["y"] - cam_y)
            if not (-400 < bx < SCREEN_W + 400 and -400 < by < SCREEN_H + 400):
                continue
            done = b["name"] in fl.completed_tasks
            pygame.draw.circle(self.screen, (18, 40, 78), (bx, by), int(b["r"] * 3.2), 1)
            pygame.draw.circle(self.screen, b["color"], (bx, by), b["r"])
            pygame.draw.circle(self.screen, OK_GREEN if done else WHITE, (bx, by), b["r"], 3)
            tag = f"[{self.T('completed')}] " if done else (f"[{self.T('target_label')}] ")
            lbl = self.font_sm.render(tag + b["name"], True, OK_GREEN if done else WHITE)
            self.screen.blit(lbl, (bx - lbl.get_width() // 2, by - b["r"] - 24))

        sx, sy = int(fl.x - cam_x), int(fl.y - cam_y)

        target, tdist = fl.nearest_target()
        if target is not None and tdist > 1:
            ux, uy = (target["x"] - fl.x) / tdist, (target["y"] - fl.y) / tdist
            
            tbx, tby = target["x"] - cam_x, target["y"] - cam_y
            on_screen = 0 < tbx < SCREEN_W and 70 < tby < SCREEN_H
            
            if on_screen:
                line_len = min(230.0, tdist - target["r"] - 14)
                if line_len > 20:
                    dashed_line(self.screen, GOLD, (sx + ux * 24, sy + uy * 24), (sx + ux * line_len, sy + uy * line_len), 16, 11, 2)
                    tip = (sx + ux * (line_len + 12), sy + uy * (line_len + 12))
                    left = (tip[0] - ux * 16 - uy * 8, tip[1] - uy * 16 + ux * 8)
                    right = (tip[0] - ux * 16 + uy * 8, tip[1] - uy * 16 - ux * 8)
                    pygame.draw.polygon(self.screen, GOLD, [tip, left, right])
                    info = self.font_sm.render(f"{target['name']}  {int(tdist)} m", True, GOLD)
                    self.screen.blit(info, (tip[0] - info.get_width() // 2, tip[1] + 10))
            else:
                margin = 80
                edge_x = max(margin, min(SCREEN_W - margin, tbx))
                edge_y = max(110, min(SCREEN_H - 90, tby))
                
                dashed_line(self.screen, GOLD, (sx + ux * 24, sy + uy * 24), (edge_x, edge_y), 16, 11, 2)
                
                arrow_size = 14
                left = (edge_x - ux * arrow_size - uy * arrow_size // 2, edge_y - uy * arrow_size + ux * arrow_size // 2)
                right = (edge_x - ux * arrow_size + uy * arrow_size // 2, edge_y - uy * arrow_size - ux * arrow_size // 2)
                tip = (edge_x + ux * 8, edge_y + uy * 8)
                pygame.draw.polygon(self.screen, GOLD, [tip, left, right])
                
                info = self.font_sm.render(f"{target['name']}  {int(tdist)} m", True, GOLD)
                info_x = edge_x - info.get_width() // 2
                info_y = edge_y + 20 if edge_y < SCREEN_H // 2 else edge_y - 30
                self.screen.blit(info, (info_x, info_y))

        ca, sa = math.cos(fl.angle), math.sin(fl.angle)
        wx, wy = -sa * 18, ca * 18
        pygame.draw.line(self.screen, NASA_BLUE, (sx - wx, sy - wy), (sx + wx, sy + wy), 4)
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and fl.dv_remaining > 0 and fl.landed_body is None:
            pygame.draw.polygon(self.screen, LIGHT_BLUE, [(sx - ca * 12 - sa * 5, sy - sa * 12 + ca * 5), (sx - ca * 12 + sa * 5, sy - sa * 12 - ca * 5), (sx - ca * 30, sy - sa * 30)])
        pts = [(sx + ca * 16, sy + sa * 16), (sx - ca * 11 - sa * 9, sy - sa * 11 + ca * 9), (sx - ca * 11 + sa * 9, sy - sa * 11 - ca * 9)]
        pygame.draw.polygon(self.screen, WHITE, pts)
        pygame.draw.polygon(self.screen, NASA_BLUE, pts, 2)

        mm = pygame.Rect(SCREEN_W - 220, SCREEN_H - 130, 200, 100)
        pygame.draw.rect(self.screen, (5, 10, 20), mm)
        pygame.draw.rect(self.screen, BORDER_BLUE, mm, 1)
        for b in fl.mission_data["bodies"]:
            px = mm.x + int(b["x"] / fl.world_w * mm.w)
            py = mm.y + int(b["y"] / fl.world_h * mm.h)
            col = OK_GREEN if b["name"] in fl.completed_tasks else b["color"]
            pygame.draw.circle(self.screen, col, (px, py), 4)
        pygame.draw.circle(self.screen, GOLD, (mm.x + int(fl.x / fl.world_w * mm.w), mm.y + int(fl.y / fl.world_h * mm.h)), 3)
        self.screen.blit(self.font_xs.render(self.T("sector_map"), True, MUTED_GRAY), (mm.x, mm.y - 16))

        # HUD
        pygame.draw.rect(self.screen, PANEL_BLACK, (0, 0, SCREEN_W, 62))
        pygame.draw.line(self.screen, BORDER_BLUE, (0, 62), (SCREEN_W, 62), 2)
        speed = int(math.hypot(fl.vx, fl.vy))
        time_left = int(fl.flight_timer)
        total_score = fl.tele["design_sci"] + fl.flight_score_bonus
        
        l1 = f"{self.T('flight_controls')}   |   {self.T('speed')} {speed} m/s ({self.T('landing_limit')} 95)"
        self.screen.blit(self.font_sm.render(l1, True, WHITE), (16, 10))
        
        l2_base = f"{self.T('delta_v')} {int(fl.dv_remaining)} m/s   {self.T('battery')} %{int(fl.battery_pct)}   {self.T('target')} {len(fl.completed_tasks)}/3   {self.T('score')} {total_score}   "
        self.screen.blit(self.font_sm.render(l2_base, True, LIGHT_BLUE), (16, 34))
        
        time_txt = f"{self.T('time')} {time_left}s"
        if time_left <= 10:
            if (pygame.time.get_ticks() // 300) % 2 == 0:
                time_col = ALERT_RED
            else:
                time_col = (255, 100, 100)
        else:
            time_col = LIGHT_BLUE
        time_surf = self.font_sm.render(time_txt, True, time_col)
        self.screen.blit(time_surf, (SCREEN_W - time_surf.get_width() - 260, 34))

        if fl.banner_timer > 0:
            pygame.draw.rect(self.screen, NASA_NAVY, (SCREEN_W // 2 - 400, 72, 800, 30))
            pygame.draw.rect(self.screen, WHITE, (SCREEN_W // 2 - 400, 72, 800, 30), 1)
            b = self.font_sm.render(fl.status_banner, True, WHITE)
            self.screen.blit(b, (SCREEN_W // 2 - b.get_width() // 2, 79))

        if fl.landed_body is not None:
            b = fl.landed_body
            card = pygame.Rect(24, SCREEN_H - 190, 760, 168)
            pygame.draw.rect(self.screen, PANEL_BLACK, card)
            pygame.draw.rect(self.screen, WHITE, card, 2)
            pygame.draw.rect(self.screen, NASA_NAVY, (card.x + 2, card.y + 2, card.w - 4, 32))
            self.screen.blit(self.font_md.render(f"{self.T('surface_telemetry')} — {b['name'].upper()}", True, WHITE), (card.x + 12, card.y + 7))
            self.screen.blit(self.font_sm.render(f"{self.T('task')}: {self.body_task(b)}", True, WHITE), (card.x + 12, card.y + 44))
            state = self.T("completed_lift") if b["name"] in fl.completed_tasks else self.T("hold_e")
            self.screen.blit(self.font_sm.render(state, True, LIGHT_BLUE), (card.x + 12, card.y + 70))
            draw_telemetry_bar(self.screen, card.x + 12, card.bottom - 30, card.w - 24, 16, self.T("scanning"), f"%{int(fl.scan_progress)}", fl.scan_progress / 100.0, must_exceed=True, font=self.font_xs)

    def run(self):
        while True:
            dt = min(0.05, self.clock.tick(FPS) / 1000.0)
            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            self.sanitize_owned()
            self.build_buttons()
            tele = self.ms.compute_telemetry()

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.quit_game()
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.toggle_fullscreen()
                    elif self.mode == "SHOP":
                        if ev.key == pygame.K_UP:
                            self.scroll_shop(-90)
                        elif ev.key == pygame.K_DOWN:
                            self.scroll_shop(90)
                        elif ev.key == pygame.K_PAGEUP:
                            self.scroll_shop(-400)
                        elif ev.key == pygame.K_PAGEDOWN:
                            self.scroll_shop(400)
                elif ev.type == pygame.MOUSEWHEEL:
                    if self.mode == "SHOP":
                        self.scroll_shop(-ev.y * 70)
                elif ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button == 4 and self.mode == "SHOP":
                        self.scroll_shop(-70)
                    elif ev.button == 5 and self.mode == "SHOP":
                        self.scroll_shop(70)
                    elif ev.button == 1:
                        for b in self.buttons + self.shop_buttons:
                            if b.rect.collidepoint(mouse) and not b.disabled:
                                b.callback()
                                break

            if self.mode == "FLIGHT" and self.flight is not None:
                self.flight.update(keys, dt)
                self.draw_flight(keys)
                if self.flight.crashed:
                    self.crash_mission()
                elif len(self.flight.completed_tasks) == len(self.flight.mission_data["bodies"]):
                    self.finish_mission()
            else:
                self.screen.fill(BLACK)
                if self.mode == "TUTORIAL":
                    self.draw_header()
                    self.draw_tutorial()
                elif self.mode == "VICTORY":
                    self.draw_header()
                    self.draw_victory()
                elif self.mode == "SHOP":
                    self.draw_header(self.T("shop_hint"))
                    self.draw_shop()
                else:
                    self.draw_header(self.T("esc_hint"))
                    self.draw_design(tele)

            for b in self.buttons:
                b.draw(self.screen, self.font_xs, mouse, self.font_xs)

            pygame.display.flip()


if __name__ == "__main__":
    NASASpaceAppsGame().run()