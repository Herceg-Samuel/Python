import re
import csv
from collections import defaultdict

INPUT_FILE = "sugarcane_kb.pl"
OUTPUT_FILE = "casebase.csv"

def clean_text(text):
    """Formats 'red_rot' to 'Red Rot'"""
    return text.replace("_", " ").title().strip()

def parse_sugarcane_kb():

    disease_data = defaultdict(lambda: {
        'symptoms': set(), 
        'pests': set(), 
        'effects': set(), 
        'controls': set()
    })


    pest_to_disease = defaultdict(list)
    
    
    pest_effects = defaultdict(set)  
    pest_controls = defaultdict(set)  

    print(f"--- Reading {INPUT_FILE} ---")
    
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # --- PASS 1: Parse the facts ---
        for line in lines:
            line = line.strip()
            if not line or line.startswith("%"): continue

            # 1. SYMPTOMS: symptom(red_rot, white_spots).
            m_sym = re.match(r"symptom\((.*?),(.*?)\)\.", line)
            if m_sym:
                d_key = m_sym.group(1).strip()
                s_val = clean_text(m_sym.group(2))
                disease_data[d_key]['symptoms'].add(s_val)
                continue

            # 2. CAUSES (Links Pest -> Disease): causes(pest_name, disease_name).
            m_cause = re.match(r"causes\((.*?),(.*?)\)\.", line)
            if m_cause:
                p_key = m_cause.group(1).strip()
                d_key = m_cause.group(2).strip()
                
                # Link pest to disease
                pest_to_disease[p_key].append(d_key)
                disease_data[d_key]['pests'].add(clean_text(p_key))
                continue

            # 3. EFFECTS (Linked to Pest): effect(pest_name, effect_desc).
            m_eff = re.match(r"effect\((.*?),(.*?)\)\.", line)
            if m_eff:
                p_key = m_eff.group(1).strip()
                e_val = clean_text(m_eff.group(2))
                pest_effects[p_key].add(e_val)
                continue

            # 4. CONTROLS (Linked to Pest): controls(drug, pest_name).
            m_ctrl = re.match(r"controls\((.*?),(.*?)\)\.", line)
            if m_ctrl:
                drug_val = clean_text(m_ctrl.group(1))
                p_key = m_ctrl.group(2).strip()
                pest_controls[p_key].add(drug_val)
                continue

            # 5. DISEASE LIST: disease(red_rot). (Just ensures it exists in our dict)
            m_dis = re.match(r"disease\((.*?)\)\.", line)
            if m_dis:
                d_key = m_dis.group(1).strip()
                _ = disease_data[d_key] # Accessing it creates the default entry

        for pest, effects in pest_effects.items():
            associated_diseases = pest_to_disease.get(pest, [])
            for d_key in associated_diseases:
                disease_data[d_key]['effects'].update(effects)

        # Merge Pest Controls into Disease
        for pest, controls in pest_controls.items():
            associated_diseases = pest_to_disease.get(pest, [])
            for d_key in associated_diseases:
                disease_data[d_key]['controls'].update(controls)

        # --- PASS 3: Write to CSV ---
        headers = ["id", "disease_name", "symptoms", "pests", "effects", "control_measures"]
        
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for idx, (d_key, data) in enumerate(disease_data.items()):
                # Create the row
                row = {
                    "id": idx + 1,
                    "disease_name": clean_text(d_key),
                    "symptoms": "|".join(sorted(data['symptoms'])),
                    "pests": "|".join(sorted(data['pests'])),
                    "effects": "|".join(sorted(data['effects'])),
                    "control_measures": "|".join(sorted(data['controls']))
                }
                writer.writerow(row)

        print(f"Success! Converted {len(disease_data)} diseases.")
        print(f"Data saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: Could not find file '{INPUT_FILE}'")

if __name__ == "__main__":
    parse_sugarcane_kb()