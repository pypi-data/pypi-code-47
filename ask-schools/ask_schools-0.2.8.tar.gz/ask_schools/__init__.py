__version__ = '0.2.8'

school_name = {
    'Toronto':{'suffix':'_tor', 'short':'Toronto', 'full':'University of Toronto'},
    'Mentee':{'suffix':'_int', 'short':'Mentee', 'full':'Mentee'},
    'Western':{'suffix':'_west', 'short':'Western', 'full':'University of Western Ontario'},
    'Carleton':{'suffix':'_car', 'short':'Carleton', 'full':'Carleton University'},
    'Ryerson':{'suffix':'_rye', 'short':'Ryerson', 'full':'Ryerson University'},
    'Laurentian':{'suffix':'_lan', 'short':'Laurentian', 'full':'Laurentian University'},
    'Queens':{'suffix':'_queens', 'short':'Queens', 'full':'Queens university'},
    'Brock':{'suffix':'_brk', 'short':'Brock', 'full':'Brock University'},
    'Guelph-Humber':{'suffix':'_guehum', 'short':'Guelph-Humber', 'full':'University of Guelph-Humber'},
    'Guelph':{'suffix':'_gue', 'short':'Guelph', 'full':'University of Guelph'},
    'Ontario Tech':{'suffix':'_uoit', 'short':'Ontario Tech', 'full':'Ontario Tech University'},
    'Ontario Tech':{'suffix':'_otech', 'short':'Ontario Tech', 'full':'Ontario Tech University'},
    'Saint-Paul':{'suffix':'_stp', 'short':'Saint-Paul', 'full':'Saint-Paul University'},
    'OCAD':{'suffix':'_ocad', 'short':'OCAD', 'full':'OCAD'},
    'Lakehead':{'suffix':'_lake', 'short':'Lakehead', 'full':'Lakehead university'},
    'Algoma':{'suffix':'_alg', 'short':'Algoma', 'full':'Algoma university'},
    'McMaster':{'suffix':'_mac', 'short':'McMaster', 'full':'McMaster university'},
    'York':{'suffix':'_york', 'short':'York', 'full':'York university'},
    'Scholars Portal':{'suffix':'_sp', 'short':'Scholars Portal', 'full':'Scholars Portal'},
    'Ottawa':{'suffix':'_ott', 'short':'Ottawa', 'full':'Ottawa University'}
}

def find_school_by_operator_suffix(operator):
    """from a suffix find the short name of that School
    
    Arguments:
        operator {str} -- suffix of the schoo i.e. _tor
    
    Returns:
        str -- The short name of the school i.e. Toronto
    """
    if operator is None:
        return operator 

    
    if "_tor" in operator:
        return "Toronto"
    elif "_int" in operator:
        return "Mentee"
    elif "_west" in operator:
        return "Western"
    elif "_car" in operator:
        return "Carleton"
    elif "_rye" in operator:
        return "Ryerson"
    elif "_lan" in operator:
        return "Laurentian"
    elif "_queens" in operator:
        return "Queens"
    elif "_brk" in operator:
        return "Brock"
    elif "_guehum" in operator:
        return "Guelph-Humber"
    elif "_gue" in operator:
        return "Guelph"
    elif "_uoit" in operator:
        return "Ontario Tech"
    elif "_otech" in operator:
        return "Ontario Tech"
    elif "_stp" in operator:
        return "Saint-Paul"
    elif "_ocad" in operator:
        return "OCAD"
    elif "_lake" in operator:
        return "Lakehead"
    elif "_alg" in operator:
        return "Algoma"
    elif "_mac" in operator:
        return "McMaster"
    elif "_york" in operator:
        return "York"
    elif "_sp" in operator:
        return "Scholars Portal"
    elif "_ott" in operator:
        return "Ottawa"
    else:
        return "Unknown"


