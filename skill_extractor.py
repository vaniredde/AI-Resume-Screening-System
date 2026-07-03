SKILLS=['python','sql','machine learning','tensorflow','pandas','numpy']
def extract_skills(t):
 t=t.lower();return [s for s in SKILLS if s in t]