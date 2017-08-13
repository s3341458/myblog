from model import QuestionEntry, QuestionReplyAssociation, Reply
from flaskr import engine, Session
import arrow

COMMENCE_WORK_PERIOD = "commence work waiting period"

SALARY_EXPECTATION = "salary expectation"
SALARY_EXPECTATION_ANSWER = \
""" This really depends on the type of contract as I list as follows(in AUD):
    permanent role $58/hr.
    contract (equal or over one year)  $78/hr.
    contract (equal or over three month)  $88/hr.
    contract (less than three month)  $108-128/hr.
    All above payment rates may varies due the specific position requirements,
    to me the meaning of the project and who am I working with are somehow more
    important than the pay rate.
"""

HOLIDAY_PLAN = "holiday plan"
HOLIDAY_PLAN_ANSWER =\
""" No plan at the moment plus I am willing to work during christmas period.
    If possible hope to have one week holiday for spring festival(Feb 15 - Feb 21).
    Any way holiday is not a very important thing for me.
"""

EMERGENCY_CONTACT = "emergency contact"
EMERGENCY_CONTACT_ANSWER = \
""" Name: Yao Yang
    Relationship: wife
    Number: 0488180316
"""

CURRENT_WORKING_STATUS = "current work status"

IDENTITY = "australia identity"
IDENTITY_ANSWER = \
""" I am not australia citizen at the moment but I am holding the permanent
    resident visa(subclass 189) of Australia. I am original come from China
    mainland and my nationality is People's Republic of China as well.
"""

CONTRACTOR_PAYMENT_TYPE = "contractor payment type"
CONTRACTOR_PAYMENT_TYPE_ANSWER = "Only PAYG acceptable at the moment"

PAXUS_AVANDE_CAPABILITY = "capability regarding paxus avanda"
PAXUS_AVANDE_CAPABILITY_ANSWER = \
""" I think I am the ideal person for this role since I am good at programming
    and has experience in solving scientific level problem by using my
    programming, algorithm and math knowledge.

    Also I do system admin work in my current role (Actually I do everything).
    I am also an operating system lover who love to spend spare my time
    playing different OS and diging the kernel code of Linux and BSD Unix.
    I understanding in financial area you need a deep understanding about
    system architecture since every request is crucial and potientially there
    are tons of requests need to be handle in a very short period of time.

    Although I have not worked in finance deparment yet, I have a comprehensive
    understanding of finance and I studied yale's open course Finanical Markets 
    (ECON 252) in 2011 and I read books about finance as well.

    ps my history with finance:
    To be honest quant analyst (not quant developer) is always my dream job.
    I was plan to apply finance as my bachelor major but due to financial crisis
    in 2008 since I was afraid that I can not got a job after graduated.

    I was plan to apply financial engineering as my master major, however since
    finance anlyst is not on the immigration skill list I choose Computer
    Science as my major and during my master degree I spend a lot time on
    researching machine learning since I forsee the potiential widely usage of
    this technology in finance area.
    I have a plan to study phD in RMIT (With scholarship), my researching plan
    was:
    1. Find a model to automatically distinguish official business twitter
    account and personal account.
    2. develop a twits sentiment analysis.
    3. build a automatic twitter anaylsis system to finding a happening event
       and how public respond to it.
    4(personal). Base on the system build on above I can get the ability to
       predict the trend of a thing before market noticed. Anyone knows finance
       will know the value of this research.
    However I refused the phD offer since at that time find a job is more
    beneficial to get premanent resident visa.

"""


QUESTIONS = [
    {"title": COMMENCE_WORK_PERIOD,
     "question": "When can you commence work?",
     "answer": "Needs one month notice (4 weeks) before leave"},
    {"title": SALARY_EXPECTATION,
     "question": "What rate are you targeting?",
     "answer": SALARY_EXPECTATION_ANSWER},
    {"title": HOLIDAY_PLAN,
     "question": "Do you have any planned holidays? Please give details.",
     "answer": HOLIDAY_PLAN_ANSWER},
    {"title": CURRENT_WORKING_STATUS,
     "question": "Are you currently in a contractor or permanent role? If so " +
                 "please give detail including any possiblity of extensions.",
     "answer": "I am in a permanent role at the moment"},
    {"title": EMERGENCY_CONTACT,
     "question": "Please include your next of kin/emergency contact details.",
     "answer": EMERGENCY_CONTACT_ANSWER},
    {"title": IDENTITY,
     "question": "Are you an Australian Citizen? If not, please advise your" +
                 "nationality and visa status",
     "answer": IDENTITY_ANSWER},
    {"title": CONTRACTOR_PAYMENT_TYPE,
     "question": "Confirm Engagement Type (PAYG or PTY LTD)",
     "answer": "Only PAYG acceptable at the moment since I do not have abn"},
    {"title": PAXUS_AVANDE_CAPABILITY,
     "question": "Please detail a couple of paragraphs addressing the key " +
                 "responsibilities of the role including an example of your " +
                 "relevant experience.",
     "answer": PAXUS_AVANDE_CAPABILITY_ANSWER},
]

REPLIES = [
    {"token": "4d4beac2",
     "receiver_name": "EMalin@paxus.com.au",
     "about": "Avadar Senior Consultant",
     "questions": [COMMENCE_WORK_PERIOD, SALARY_EXPECTATION,
                   CURRENT_WORKING_STATUS, EMERGENCY_CONTACT, IDENTITY,
                   CONTRACTOR_PAYMENT_TYPE, PAXUS_AVANDE_CAPABILITY]
    }
]



def input_question(question_entry_dict, session):
    question = QuestionEntry()
    question.title = question_entry_dict["title"]
    question.question = question_entry_dict["question"]
    question.answer = question_entry_dict["answer"]
    question.last_update_date = arrow.utcnow().datetime
    session.add(question)
    session.commit()

def input_questions(question_dicts, session):
    for question_dict in question_dicts:
        input_question(question_dict, session)

def find_question(title, session):
    return session.query(QuestionEntry).\
        filter(QuestionEntry.title == title).first()

def input_reply(reply_dict, session):
    reply = Reply()
    reply.token = reply_dict["token"]
    reply.receiver_name = reply_dict["receiver_name"]
    reply.about = reply_dict["about"]
    for question_title in reply_dict["questions"]:
        question = find_question(question_title, session)
        reply.question_entries.append(question)
    session.add(reply)
    session.commit()

def input_replies(reply_dicts, session):
    for reply_dict in reply_dicts:
        input_reply(reply_dict, session)

def refresh_replies(session):
    input_questions(QUESTIONS, session)
    input_replies(REPLIES, session)

if __name__ == "__main__":
    session = Session()
    session.query(QuestionEntry).delete()
    session.query(Reply).delete()
    refresh_replies(session)