def find_school_by_queue_or_profile_name(queue):
    if queue is None:
        return queue 

    if queue in ["toronto-st-george", 'toronto-st-george-proactive', 'toronto-scarborough', 'toronto-mississauga']:
        return "University of Toronto"
    elif queue in ["york", 'york-glendon-fr', 'york-glendon']:
        return "York University"
    elif queue in ['guelph']:
        return 'Guelph University'
    elif queue in ['ryerson']:
        return 'Ryerson University'
    elif queue in ["western", 'western-proactive', 'western-fr']:
        return "Western Ontario University"
    elif queue in ["lakehead-proactive", 'lakehead']:
        return "Lakehead University"
    elif queue in ["mcmaster", 'mcmaster-txt']:
        return "McMaster University"
    elif queue in ['queens']:
        return "Queens University"
    elif queue in ['brock']:
        return "Brock University"
    elif queue in ['otech']:
        return "Ontario Tech Universtiy"
    elif queue in ['carleton', 'carleton-txt']:
        return "Carleton University"
    elif queue in ['saintpaul', 'saintpaul-fr']:
        return "St-Paul University"
    elif queue in ['ottawa', 'ottawa-txt', 'ottawa-fr']:
        return "Ottawa University"
    elif queue in ['laurentian','laurentian-fr' ]:
        return "Laurentian University"
    elif queue in ['guelph-humber','guelph-humber-txt' ]:
        return "Guelph-Humber University"
    elif queue in ["ocad"]:
        return "OCAD University"
    elif queue in ['algoma-proactive','algoma', 'algoma-fr']:
        return "Algoma University"
    elif queue in ['practice-webinars-fr', 'practice-webinars']:
        return "SP-Practice-queue"
    elif queue in ['scholars-portal']:
        return "Scholars-Portal"
    else:
        return "Unknown"

def find_school_abbr_by_queue_or_profile_name(queue):
    if queue is None:
        return queue 

    if queue in ["toronto-st-george", 'toronto-st-george-proactive', 'toronto-scarborough', 'toronto-mississauga']:
        return "UofT"
    elif queue in ["york", 'york-glendon-fr', 'york-glendon']:
        return "YorkU"
    elif queue in ['guelph']:
        return 'GuelphU'
    elif queue in ['ryerson']:
        return 'RyersonU'
    elif queue in ["western", 'western-proactive', 'western-fr']:
        return "Western"
    elif queue in ["lakehead-proactive", 'lakehead']:
        return "Lakehead"
    elif queue in ["mcmaster", 'mcmaster-txt']:
        return "McMaster"
    elif queue in ['queens']:
        return "Queens"
    elif queue in ['brock']:
        return "Brock"
    elif queue in ['otech']:
        return "Ontario Tech"
    elif queue in ['carleton', 'carleton-txt']:
        return "Carleton"
    elif queue in ['saintpaul', 'saintpaul-fr']:
        return "St-Paul"
    elif queue in ['ottawa', 'ottawa-txt', 'ottawa-fr']:
        return "Ottawa"
    elif queue in ['laurentian','laurentian-fr' ]:
        return "Laurentian"
    elif queue in ['guelph-humber','guelph-humber-txt' ]:
        return "Guelph-Humber"
    elif queue in ["ocad"]:
        return "OCAD"
    elif queue in ['algoma-proactive','algoma', 'algoma-fr']:
        return "Algoma"
    elif queue in ['practice-webinars-fr', 'practice-webinars']:
        return "SP-Practice"
    elif queue in ['scholars-portal']:
        return "Scholars-Portal"
    else:
        return "Unknown"

HTF_schools = ["Brock University", "Carleton University", 
                "Laurentian University", "University of Toronto",
                "Ontario Tech University", "Western Ontario University", 
                "Queens University"]

FRENCH_QUEUES = ['algoma-fr', 'clavardez', 'laurentian-fr', 'ottawa-fr', 
        'saintpaul-fr', 'western-fr', 'york-glendon-fr']
SMS_QUEUES = ['carleton-txt', 'clavardez-txt', 'guelph-humber-txt',
            'mcmaster-txt', 'ottawa-fr-txt', 'ottawa-txt', 
            'scholars-portal-txt', 'western-txt', 'york-txt']
PRACTICE_QUEUES = ['practice-webinars', 'practice-webinars-fr', 'practice-webinars-txt']

def find_routing_model_by_profile_name(university_name):
    if university_name is None:
        return university_name
    if university_name in HTF_schools:
        return "HTF"
    else:
        return "FLAT"


if __name__ == '__main__':
    pass