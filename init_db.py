import datetime


def ref_string(ref_string, ref_url):
    return '<a href="{}">{}</a>'.format(ref_url, ref_string)


unitix_ref = ref_string("UNITIX", "https://gracecrm.com/")
dan_ref = ref_string("Daniel Collins", "https://dcollins.info/")
jenny_ref = ref_string("Dr Jenny (Xiuzhen) Zhang",
                       "http://www.xiuzhenzhang.org/")
culpepper_ref = ref_string("Dr Jason Shane Culpepper",
                           "http://www.culpepper.io/")

def date_from_str(date_str):
    return datetime.datetime.strptime(date_str, "%d/%m/%Y")

def init_data(events, session):
    for event in events:
        timeline_entry = Timeline()
        timeline_entry.title = event["title"]
        timeline_entry.date_from = date_from_str(event["time_from"])
        timeline_entry.date_to = date_from_str(event["time_to"])
        timeline_entry.event_type = event["event_type"]
        timeline_entry.description = event["description"]
        session.add(timeline_entry)

    session.commit()

if __name__ == "__main__":
    from model import Base, Timeline
    from model import LIFE, WORK_BUSINESS, EDUCATION
    from flaskr import engine, Session
    Base.metadata.create_all(engine)
    session = Session()
    events = [
            {"title": "Marry Yao",
             "time_from": "15/9/2016",
             "time_to": "15/9/2016",
             "event_type": LIFE,
             "description": "Most Beautiful Day of my life"},
            {"title": "Get 189(independent skill) permanent resident VISA with Yao",
             "time_from": "20/12/2015",
             "time_to": "20/12/2015",
             "event_type": LIFE,
             "description": "Thanks Australia, it is a wonderful land and legally" +
                            " I can live here for a very long time"},
            {"title": "Become Fulltime Fullstack Developer for {}".\
                    format(unitix_ref),
             "time_from": "10/05/2015",
             "time_to": "10/05/2015",
             "event_type": WORK_BUSINESS,
             "description": "After nearly one year of casual work finally become " +
                            "the full time developer for UNITIX"},
            {"title": "Pass NATTI Interpretation Test(Chinese to English) become"
                      " cerificated level 2 interpreter",
             "time_from": "19/02/2015",
             "time_to": "19/02/2015",
             "event_type": EDUCATION,
             "description": ""},
            {"title": "Become Causal Fullstack Developer for {}".format(unitix_ref),
             "time_from": "09/08/2014",
             "time_to": "09/08/2014",
             "event_type": WORK_BUSINESS,
             "description": "Thanks James Strachen, Richard Walker, {}".\
                            format(dan_ref) + " give me this chance"},
            {"title": "RMIT research project",
             "time_from": "01/03/2014",
             "time_to": "01/04/2014",
             "event_type": WORK_BUSINESS,
             "description": "This project was done by me and my friend Zheng Xin " +
                            "supervised by {} sponsored by RMIT".format(jenny_ref) +
                            " for participating iAwards"},
            {"title": "RMIT summer internship project",
             "time_from": "01/01/2014",
             "time_to": "01/03/2014",
             "event_type": WORK_BUSINESS,
             "description": "This project was supervised by {} sponsored " +
                            "by RMIT".format(jenny_ref) + " for extending my " +
                            "previous graduation research thesis"},
            {"title": "Graduated From RMIT with overall GPA 3.8",
             "time_from": "20/12/2013",
             "time_to": "20/12/2013",
             "event_type": EDUCATION,
             "description": "I graduated from RMIT with master degree of " +
                            "computer science"},
            {"title": "RMIT lexer collabroated project",
             "time_from": "03/01/2013",
             "time_to": "15/05/2013",
             "event_type": WORK_BUSINESS,
             "description": "This project was done by me and my friend phD " +
                            "Warrick Wang supervised by {} sponsored by RMIT and ".\
                            format(jenny_ref) + " for classify whether a tweet" +
                            " comes from a bussiness account or personal account"},
            {"title": "RMIT summer internship project",
             "time_from": "03/01/2013",
             "time_to": "01/03/2013",
             "event_type": WORK_BUSINESS,
             "description": "This project was supervised by {} sponsored ".\
                            format(culpepper_ref) + "by RMIT for trying to " +
                            "finding a better architecture for search engine"},
            {"title": "Started Studying at RMIT",
             "time_from": "19/02/2012",
             "time_to": "19/02/2012",
             "event_type": EDUCATION,
             "description": "No description"}
    ]
    init_data(events, session)
