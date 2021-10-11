import datetime

def log ( message ) :

    print(f"[ LOG ] status : {message} --> {datetime.datetime.now().strftime('%H:%M:%S')}")